## -*- coding: utf-8 -*-
from .vendor.Qt import QtCore, QtGui, QtWidgets
from . import button_setting
from . import button
from . import partition
from . import partition_setting
from . import lib
from . import shelf_option
from . import xpop

import json
import os
import os.path
import pymel.core as pm
import re
import copy

if lib.maya_api_version() < 201500:
    #For version below 2014
    MayaQWidgetDockableMixin = object

elif lib.maya_api_version() < 201700:
    from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

elif 201700 <= lib.maya_api_version() and lib.maya_api_version() < 201800:
    #  TODO : Check if new version comes out
    from .patch import m2017
    MayaQWidgetDockableMixin = m2017.MayaQWidgetDockableMixin2017

else:
    from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class SiShelfWeight(MayaQWidgetDockableMixin, QtWidgets.QTabWidget):
    URL = "https://github.com/mochio326/SiShelf"
    VAR  =  '1.7.1'
    PEN_WIDTH = 1  # Thickness of rectangular frame

    def __init__(self, parent=None, load_file=None, edit_lock=False):
        super(SiShelfWeight, self).__init__(parent)
        # Memory management funny
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # Change object name and title
        self.setObjectName(lib.TITLE)
        self.setWindowTitle(lib.TITLE)

        self.load_file = load_file
        self.edit_lock = edit_lock

        if self.edit_lock is False:
            self.setMovable(True)
            self.setAcceptDrops(True)

        self.load_all_tab_data()

        self._origin = None
        self._band = None
        self._selected = []
        self._floating_save = False
        self._clipboard = None
        self._context_pos = QtCore.QPoint()
        self._cut_flag = False
        self._parts_moving = False
        self._shelf_option = shelf_option.OptionData()

        self._set_stylesheet()

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._context_menu)
        self.currentChanged.connect(self._current_tab_change)
        self.tabBar().tabMoved.connect(self._tab_moved)

    def _current_tab_change(self):
        self._selected = []
        self._set_stylesheet()
        self.update()
        self.save_all_tab_data()

    def _tab_moved(self, event):
        self.save_all_tab_data()

    # -----------------------
    # ContextMenu
    # -----------------------
    def _context_menu(self, event):
        _menu = QtWidgets.QMenu()
        # Setting item names and functions to be executed
        if self.edit_lock is False:
            if self.currentWidget().reference is None:
                _menu.addAction('Add button', self._add_button)
                _menu.addAction('Add partition', self._add_partition)
                _menu.addSeparator()
                _menu.addAction('Edit', self._edit)
                _menu.addAction('Delete', self._delete)
                _menu.addAction('Copy', self._copy)
                _menu.addAction('Paste', self._paste)
                _menu.addAction('Cut', self._cut)
                _menu.addSeparator()

            _tb = _menu.addMenu('Tab')
            _tb.addAction('Add', self._add_tab)
            _tb.addAction('Rename', self._rename_tab)
            _tb.addAction('Delete', self._delete_tab)
            _tb.addSeparator()
            if self.currentWidget().reference is None:
                _tb.addAction('Export', self._export_tab)
                _tb.addAction('Import', self._import_tab)
                _tb.addSeparator()
                _tb.addAction('External reference', self._reference_tab)  # 外部参照設定
            else:
                _tb.addAction('Remove external reference', self._remove_reference_tab)  # 外部参照設定解除

            _df = _menu.addMenu('Default setting')
            _df.addAction('Button', self._button_default_setting)
            _df.addAction('Partition', self._partition_default_setting)
            if self.currentWidget().reference is None:
                _menu.addAction('XPOP setting', self._xpop_setting)

            _menu.addSeparator()
            _menu.addAction('Option', self._option)
        _menu.addAction('Version information', self._info)

        self._select_cursor_pos_parts()
        # Appear in mouse position
        cursor = QtGui.QCursor.pos()
        _menu.exec_(cursor)

    def _info(self):
        _status = QtWidgets.QMessageBox.information(
            self, 'Version information',
            'SiShelf ' + self.VAR,
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )

    def _option(self):
        self._shelf_option = shelf_option.OptionDialog.open(self)
        self._set_stylesheet()

    def _copy(self):
        self._clipboard = copy.deepcopy(self._selected[0].data)

    def _paste(self):
        if self._clipboard is None:
            return
        data = copy.deepcopy(self._clipboard)
        data.position = self._context_pos

        if isinstance(data, button.ButtonData):
            button.create(self.currentWidget(), data)
        elif isinstance(data, partition.PartitionData):
            partition.create(self.currentWidget(), data)

        self._selected = []
        self.repaint()
        self.save_all_tab_data()
        self._set_stylesheet()
        # In the case of cut, paste only once
        if self._cut_flag is True:
            self._clipboard = None
            self._cut_flag = False

    def _cut(self):
        self._copy()
        self.delete_parts(self._selected[0])
        self._selected = []
        self._cut_flag = True

    def _delete(self):
        for s in self._selected:
            self.delete_parts(s)
        self._selected = []
        self.save_all_tab_data()

    def _edit(self):
        if len(self._selected) != 1:
            print('Only standalone selection is supported.')
            return
        parts = self._selected[0]

        if isinstance(parts.data, button.ButtonData):
            data, _result = button_setting.SettingDialog.get_data(self, parts.data)
            if _result is not True:
                print("Cancel.")
                return None
            parts.data = data
            button.update(parts, parts.data)

        elif isinstance(parts.data, partition.PartitionData):
            data, _result = partition_setting.SettingDialog.get_data(self, parts.data)
            if _result is not True:
                print("Cancel.")
                return None
            parts.data = data

        '''
        I do not want to change the order of the widgets for XPOP, so I tried to change the drawing setting of the button with utton.update
        When the vertical and horizontal sizes are not fixed, the size of the button did not change properly.
        As a countermeasure to this, we avoid this by recreating all the parts.
        '''
        # self.repaint()
        _data = self.currentWidget().get_all_parts_dict()
        self.currentWidget().delete_all_parts()
        self.currentWidget().create_parts_from_dict(_data)

        self._set_stylesheet()
        self.save_all_tab_data()

    def _add_button(self):
        data = button.get_default()
        data.position = self._context_pos
        self.create_button(data)
        self.save_all_tab_data()
        self._set_stylesheet()

    def _add_partition(self):
        data = partition.get_default()
        data.position = self._context_pos
        self.create_partition(data)
        self.save_all_tab_data()

    def delete_parts(self, widget):
        widget.setParent(None)
        widget.deleteLater()

    def create_button(self, data):
        return self._create_parts(button_setting, button, data)

    def create_partition(self, data):
        return self._create_parts(partition_setting, partition, data)

    def _create_parts(self, ui_obj, data_obj, data):
        data, _result = ui_obj.SettingDialog.get_data(self, data)
        if _result is not True:
            print("Cancel.")
            return None
        data_obj.create(self.currentWidget(), data)
        self._selected = []
        self.repaint()
        return data

    def _button_default_setting(self):
        data = button.get_default()
        data, _result = button_setting.SettingDialog.get_data(self, data)
        if _result is not True:
            print("Cancel.")
            return None
        lib.make_save_dir()
        path = lib.get_button_default_filepath()
        lib.not_escape_json_dump(path, vars(data))

    def _partition_default_setting(self):
        data = partition.get_default()
        data, _result = partition_setting.SettingDialog.get_data(self, data)
        if _result is not True:
            print("Cancel.")
            return None
        lib.make_save_dir()
        path = lib.get_partition_default_filepath()
        lib.not_escape_json_dump(path, vars(data))

    def _xpop_setting(self):
        _w = self.currentWidget()
        ls = _w.get_all_button()
        parts, _result = xpop.XpopSettingDialog.show_dialog(self, ls)
        if _result is not True:
            print("Cancel.")
            return None
        _w.delete_all_button()
        _w.create_button_from_instance(parts)
        self._set_stylesheet()
        self.save_all_tab_data()

    # -----------------------
    # Tab
    # -----------------------
    def _delete_tab(self):
        if self.count() == 1:
            return
        _status = QtWidgets.QMessageBox.question(
            self, 'Confirmation',
            'Are you sure you want to delete the tab?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if _status == QtWidgets.QMessageBox.Yes:
            self.removeTab(self.currentIndex())
            self.save_all_tab_data()
        else:
            return

    def _rename_tab(self):
        new_tab_name, _status = QtWidgets.QInputDialog.getText(
            self,
            'Rename Tab',
            'Specify new tab name',
            QtWidgets.QLineEdit.Normal,
            self.tabText(self.currentIndex())
        )
        if not _status:
            return
        self.setTabText(self.currentIndex(), new_tab_name)
        self.save_all_tab_data()

    def _add_tab(self):
        new_tab_name, _status = QtWidgets.QInputDialog.getText(
            self,
            'Add New Tab',
            'Specify new tab name',
            QtWidgets.QLineEdit.Normal,
            'Tab{0}'.format(self.count() + 1)
        )
        if not _status:
            return
        self.insertTab(self.count() + 1, ShelfTabWeight(), new_tab_name)
        self.setCurrentIndex(self.count() + 1)
        self.save_all_tab_data()

    def _export_tab(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Export Tab',
            os.environ.get('MAYA_APP_DIR'),
            'Json Files (*.json)'
        )
        if not file_name:
            return
        root, ext = os.path.splitext(file_name[0])
        if ext != '.json':
            return
        _data = self.currentWidget().get_all_parts_dict()
        lib.not_escape_json_dump(file_name[0], _data)

    def _import_tab(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Import Tab',
            os.environ.get('MAYA_APP_DIR'),
            'Json Files (*.json)'
        )
        if not file_name:
            return
        root, ext = os.path.splitext(file_name[0])
        if ext != '.json':
            return
        _status = QtWidgets.QMessageBox.question(
            self, 'Confirmation',
            'Existing parts of the tab will be deleted. Are you sure to execute?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if _status == QtWidgets.QMessageBox.Yes:
            _data = lib.not_escape_json_load(file_name[0])
            self.currentWidget().delete_all_parts()
            self.currentWidget().create_parts_from_dict(_data)
            self._set_stylesheet()
            self.save_all_tab_data()

    def _reference_tab(self):
        _p = os.environ.get('MAYA_APP_DIR')
        if self.currentWidget().reference is not None:
            _p = self.currentWidget().reference
        else:
            # Setting up external references for the first time
            _status = QtWidgets.QMessageBox.question(
                self, 'Confirmation',
                'Existing parts of the tab will be deleted. Are you sure to execute?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )
            if _status == QtWidgets.QMessageBox.No:
                return

        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Reference Tab',
            _p,
            'Json Files (*.json)'
        )
        if not file_name:
            return
        root, ext = os.path.splitext(file_name[0])
        if ext != '.json':
            return

        icon = QtGui.QIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))
        self.setTabIcon(self.currentIndex(), icon)

        self.currentWidget().reference = file_name[0]
        _data = lib.not_escape_json_load(file_name[0])
        self.currentWidget().delete_all_parts()
        self.currentWidget().create_parts_from_dict(_data)
        self._set_stylesheet()
        self.save_all_tab_data()

    def _remove_reference_tab(self):
        if self.currentWidget().reference is not None:
            self.currentWidget().reference = None
            self.currentWidget().delete_all_parts()
            self._set_stylesheet()
            self.save_all_tab_data()
            self.setTabIcon(self.currentIndex(), QtGui.QIcon())

    # -----------------------
    # Save Load
    # -----------------------
    def load_all_tab_data(self):
        if self.load_file is None:
            path = lib.get_tab_data_path()
        else:
            path = self.load_file
        data = lib.not_escape_json_load(path)
        if data is None:
            self.insertTab(0, ShelfTabWeight(), 'Tab1')
            return

        for _vars in data:
            tab_number = self.count()
            self.insertTab(tab_number, ShelfTabWeight(), _vars['name'])

            if _vars['current'] is True:
                self.setCurrentIndex(tab_number)
            if _vars.get('reference') is None:
                self.widget(tab_number).create_parts_from_dict(_vars)
            else:
                if _vars['reference'] is None:
                    self.widget(tab_number).create_parts_from_dict(_vars)
                else:
                    icon = QtGui.QIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))
                    self.setTabIcon(tab_number, icon)
                    _data = lib.not_escape_json_load(_vars['reference'])
                    self.widget(tab_number).reference = _vars['reference']
                    self.widget(tab_number).delete_all_parts()
                    self.widget(tab_number).create_parts_from_dict(_data)

    def save_all_tab_data(self):
        if self.edit_lock is True:
            return

        ls = []
        current = self.currentIndex()
        for i in range(self.count()):
            _tab_data = {}
            _tab_data['name'] = self.tabText(i)
            _tab_data['current'] = (i == current)  # カレントタブ
            if self.widget(i).reference is None:
                _tab_data.update(self.widget(i).get_all_parts_dict())
            _tab_data['reference'] = self.widget(i).reference
            ls.append(_tab_data)

        lib.make_save_dir()
        if self.load_file is None:
            path = lib.get_tab_data_path()
        else:
            path = self.load_file
        lib.not_escape_json_dump(path, ls)

    # -----------------------
    # Event
    # -----------------------

    def dropEvent(self, event):
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return

        _mimedata = event.mimeData()

        if _mimedata.hasText() is True or _mimedata.hasUrls() is True:
            # Move the drop position to the upper left of the button
            # Consider tab height from drop position
            x = event.pos().x()
            y = event.pos().y() - self.sizeHint().height()
            if y < 0:
                y = 0
            _position = QtCore.QPoint(x, y)

            data = button.get_default()
            data.position = _position

            if _mimedata.hasText() is True:
                data.code = _mimedata.text()

            if _mimedata.hasUrls() is True:
                # Last file becomes valid for multiple files
                for url in _mimedata.urls():
                    if hasattr(url, 'path'):  # PySide
                        _path = re.sub("^/", "", url.path())
                    else:  # PySide2
                        _path = re.sub("^file:///", "", url.url())
                # If you throw in from an external editor also come around here
                if _path != '':
                    data.externalfile = _path
                    data.use_externalfile = True
                    _info = QtCore.QFileInfo(_path)
                    _suffix = _info.completeSuffix()
                    if _suffix == 'py':
                        data.script_language = 'Python'
                    elif _suffix == 'mel':
                        data.script_language = 'MEL'
                    else:
                        print('This file format is not supported.')
                        return
                    data.label = _info.completeBaseName()
                    data.code = ''

            self.create_button(data)
            self.save_all_tab_data()

        elif isinstance(event.source(), (button.ButtonWidget, partition.PartitionWidget)):

            if len(self._selected) > 1:
                # If multiple selections are made, move is prioritized collectively
                self._selected_parts_move(event.pos())
            else:
                self._parts_move(event.source(), event.pos())
                self.save_all_tab_data()
                self._origin = QtCore.QPoint()

            # I do not know well
            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()

        self._parts_moving = False
        self.repaint()

    def dragMoveEvent(self, event):
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return
        # Drawing update while moving parts
        if len(self._selected) > 0:
            self._parts_moving = True
            self._selected_parts_move(event.pos(), False, False)
        self.repaint()

    def dragEnterEvent(self, event):
        '''
        Decide whether to allow dragged objects
        Allow if dragged object is text or file
        '''
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return
        mime = event.mimeData()
        if mime.hasText() is True or mime.hasUrls() is True:
            event.accept()
        elif isinstance(event.source(), (button.ButtonWidget, partition.PartitionWidget)):
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return

        self._origin = event.pos()
        if event.button() == QtCore.Qt.LeftButton:
            self._band = QtCore.QRect()
            self._parts_moving = False

        if event.button() == QtCore.Qt.MiddleButton:
            self._select_cursor_pos_parts()
            if len(self._selected) <= 1:
                self._set_stylesheet()
        self.repaint()

    def mouseMoveEvent(self, event):
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return

        if self._band is not None:
            self._band = QtCore.QRect(self._origin, event.pos())
        else:
            # Drawing update while moving parts
            if len(self._selected) > 0:
                self._parts_moving = True
                self._selected_parts_move(event.pos(), False, False)

        self.repaint()

    def mouseReleaseEvent(self, event):
        if self.edit_lock is True or self.currentWidget().reference is not None:
            return

        if event.button() == QtCore.Qt.LeftButton:
            if not self._origin:
                self._origin = event.pos()
            rect = QtCore.QRect(self._origin, event.pos()).normalized()
            self._get_parts_in_rectangle(rect)
            self._set_stylesheet()
            self._origin = QtCore.QPoint()
            self._band = None

        # Move selected part
        if event.button() == QtCore.Qt.MiddleButton:
            self._selected_parts_move(event.pos())

        self._parts_moving = False
        self.repaint()

    def paintEvent(self, event):
        # Draw a rectangular area
        if self._band is not None:
            painter = QtGui.QPainter(self)
            color = QtGui.QColor(255, 255, 255, 125)
            pen = QtGui.QPen(color, self.PEN_WIDTH)
            painter.setPen(pen)
            painter.drawRect(self._band)
            painter.restore()
        # Draw a guide grid
        if self._parts_moving is True \
                and self._shelf_option.snap_active is True\
                and self._shelf_option.snap_grid is True:
            self._draw_snap_gide()

    def closeEvent(self, event):
        if self.edit_lock is False:
            # If it is 2017 or earlier, hideEvent makes it impossible to get information such as window size normally
            if lib.maya_api_version() < 201700:
                if self._floating_save is False:
                    lib.floating_save(self)
                self._floating_save = True
        # super because it caused an error in 2017 and is no longer in use
        # super(SiShelfWeight, self).closeEvent(event)
        QtWidgets.QWidget.close(self)

    # -----------------------
    # Others
    # -----------------------
    def _selected_parts_move(self, after_pos, save=True, data_pos_update=True):
        # Move selected part
        if len(self._selected) > 0:
            for p in self._selected:
                self._parts_move(p, after_pos, data_pos_update)
            if save is True:
                self._origin = QtCore.QPoint()
                self.save_all_tab_data()

    def _parts_move(self, parts, after_pos, data_pos_update=True):
        # Add the relative position moved during dragging
        _rect = QtCore.QRect(self._origin, after_pos)
        _x = parts.data.position_x + _rect.width()
        _y = parts.data.position_y + _rect.height()
        if _x < 0:
            _x = 0
        if _y < 0:
            _y = 0

        if self._shelf_option.snap_active is True:
            _x = int(_x / self._shelf_option.snap_width) * self._shelf_option.snap_width
            _y = int(_y / self._shelf_option.snap_height) * self._shelf_option.snap_height

        _position = QtCore.QPoint(_x, _y)
        parts.move(_position)
        if data_pos_update is True:
            parts.data.position_x = _x
            parts.data.position_y = _y

    def _get_parts_in_rectangle(self, rect):
        self._selected = []
        chidren = []
        chidren.extend(self.currentWidget().findChildren(button.ButtonWidget))
        chidren.extend(self.currentWidget().findChildren(partition.PartitionWidget))

        for child in chidren:
            # Determine whether it is located within a rectangle
            if rect.intersects(self._get_parts_absolute_geometry(child)) is False:
                continue
            self._selected.append(child)

    def _get_parts_absolute_geometry(self, parts):
        '''
        type:ShelfButton.ButtonWidget -> QtCore.QSize
        '''
        geo = parts.geometry()
        point = parts.mapTo(self, geo.topLeft())
        point -= geo.topLeft()
        geo = QtCore.QRect(point, geo.size())
        return geo

    def _set_stylesheet(self):
        css = ''

        # Tab
        css += 'QTabBar::tab { ' \
                'height: ' + str(self._shelf_option.tab_height) + 'px;' \
                'font-size: ' + str(self._shelf_option.tab_label_size) + 'pt;' \
                '}'

        # Button
        buttons = self.currentWidget().findChildren(button.ButtonWidget)
        css = lib.button_css(buttons, css)

        # Exaggerate selected parts
        if self.edit_lock is True:
            pass
        elif self.currentWidget().reference is None:
            for s in self._selected:
                css += '#' + s.objectName() + '{'
                if isinstance(s.data, button.ButtonData):
                    if s.data.use_bgcolor is True:
                        css += 'background:' + s.data.bgcolor + ';'
                css += 'border-color:red; border-style:solid; border-width:1px;}'
        self.setStyleSheet(css)

    def _select_cursor_pos_parts(self):
        '''
        If not selected multiple parts are selected directly under the mouse
        :return:
        '''
        cursor = QtGui.QCursor.pos()
        _ui = lib.get_show_repr()
        pos = QtCore.QPoint(cursor.x() - _ui['x'], cursor.y() - _ui['y'])
        # Feel that shifted the size and number of pixels to the consideration of the height of the tab bar (just the actual tab
        self._context_pos = QtCore.QPoint(pos.x(), pos.y() - self.sizeHint().height())
        # If the part is not selected as a rectangle, select the button under the mouse position
        #In the case of 1 selected state, it seems intuitive is better if you select it again
        if len(self._selected) <= 1:
            _l = len(self._selected)
            _s = self._selected

            rect = QtCore.QRect(pos, pos)
            # In the docking state it is better to consider tab height! What? What is this behavior ...
            if self.isFloating() is False and self.dockArea() is not None:
                rect = QtCore.QRect(self._context_pos, self._context_pos)
            self._get_parts_in_rectangle(rect)
            if len(self._selected) > 1:
                self._selected = [self._selected[0]]
            if _l == 1 and len(self._selected) == 0:
                self._selected = _s
            self._set_stylesheet()
            self.repaint()

    def _draw_snap_gide(self):
        # Display snap guide
        painter = QtGui.QPainter(self)
        color = QtGui.QColor(255, 255, 255, 40)
        pen = QtGui.QPen(color, )
        pen.setStyle(QtCore.Qt.DashDotLine)
        painter.setPen(pen)

        snap_unit_x = self._shelf_option.snap_width
        snap_unit_y = self._shelf_option.snap_height
        _tab_h = self.sizeHint().height() - 4

        # Horizontal line
        for i in range(self.height() / snap_unit_y):
            _h = snap_unit_y * i + _tab_h
            line = QtCore.QLine(QtCore.QPoint(0, _h), QtCore.QPoint(self.width(), _h))
            painter.drawLine(line)
        # Vertical line
        for i in range(self.width() / snap_unit_x + 1):
            _w = snap_unit_x * i + 1
            line = QtCore.QLine(QtCore.QPoint(_w, _tab_h), QtCore.QPoint(_w, self.height() + _tab_h))
            painter.drawLine(line)
        painter.restore()


