# -*- coding: utf-8 -*-

from ..vendor import Qt
from ..vendor.Qt import QtCore, QtWidgets, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(524, 611)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonbox = QtWidgets.QDialogButtonBox(Form)
        self.buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonbox.setObjectName("buttonbox")
        self.gridLayout.addWidget(self.buttonbox, 1, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_ScriptCommands = QtWidgets.QGroupBox(Form)
        self.groupBox_ScriptCommands.setObjectName("groupBox_ScriptCommands")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_ScriptCommands)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_script_language = QtWidgets.QLabel(self.groupBox_ScriptCommands)
        self.label_script_language.setObjectName("label_script_language")
        self.horizontalLayout.addWidget(self.label_script_language)
        self.combo_script_language = QtWidgets.QComboBox(self.groupBox_ScriptCommands)
        self.combo_script_language.setObjectName("combo_script_language")
        self.combo_script_language.addItem("")
        self.combo_script_language.addItem("")
        self.horizontalLayout.addWidget(self.combo_script_language)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.text_script_code = QtWidgets.QTextEdit(self.groupBox_ScriptCommands)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_script_code.sizePolicy().hasHeightForWidth())
        self.text_script_code.setSizePolicy(sizePolicy)
        self.text_script_code.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_script_code.setObjectName("text_script_code")
        self.verticalLayout_4.addWidget(self.text_script_code)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkbox_externalfile = QtWidgets.QCheckBox(self.groupBox_ScriptCommands)
        self.checkbox_externalfile.setObjectName("checkbox_externalfile")
        self.horizontalLayout_10.addWidget(self.checkbox_externalfile)
        self.line_externalfile = QtWidgets.QLineEdit(self.groupBox_ScriptCommands)
        self.line_externalfile.setObjectName("line_externalfile")
        self.horizontalLayout_10.addWidget(self.line_externalfile)
        self.button_externalfile = QtWidgets.QToolButton(self.groupBox_ScriptCommands)
        self.button_externalfile.setObjectName("button_externalfile")
        self.horizontalLayout_10.addWidget(self.button_externalfile)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_ScriptCommands)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_preview = QtWidgets.QHBoxLayout()
        self.button_preview.setObjectName("button_preview")
        self.horizontalLayout_9.addLayout(self.button_preview)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinbox_btn_position_x = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_btn_position_x.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_btn_position_x.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinbox_btn_position_x.setMaximum(9999)
        self.spinbox_btn_position_x.setObjectName("spinbox_btn_position_x")
        self.horizontalLayout_5.addWidget(self.spinbox_btn_position_x)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spinbox_btn_position_y = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_btn_position_y.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_btn_position_y.setMaximum(9999)
        self.spinbox_btn_position_y.setObjectName("spinbox_btn_position_y")
        self.horizontalLayout_5.addWidget(self.spinbox_btn_position_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.checkbox_fix_size = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_fix_size.setObjectName("checkbox_fix_size")
        self.horizontalLayout_2.addWidget(self.checkbox_fix_size)
        self.spinbox_width = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_width.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_width.setMaximum(9999)
        self.spinbox_width.setObjectName("spinbox_width")
        self.horizontalLayout_2.addWidget(self.spinbox_width)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinbox_height = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_height.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_height.setMaximum(9999)
        self.spinbox_height.setObjectName("spinbox_height")
        self.horizontalLayout_2.addWidget(self.spinbox_height)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinbox_label_font_size = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinbox_label_font_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_label_font_size.setObjectName("spinbox_label_font_size")
        self.horizontalLayout_3.addWidget(self.spinbox_label_font_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.checkbox_use_label = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_use_label.setText("")
        self.checkbox_use_label.setChecked(True)
        self.checkbox_use_label.setObjectName("checkbox_use_label")
        self.horizontalLayout_4.addWidget(self.checkbox_use_label)
        self.label_label = QtWidgets.QLabel(self.groupBox_2)
        self.label_label.setObjectName("label_label")
        self.horizontalLayout_4.addWidget(self.label_label)
        self.text_label = QtWidgets.QTextEdit(self.groupBox_2)
        self.text_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_label.sizePolicy().hasHeightForWidth())
        self.text_label.setSizePolicy(sizePolicy)
        self.text_label.setMaximumSize(QtCore.QSize(160, 50))
        self.text_label.setObjectName("text_label")
        self.horizontalLayout_4.addWidget(self.text_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_tooltip = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_tooltip.sizePolicy().hasHeightForWidth())
        self.text_tooltip.setSizePolicy(sizePolicy)
        self.text_tooltip.setMaximumSize(QtCore.QSize(160, 30))
        self.text_tooltip.setObjectName("text_tooltip")
        self.verticalLayout_3.addWidget(self.text_tooltip)
        self.checkbox_tooltip = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_tooltip.setChecked(True)
        self.checkbox_tooltip.setObjectName("checkbox_tooltip")
        self.verticalLayout_3.addWidget(self.checkbox_tooltip)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.checkbox_label_color = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_label_color.setText("")
        self.checkbox_label_color.setObjectName("checkbox_label_color")
        self.horizontalLayout_12.addWidget(self.checkbox_label_color)
        self.button_label_color = QtWidgets.QPushButton(self.groupBox_2)
        self.button_label_color.setObjectName("button_label_color")
        self.horizontalLayout_12.addWidget(self.button_label_color)
        spacerItem7 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.checkbox_bgcolor = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkbox_bgcolor.setMinimumSize(QtCore.QSize(0, 0))
        self.checkbox_bgcolor.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkbox_bgcolor.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_bgcolor.setText("")
        self.checkbox_bgcolor.setObjectName("checkbox_bgcolor")
        self.horizontalLayout_12.addWidget(self.checkbox_bgcolor)
        self.button_bgcolor = QtWidgets.QPushButton(self.groupBox_2)
        self.button_bgcolor.setObjectName("button_bgcolor")
        self.horizontalLayout_12.addWidget(self.button_bgcolor)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.line_icon_file = QtWidgets.QLineEdit(self.groupBox)
        self.line_icon_file.setObjectName("line_icon_file")
        self.horizontalLayout_8.addWidget(self.line_icon_file)
        self.button_icon = QtWidgets.QToolButton(self.groupBox)
        self.button_icon.setObjectName("button_icon")
        self.horizontalLayout_8.addWidget(self.button_icon)
        self.button_maya_icon = QtWidgets.QToolButton(self.groupBox)
        self.button_maya_icon.setText("")
        self.button_maya_icon.setAutoRaise(True)
        self.button_maya_icon.setObjectName("button_maya_icon")
        self.horizontalLayout_8.addWidget(self.button_maya_icon)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkbox_use_icon = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_use_icon.setObjectName("checkbox_use_icon")
        self.horizontalLayout_11.addWidget(self.checkbox_use_icon)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.combo_icon_style = QtWidgets.QComboBox(self.groupBox)
        self.combo_icon_style.setObjectName("combo_icon_style")
        self.combo_icon_style.addItem("")
        self.combo_icon_style.addItem("")
        self.horizontalLayout_11.addWidget(self.combo_icon_style)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.spinbox_icon_size = QtWidgets.QSpinBox(self.groupBox)
        self.spinbox_icon_size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinbox_icon_size.setMaximum(9999)
        self.spinbox_icon_size.setObjectName("spinbox_icon_size")
        self.horizontalLayout_11.addWidget(self.spinbox_icon_size)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(Qt.QtCompat.translate("Form", "Form", None, -1))
        self.groupBox_ScriptCommands.setTitle(Qt.QtCompat.translate("Form", "Script Commands", None, -1))
        self.label_script_language.setText(Qt.QtCompat.translate("Form", "Scripting Language", None, -1))
        self.combo_script_language.setItemText(0, Qt.QtCompat.translate("Form", "MEL", None, -1))
        self.combo_script_language.setItemText(1, Qt.QtCompat.translate("Form", "Python", None, -1))
        self.checkbox_externalfile.setText(Qt.QtCompat.translate("Form", "External File", None, -1))
        self.button_externalfile.setText(Qt.QtCompat.translate("Form", "...", None, -1))
        self.groupBox_2.setTitle(Qt.QtCompat.translate("Form", "Button", None, -1))
        self.label_7.setText(Qt.QtCompat.translate("Form", "Position ", None, -1))
        self.label_6.setText(Qt.QtCompat.translate("Form", "×", None, -1))
        self.checkbox_fix_size.setText(Qt.QtCompat.translate("Form", "FixSize", None, -1))
        self.label_3.setText(Qt.QtCompat.translate("Form", "×", None, -1))
        self.label_4.setText(Qt.QtCompat.translate("Form", "Label Font Size ", None, -1))
        self.label_label.setText(Qt.QtCompat.translate("Form", "Label ", None, -1))
        self.text_label.setHtml(Qt.QtCompat.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Button</p></body></html>", None, -1))
        self.label.setText(Qt.QtCompat.translate("Form", "Tooltip ", None, -1))
        self.checkbox_tooltip.setText(Qt.QtCompat.translate("Form", "Same as code", None, -1))
        self.button_label_color.setText(Qt.QtCompat.translate("Form", "LabelColor", None, -1))
        self.button_bgcolor.setText(Qt.QtCompat.translate("Form", "BackgroundColor", None, -1))
        self.groupBox.setTitle(Qt.QtCompat.translate("Form", "Icon", None, -1))
        self.label_8.setText(Qt.QtCompat.translate("Form", "File", None, -1))
        self.button_icon.setText(Qt.QtCompat.translate("Form", "...", None, -1))
        self.checkbox_use_icon.setText(Qt.QtCompat.translate("Form", "Use Icon", None, -1))
        self.label_5.setText(Qt.QtCompat.translate("Form", "Style ", None, -1))
        self.combo_icon_style.setItemText(0, Qt.QtCompat.translate("Form", "[ Icon ]Left  [ Label ]Right", None, -1))
        self.combo_icon_style.setItemText(1, Qt.QtCompat.translate("Form", "[ Icon ]Up  [ Label ]Under", None, -1))
        self.label_2.setText(Qt.QtCompat.translate("Form", " Size ", None, -1))

