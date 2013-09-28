# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, time
import re
import subprocess
import urllib
import ConfigParser

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

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

class Ui_RDPGUI(object):
    def setupUi(self, RDPGUI):
        RDPGUI.setObjectName(_fromUtf8("RDPGUI"))
        RDPGUI.resize(628, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("selectuser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RDPGUI.setWindowIcon(icon)
        RDPGUI.setStyleSheet(_fromUtf8("background-color: rgb(24, 93, 123);"))
        self.image = QtGui.QLabel(RDPGUI)
        self.image.setGeometry(QtCore.QRect(220, 30, 191, 191))
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("selectuser.png")))
        self.image.setObjectName(_fromUtf8("image"))
        self.enterButton = QtGui.QPushButton(RDPGUI)
        self.enterButton.setGeometry(QtCore.QRect(430, 340, 31, 31))
        self.enterButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.enterButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("enter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enterButton.setIcon(icon1)
        self.enterButton.setIconSize(QtCore.QSize(40, 40))
        self.enterButton.setObjectName(_fromUtf8("enterButton"))
        self.RDPusername = QtGui.QLineEdit(RDPGUI)
        self.RDPusername.setGeometry(QtCore.QRect(190, 290, 231, 31))
        self.RDPusername.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.RDPusername.setObjectName(_fromUtf8("RDPusername"))
        self.RDPpassword = QtGui.QLineEdit(RDPGUI)
        self.RDPpassword.setGeometry(QtCore.QRect(190, 340, 231, 31))
        self.RDPpassword.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.RDPpassword.setEchoMode(QtGui.QLineEdit.Password)
        self.RDPpassword.setObjectName(_fromUtf8("RDPpassword"))
        self.version = QtGui.QLabel(RDPGUI)
        self.version.setGeometry(QtCore.QRect(520, 460, 101, 20))
        self.version.setStyleSheet(_fromUtf8("color: rgb(193, 193, 193);"))
        self.version.setObjectName(_fromUtf8("version"))
        self.label = QtGui.QLabel(RDPGUI)
        self.label.setGeometry(QtCore.QRect(130, 230, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(RDPGUI)
        self.widget.setGeometry(QtCore.QRect(190, 380, 231, 44))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.serverlabel = QtGui.QLabel(self.widget)
        self.serverlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.serverlabel.setObjectName(_fromUtf8("serverlabel"))
        self.gridLayout.addWidget(self.serverlabel, 0, 0, 1, 1)
        self.serverBox = QtGui.QComboBox(self.widget)
        self.serverBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.serverBox.setObjectName(_fromUtf8("serverBox"))
        self.gridLayout.addWidget(self.serverBox, 0, 1, 1, 1)
        self.domainlabel = QtGui.QLabel(self.widget)
        self.domainlabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.domainlabel.setObjectName(_fromUtf8("domainlabel"))
        self.gridLayout.addWidget(self.domainlabel, 1, 0, 1, 1)
        self.RDPdomain = QtGui.QLabel(self.widget)
        self.RDPdomain.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.RDPdomain.setObjectName(_fromUtf8("RDPdomain"))
        self.gridLayout.addWidget(self.RDPdomain, 1, 1, 1, 1)

        self.retranslateUi(RDPGUI)
        QtCore.QObject.connect(self.RDPpassword, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.enterButton.click)
	QtCore.QObject.connect(self.RDPusername, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.checkdomain)
        QtCore.QMetaObject.connectSlotsByName(RDPGUI)
	centreWidget(RDPGUI)

    def retranslateUi(self, RDPGUI):
        RDPGUI.setWindowTitle(_translate("RDPGUI", "RDPGUI", None))
        self.RDPusername.setPlaceholderText(_translate("RDPGUI", "Username", None))
        self.RDPpassword.setToolTip(_translate("RDPGUI", "Insert username", None))
        self.RDPpassword.setPlaceholderText(_translate("RDPGUI", "Password", None))
        self.version.setText(_translate("RDPGUI", "rpi-tc rdp gui v3", None))
        self.serverlabel.setText(_translate("RDPGUI", "Server:", None))
        self.serverBox.setItemText(0, _translate("RDPGUI", "server1.domain.lan", None))
        self.domainlabel.setText(_translate("RDPGUI", "Domain:", None))
        self.RDPdomain.setText(_translate("RDPGUI", "DOMAIN", None))
	self.enterButton.clicked.connect(self.handleButton)
	config = ConfigParser.ConfigParser()
	config.read('rdpgui.ini')
	serverlist = str(config.get("DEFAULT", "RDPServer")).split()
	for n in range(len(serverlist)):
		self.serverBox.addItem(_fromUtf8(""))
		self.serverBox.setItemText(n, _translate("RDPGUI", serverlist[n].strip(), None))

	self.RDPdomain.setText(_translate("RDPGUI", config.get("DEFAULT", "RDPDomain"), None))


    def checkdomain(self):
	#updating DOMAIN label if domain in. ex: DOMAIN\username
	if str(self.RDPusername.text()).find("\\") > 0:
		self.RDPdomain.setText(_translate("RDPGUI", str(self.RDPusername.text()).split('\\')[0], None))
	else:
		config = ConfigParser.ConfigParser()
		config.read('rdpgui.ini')
		self.RDPdomain.setText(_translate("RDPGUI", config.get("DEFAULT", "RDPDomain"), None))


    def handleButton(self):
	config = ConfigParser.ConfigParser()
	config.read('rdpgui.ini')
	ServerFlag = config.get("DEFAULT", "RDPServerFlags") + str(self.serverBox.currentText())
	#checking if username have domain in. ex: DOMAIN\username
	if str(self.RDPusername.text()).find("\\") > 0:
		DomainFlag = config.get("DEFAULT", "RDPDomainFlags") + str(self.RDPusername.text()).split('\\')[0]
		UserFlag = config.get("DEFAULT", "RDPUserFlags") + str(self.RDPusername.text()).split('\\')[1]
	else:
		DomainFlag = config.get("DEFAULT", "RDPDomainFlags") + config.get("DEFAULT", RDPDomain)
		UserFlag = config.get("DEFAULT", "RDPUserFlags") + self.RDPusername.text()
	User_Pass = config.get("DEFAULT", "RDPPasswordFlags") + self.RDPpassword.text() + ' ' + UserFlag
	commandline = str(config.get("DEFAULT", "RDPBinary") + ' ' + DomainFlag +' '+ User_Pass + ' ' + config.get("DEFAULT", "RDPDefaulfFlags") + ' ' + config.get("DEFAULT", "RDPExtraFlags") + ' ' + ServerFlag)
	#cleaning dquote from confi.ini params
	commandline = re.sub('["]','',commandline)
	#print commandline
	proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	(out, err) = proc.communicate()
	print "-------------------------------------------------------------"
	print out
	if out.find("Authentication failure, check credentials") > 0:
		print "Authentication failure!"
		self.version.setText(_translate("RDPGUI", "Auth Error...", None))
		self.label.setText(_fromUtf8("Wrong username or password!"))
	elif out.find("getaddrinfo (System error)") > 0 or out.find("getaddrinfo: System error") >= 0:
		print "Error connecting to server!"
		self.version.setText(_translate("RDPGUI", "Server Error...", None))
		self.label.setText(_fromUtf8("Server Error, call your sysadmin"))
	elif out.find("unable to connect to") >= 0 or out.find("A Remote Desktop Protocol client") >= 0:
		print "Error connecting to server!"
		self.version.setText(_translate("RDPGUI", "Server Error...", None))
		self.label.setText(_fromUtf8("Server Error, call your sysadmin"))
	else:
		self.RDPusername.setText(_translate("RDPGUI", "", None))
		self.RDPpassword.setText(_translate("RDPGUI", "", None))
		self.version.setText(_translate("RDPGUI", "rpi-tc rdp gui v1", None))
		self.RDPdomain.setText(_translate("RDPGUI", config.get("DEFAULT", "RDPDomain"), None))
		self.label.setText(_fromUtf8(""))


def centreWidget(self):
    screen = QtGui.QDesktopWidget().screenGeometry()
    mysize = self.geometry()
    hpos = ( screen.width() - mysize.width() ) / 2
    vpos = ( screen.height() - mysize.height() ) / 2
    self.move(hpos, vpos)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RDPGUI = QtGui.QWidget()
    ui = Ui_RDPGUI()
    ui.setupUi(RDPGUI)
    RDPGUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    RDPGUI.show()
    RDPGUI.setFixedSize(RDPGUI.size());
    sys.exit(app.exec_())

