# Form implementation generated from reading ui file 'UI/addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.formContainer = QtWidgets.QWidget(parent=Dialog)
        self.formContainer.setObjectName("formContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.formContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formWidget = QtWidgets.QWidget(parent=self.formContainer)
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setObjectName("formLayout")
        self.labelName = QtWidgets.QLabel(parent=self.formWidget)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditName)
        self.labelRoast = QtWidgets.QLabel(parent=self.formWidget)
        self.labelRoast.setObjectName("labelRoast")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelRoast)
        self.lineEditRoast = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditRoast.setObjectName("lineEditRoast")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditRoast)
        self.labelGround = QtWidgets.QLabel(parent=self.formWidget)
        self.labelGround.setObjectName("labelGround")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelGround)
        self.lineEditGround = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditGround.setObjectName("lineEditGround")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditGround)
        self.labelTaste = QtWidgets.QLabel(parent=self.formWidget)
        self.labelTaste.setObjectName("labelTaste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelTaste)
        self.lineEditTaste = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditTaste.setObjectName("lineEditTaste")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditTaste)
        self.labelPrice = QtWidgets.QLabel(parent=self.formWidget)
        self.labelPrice.setObjectName("labelPrice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPrice)
        self.lineEditPrice = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditPrice)
        self.labelVolume = QtWidgets.QLabel(parent=self.formWidget)
        self.labelVolume.setObjectName("labelVolume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelVolume)
        self.lineEditVolume = QtWidgets.QLineEdit(parent=self.formWidget)
        self.lineEditVolume.setObjectName("lineEditVolume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditVolume)
        self.verticalLayout.addWidget(self.formWidget)
        self.pushButton = QtWidgets.QPushButton(parent=self.formContainer)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add/Edit Coffee"))
        self.labelName.setText(_translate("Dialog", "Name"))
        self.labelRoast.setText(_translate("Dialog", "Roast Level"))
        self.labelGround.setText(_translate("Dialog", "Ground"))
        self.labelTaste.setText(_translate("Dialog", "Taste Description"))
        self.labelPrice.setText(_translate("Dialog", "Price"))
        self.labelVolume.setText(_translate("Dialog", "Volume"))
        self.pushButton.setText(_translate("Dialog", "Save"))
