
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sshHandler as sshHandle
import gpgHandler as gpgHandle
class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName("Auto SSH")
        Form.resize(400 , 550)
        self.Form = Form
        self.et_full_name = QtWidgets.QTextEdit(Form)
        self.et_full_name.setGeometry(QtCore.QRect(110, 40, 171, 31))
        self.et_full_name.setObjectName("et_full_name")
        self.et_full_name.setTabChangesFocus(True)

        self.et_email_id = QtWidgets.QTextEdit(Form)
        self.et_email_id.setGeometry(QtCore.QRect(110, 100, 171, 31))
        self.et_email_id.setObjectName("et_email_id")
        self.et_email_id.setTabChangesFocus(True)
        self.et_password = QtWidgets.QLineEdit(Form)
        self.et_password.setGeometry(QtCore.QRect(110, 160, 171, 31))
        self.et_password.setObjectName("et_password")
        self.et_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tv_email_id = QtWidgets.QLabel(Form)
        self.tv_email_id.setGeometry(QtCore.QRect(110, 80, 67, 17))
        self.tv_email_id.setObjectName("tv_email_id")

        self.tv_full_name = QtWidgets.QLabel(Form)
        self.tv_full_name.setGeometry(QtCore.QRect(110, 20, 67, 17))
        self.tv_full_name.setObjectName("tv_full_name")

        self.tv_password = QtWidgets.QLabel(Form)
        self.tv_password.setGeometry(QtCore.QRect(110, 140, 67, 17))
        self.tv_password.setObjectName("tv_password")
        self.bt_ssh = QtWidgets.QPushButton(Form)
        self.bt_ssh.setGeometry(QtCore.QRect(140, 200, 35, 30))
        self.bt_ssh.setObjectName("bt_ssh")
        self.bt_ssh.clicked.connect(self.btn_ssh_click)


        self.bt_gpg = QtWidgets.QPushButton(Form)
        self.bt_gpg.setGeometry(QtCore.QRect(200,200,35,30))
        self.bt_gpg.setObjectName("bt_gpg")
        self.bt_gpg.clicked.connect(self.btn_gpg_click)

        self.tv_key_title = QtWidgets.QLabel(Form)
        self.tv_key_title.setGeometry(QtCore.QRect(160, 232, 67, 17))
        self.tv_key_title.setObjectName("tv_key_title")

        self.et_rsa_label =  QtWidgets.QTextEdit(self.Form)
        self.et_rsa_label.setGeometry(QtCore.QRect(50, 250, 300, 250))
        self.et_rsa_label.setObjectName("et_rsa_label")
        self.et_rsa_label.setTabChangesFocus(True)
        self.et_rsa_label.setText("Your Key Will be here in a while...")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def btn_ssh_click(self):
        self.tv_key_title.setText("SSH Key")
        email_id = self.et_email_id.toPlainText()
        password = self.et_password.text()
        sshHandle.create_key(email_id,password)
        sshHandle.add_to_agent()
        rsa = sshHandle.load_rsa_key()
        self.et_rsa_label.setText(rsa)

    def btn_gpg_click(self):
        self.tv_key_title.setText("GPG Key")
        email_id = self.et_email_id.toPlainText()
        password = self.et_password.text()
        name = self.et_full_name.toPlainText()
        gpgHandle.create_key(name,email_id,"",password)
        gpg = gpgHandle.load_gpg_key()
        self.et_rsa_label.setText(gpg)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tv_email_id.setText(_translate("Form", "Email Id"))
        self.tv_password.setText(_translate("Form", "Password"))
        self.bt_ssh.setText(_translate("Form", "SSH"))
        self.tv_full_name.setText(_translate("Form","Full Name"))
        self.tv_key_title.setText(_translate("Form","SSH Key"))
        self.bt_gpg.setText(_translate("Form","GPG"))
