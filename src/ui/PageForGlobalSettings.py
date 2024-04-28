# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageForGlobalSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_PageForGlobalSettings(object):
    def setupUi(self, PageForGlobalSettings):
        if not PageForGlobalSettings.objectName():
            PageForGlobalSettings.setObjectName(u"PageForGlobalSettings")
        PageForGlobalSettings.resize(281, 102)
        self.gridLayout = QGridLayout(PageForGlobalSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(PageForGlobalSettings)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(PageForGlobalSettings)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(PageForGlobalSettings)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(PageForGlobalSettings)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalLayout.setStretch(0, 5)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(PageForGlobalSettings)

        QMetaObject.connectSlotsByName(PageForGlobalSettings)
    # setupUi

    def retranslateUi(self, PageForGlobalSettings):
        PageForGlobalSettings.setWindowTitle(QCoreApplication.translate("PageForGlobalSettings", u"\u5168\u5c40\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PageForGlobalSettings", u"\u7f13\u5b58\u76ee\u5f55:", None))
        self.pushButton.setText(QCoreApplication.translate("PageForGlobalSettings", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("PageForGlobalSettings", u"\u53d6\u6d88", None))
    # retranslateUi