class ShelfTabWeight(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ShelfTabWeight, self).__init__(parent)
        self.reference = None

    def get_all_parts_dict(self):
        # Acquire parts under specified tab
        dict_ = {}
        # Button data
        _b = []
        _ls = self.get_all_button()
        for child in _ls:
            _b.append(vars(child))
        dict_['button'] = _b

        # Partition line data
        _p = []
        _ls = self.get_all_partition()
        for child in _ls:
            _p.append(vars(child))
        dict_['partition'] = _p

        return dict_

    def create_parts_from_dict(self, data):
        if data.get('button') is not None:
            for _var in data['button']:
                # Assign to instance property from dictionary
                _d = button.ButtonData()
                for k, v in _var.items():
                    setattr(_d, k, v)
                button.create(self, _d)

        if data.get('partition') is not None:
            for _var in data['partition']:
                # Assign to instance property from dictionary
                _d = partition.PartitionData()
                for k, v in _var.items():
                    setattr(_d, k, v)
                partition.create(self, _d)

    def create_button_from_instance(self, ls):
        for _l in ls:
            button.create(self, _l)

    def delete_all_parts(self):
        self.delete_all_button()
        self.delete_all_partition()

    def delete_all_button(self):
        for child in self.findChildren(button.ButtonWidget):
            self.delete_parts(child)

    def delete_all_partition(self):
        for child in self.findChildren(partition.PartitionWidget):
            self.delete_parts(child)

    def get_all_button(self):
        ls = []
        for child in self.findChildren(button.ButtonWidget):
            ls.append(child.data)
        return ls

    def get_all_partition(self):
        ls = []
        for child in self.findChildren(partition.PartitionWidget):
            ls.append(child.data)
        return ls

    def delete_parts(self, widget):
        widget.setParent(None)
        widget.deleteLater()
