# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\corazzal\Desktop\RoboRally-master\RoboRally\interface.ui'
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
        interface_ihm.resize(1395, 878)
        self.centralwidget = QtGui.QWidget(interface_ihm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.conteneur = QtGui.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(0, 0, 781, 621))
        self.conteneur.setObjectName(_fromUtf8("conteneur"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(360, 740, 141, 82))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pv = QtGui.QProgressBar(self.formLayoutWidget)
        self.pv.setProperty("value", 100)
        self.pv.setObjectName(_fromUtf8("pv"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pv)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 10, 221, 621))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pioche = QtGui.QWidget(self.verticalLayoutWidget)
        self.pioche.setObjectName(_fromUtf8("pioche"))
        self.tapiscarte = QtGui.QLabel(self.pioche)
        self.tapiscarte.setGeometry(QtCore.QRect(0, 10, 331, 621))
        self.tapiscarte.setText(_fromUtf8(""))
        self.tapiscarte.setObjectName(_fromUtf8("tapiscarte"))
        self.verticalLayout.addWidget(self.pioche)
        self.bouton_distrib = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bouton_distrib.setObjectName(_fromUtf8("bouton_distrib"))
        self.verticalLayout.addWidget(self.bouton_distrib)
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(740, 630, 271, 195))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bouton_instru = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.bouton_instru.setObjectName(_fromUtf8("bouton_instru"))
        self.gridLayout_2.addWidget(self.bouton_instru, 3, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.choixcarte = QtGui.QTextEdit(self.gridLayoutWidget_2)
        self.choixcarte.setObjectName(_fromUtf8("choixcarte"))
        self.gridLayout_2.addWidget(self.choixcarte, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 740, 64, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.nbjoueur = QtGui.QSpinBox(self.centralwidget)
        self.nbjoueur.setGeometry(QtCore.QRect(140, 660, 64, 33))
        self.nbjoueur.setMinimum(1)
        self.nbjoueur.setMaximum(4)
        self.nbjoueur.setObjectName(_fromUtf8("nbjoueur"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 670, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        interface_ihm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(interface_ihm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 21))
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
        self.lineEdit.setText(_translate("interface_ihm", "KerTwonkaradec", None))
        self.bouton_distrib.setText(_translate("interface_ihm", "Distribuer", None))
        self.bouton_partie.setText(_translate("interface_ihm", "Nouvelle partie", None))
        self.Quitter.setText(_translate("interface_ihm", "Quitter", None))
        self.bouton_instru.setText(_translate("interface_ihm", "Envoyer les instructions au robot", None))
        self.bouton_instru.setShortcut(_translate("interface_ihm", "Return", None))
        self.plainTextEdit.setPlainText(_translate("interface_ihm", "Cliquez sur distribuer,\n"
"choisissez vos 5 cartes (ex: 1 2 3 4 5)\n"
"puis envoyez les instructions au robot.", None))
        self.label.setText(_translate("interface_ihm", "Choix", None))
        self.label_2.setText(_translate("interface_ihm", "Nombre de joueurs", None))
        self.menuFIchier.setTitle(_translate("interface_ihm", "Fichier", None))
        self.actionQuitter.setText(_translate("interface_ihm", "Quitter", None))
        self.actionSolo.setText(_translate("interface_ihm", "Solo", None))
        self.actionMultijoueur.setText(_translate("interface_ihm", "Multijoueur", None))
        self.actionIntelligence_Artificielle.setText(_translate("interface_ihm", "Intelligence Artificielle", None))

