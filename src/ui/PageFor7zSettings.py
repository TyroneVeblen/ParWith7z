# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageFor7zSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_PageFor7zSettings(object):
    def setupUi(self, PageFor7zSettings):
        if not PageFor7zSettings.objectName():
            PageFor7zSettings.setObjectName(u"PageFor7zSettings")
        PageFor7zSettings.resize(296, 331)
        self.gridLayout_3 = QGridLayout(PageFor7zSettings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(PageFor7zSettings)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.is_delete_file_after_compress = QCheckBox(self.groupBox)
        self.is_delete_file_after_compress.setObjectName(u"is_delete_file_after_compress")
        self.is_delete_file_after_compress.setLayoutDirection(Qt.LeftToRight)
        self.is_delete_file_after_compress.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.is_delete_file_after_compress, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.compress_level = QComboBox(self.groupBox)
        self.compress_level.addItem("")
        self.compress_level.addItem("")
        self.compress_level.addItem("")
        self.compress_level.setObjectName(u"compress_level")

        self.gridLayout.addWidget(self.compress_level, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.volume_size = QLineEdit(self.groupBox)
        self.volume_size.setObjectName(u"volume_size")

        self.gridLayout.addWidget(self.volume_size, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.is_encrypted_file_name = QCheckBox(self.groupBox)
        self.is_encrypted_file_name.setObjectName(u"is_encrypted_file_name")

        self.gridLayout.addWidget(self.is_encrypted_file_name, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.is_folder_only = QCheckBox(self.groupBox)
        self.is_folder_only.setObjectName(u"is_folder_only")

        self.gridLayout.addWidget(self.is_folder_only, 4, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.path_recursion_depth = QLineEdit(self.groupBox)
        self.path_recursion_depth.setObjectName(u"path_recursion_depth")

        self.gridLayout.addWidget(self.path_recursion_depth, 5, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(PageFor7zSettings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.is_delete_file_after_decompress = QCheckBox(self.groupBox_2)
        self.is_delete_file_after_decompress.setObjectName(u"is_delete_file_after_decompress")
        self.is_delete_file_after_decompress.setLayoutDirection(Qt.LeftToRight)
        self.is_delete_file_after_decompress.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.is_delete_file_after_decompress, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.is_create_subfolder = QCheckBox(self.groupBox_2)
        self.is_create_subfolder.setObjectName(u"is_create_subfolder")
        self.is_create_subfolder.setLayoutDirection(Qt.LeftToRight)
        self.is_create_subfolder.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.is_create_subfolder, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.is_test_zip_first = QCheckBox(self.groupBox_2)
        self.is_test_zip_first.setObjectName(u"is_test_zip_first")

        self.gridLayout_2.addWidget(self.is_test_zip_first, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_settings = QPushButton(PageFor7zSettings)
        self.save_settings.setObjectName(u"save_settings")

        self.horizontalLayout.addWidget(self.save_settings)

        self.cancel_settings = QPushButton(PageFor7zSettings)
        self.cancel_settings.setObjectName(u"cancel_settings")

        self.horizontalLayout.addWidget(self.cancel_settings)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(PageFor7zSettings)

        QMetaObject.connectSlotsByName(PageFor7zSettings)
    # setupUi

    def retranslateUi(self, PageFor7zSettings):
        PageFor7zSettings.setWindowTitle(QCoreApplication.translate("PageFor7zSettings", u"7z\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("PageFor7zSettings", u"\u538b\u7f29", None))
        self.label.setText(QCoreApplication.translate("PageFor7zSettings", u"\u89e3\u538b\u5b8c\u6210\u540e\u5220\u9664\u6e90\u6587\u4ef6\uff1a", None))
        self.is_delete_file_after_compress.setText("")
        self.label_2.setText(QCoreApplication.translate("PageFor7zSettings", u"\u538b\u7f29\u7b49\u7ea7\uff1a", None))
        self.compress_level.setItemText(0, QCoreApplication.translate("PageFor7zSettings", u"0 \u4ec5\u5b58\u50a8", None))
        self.compress_level.setItemText(1, QCoreApplication.translate("PageFor7zSettings", u"5 \u6807\u51c6\u538b\u7f29", None))
        self.compress_level.setItemText(2, QCoreApplication.translate("PageFor7zSettings", u"9 \u6781\u9650\u538b\u7f29", None))

        self.label_3.setText(QCoreApplication.translate("PageFor7zSettings", u"\u5206\u5377\u5927\u5c0f(MB)\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("PageFor7zSettings", u"\u52a0\u5bc6\u6587\u4ef6\u540d\uff1a", None))
        self.is_encrypted_file_name.setText("")
        self.label_7.setText(QCoreApplication.translate("PageFor7zSettings", u"\u4ec5\u6587\u4ef6\u5939\u6a21\u5f0f\uff1a", None))
        self.is_folder_only.setText("")
        self.label_8.setText(QCoreApplication.translate("PageFor7zSettings", u"\u8def\u5f84\u9012\u5f52\u6df1\u5ea6\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PageFor7zSettings", u"\u89e3\u538b", None))
        self.label_5.setText(QCoreApplication.translate("PageFor7zSettings", u"\u89e3\u538b\u5b8c\u6210\u540e\u5220\u9664\u6e90\u6587\u4ef6\uff1a", None))
        self.is_delete_file_after_decompress.setText("")
        self.label_6.setText(QCoreApplication.translate("PageFor7zSettings", u"\u521b\u5efa\u5b50\u6587\u4ef6\u5939\uff1a", None))
        self.is_create_subfolder.setText("")
        self.label_9.setText(QCoreApplication.translate("PageFor7zSettings", u"\u9996\u5148\u6d4b\u8bd5\u538b\u7f29\u5305\uff1a", None))
        self.is_test_zip_first.setText("")
        self.save_settings.setText(QCoreApplication.translate("PageFor7zSettings", u"\u4fdd\u5b58", None))
        self.cancel_settings.setText(QCoreApplication.translate("PageFor7zSettings", u"\u53d6\u6d88", None))
    # retranslateUi

