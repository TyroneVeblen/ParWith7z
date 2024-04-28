# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageForPar2Config.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_PageForPar2Config(object):
    def setupUi(self, PageForPar2Config):
        if not PageForPar2Config.objectName():
            PageForPar2Config.setObjectName(u"PageForPar2Config")
        PageForPar2Config.resize(260, 68)
        self.gridLayout = QGridLayout(PageForPar2Config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(PageForPar2Config)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(PageForPar2Config)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.retranslateUi(PageForPar2Config)

        QMetaObject.connectSlotsByName(PageForPar2Config)
    # setupUi

    def retranslateUi(self, PageForPar2Config):
        PageForPar2Config.setWindowTitle(QCoreApplication.translate("PageForPar2Config", u"Par2\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PageForPar2Config", u"Par2\u5757\u5927\u5c0f(KB)\uff1a", None))
    # retranslateUi