# #################################################################################################


def make_ui(load_file=None, edit_lock=False):
    # Delete if window with the same name exists
    ui = lib.get_ui(lib.TITLE, 'SiShelfWeight')
    if ui is not None:
        ui.close()

    app = QtWidgets.QApplication.instance()
    ui = SiShelfWeight(load_file=load_file, edit_lock=edit_lock)
    return ui


def quit_app():
    dict = lib.get_show_repr()
    lib.make_save_dir()
    _f = open(lib.get_shelf_docking_filepath(), 'w')
    json.dump(dict, _f)
    _f.close()


def make_quit_app_job():
    pm.scriptJob(e=("quitApplication", pm.Callback(quit_app)))


def restoration_docking_ui():
    '''
    Restore docked UI
    :return:
    '''
    path = lib.get_shelf_docking_filepath()
    if os.path.isfile(path) is False:
        return
    f = open(path, 'r')
    _dict = json.load(f)
    if _dict['display'] is False:
        return
    if _dict['floating'] is False and _dict['area'] is not None:
        window = SiShelfWeight()
        window.show(
            dockable=True,
            area=_dict['area'],
            floating=_dict['floating'],
            width=_dict['width'],
            height=_dict['height']
        )


def popup():
    # Pop-up at mouse position
    cursor = QtGui.QCursor.pos()
    main(x=cursor.x(), y=cursor.y())


