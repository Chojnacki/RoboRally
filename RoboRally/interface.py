# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_interface_ihm(object):
    def setupUi(self, interface_ihm):
        interface_ihm.setObjectName(_fromUtf8("interface_ihm"))
        interface_ihm.resize(1406, 900)
        interface_ihm.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtGui.QWidget(interface_ihm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(390, 700, 141, 82))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.progress_pv = QtGui.QProgressBar(self.formLayoutWidget)
        self.progress_pv.setMaximum(9)
        self.progress_pv.setProperty("value", 9)
        self.progress_pv.setObjectName(_fromUtf8("progress_pv"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.progress_pv)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 750, 160, 70))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.bouton_partie = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.bouton_partie.setObjectName(_fromUtf8("bouton_partie"))
        self.verticalLayout_2.addWidget(self.bouton_partie)
        self.Quitter = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.Quitter.setObjectName(_fromUtf8("Quitter"))
        self.verticalLayout_2.addWidget(self.Quitter)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(860, 640, 411, 201))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.choixcarte = QtGui.QTextEdit(self.gridLayoutWidget_2)
        self.choixcarte.setObjectName(_fromUtf8("choixcarte"))
        self.gridLayout_2.addWidget(self.choixcarte, 2, 0, 1, 1)
        self.bouton_instru = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.bouton_instru.setObjectName(_fromUtf8("bouton_instru"))
        self.gridLayout_2.addWidget(self.bouton_instru, 3, 0, 1, 1)
        self.nbjoueur = QtGui.QSpinBox(self.centralwidget)
        self.nbjoueur.setGeometry(QtCore.QRect(140, 650, 64, 33))
        self.nbjoueur.setMinimum(1)
        self.nbjoueur.setMaximum(4)
        self.nbjoueur.setObjectName(_fromUtf8("nbjoueur"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 660, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(910, 400, 81, 26))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(1110, 400, 81, 26))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_8 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(1010, 600, 81, 26))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_9 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(1110, 600, 81, 26))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(1010, 400, 81, 26))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(1120, 200, 81, 26))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_7 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(910, 600, 81, 26))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(1010, 200, 81, 26))
        self.checkBox_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBox_2.setAcceptDrops(False)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_1 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(910, 200, 78, 26))
        self.checkBox_1.setMouseTracking(True)
        self.checkBox_1.setAutoFillBackground(False)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        interface_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(interface_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1406, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIchier = QtGui.QMenu(self.menubar)
        self.menuFIchier.setObjectName(_fromUtf8("menuFIchier"))
        interface_ihm.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(interface_ihm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        interface_ihm.setStatusBar(self.statusbar)
        self.actionQuitter = QtGui.QAction(interface_ihm)
        self.actionQuitter.setCheckable(False)
        self.actionQuitter.setChecked(False)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionSolo = QtGui.QAction(interface_ihm)
        self.actionSolo.setObjectName(_fromUtf8("actionSolo"))
        self.actionMultijoueur = QtGui.QAction(interface_ihm)
        self.actionMultijoueur.setObjectName(_fromUtf8("actionMultijoueur"))
        self.actionIntelligence_Artificielle = QtGui.QAction(interface_ihm)
        self.actionIntelligence_Artificielle.setObjectName(_fromUtf8("actionIntelligence_Artificielle"))
        self.menuFIchier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFIchier.menuAction())

        self.retranslateUi(interface_ihm)
        QtCore.QObject.connect(self.Quitter, QtCore.SIGNAL(_fromUtf8("clicked()")), interface_ihm.close)
        QtCore.QObject.connect(self.actionQuitter, QtCore.SIGNAL(_fromUtf8("triggered()")), interface_ihm.close)
        QtCore.QMetaObject.connectSlotsByName(interface_ihm)

    def retranslateUi(self, interface_ihm):
        interface_ihm.setWindowTitle(_translate("interface_ihm", "RoboRally", None))
        self.progress_pv.setFormat(_translate("interface_ihm", "%v/%m", None))
        self.lineEdit.setText(_translate("interface_ihm", "KerTwonkaradec", None))
        self.bouton_partie.setText(_translate("interface_ihm", "Nouvelle partie", None))
        self.Quitter.setText(_translate("interface_ihm", "Quitter", None))
        self.plainTextEdit.setPlainText(_translate("interface_ihm", "Lancez une partie\n"
"choisissez 5 cartes differentes\n"
"puis envoyez les instructions au robot !", None))
        self.choixcarte.setHtml(_translate("interface_ihm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bouton_instru.setText(_translate("interface_ihm", "Envoyer les instructions au robot", None))
        self.bouton_instru.setShortcut(_translate("interface_ihm", "Enter", None))
        self.label_2.setText(_translate("interface_ihm", "Nombre de joueurs", None))
        self.checkBox_4.setText(_translate("interface_ihm", "Carte 4", None))
        self.checkBox_4.setShortcut(_translate("interface_ihm", "4", None))
        self.checkBox_6.setText(_translate("interface_ihm", "Carte 6", None))
        self.checkBox_6.setShortcut(_translate("interface_ihm", "6", None))
        self.checkBox_8.setText(_translate("interface_ihm", "Carte 8", None))
        self.checkBox_8.setShortcut(_translate("interface_ihm", "8", None))
        self.checkBox_9.setText(_translate("interface_ihm", "Carte 9", None))
        self.checkBox_9.setShortcut(_translate("interface_ihm", "9", None))
        self.checkBox_5.setText(_translate("interface_ihm", "Carte 5", None))
        self.checkBox_5.setShortcut(_translate("interface_ihm", "5", None))
        self.checkBox_3.setText(_translate("interface_ihm", "Carte 3", None))
        self.checkBox_3.setShortcut(_translate("interface_ihm", "3", None))
        self.checkBox_7.setText(_translate("interface_ihm", "Carte 7", None))
        self.checkBox_7.setShortcut(_translate("interface_ihm", "7", None))
        self.checkBox_2.setText(_translate("interface_ihm", "Carte 2", None))
        self.checkBox_2.setShortcut(_translate("interface_ihm", "2", None))
        self.checkBox_1.setText(_translate("interface_ihm", "Carte 1", None))
        self.checkBox_1.setShortcut(_translate("interface_ihm", "1", None))
        self.menuFIchier.setTitle(_translate("interface_ihm", "Fichier", None))
        self.actionQuitter.setText(_translate("interface_ihm", "Quitter", None))
        self.actionSolo.setText(_translate("interface_ihm", "Solo", None))
        self.actionMultijoueur.setText(_translate("interface_ihm", "Multijoueur", None))
        self.actionIntelligence_Artificielle.setText(_translate("interface_ihm", "Intelligence Artificielle", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    interface_ihm = QtGui.QMainWindow()
    ui = Ui_interface_ihm()
    ui.setupUi(interface_ihm)
    interface_ihm.show()
    sys.exit(app.exec_())

