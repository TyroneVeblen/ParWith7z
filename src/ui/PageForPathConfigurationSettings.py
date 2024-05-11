# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageForPathConfigurationSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PageForPathConfigurationSettings(object):
    def setupUi(self, PageForPathConfigurationSettings):
        if not PageForPathConfigurationSettings.objectName():
            PageForPathConfigurationSettings.setObjectName(u"PageForPathConfigurationSettings")
        PageForPathConfigurationSettings.resize(518, 152)
        self.verticalLayout_2 = QVBoxLayout(PageForPathConfigurationSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(PageForPathConfigurationSettings)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.SevenZip_bin_path = QLineEdit(PageForPathConfigurationSettings)
        self.SevenZip_bin_path.setObjectName(u"SevenZip_bin_path")

        self.gridLayout.addWidget(self.SevenZip_bin_path, 0, 1, 1, 1)

        self.select_7z_bin_file = QPushButton(PageForPathConfigurationSettings)
        self.select_7z_bin_file.setObjectName(u"select_7z_bin_file")

        self.gridLayout.addWidget(self.select_7z_bin_file, 0, 2, 1, 1)

        self.label_2 = QLabel(PageForPathConfigurationSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.par2_bin_path = QLineEdit(PageForPathConfigurationSettings)
        self.par2_bin_path.setObjectName(u"par2_bin_path")

        self.gridLayout.addWidget(self.par2_bin_path, 1, 1, 1, 1)

        self.select_par2_bin_file = QPushButton(PageForPathConfigurationSettings)
        self.select_par2_bin_file.setObjectName(u"select_par2_bin_file")

        self.gridLayout.addWidget(self.select_par2_bin_file, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save = QPushButton(PageForPathConfigurationSettings)
        self.save.setObjectName(u"save")

        self.horizontalLayout.addWidget(self.save)

        self.cancel = QPushButton(PageForPathConfigurationSettings)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(PageForPathConfigurationSettings)

        QMetaObject.connectSlotsByName(PageForPathConfigurationSettings)
    # setupUi

    def retranslateUi(self, PageForPathConfigurationSettings):
        PageForPathConfigurationSettings.setWindowTitle(QCoreApplication.translate("PageForPathConfigurationSettings", u"\u53ef\u6267\u884c\u6587\u4ef6\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"7z\u53ef\u6267\u884c\u6587\u4ef6\u8def\u5f84:", None))
        self.select_7z_bin_file.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"\u9009\u62e9\u8def\u5f84...", None))
        self.label_2.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"par2\u53ef\u6267\u884c\u6587\u4ef6\u8def\u5f84:", None))
        self.select_par2_bin_file.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"\u9009\u62e9\u8def\u5f84...", None))
        self.save.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"\u4fdd\u5b58", None))
        self.cancel.setText(QCoreApplication.translate("PageForPathConfigurationSettings", u"\u53d6\u6d88", None))
    # retranslateUi

