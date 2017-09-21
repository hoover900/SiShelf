## -*- coding: utf-8 -*-
import functools

from .vendor.Qt import QtWidgets, QtCore
from . import partition
from .gui import partition_setting_ui


class SettingDialog(QtWidgets.QDialog, partition_setting_ui.Ui_Form):
    def __init__(self, parent, data):
        super(SettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Partition Setting")

        # Dialog OK / Cancel button
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)

        self._data_input(data)
        self._preview_partition_drawing()

        # Setting the callback function
        func = self._redraw_ui
        self.spinbox_label_font_size.valueChanged.connect(func)

        self.spinbox_line_length.valueChanged.connect(func)
        self.spinbox_line_width.valueChanged.connect(func)

        self.checkbox_use_label.stateChanged.connect(func)
        self.combo_style.currentIndexChanged.connect(func)

        '''
        There was a case that Maya crashed while entering Japanese into the text area (IME uncertain state).
        Stop textChanged.connect, for example by pressing focusOut or enter key press to firing conditions
        '''
        # self.line_label.textChanged.connect(func)

        def _focus_out(event):
            self._redraw_ui()

        def _key_press(event, widget=None):
            QtWidgets.QLineEdit.keyPressEvent(widget, event)

            key = event.key()
            print key
            if (key == QtCore.Qt.Key_Enter) or (key == QtCore.Qt.Key_Return):
                self._redraw_ui()

        self.line_label.focusOutEvent = _focus_out
        self.line_label.keyPressEvent = functools.partial(_key_press, widget=self.line_label)
        self.line_label.setToolTip('It will be reflected in the preview when focus is out.')

        self.button_color.clicked.connect(self._select_color)

    def _redraw_ui(self):
        self._preview_partition_drawing()

    def _select_color(self):
        color = QtWidgets.QColorDialog.getColor(self.color, self)
        if color.isValid():
            self.color = color.name()
            self._preview_partition_drawing()

    def _data_input(self, data):
        # Enter data
        self.line_label.setText(data.label)

        self.spinbox_btn_position_x.setValue(data.position_x)
        self.spinbox_btn_position_y.setValue(data.position_y)

        self.checkbox_use_label.setChecked(data.use_label)
        self.combo_style.setCurrentIndex(data.style)

        self.spinbox_label_font_size.setValue(data.label_font_size)

        self.color = data.color

        self.spinbox_line_length.setValue(data.line_length)
        self.spinbox_line_width.setValue(data.line_width)

    def _preview_partition_drawing(self):
        for child in self.findChildren(partition.PartitionWidget):
            child.setParent(None)
            child.deleteLater()
        parts = partition.create(self, self.get_partition_data_instance())
        parts.position_x = 10
        self.button_preview.addWidget(parts)

    def get_partition_data_instance(self):
        data = partition.PartitionData()
        data.label = self.line_label.text()

        data.position_x = self.spinbox_btn_position_x.value()
        data.position_y = self.spinbox_btn_position_y.value()

        data.use_label = self.checkbox_use_label.isChecked()
        data.style = self.combo_style.currentIndex()

        data.line_length = self.spinbox_line_length.value()
        data.line_width = self.spinbox_line_width.value()

        data.label_font_size = self.spinbox_label_font_size.value()

        data.color = self.color

        return data

    @staticmethod
    def get_data(parent=None, data=None):
        '''
        Open a modal dialog and return button setting and OK cancel
        '''
        dialog = SettingDialog(parent, data)
        result = dialog.exec_()   # Opens a dialog
        data = dialog.get_partition_data_instance()
        return (data, result == QtWidgets.QDialog.Accepted)



#-----------------------------------------------------------------------------
# EOF
#-----------------------------------------------------------------------------
