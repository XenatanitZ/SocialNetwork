import sys
from PyQt5 import QtWidgets

from FlaskMethods import register, auth, checkInfo
from Interface import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
import easygui as e

QT_QPA_PLATFORM_PLUGIN_PATH="C:\\Users\\furys\\PycharmProjects\\SocialNetwork\\venv\\Lib\\site-packages\\PyQt5\\Qt5\\plugins\\platforms"

class MainPage:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Registration)

        self.ui.acceptMenuButton.clicked.connect(self.goToAuth)

        self.ui.regMenuButton.clicked.connect(self.goToReg)

        self.ui.messagesButton.clicked.connect(self.goToMessages)
        self.ui.messagesButton_2.clicked.connect(self.goToMessages)
        self.ui.messagesButton_3.clicked.connect(self.goToMessages)
        self.ui.messagesButton_4.clicked.connect(self.goToMessages)
        self.ui.messagesButton_5.clicked.connect(self.goToMessages)

        self.ui.mainPageButton.clicked.connect(self.goToMyPage)
        self.ui.mainPageButton_2.clicked.connect(self.goToMyPage)
        self.ui.mainPageButton_3.clicked.connect(self.goToMyPage)
        self.ui.mainPageButton_4.clicked.connect(self.goToMyPage)
        self.ui.mainPageButton_5.clicked.connect(self.goToMyPage)

        self.ui.backButton.clicked.connect(self.goToMyPage)

        self.ui.friendsButton.clicked.connect(self.goToFriends)
        self.ui.friendsButton_2.clicked.connect(self.goToFriends)
        self.ui.friendsButton_3.clicked.connect(self.goToFriends)
        self.ui.friendsButton_4.clicked.connect(self.goToFriends)
        self.ui.friendsButton_5.clicked.connect(self.goToFriends)

        self.ui.editButton.clicked.connect(self.goToEdit)

        self.ui.acceptRegButton.clicked.connect(self.regCheck)

        self.ui.acceptAuthButton.clicked.connect(self.authCheck)


    def show(self):
        self.main_win.show()

    def goToAuth(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Authorization)

    def goToReg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Registration)

    def successAuth(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MyselfPage)

    def goToMessages(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.InactiveMessenger)

    def goToMyPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MyselfPage)

    def goToFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Friends)

    def goToEdit(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Editing)

    def regCheck(self):
        login = self.ui.login.text()
        password = self.ui.password.text()
        repPassword = self.ui.passwordRepeat.text()
        print(login, password, repPassword)
        if password == repPassword:
            if len(login) != 0:
                if len(password) != 0:
                    if len(repPassword) != 0:
                        if len(password) > 2:
                            register(login, password)
                        else:
                            e.msgbox("Field 'Password' must contain at least 3 symbols", "Registration error")
                    else:
                        e.msgbox("Field 'Password accept' is empty", "Registration error")
                else:
                    e.msgbox("Field 'Password' is empty", "Registration error")
            else:
                e.msgbox("Field 'Login' is empty", "Registration error")
        else:
            e.msgbox("Fields 'Password' and 'Password accept' don't match", "Registration error")

    def authCheck(self):
        login = self.ui.loginAuth.text()
        password = self.ui.passwordAuth.text()
        if len(login) != 0:
            if len(password) != 0:
                if len(password) > 2:
                    result = auth(login, password)
                    if result != False:
                        result2 = checkInfo(result)
                        if result2 != False:
                            userInfoMas = result2
                            sexM = "Мужской"
                            sexZh = "Женский"
                            self.ui.mySurname.setText(userInfoMas[1])
                            self.ui.myName.setText(userInfoMas[0])
                            if userInfoMas[2] == "М":
                                self.ui.mySex.setText(sexM)
                            else:
                                self.ui.mySex.setText(sexZh)
                            self.ui.myBirthDate.setText(userInfoMas[3])
                            self.ui.myCity.setText(userInfoMas[4])
                            self.ui.myStatus.setText(userInfoMas[5])
                            self.ui.myEmail.setText(userInfoMas[6])
                            self.ui.myNumber.setText(userInfoMas[7])
                            self.successAuth()
                        else:
                            e.msgbox("Something went wrong", "Authorization error")
                    else:
                        e.msgbox("Invalid login or password", "Authorization error")
                else:
                    e.msgbox("Field 'Password' must contain at least 3 symbols", "Authorization error")
            else:
                e.msgbox("Field 'Password' is empty", "Authorization error")
        else:
            e.msgbox("Field 'Login' is empty", "Authorization error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainPage()
    main_win.show()

    sys.exit(app.exec_())