def main(x=None, y=None, load_file=None, edit_lock=False):
    # Display in center of screen
    ui = make_ui(load_file=load_file, edit_lock=edit_lock)
    _floating = lib.load_floating_data()
    if _floating:
        width = _floating['width']
        height = _floating['height']
    else:
        width = None
        height = None

    if lib.maya_api_version() > 201300:

        ui_script = "import sishelf.shelf;sishelf.shelf.restoration_workspacecontrol()"
        # If you use the window position of the saved data, the window of the window is not taken into consideration, so it will be shifted
        opts = {
            "dockable": True,
            "floating": True,
            "width": width,
            "height": height,
            # Although I have decided it by area: left to avoid a bug in # 2017
            # If it is less than # 2017, there is no problem because the area is reset by restoration_docking_ui
            # In 2017 there is an entity such as where you are in the workspace layout
            "area": "left",
            "allowedArea": None,
            "x": x,
            "y": y,

            # below options have been introduced at 2017
            "widthSizingProperty": None,
            "heightSizingProperty": None,
            "initWidthAsMinimum": None,
            "retain": False,
            "plugins": None,
            "controls": None,
            "uiScript": ui_script,
            "closeCallback": None
        }

        ui.setDockableParameters(**opts)

        #If it is 2017, it will be displayed as UI with the workspaceControl command, so there is no need to show
        if lib.maya_api_version() > 201700:
            ui.show()

    else:
        # 2013
        ui.show()


def restoration_workspacecontrol():
    # For reproducing workspacecontrol
    ui = make_ui()
    ui_script = "import sishelf.shelf;sishelf.shelf.restoration_workspacecontrol()"
    # If you use the window position of the saved data, the window of the window is not taken into consideration, so it will be shifted
    opts = {
        "dockable": True,
        "floating": False,
        "area": "left",
        "allowedArea": None,
        "x": None,
        "y": None,
        # below options have been introduced at 2017
        "widthSizingProperty": None,
        "heightSizingProperty": None,
        "initWidthAsMinimum": None,
        "retain": False,
        "plugins": None,
        "controls": None,
        "uiScript": ui_script,
        "closeCallback": None
    }
    ui.setDockableParameters(**opts)


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------
# EOF
#-----------------------------------------------------------------------------
