# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageForPar2Config.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_PageForPar2Config(object):
    def setupUi(self, PageForPar2Config):
        if not PageForPar2Config.objectName():
            PageForPar2Config.setObjectName(u"PageForPar2Config")
        PageForPar2Config.resize(260, 110)
        self.gridLayout = QGridLayout(PageForPar2Config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(PageForPar2Config)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.par2_block_size = QLineEdit(PageForPar2Config)
        self.par2_block_size.setObjectName(u"par2_block_size")

        self.horizontalLayout_2.addWidget(self.par2_block_size)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_settings = QPushButton(PageForPar2Config)
        self.save_settings.setObjectName(u"save_settings")

        self.horizontalLayout.addWidget(self.save_settings)

        self.cancel_settings = QPushButton(PageForPar2Config)
        self.cancel_settings.setObjectName(u"cancel_settings")

        self.horizontalLayout.addWidget(self.cancel_settings)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(PageForPar2Config)

        QMetaObject.connectSlotsByName(PageForPar2Config)
    # setupUi

    def retranslateUi(self, PageForPar2Config):
        PageForPar2Config.setWindowTitle(QCoreApplication.translate("PageForPar2Config", u"Par2\u914d\u7f6e", None))
        self.label.setText(QCoreApplication.translate("PageForPar2Config", u"Par2\u5757\u5927\u5c0f(KB)\uff1a", None))
        self.save_settings.setText(QCoreApplication.translate("PageForPar2Config", u"\u4fdd\u5b58", None))
        self.cancel_settings.setText(QCoreApplication.translate("PageForPar2Config", u"\u53d6\u6d88", None))
    # retranslateUi

