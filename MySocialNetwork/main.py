import json
import sys
from PyQt5 import QtWidgets, QtCore
import pyodbc
from datetime import datetime
from FlaskRequests import register, auth, checkInfo, editing, editStatus, postAdding, checkPosts, changingPosts, \
    sendingMessage, gettingMessage
from Interface import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
import easygui as e
from datetime import datetime
import time


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

        self.ui.saveButton.clicked.connect(self.editing)

        self.ui.saveStatusButton.clicked.connect(self.editStat)

        self.ui.publishButton.clicked.connect(self.postAdd)

        self.ui.exitButton.clicked.connect(self.exit)

        self.ui.sendingButton.clicked.connect(self.goToSend)

        self.after = time.time() - 24*60*60


    def exit(self):
        sys.exit()

    def show(self):
        self.main_win.show()

    def goToAuth(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Authorization)

    def goToReg(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Registration)

    def successAuth(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MyselfPage)

    def goToMessages(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ActiveMessenger)

    def goToMyPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MyselfPage)

    def goToFriends(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Friends)

    def goToEdit(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Editing)

    def goToSend(self):
        message = self.ui.TextMessageButton.text()
        login = self.ui.loginAuth.text()
        print(login)
        if len(message) != 0:
            message = f"{{\"login\": \"{login}\", \"message\": \"{message}\"}}"
            data = json.loads(message)
            sendingMessage(data)
        else:
            return


    def formatmessage(self, message):
        login = message['login']
        message_text = message['message']
        dt = datetime.fromtimestamp(message['date'])
        dt = dt.strftime('%Y/%m/%d %H:%M:%S')
        print(f'{login} {dt}\n{message_text}\n')
        return f'{login} {dt}\n{message_text}\n'


    def updateMessage(self):
        result = gettingMessage(self.after)
        messages = result.json()['messages']
        for message in messages:
            print(message)
            self.ui.textBrowser.append(self.formatmessage(message))
            self.ui.textBrowser.repaint()
            self.after = message['date']


    def regCheck(self):
        login = self.ui.login.text()
        password = self.ui.password.text()
        repPassword = self.ui.passwordRepeat.text()
        if password == repPassword:
            if len(login) != 0:
                if len(password) != 0:
                    if len(repPassword) != 0:
                        if len(password) > 2:
                            result = register(login, password)
                            if result:
                                e.msgbox("You have successfully registered!", "Registration success")
                                self.goToAuth()
                            else:
                                e.msgbox("Something went wrong", "Registration error")
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
                    if result:
                        result2 = checkInfo(login)
                        if result2 != False:
                            result3 = checkPosts(login)
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
                            if result3 != False:
                                postInfoMas = result3
                                self.ui.postDate1.setText(postInfoMas[0])
                                self.ui.postText1.setText(postInfoMas[1])
                            self.successAuth()
                            self.timer = QtCore.QTimer()
                            self.timer.timeout.connect(self.updateMessage)
                            self.timer.start(1000)
                        else:
                            e.msgbox("Something went wrong", "Authorization error")
                else:
                    e.msgbox("Field 'Password' must contain at least 3 symbols", "Authorization error")
            else:
                e.msgbox("Field 'Password' is empty", "Authorization error")
        else:
            e.msgbox("Field 'Login' is empty", "Authorization error")


    def editing(self):
        login = self.ui.loginAuth.text()
        if len(self.ui.surname.text()) != 0:
            surname = self.ui.surname.text()
            if len(self.ui.name.text()) != 0:
                name = self.ui.name.text()
                if len(self.ui.city.text()) != 0:
                    city = self.ui.city.text()
                    if len(self.ui.email.text()) != 0:
                        email = self.ui.email.text()
                        if len(self.ui.phoneNumber.text()) != 0:
                            if len(self.ui.phoneNumber.text()) < 13:
                                if ((self.ui.phoneNumber.text()[0] == '+') and (len(self.ui.phoneNumber.text()) == 12)) or ((self.ui.phoneNumber.text()[0] == '8') and (len(self.ui.phoneNumber.text()) == 11)):
                                    number = self.ui.phoneNumber.text()
                                    if len(self.ui.comboBox) != 0:
                                        sex_full = self.ui.comboBox.currentText()
                                        #print(sex_full)
                                        if sex_full == "Мужской":
                                            sex = "М"
                                        else:
                                            sex = "Ж"
                                        if len(self.ui.dateEdit.text()) != 0:
                                            date = str(self.ui.dateEdit.text())
                                            #print(date)
                                            result = editing(surname, name, sex, city, number, email, date, login)
                                            #print(result)
                                            if result:
                                                result2 = checkInfo(login)
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
                                            e.msgbox("Field 'Date' is empty", "Editing error")
                                    else:
                                        e.msgbox("Field 'Sex' is empty", "Editing error")
                                else:
                                    e.msgbox("Invalid phone number", "Editing error")
                            else:
                                e.msgbox("Invalid phone number", "Editing error")
                        else:
                            e.msgbox("Field 'Phone number' is empty", "Editing error")
                    else:
                        e.msgbox("Field 'Email' is empty", "Editing error")
                else:
                    e.msgbox("Field 'City' is empty", "Editing error")
            else:
                e.msgbox("Field 'Name' is empty", "Editing error")
        else:
            e.msgbox("Field 'Surname' is empty", "Editing error")

    def editStat(self):
        login = self.ui.loginAuth.text()
        status = self.ui.myStatus.text()
        result = editStatus(login, status)
        if result:
            self.successAuth()
        else:
            e.msgbox("Something went wrong", "Status editing error")


    def postChange(self):
        login = self.ui.loginAuth.text()
        newPost = self.ui.addingPostButton.text()
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        result = changingPosts(login, newPost, formatted_date)
        if result:
            mas = checkPosts(login)
            self.ui.postDate1.setText(mas[0])
            self.ui.postText1.setText(mas[1])
            self.successAuth()
        else:
            e.msgbox("Something went wrong", "Status editing error")

    def postAdd(self):
        login = self.ui.loginAuth.text()
        if len(self.ui.addingPostButton.text()) != 0:
            post = self.ui.addingPostButton.text()
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            if self.ui.postText1.text() == "":
                result = postAdding(login, post, formatted_date)
                if result:
                    mas = checkPosts(login)
                    self.ui.postDate1.setText(mas[0])
                    self.ui.postText1.setText(mas[1])
                    self.successAuth()
                else:
                    e.msgbox("Something went wrong", "Post adding error")
            else:
                self.postChange()

        else:
            e.msgbox("Field 'Text of publication' is empty", "Publication error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainPage()
    main_win.show()

    sys.exit(app.exec_())
