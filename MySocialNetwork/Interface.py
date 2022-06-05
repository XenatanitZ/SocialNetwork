from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1280, 720)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("background-color:#c3c3c3\n"
"/* #C3BEF0 #5AB9EA background-color:#00bfff")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Registration = QtWidgets.QWidget()
        self.Registration.setObjectName("Registration")
        self.acceptRegButton = QtWidgets.QPushButton(self.Registration)
        self.acceptRegButton.setGeometry(QtCore.QRect(670, 410, 131, 41))
        self.acceptRegButton.setMinimumSize(QtCore.QSize(131, 41))
        self.acceptRegButton.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.acceptRegButton.setFont(font)
        self.acceptRegButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.acceptRegButton.setObjectName("acceptRegButton")
        self.password = QtWidgets.QLineEdit(self.Registration)
        self.password.setGeometry(QtCore.QRect(490, 290, 311, 41))
        self.password.setMinimumSize(QtCore.QSize(311, 41))
        self.password.setMaximumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setReadOnly(False)
        self.password.setObjectName("password")
        self.login = QtWidgets.QLineEdit(self.Registration)
        self.login.setGeometry(QtCore.QRect(490, 230, 311, 41))
        self.login.setMinimumSize(QtCore.QSize(311, 41))
        self.login.setMaximumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.login.setFont(font)
        self.login.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.login.setObjectName("login")
        self.acceptMenuButton = QtWidgets.QPushButton(self.Registration)
        self.acceptMenuButton.setGeometry(QtCore.QRect(490, 410, 131, 41))
        self.acceptMenuButton.setMinimumSize(QtCore.QSize(131, 41))
        self.acceptMenuButton.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.acceptMenuButton.setFont(font)
        self.acceptMenuButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.acceptMenuButton.setObjectName("acceptMenuButton")
        self.label = QtWidgets.QLabel(self.Registration)
        self.label.setGeometry(QtCore.QRect(480, 160, 331, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(331, 41))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLineWidth(5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Registration)
        self.stackedWidget_2.setGeometry(QtCore.QRect(20, 460, 1281, 721))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.passwordRepeat = QtWidgets.QLineEdit(self.Registration)
        self.passwordRepeat.setGeometry(QtCore.QRect(490, 350, 311, 41))
        self.passwordRepeat.setMinimumSize(QtCore.QSize(311, 41))
        self.passwordRepeat.setMaximumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordRepeat.setFont(font)
        self.passwordRepeat.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.passwordRepeat.setText("")
        self.passwordRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordRepeat.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordRepeat.setReadOnly(False)
        self.passwordRepeat.setObjectName("passwordRepeat")
        self.stackedWidget.addWidget(self.Registration)
        self.Authorization = QtWidgets.QWidget()
        self.Authorization.setObjectName("Authorization")
        self.label_2 = QtWidgets.QLabel(self.Authorization)
        self.label_2.setGeometry(QtCore.QRect(480, 200, 331, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(331, 41))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(33)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.loginAuth = QtWidgets.QLineEdit(self.Authorization)
        self.loginAuth.setGeometry(QtCore.QRect(490, 270, 311, 41))
        self.loginAuth.setMinimumSize(QtCore.QSize(311, 41))
        self.loginAuth.setMaximumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginAuth.setFont(font)
        self.loginAuth.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.loginAuth.setAlignment(QtCore.Qt.AlignCenter)
        self.loginAuth.setObjectName("loginAuth")
        self.acceptAuthButton = QtWidgets.QPushButton(self.Authorization)
        self.acceptAuthButton.setGeometry(QtCore.QRect(670, 390, 131, 41))
        self.acceptAuthButton.setMinimumSize(QtCore.QSize(131, 41))
        self.acceptAuthButton.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.acceptAuthButton.setFont(font)
        self.acceptAuthButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.acceptAuthButton.setObjectName("acceptAuthButton")
        self.passwordAuth = QtWidgets.QLineEdit(self.Authorization)
        self.passwordAuth.setGeometry(QtCore.QRect(490, 330, 311, 41))
        self.passwordAuth.setMinimumSize(QtCore.QSize(311, 41))
        self.passwordAuth.setMaximumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordAuth.setFont(font)
        self.passwordAuth.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.passwordAuth.setText("")
        self.passwordAuth.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordAuth.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordAuth.setReadOnly(False)
        self.passwordAuth.setObjectName("passwordAuth")
        self.regMenuButton = QtWidgets.QPushButton(self.Authorization)
        self.regMenuButton.setGeometry(QtCore.QRect(490, 390, 131, 41))
        self.regMenuButton.setMinimumSize(QtCore.QSize(131, 41))
        self.regMenuButton.setMaximumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.regMenuButton.setFont(font)
        self.regMenuButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.regMenuButton.setObjectName("regMenuButton")
        self.stackedWidget.addWidget(self.Authorization)
        self.Editing = QtWidgets.QWidget()
        self.Editing.setObjectName("Editing")
        self.label_3 = QtWidgets.QLabel(self.Editing)
        self.label_3.setGeometry(QtCore.QRect(460, 40, 371, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(331, 41))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black")
        self.label_3.setLineWidth(5)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.surname = QtWidgets.QLineEdit(self.Editing)
        self.surname.setGeometry(QtCore.QRect(470, 110, 351, 41))
        self.surname.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.surname.setFont(font)
        self.surname.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.surname.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.surname.setFrame(True)
        self.surname.setCursorPosition(0)
        self.surname.setAlignment(QtCore.Qt.AlignCenter)
        self.surname.setObjectName("surname")
        self.name = QtWidgets.QLineEdit(self.Editing)
        self.name.setGeometry(QtCore.QRect(470, 170, 351, 41))
        self.name.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name.setFont(font)
        self.name.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.city = QtWidgets.QLineEdit(self.Editing)
        self.city.setGeometry(QtCore.QRect(470, 230, 351, 41))
        self.city.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.city.setFont(font)
        self.city.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.city.setAlignment(QtCore.Qt.AlignCenter)
        self.city.setObjectName("city")
        self.email = QtWidgets.QLineEdit(self.Editing)
        self.email.setGeometry(QtCore.QRect(470, 290, 351, 41))
        self.email.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email.setFont(font)
        self.email.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.email.setAlignment(QtCore.Qt.AlignCenter)
        self.email.setObjectName("email")
        self.phoneNumber = QtWidgets.QLineEdit(self.Editing)
        self.phoneNumber.setGeometry(QtCore.QRect(470, 350, 351, 41))
        self.phoneNumber.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.phoneNumber.setFont(font)
        self.phoneNumber.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.phoneNumber.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.phoneNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneNumber.setObjectName("phoneNumber")
        self.dateEdit = QtWidgets.QDateEdit(self.Editing)
        self.dateEdit.setGeometry(QtCore.QRect(650, 470, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(self.Editing)
        self.label_4.setGeometry(QtCore.QRect(460, 460, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Editing)
        self.label_5.setGeometry(QtCore.QRect(460, 410, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.Editing)
        self.comboBox.setGeometry(QtCore.QRect(540, 410, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("Мужской")
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.backButton = QtWidgets.QPushButton(self.Editing)
        self.backButton.setGeometry(QtCore.QRect(470, 530, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color:#eebef1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.backButton.setObjectName("backButton")
        self.saveButton = QtWidgets.QPushButton(self.Editing)
        self.saveButton.setGeometry(QtCore.QRect(650, 530, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton {\n"
"        /*background-color: #d39fcf;*/\n"
"    background-color:#eebef1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.stackedWidget.addWidget(self.Editing)
        self.MyselfPage = QtWidgets.QWidget()
        self.MyselfPage.setObjectName("MyselfPage")
        self.messagesButton = QtWidgets.QPushButton(self.MyselfPage)
        self.messagesButton.setGeometry(QtCore.QRect(0, 0, 427, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.messagesButton.setFont(font)
        self.messagesButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.messagesButton.setObjectName("messagesButton")
        self.mainPageButton = QtWidgets.QPushButton(self.MyselfPage)
        self.mainPageButton.setGeometry(QtCore.QRect(427, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainPageButton.setFont(font)
        self.mainPageButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.mainPageButton.setObjectName("mainPageButton")
        self.friendsButton = QtWidgets.QPushButton(self.MyselfPage)
        self.friendsButton.setGeometry(QtCore.QRect(848, 0, 433, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.friendsButton.setFont(font)
        self.friendsButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.friendsButton.setObjectName("friendsButton")
        self.myPhoto = QtWidgets.QLineEdit(self.MyselfPage)
        self.myPhoto.setGeometry(QtCore.QRect(10, 130, 400, 400))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.myPhoto.setFont(font)
        self.myPhoto.setStyleSheet("/*background-color: #d39fcf;*/\n"
"background-color: #e7d2f1;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"/*color: #8860D0;*/\n"
"color: black;\n"
"border-radius: 200;\n"
"/*#F1D0E9; */")
        self.myPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.myPhoto.setObjectName("myPhoto")
        self.editButton = QtWidgets.QPushButton(self.MyselfPage)
        self.editButton.setGeometry(QtCore.QRect(10, 550, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.editButton.setObjectName("editButton")
        self.myStatus = QtWidgets.QLineEdit(self.MyselfPage)
        self.myStatus.setGeometry(QtCore.QRect(450, 60, 671, 41))
        self.myStatus.setAcceptDrops(True)
        self.myStatus.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.myStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.myStatus.setObjectName("myStatus")
        self.line = QtWidgets.QFrame(self.MyselfPage)
        self.line.setGeometry(QtCore.QRect(450, 240, 811, 20))
        self.line.setStyleSheet("color:black")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.addingPostButton = QtWidgets.QLineEdit(self.MyselfPage)
        self.addingPostButton.setGeometry(QtCore.QRect(450, 290, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addingPostButton.setFont(font)
        self.addingPostButton.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.addingPostButton.setAlignment(QtCore.Qt.AlignCenter)
        self.addingPostButton.setObjectName("addingPostButton")
        self.publishButton = QtWidgets.QPushButton(self.MyselfPage)
        self.publishButton.setGeometry(QtCore.QRect(1140, 290, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.publishButton.setFont(font)
        self.publishButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.publishButton.setObjectName("publishButton")
        self.line_4 = QtWidgets.QFrame(self.MyselfPage)
        self.line_4.setGeometry(QtCore.QRect(450, 260, 811, 20))
        self.line_4.setStyleSheet("color:black")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.label_6 = QtWidgets.QLabel(self.MyselfPage)
        self.label_6.setGeometry(QtCore.QRect(450, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.myCity = QtWidgets.QLabel(self.MyselfPage)
        self.myCity.setGeometry(QtCore.QRect(520, 120, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.myCity.setFont(font)
        self.myCity.setObjectName("myCity")
        self.mySurname = QtWidgets.QLabel(self.MyselfPage)
        self.mySurname.setGeometry(QtCore.QRect(30, 50, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mySurname.setFont(font)
        self.mySurname.setAlignment(QtCore.Qt.AlignCenter)
        self.mySurname.setObjectName("mySurname")
        self.myName = QtWidgets.QLabel(self.MyselfPage)
        self.myName.setGeometry(QtCore.QRect(240, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.myName.setFont(font)
        self.myName.setAlignment(QtCore.Qt.AlignCenter)
        self.myName.setObjectName("myName")
        self.label_8 = QtWidgets.QLabel(self.MyselfPage)
        self.label_8.setGeometry(QtCore.QRect(710, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.saveStatusButton = QtWidgets.QPushButton(self.MyselfPage)
        self.saveStatusButton.setGeometry(QtCore.QRect(1140, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveStatusButton.setFont(font)
        self.saveStatusButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.saveStatusButton.setObjectName("saveStatusButton")
        self.myEmail = QtWidgets.QLabel(self.MyselfPage)
        self.myEmail.setGeometry(QtCore.QRect(780, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.myEmail.setFont(font)
        self.myEmail.setObjectName("myEmail")
        self.line_5 = QtWidgets.QFrame(self.MyselfPage)
        self.line_5.setGeometry(QtCore.QRect(420, 60, 20, 641))
        self.line_5.setStyleSheet("color: black;")
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_9 = QtWidgets.QLabel(self.MyselfPage)
        self.label_9.setGeometry(QtCore.QRect(980, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.myNumber = QtWidgets.QLabel(self.MyselfPage)
        self.myNumber.setGeometry(QtCore.QRect(1080, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.myNumber.setFont(font)
        self.myNumber.setObjectName("myNumber")
        self.label_10 = QtWidgets.QLabel(self.MyselfPage)
        self.label_10.setGeometry(QtCore.QRect(450, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.mySex = QtWidgets.QLabel(self.MyselfPage)
        self.mySex.setGeometry(QtCore.QRect(500, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mySex.setFont(font)
        self.mySex.setObjectName("mySex")
        self.label_11 = QtWidgets.QLabel(self.MyselfPage)
        self.label_11.setGeometry(QtCore.QRect(710, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.myBirthDate = QtWidgets.QLabel(self.MyselfPage)
        self.myBirthDate.setGeometry(QtCore.QRect(870, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.myBirthDate.setFont(font)
        self.myBirthDate.setObjectName("myBirthDate")
        self.myPosts = QtWidgets.QScrollArea(self.MyselfPage)
        self.myPosts.setGeometry(QtCore.QRect(450, 360, 811, 331))
        self.myPosts.setWidgetResizable(True)
        self.myPosts.setObjectName("myPosts")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 809, 329))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.postDate1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.postDate1.setGeometry(QtCore.QRect(9, 40, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.postDate1.setFont(font)
        self.postDate1.setText("")
        self.postDate1.setObjectName("postDate1")
        self.postText1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.postText1.setGeometry(QtCore.QRect(200, 40, 601, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.postText1.setFont(font)
        self.postText1.setText("")
        self.postText1.setObjectName("postText1")
        self.myPosts.setWidget(self.scrollAreaWidgetContents_4)
        self.exitButton = QtWidgets.QPushButton(self.MyselfPage)
        self.exitButton.setGeometry(QtCore.QRect(10, 620, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.stackedWidget.addWidget(self.MyselfPage)
        self.Page = QtWidgets.QWidget()
        self.Page.setObjectName("Page")
        self.messagesButton_2 = QtWidgets.QPushButton(self.Page)
        self.messagesButton_2.setGeometry(QtCore.QRect(0, 0, 427, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.messagesButton_2.setFont(font)
        self.messagesButton_2.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.messagesButton_2.setObjectName("messagesButton_2")
        self.friendsButton_2 = QtWidgets.QPushButton(self.Page)
        self.friendsButton_2.setGeometry(QtCore.QRect(848, 0, 433, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.friendsButton_2.setFont(font)
        self.friendsButton_2.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.friendsButton_2.setObjectName("friendsButton_2")
        self.Photo = QtWidgets.QLineEdit(self.Page)
        self.Photo.setGeometry(QtCore.QRect(10, 130, 400, 400))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.Photo.setFont(font)
        self.Photo.setStyleSheet("/*background-color: #d39fcf;*/\n"
"background-color: #e7d2f1;\n"
"border: 1px solid;\n"
"border-color: black;\n"
"/*color: #8860D0;*/\n"
"color: black;\n"
"border-radius: 200;\n"
"/*#F1D0E9; */")
        self.Photo.setAlignment(QtCore.Qt.AlignCenter)
        self.Photo.setObjectName("Photo")
        self.mainPageButton_2 = QtWidgets.QPushButton(self.Page)
        self.mainPageButton_2.setGeometry(QtCore.QRect(427, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainPageButton_2.setFont(font)
        self.mainPageButton_2.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.mainPageButton_2.setObjectName("mainPageButton_2")
        self.line_2 = QtWidgets.QFrame(self.Page)
        self.line_2.setGeometry(QtCore.QRect(450, 240, 811, 20))
        self.line_2.setStyleSheet("color:black")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.addingFriendButton = QtWidgets.QPushButton(self.Page)
        self.addingFriendButton.setGeometry(QtCore.QRect(10, 620, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.addingFriendButton.setFont(font)
        self.addingFriendButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.addingFriendButton.setObjectName("addingFriendButton")
        self.goToDialogButton = QtWidgets.QPushButton(self.Page)
        self.goToDialogButton.setGeometry(QtCore.QRect(10, 550, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.goToDialogButton.setFont(font)
        self.goToDialogButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.goToDialogButton.setObjectName("goToDialogButton")
        self.line_3 = QtWidgets.QFrame(self.Page)
        self.line_3.setGeometry(QtCore.QRect(450, 260, 811, 20))
        self.line_3.setStyleSheet("color:black")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_6 = QtWidgets.QFrame(self.Page)
        self.line_6.setGeometry(QtCore.QRect(420, 60, 20, 641))
        self.line_6.setStyleSheet("color: black;")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.number = QtWidgets.QLabel(self.Page)
        self.number.setGeometry(QtCore.QRect(1080, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.label_15 = QtWidgets.QLabel(self.Page)
        self.label_15.setGeometry(QtCore.QRect(450, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.email_2 = QtWidgets.QLabel(self.Page)
        self.email_2.setGeometry(QtCore.QRect(780, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.email_2.setFont(font)
        self.email_2.setObjectName("email_2")
        self.city_2 = QtWidgets.QLabel(self.Page)
        self.city_2.setGeometry(QtCore.QRect(520, 120, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.city_2.setFont(font)
        self.city_2.setObjectName("city_2")
        self.label_12 = QtWidgets.QLabel(self.Page)
        self.label_12.setGeometry(QtCore.QRect(450, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(self.Page)
        self.label_16.setGeometry(QtCore.QRect(710, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.surname_2 = QtWidgets.QLabel(self.Page)
        self.surname_2.setGeometry(QtCore.QRect(30, 50, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.surname_2.setFont(font)
        self.surname_2.setAlignment(QtCore.Qt.AlignCenter)
        self.surname_2.setObjectName("surname_2")
        self.sex = QtWidgets.QLabel(self.Page)
        self.sex.setGeometry(QtCore.QRect(500, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.sex.setFont(font)
        self.sex.setObjectName("sex")
        self.label_17 = QtWidgets.QLabel(self.Page)
        self.label_17.setGeometry(QtCore.QRect(710, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(self.Page)
        self.label_13.setGeometry(QtCore.QRect(980, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.name_2 = QtWidgets.QLabel(self.Page)
        self.name_2.setGeometry(QtCore.QRect(240, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.name_2.setFont(font)
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setObjectName("name_2")
        self.birthDate = QtWidgets.QLabel(self.Page)
        self.birthDate.setGeometry(QtCore.QRect(870, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.birthDate.setFont(font)
        self.birthDate.setObjectName("birthDate")
        self.status = QtWidgets.QLabel(self.Page)
        self.status.setGeometry(QtCore.QRect(450, 70, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.postsArea = QtWidgets.QScrollArea(self.Page)
        self.postsArea.setGeometry(QtCore.QRect(450, 290, 811, 411))
        self.postsArea.setWidgetResizable(True)
        self.postsArea.setObjectName("postsArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 809, 409))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.postsArea.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.Page)
        self.Friends = QtWidgets.QWidget()
        self.Friends.setObjectName("Friends")
        self.friendsButton_5 = QtWidgets.QPushButton(self.Friends)
        self.friendsButton_5.setGeometry(QtCore.QRect(848, 0, 433, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.friendsButton_5.setFont(font)
        self.friendsButton_5.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.friendsButton_5.setObjectName("friendsButton_5")
        self.messagesButton_5 = QtWidgets.QPushButton(self.Friends)
        self.messagesButton_5.setGeometry(QtCore.QRect(0, 0, 427, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.messagesButton_5.setFont(font)
        self.messagesButton_5.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.messagesButton_5.setObjectName("messagesButton_5")
        self.mainPageButton_5 = QtWidgets.QPushButton(self.Friends)
        self.mainPageButton_5.setGeometry(QtCore.QRect(427, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainPageButton_5.setFont(font)
        self.mainPageButton_5.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.mainPageButton_5.setObjectName("mainPageButton_5")
        self.line_13 = QtWidgets.QFrame(self.Friends)
        self.line_13.setGeometry(QtCore.QRect(350, 60, 20, 641))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.Friends)
        self.line_14.setGeometry(QtCore.QRect(900, 60, 20, 641))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.areaForFriends = QtWidgets.QScrollArea(self.Friends)
        self.areaForFriends.setGeometry(QtCore.QRect(361, 60, 549, 641))
        self.areaForFriends.setWidgetResizable(True)
        self.areaForFriends.setObjectName("areaForFriends")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 547, 639))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.areaForFriends.setWidget(self.scrollAreaWidgetContents_5)
        self.searchByID = QtWidgets.QLineEdit(self.Friends)
        self.searchByID.setGeometry(QtCore.QRect(0, 60, 231, 41))
        self.searchByID.setAcceptDrops(True)
        self.searchByID.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.searchByID.setAlignment(QtCore.Qt.AlignCenter)
        self.searchByID.setObjectName("searchByID")
        self.toSearchButton = QtWidgets.QPushButton(self.Friends)
        self.toSearchButton.setGeometry(QtCore.QRect(240, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.toSearchButton.setFont(font)
        self.toSearchButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.toSearchButton.setObjectName("toSearchButton")
        self.areaForSearch = QtWidgets.QScrollArea(self.Friends)
        self.areaForSearch.setGeometry(QtCore.QRect(0, 110, 360, 591))
        self.areaForSearch.setWidgetResizable(True)
        self.areaForSearch.setObjectName("areaForSearch")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 358, 589))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.areaForSearch.setWidget(self.scrollAreaWidgetContents_6)
        self.stackedWidget.addWidget(self.Friends)
        self.InactiveMessenger = QtWidgets.QWidget()
        self.InactiveMessenger.setObjectName("InactiveMessenger")
        self.mainPageButton_3 = QtWidgets.QPushButton(self.InactiveMessenger)
        self.mainPageButton_3.setGeometry(QtCore.QRect(427, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainPageButton_3.setFont(font)
        self.mainPageButton_3.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.mainPageButton_3.setObjectName("mainPageButton_3")
        self.messagesButton_3 = QtWidgets.QPushButton(self.InactiveMessenger)
        self.messagesButton_3.setGeometry(QtCore.QRect(0, 0, 427, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.messagesButton_3.setFont(font)
        self.messagesButton_3.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.messagesButton_3.setObjectName("messagesButton_3")
        self.friendsButton_3 = QtWidgets.QPushButton(self.InactiveMessenger)
        self.friendsButton_3.setGeometry(QtCore.QRect(848, 0, 433, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.friendsButton_3.setFont(font)
        self.friendsButton_3.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.friendsButton_3.setObjectName("friendsButton_3")
        self.line_7 = QtWidgets.QFrame(self.InactiveMessenger)
        self.line_7.setGeometry(QtCore.QRect(420, 60, 20, 641))
        self.line_7.setStyleSheet("color: black;")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.InactiveMessenger)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 60, 431, 661))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 429, 659))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.InactiveMessenger)
        self.ActiveMessenger = QtWidgets.QWidget()
        self.ActiveMessenger.setObjectName("ActiveMessenger")
        self.friendsButton_4 = QtWidgets.QPushButton(self.ActiveMessenger)
        self.friendsButton_4.setGeometry(QtCore.QRect(848, 0, 433, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.friendsButton_4.setFont(font)
        self.friendsButton_4.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.friendsButton_4.setObjectName("friendsButton_4")
        self.line_8 = QtWidgets.QFrame(self.ActiveMessenger)
        self.line_8.setGeometry(QtCore.QRect(420, 60, 20, 641))
        self.line_8.setStyleSheet("color: black;")
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.messagesButton_4 = QtWidgets.QPushButton(self.ActiveMessenger)
        self.messagesButton_4.setGeometry(QtCore.QRect(0, 0, 427, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.messagesButton_4.setFont(font)
        self.messagesButton_4.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.messagesButton_4.setObjectName("messagesButton_4")
        self.mainPageButton_4 = QtWidgets.QPushButton(self.ActiveMessenger)
        self.mainPageButton_4.setGeometry(QtCore.QRect(427, 0, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mainPageButton_4.setFont(font)
        self.mainPageButton_4.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"}")
        self.mainPageButton_4.setObjectName("mainPageButton_4")
        self.TextMessageButton = QtWidgets.QLineEdit(self.ActiveMessenger)
        self.TextMessageButton.setGeometry(QtCore.QRect(440, 650, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TextMessageButton.setFont(font)
        self.TextMessageButton.setStyleSheet("/*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black")
        self.TextMessageButton.setAlignment(QtCore.Qt.AlignCenter)
        self.TextMessageButton.setObjectName("TextMessageButton")
        self.sendingButton = QtWidgets.QPushButton(self.ActiveMessenger)
        self.sendingButton.setGeometry(QtCore.QRect(1150, 650, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sendingButton.setFont(font)
        self.sendingButton.setStyleSheet("QPushButton {\n"
"    /*background-color: #d39fcf;*/\n"
"    background-color: #e7d2f1;\n"
"    border: 1px solid;\n"
"    border-radius:15;\n"
"    border-color: black;\n"
"    /*color: #8860D0;*/\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECB6DF;\n"
"    vertical-align: middle;\n"
"}")
        self.sendingButton.setObjectName("sendingButton")
        self.line_9 = QtWidgets.QFrame(self.ActiveMessenger)
        self.line_9.setGeometry(QtCore.QRect(-10, 50, 1281, 20))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.scrollArea = QtWidgets.QScrollArea(self.ActiveMessenger)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 431, 661))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 659))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textBrowser = QtWidgets.QTextBrowser(self.ActiveMessenger)
        self.textBrowser.setGeometry(QtCore.QRect(440, 60, 831, 581))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.ActiveMessenger)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(7)
        self.stackedWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.acceptRegButton.setText(_translate("Form", "ПОДТВЕРДИТЬ"))
        self.password.setPlaceholderText(_translate("Form", "Пароль"))
        self.login.setPlaceholderText(_translate("Form", "Логин"))
        self.acceptMenuButton.setText(_translate("Form", "АВТОРИЗАЦИЯ"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.passwordRepeat.setPlaceholderText(_translate("Form", "Повтор пароля"))
        self.label_2.setText(_translate("Form", "Авторизация"))
        self.loginAuth.setPlaceholderText(_translate("Form", "Логин"))
        self.acceptAuthButton.setText(_translate("Form", "ВОЙТИ"))
        self.passwordAuth.setPlaceholderText(_translate("Form", "Пароль"))
        self.regMenuButton.setText(_translate("Form", "РЕГИСТРАЦИЯ"))
        self.label_3.setText(_translate("Form", "Редактирование"))
        self.surname.setPlaceholderText(_translate("Form", "Фамилия"))
        self.name.setPlaceholderText(_translate("Form", "Имя"))
        self.city.setPlaceholderText(_translate("Form", "Город"))
        self.email.setPlaceholderText(_translate("Form", "Почта"))
        self.phoneNumber.setPlaceholderText(_translate("Form", "Телефон"))
        self.label_4.setText(_translate("Form", "Дата рождения:"))
        self.label_5.setText(_translate("Form", "Пол:"))
        self.comboBox.setItemText(0, _translate("Form", "Мужской"))
        self.comboBox.setItemText(1, _translate("Form", "Женский"))
        self.backButton.setText(_translate("Form", "ВЕРНУТЬСЯ"))
        self.saveButton.setText(_translate("Form", "СОХРАНИТЬ"))
        self.messagesButton.setText(_translate("Form", "Сообщения"))
        self.mainPageButton.setText(_translate("Form", "Моя страница"))
        self.friendsButton.setText(_translate("Form", "Друзья"))
        self.myPhoto.setText(_translate("Form", "Фото"))
        self.editButton.setText(_translate("Form", "Редактировать"))
        self.myStatus.setText(_translate("Form", "Статус"))
        self.addingPostButton.setText(_translate("Form", "Текст поста"))
        self.publishButton.setText(_translate("Form", "Опубликовать"))
        self.label_6.setText(_translate("Form", "Город:"))
        self.myCity.setText(_translate("Form", "Unknown"))
        self.mySurname.setText(_translate("Form", "Unknown"))
        self.myName.setText(_translate("Form", "Unknown"))
        self.label_8.setText(_translate("Form", "Почта:"))
        self.saveStatusButton.setText(_translate("Form", "Сохранить"))
        self.myEmail.setText(_translate("Form", "Unknown"))
        self.label_9.setText(_translate("Form", "Телефон:"))
        self.myNumber.setText(_translate("Form", "Unknown"))
        self.label_10.setText(_translate("Form", "Пол:"))
        self.mySex.setText(_translate("Form", "Unknown"))
        self.label_11.setText(_translate("Form", "Дата рождения:"))
        self.myBirthDate.setText(_translate("Form", "Unknown"))
        self.exitButton.setText(_translate("Form", "Выйти"))
        self.messagesButton_2.setText(_translate("Form", "Сообщения"))
        self.friendsButton_2.setText(_translate("Form", "Друзья"))
        self.Photo.setText(_translate("Form", "Фото"))
        self.mainPageButton_2.setText(_translate("Form", "Моя страница"))
        self.addingFriendButton.setText(_translate("Form", "Добавить в друзья"))
        self.goToDialogButton.setText(_translate("Form", "Перейти к диалогу"))
        self.number.setText(_translate("Form", "Unknown"))
        self.label_15.setText(_translate("Form", "Пол:"))
        self.email_2.setText(_translate("Form", "Unknown"))
        self.city_2.setText(_translate("Form", "Unknown"))
        self.label_12.setText(_translate("Form", "Город:"))
        self.label_16.setText(_translate("Form", "Почта:"))
        self.surname_2.setText(_translate("Form", "Unknown"))
        self.sex.setText(_translate("Form", "Unknown"))
        self.label_17.setText(_translate("Form", "Дата рождения:"))
        self.label_13.setText(_translate("Form", "Телефон:"))
        self.name_2.setText(_translate("Form", "Unknown"))
        self.birthDate.setText(_translate("Form", "Unknown"))
        self.status.setText(_translate("Form", "Unknown"))
        self.friendsButton_5.setText(_translate("Form", "Друзья"))
        self.messagesButton_5.setText(_translate("Form", "Сообщения"))
        self.mainPageButton_5.setText(_translate("Form", "Моя страница"))
        self.searchByID.setText(_translate("Form", "Поиск по ID"))
        self.toSearchButton.setText(_translate("Form", "Искать"))
        self.mainPageButton_3.setText(_translate("Form", "Моя страница"))
        self.messagesButton_3.setText(_translate("Form", "Сообщения"))
        self.friendsButton_3.setText(_translate("Form", "Друзья"))
        self.friendsButton_4.setText(_translate("Form", "Друзья"))
        self.messagesButton_4.setText(_translate("Form", "Сообщения"))
        self.mainPageButton_4.setText(_translate("Form", "Моя страница"))
        self.TextMessageButton.setText(_translate("Form", "Текст сообщения"))
        self.sendingButton.setText(_translate("Form", "Отправить"))
