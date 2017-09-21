## -*- coding: utf-8 -*-
from.vendor.Qt import QtCore, QtGui, QtWidgets

from . import lib


class PartitionWidget(QtWidgets.QWidget):

    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        super(PartitionWidget, self).__init__(parent)

    def mouseMoveEvent(self, event):
        # Make drag & drop possible only by middle click
        if event.buttons() != QtCore.Qt.MidButton:
            return
        # Assign data format to be dragged and dropped
        mimedata = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimedata)
        drag.exec_(QtCore.Qt.MoveAction)

    def paintEvent(self, event):
        # Use style sheet
        super(PartitionWidget, self).paintEvent(event)
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        p = QtGui.QPainter(self)
        s = self.style()
        s.drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, p, self)

        # Draw labels and lines
        painter = QtGui.QPainter(self)

        color = QtGui.QColor(self.data.color)
        pen = QtGui.QPen(color, self.data.line_width)
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setPointSize(self.data.label_font_size)
        painter.setFont(font)

        # Calculate the size of the widget Calculate the top, bottom, left and right margin
        _w = self.data.line_length
        _h = self.data.margin + int(self.data.line_width * 1.5)
        if self.data.use_label is True:
            fm = painter.fontMetrics()
            if _w < fm.width(self.data.label):
                _w = fm.width(self.data.label)
            if _h < fm.height():
                _h = fm.height()
        _w += self.data.margin * 2
        _h += self.data.margin * 2

        # Calculate placement point of line
        _line_start_point = self.data.margin
        _line_end_point = self.data.line_length + self.data.margin

        if self.data.style == 0:
            # Level
            self.resize(_w, _h)
            if self.data.use_label is True:
                _line_height_point = self.data.label_font_size + round(self.data.margin + self.data.line_width / 2)
            else:
                _line_height_point = self.data.margin + round(self.data.line_width / 2)

            line = QtCore.QLine(
                QtCore.QPoint(_line_start_point, _line_height_point),
                QtCore.QPoint(_line_end_point, _line_height_point)
            )
            painter.drawLine(line)

            if self.data.use_label is True:
                painter.drawText(QtCore.QPoint(0,  self.data.label_font_size), self.data.label)

        elif self.data.style == 1:
            # Vertical
            self.resize(_h, _w)
            line = QtCore.QLine(
                QtCore.QPoint(self.data.margin, _line_start_point),
                QtCore.QPoint(self.data.margin, _line_end_point)
            )
            painter.drawLine(line)
            if self.data.use_label is True:
                painter.rotate(90)
                _p = QtCore.QPoint(self.data.margin, -self.data.margin * 2 - round(self.data.line_width / 2))
                painter.drawText(_p, self.data.label)


class PartitionData(lib.PartsData):
    def __init__(self):
        super(PartitionData, self).__init__()
        self.color = '#aaaaaa'
        self.style = 0 # 0: level 1: vertical
        self.line_width = 1
        self.line_length = 150
        self.margin = 2


def create(parent, data):
    widget = PartitionWidget(parent, data)
    widget.setObjectName(lib.random_string(15))
    widget.show()
    widget.move(data.position)
    return widget


def get_default():
    path = lib.get_partition_default_filepath()
    data = PartitionData()
    js = lib.not_escape_json_load(path)
    if js is not None:
        for k, v in js.items():
            setattr(data, k, v)
    return data

#-----------------------------------------------------------------------------
# EOF
#-----------------------------------------------------------------------------
