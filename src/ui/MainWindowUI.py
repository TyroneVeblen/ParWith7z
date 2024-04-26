# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 382)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action.setCheckable(False)
        self.action.setChecked(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.select_files = QPushButton(self.centralwidget)
        self.select_files.setObjectName(u"select_files")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_files.sizePolicy().hasHeightForWidth())
        self.select_files.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.select_files, 0, 1, 1, 1)

        self.select_folders = QPushButton(self.centralwidget)
        self.select_folders.setObjectName(u"select_folders")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_folders.sizePolicy().hasHeightForWidth())
        self.select_folders.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.select_folders, 1, 1, 1, 1)

        self.unzip_or_zip = QComboBox(self.centralwidget)
        self.unzip_or_zip.addItem("")
        self.unzip_or_zip.addItem("")
        self.unzip_or_zip.setObjectName(u"unzip_or_zip")

        self.gridLayout.addWidget(self.unzip_or_zip, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.customized_parameters_edit = QLineEdit(self.centralwidget)
        self.customized_parameters_edit.setObjectName(u"customized_parameters_edit")
        self.customized_parameters_edit.setFocusPolicy(Qt.ClickFocus)
        self.customized_parameters_edit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.customized_parameters_edit, 0, 3, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.config_for_7z = QToolButton(self.centralwidget)
        self.config_for_7z.setObjectName(u"config_for_7z")
        sizePolicy.setHeightForWidth(self.config_for_7z.sizePolicy().hasHeightForWidth())
        self.config_for_7z.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.config_for_7z, 0, 4, 1, 1)

        self.comfig_for_par2 = QToolButton(self.centralwidget)
        self.comfig_for_par2.setObjectName(u"comfig_for_par2")

        self.gridLayout.addWidget(self.comfig_for_par2, 1, 4, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 4)
        self.gridLayout.setColumnStretch(4, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.start_and_end = QPushButton(self.centralwidget)
        self.start_and_end.setObjectName(u"start_and_end")
        sizePolicy1.setHeightForWidth(self.start_and_end.sizePolicy().hasHeightForWidth())
        self.start_and_end.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.start_and_end)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 506, 23))
        self.settings = QMenu(self.menubar)
        self.settings.setObjectName(u"settings")
        self.settings.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.settings.menuAction())
        self.settings.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u914d\u7f6e", None))
        self.select_files.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.select_folders.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.unzip_or_zip.setItemText(0, QCoreApplication.translate("MainWindow", u"\u89e3\u538b", None))
        self.unzip_or_zip.setItemText(1, QCoreApplication.translate("MainWindow", u"\u538b\u7f29", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u5305\u5bc6\u7801\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"par2\u6821\u9a8c\u767e\u5206\u6bd4:", None))
        self.config_for_7z.setText(QCoreApplication.translate("MainWindow", u"7z\u914d\u7f6e", None))
        self.comfig_for_par2.setText(QCoreApplication.translate("MainWindow", u"par2\u914d\u7f6e", None))
        self.start_and_end.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

