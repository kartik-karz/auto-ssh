
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sshHandler as sshHandle
class Ui_Form(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400 , 550)
        self.Form = Form
        self.et_email_id = QtWidgets.QTextEdit(Form)
        self.et_email_id.setGeometry(QtCore.QRect(110, 100, 171, 31))
        self.et_email_id.setObjectName("et_email_id")
        self.et_password = QtWidgets.QTextEdit(Form)
        self.et_password.setGeometry(QtCore.QRect(110, 160, 171, 31))
        self.et_password.setObjectName("et_password")
        self.tv_email_id = QtWidgets.QLabel(Form)
        self.tv_email_id.setGeometry(QtCore.QRect(110, 80, 67, 17))
        self.tv_email_id.setObjectName("tv_email_id")
        self.tv_password = QtWidgets.QLabel(Form)
        self.tv_password.setGeometry(QtCore.QRect(110, 140, 67, 17))
        self.tv_password.setObjectName("tv_password")
        self.bt_submit = QtWidgets.QPushButton(Form)
        self.bt_submit.setGeometry(QtCore.QRect(140, 200, 99, 27))
        self.bt_submit.setObjectName("bt_submit")
        self.bt_submit.clicked.connect(self.btn_submit_click)
        self.et_rsa_label =  QtWidgets.QTextEdit(self.Form)
        self.et_rsa_label.setGeometry(QtCore.QRect(50, 250, 300, 250))
        self.et_rsa_label.setObjectName("et_rsa_label")
        self.et_rsa_label.setText("Your Key Will be here in a while...")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def btn_submit_click(self):
        email_id = self.et_email_id.toPlainText()
        password = self.et_password.toPlainText()
        sshHandle.create_key(email_id,password)
        ssHandle.add_to_agent()
        rsa = self.load_rsa_key()
        self.et_rsa_label.setText(rsa)


    def load_rsa_key(self):
        rsa_file_path = os.path.expanduser('~/.ssh/id_rsa.pub')
        f = open(rsa_file_path, "r")

        rsa_key = f.read()
        f.close()
        return rsa_key

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tv_email_id.setText(_translate("Form", "Email Id"))
        self.tv_password.setText(_translate("Form", "Password"))
        self.bt_submit.setText(_translate("Form", "Submit"))
