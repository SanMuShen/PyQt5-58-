# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z.dl.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  QEvent,QTimer,Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from MysqlPython import MysqlHelp
# 哈希加密
from hashlib import sha1
# 加载短信验证码模块
import zhenzismsclient as smsclient
import random
from ServerZhong import *

class Ui_MainWindow(QtWidgets.QMainWindow,object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1064, 627)
        # 设置无窗口
        self.MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget{background-color:#B8DCFE}")
        #添加标题栏
        self.page = QtWidgets.QWidget(self.MainWindow)
        self.page.setObjectName("page")
        self.page.setGeometry(QtCore.QRect(0,0,1065,33))
        self.page.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/btl.png');border:none}")
        #关闭按钮
        self.pushButton_1 = QtWidgets.QPushButton(self.page)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setGeometry(1034,0,31,33)
        self.pushButton_1.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_dl.png')} QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_1.clicked.connect(self.MainWindow.close)
        #最小化按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setObjectName("pushButton_1")
        self.pushButton_2.setGeometry(1003,0,31,33)
        self.pushButton_2.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zxh_dl.png')} QWidget:hover{background-image:url('D:/tongcheng/image/zxhhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/zxhpressed.png');border:none}")
        self.pushButton_2.clicked.connect(self.MainWindow.showMinimized)

        self.textBrowser = QtWidgets.QTextBrowser   (self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 33, 1081, 611))
        self.textBrowser.setStyleSheet("background-image: url(D:/tongcheng/image/logo3.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 60, 291, 91))
        self.label_4.setStyleSheet("background: transparent;")  # 标题租房信息查询
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 61, 31))
        self.label.setStyleSheet("background: transparent;")  # 用户名标题
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 220, 51, 31))
        self.label_2.setStyleSheet("background: transparent;")  # 密码标题
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(250, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.lineEdit.setFont(font)
        self.lineEdit.setToolTip("")
        self.lineEdit.setStyleSheet("background: transparent;")  # 用户名文本框
        self.lineEdit.setPlaceholderText("账号/手机号/邮箱")
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 220, 171, 31))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setStyleSheet("background: transparent;")  # 密码文本框
        self.lineEdit_2.setPlaceholderText("密码")
        self.lineEdit_2.setMaxLength(16)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # 设置记住密码选择按钮
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 290, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet("background: transparent;")

        # 设置登录主按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 340, 121, 51))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n")
        self.pushButton.setFlat(False)
        # 设置鼠标样式
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        # 设置注册账号按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280,290,71,20))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);background:transparent;font-size:14px;")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton3")

        # 设置忘记密码按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 290, 71, 20))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);background:transparent;font-size:14px;")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton4")

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">租房信息查询</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">用户名:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">密码:</span></p></body></html>"))
        self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18px;\">记住密码</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_3.setText(_translate("MainWindow","注册账号"))
        self.pushButton_4.setText(_translate("MainWindow","忘记密码?"))
        # 点击注册账号开始进行一系列判定
        self.pushButton_3.clicked.connect(self.TZButton)

        # 点击忘记密码开始进行一系列判定
        self.pushButton_4.clicked.connect(self.WJ_MM)

        # 点击按钮开始进行数据库验证
        self.pushButton.clicked.connect(self.YZ_ZhanghuMa)

    # 定义点击忘记密码按钮跳转按钮
    def WJ_MM(self):
        self.WJ_Window()
    
    # 设置忘记密码界面
    def WJ_Window(self):
        self.dialog_w = QtWidgets.QDialog()
        self.dialog_w.setObjectName("dialog_w")
        self.dialog_w.resize(500,500)
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        self.dialog_w.move(zc_x+200,zc_y+80)

        # 设置无边框
        self.dialog_w.setWindowFlags(Qt.FramelessWindowHint)

        self.centralWidget_w = QtWidgets.QTextBrowser(self.dialog_w)
        self.centralWidget_w.setObjectName("centralWidget_w")
        self.centralWidget_w.resize(550,500)
        self.centralWidget_w.setStyleSheet("background-image: url(D:/tongcheng/image/zc_bj.png);")

        # 添加标题栏
        self.page_ww = QtWidgets.QWidget(self.dialog_w)
        self.page_ww.setObjectName("page_ww")
        self.page_ww.setGeometry(QtCore.QRect(0, 0, 500, 33))
        self.page_ww.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/zc_btl.png');border:none}")

        # 设置关闭按钮
        self.pushButton_wg = QtWidgets.QPushButton(self.dialog_w)
        self.pushButton_wg.setObjectName("pushButton_wg")
        self.pushButton_wg.setGeometry(QtCore.QRect(468, 0, 31, 33))
        self.pushButton_wg.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb.png')} QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_wg.clicked.connect(self.dialog_w.close)

        # 设置最小化按钮
        self.pushButton_wz = QtWidgets.QPushButton(self.dialog_w)
        self.pushButton_wz.setObjectName("pushButton_wz")
        self.pushButton_wz.setGeometry(440,0,31,33)
        self.pushButton_wz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zxh.png')} QWidget:hover{background-image:url('D:/tongcheng/image/zxhhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/zxhpressed.png');border:none}")
        self.pushButton_wz.clicked.connect(self.dialog_w.showMinimized)

        # 账号文本
        self.label_z = QtWidgets.QLabel(self.dialog_w)
        self.label_z.setGeometry(QtCore.QRect(100,110,101,31))
        self.label_z.setObjectName("label_z")
        self.label_z.setStyleSheet("background:transparent;")

        # 请输入手机号文本
        self.label_s = QtWidgets.QLabel(self.dialog_w)
        self.label_s.setGeometry(QtCore.QRect(90,150,101,31))
        self.label_s.setObjectName("label_s")
        self.label_s.setStyleSheet("background:transparent;")

        # 请输入验证码文本
        self.label_h = QtWidgets.QLabel(self.dialog_w)
        self.label_h.setGeometry(QtCore.QRect(90,190,101,31))
        self.label_h.setObjectName("label_h")
        self.label_h.setStyleSheet("background:transparent;")

        # 设置新的密码文本
        self.label_x = QtWidgets.QLabel(self.dialog_w)
        self.label_x.setGeometry(QtCore.QRect(90,230,101,31))
        self.label_x.setObjectName("label_x")
        self.label_x.setStyleSheet("background:transparent;")

        # 账号文本框
        self.lineEdit_z = QtWidgets.QLineEdit(self.dialog_w)
        self.lineEdit_z.setEnabled(True)
        self.lineEdit_z.setGeometry(QtCore.QRect(200,110,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_z.setFont(font)
        self.lineEdit_z.setToolTip("")
        self.lineEdit_z.setStyleSheet("background:transparent;")
        self.lineEdit_z.setMaxLength(16)
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.lineEdit_z.setPlaceholderText("请输入用户名")

        # 手机号文本框
        self.lineEdit_s = QtWidgets.QLineEdit(self.dialog_w)
        self.lineEdit_s.setEnabled(True)
        self.lineEdit_s.setGeometry(QtCore.QRect(200,150,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_s.setFont(font)
        self.lineEdit_s.setToolTip("")
        self.lineEdit_s.setStyleSheet("background:transparent;")
        self.lineEdit_s.setMaxLength(16)
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.lineEdit_s.setPlaceholderText("请输入手机号")

        # 验证码文本框
        self.lineEdit_h = QtWidgets.QLineEdit(self.dialog_w)
        self.lineEdit_h.setEnabled(True)
        self.lineEdit_h.setGeometry(QtCore.QRect(200,190,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_h.setFont(font)
        self.lineEdit_h.setToolTip("")
        self.lineEdit_h.setStyleSheet("background:transparent;")
        self.lineEdit_h.setMaxLength(16)
        self.lineEdit_h.setObjectName("lineEdit_h")
        self.lineEdit_h.setPlaceholderText("请输入验证码")

        # 设置新的密码文本框
        self.lineEdit_x = QtWidgets.QLineEdit(self.dialog_w)
        self.lineEdit_x.setEnabled(True)
        self.lineEdit_x.setGeometry(QtCore.QRect(200,230,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_x.setFont(font)
        self.lineEdit_x.setToolTip("")
        self.lineEdit_x.setStyleSheet("background:transparent;")
        self.lineEdit_x.setMaxLength(16)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.lineEdit_x.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_x.setPlaceholderText("请设置新的密码")

        # 发送验证码按钮
        self.pushButton_fs = QtWidgets.QPushButton(self.lineEdit_s)
        self.pushButton_fs.setGeometry(QtCore.QRect(120,0,80,31))
        self.pushButton_fs.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/fsyzman_bj.png')}")
        self.pushButton_fs.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_fs.setObjectName("pushButton_fs")

        # 设置确定按钮
        self.pushButton_x = QtWidgets.QPushButton(self.dialog_w)
        self.pushButton_x.setGeometry(QtCore.QRect(200,280,121,51))
        # self.pushButton_x.setStyleSheet("font: 75 12pt \"Aharoni\";")
        self.pushButton_x.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/wjqd_bj.png')}")
        self.pushButton_x.setObjectName("pushButton_x")

        self.retranslateUi_w(self.dialog_w)
        QtCore.QMetaObject.connectSlotsByName(self.dialog_w)
        self.dialog_w.exec_()

    def retranslateUi_w(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_z.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">用户名:</span></p></body></html>"))
        self.label_z.setStyleSheet("color:#000000")
        self.label_s.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">请输入手机号:</span></p></body></html>"))
        self.label_s.setStyleSheet("color:#000000")
        self.label_h.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">请输入验证码:</span></p></body></html>"))
        self.label_h.setStyleSheet("color:#000000")
        self.label_x.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">请输入新密码:</span></p></body></html>"))
        self.label_x.setStyleSheet("color:#000000")

        # 点击发送验证码
        self.pushButton_fs.clicked.connect(self.FSyanzhengma)
        # 点击确定
        self.pushButton_x.clicked.connect(self.FSYZM)

    
    # 点击验证码后进行一系列的验证
    def FSyanzhengma(self):
        zc_x = self.dialog_w.x()
        zc_y = self.dialog_w.y()
        username = self.lineEdit_z.text()
        phone = self.lineEdit_s.text()
        # 生成随机6位验证码
        n = ("1234567890")
        self.yzm = ""
        for i in range(6):
            s = random.choice(n)
            self.yzm += s
        # mysql = MysqlHelp("db4")
        # sql_select = 'select phone from user1 where username="%s"' % username
        # result = mysql.getAll(sql_select)
        S = WJY_function(username,phone)
        try:
            if int(phone) is True or len(phone) != 11:
                S = Ui_MainWindow2(zc_x,zc_y)
                S.CWO_Window()
            elif not username:
                # 请输入用户名
                self.YHM_window()
            elif S == 'YHBCZ':
                # 用户名不存在
                self.WJZ_Window()
            elif S == 'SJCW':
                # 请输入正确手机号
                E = Ui_MainWindow2(zc_x,zc_y)
                E.CWO_Window()
            elif S == 'CG':
                apiUrl = 'http://sms_developer.zhenzikj.com'
                client = smsclient.ZhenziSmsClient(apiUrl,100003,'8c921509-3b02-4e99-a349-b54bfdea070f')
                sjh = "%s"%phone
                dx = "您的验证码为%s。"%self.yzm
                result = client.send(sjh,dx)     
        except:
            S = Ui_MainWindow2(zc_x,zc_y)
            S.CWO_Window()

    # 定义点击确定按钮时输入的验证码是否与发送验证码一致以及修改密码
    def FSYZM(self):
        zc_x = self.dialog_w.x()
        zc_y = self.dialog_w.y()
        phone = self.lineEdit_s.text()
        username = self.lineEdit_z.text()
        yzmw = self.lineEdit_h.text()
        password = self.lineEdit_x.text()
        s1 = sha1()
        s1.update(password.encode('utf-8'))
        password2 = s1.hexdigest()

        S = WJX_function(username,password2,phone)

        # mysql = MysqlHelp("db4")
        # sql_select = 'select phone from user1 where username="%s"' % username
        # result = mysql.getAll(sql_select)

        try:
            if not username:
                # 请输入用户名
                self.YHM_window()
            elif S == 'YHBCZ':
                # 用户名不存在
                self.WJZ_Window()
            elif S == 'SJCW':
                # 请输入正确手机号
                E = Ui_MainWindow2(zc_x,zc_y)
                E.CWO_Window()
            elif not yzmw:
                # 验证码错误
                self.YZMC_Window()
            elif S == 'MMCG':
                if yzmw != self.yzm:
                    self.YZMC_Window()
                else:
                    
                    # sql_update = 'update user1 set password = "%s" where username="%s"'%(password2,username)
                    # P = MysqlHelp("db4")
                    # P.workOn(sql_update)
                    print("密码已成功重置")
                    self.dialog_w.close()
        except:
            self.YZMC_Window()

    # 定义点击注册账号按钮跳转窗口
    def TZButton(self):
        # parentWidget() 获取父控件
        self.centralwidget.parentWidget().close()

        # 获得主窗口的x，y坐标
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        self.zc_x = zc_x
        self.zc_y = zc_y
        w = Ui_MainWindow2(zc_x,zc_y)
        w.ZC_Window()

    # 验证用户的账号和密码
    def YZ_ZhanghuMa(self):
        # 获取登录界面文本框的内容
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not name:
            self.YHM_window()
        elif not password:
            self.SMM_Window()
        else:
            # 创建sha1加密对象
            s1 = sha1()
            # 转码 转成字节流
            s1.update(password.encode('utf-8'))
            # 返回十六进制加密结果
            password2 = s1.hexdigest()

            # 连接服务端函数
            S = DL_funtcion(name,password2)
            if S == "TG":
                self.TZButton_z()
            elif S == "SB":
                self.TZCWButton()

            # 和数据库中的表记录进行匹配
            # mysql = MysqlHelp('db4')
            # sql_select = 'select password from user1 where username="%s";' % name
            # result = mysql.getAll(sql_select)
            # if len(result) == 0:
            #     # 用户名不存在
            #     self.TZCWButton()
            # elif result[0][0] != password2:
            #     # 密码错误
            #     self.TZCWButton()
            # else:
            #     # 成功登录
            #     self.TZButton_z()

    # 设置点击登录按钮跳转到功能界面
    def TZButton_z(self):
        self.MainWindow.close()
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        w = Ui_MainWindow2(zc_x,zc_y)
        w.setupUi_d()

    # 设置账号或密码错误跳转界面
    def TZCWButton(self):
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        w = Ui_MainWindow2(zc_x, zc_y)
        w.CW_Window()

    #请输入用户名界面
    def YHM_window(self):
        self.dialog_y = QtWidgets.QDialog()
        self.dialog_y.setObjectName("dialog_y")
        self.dialog_y.resize(330, 300)
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        self.dialog_y.move(zc_x + 330, zc_y + 150)

        # 设置无窗口
        self.dialog_y.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_y = QtWidgets.QWidget(self.dialog_y)
        self.centralwidget_y.setGeometry(QtCore.QRect(0, 33, 330, 300))
        self.centralwidget_y.setObjectName("centralwidget_y")
        self.centralwidget_y.setStyleSheet("background-image:url('D:/tongcheng/image/shu_zhang_bj.png');")

        # 添加标题栏
        self.page_y = QtWidgets.QWidget(self.dialog_y)
        self.page_y.setObjectName("page_y")
        self.page_y.setGeometry(QtCore.QRect(0, 0, 330, 33))
        self.page_y.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_5 = QtWidgets.QPushButton(self.page_y)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(299, 0, 31, 33)
        self.pushButton_5.setStyleSheet(
            "QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_5.clicked.connect(self.dialog_y.close)

        # 添加关闭确定按钮
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget_y)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setGeometry(45, 200, 250, 45)
        self.pushButton_6.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_6.clicked.connect(self.dialog_y.close)

        self.dialog_y.exec_()

    # 请输入密码界面
    def SMM_Window(self):
        self.dialog_s = QtWidgets.QDialog()
        self.dialog_s.setObjectName("dialog_s")
        self.dialog_s.resize(330,300)
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        self.dialog_s.move(zc_x + 330, zc_y + 150)

        # 设置无窗口
        self.dialog_s.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_s = QtWidgets.QWidget(self.dialog_s)
        self.centralwidget_s.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_s.setObjectName("centralwidget_s")
        self.centralwidget_s.setStyleSheet("background-image:url('D:/tongcheng/image/shu_mm_bj.png');")

        # 添加标题栏
        self.page_s = QtWidgets.QWidget(self.dialog_s)
        self.page_s.setObjectName("page_s")
        self.page_s.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_s.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_Sgb = QtWidgets.QPushButton(self.page_s)
        self.pushButton_Sgb.setObjectName("pushButton_Sgb")
        self.pushButton_Sgb.setGeometry(299,0,31,33)
        self.pushButton_Sgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_Sgb.clicked.connect(self.dialog_s.close)

        # 添加关闭确定按钮
        self.pushButton_sgb = QtWidgets.QPushButton(self.centralwidget_s)
        self.pushButton_sgb.setObjectName("pushButton_sgb")
        self.pushButton_sgb.setGeometry(45,200,250,45)
        self.pushButton_sgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_sgb.clicked.connect(self.dialog_s.close)

        self.dialog_s.exec_()

    # 忘记密码界面用户名不存在
    def WJZ_Window(self):
        self.dialog_e = QtWidgets.QDialog()
        self.dialog_e.setObjectName("dialog_e")
        self.dialog_e.resize(330,300)
        zc_x = self.dialog_w.x()
        zc_y = self.dialog_w.y()
        self.dialog_e.move(zc_x + 90, zc_y + 65)

        # 设置无窗口
        self.dialog_e.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_e = QtWidgets.QWidget(self.dialog_e)
        self.centralwidget_e.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_e.setObjectName("centralwidget_e")
        self.centralwidget_e.setStyleSheet("background-image:url('D:/tongcheng/image/wj_yhmbcz_bj.png');")

        # 添加标题栏
        self.page_e = QtWidgets.QWidget(self.dialog_e)
        self.page_e.setObjectName("page_e")
        self.page_e.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_e.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_egb = QtWidgets.QPushButton(self.page_e)
        self.pushButton_egb.setObjectName("pushButton_egb")
        self.pushButton_egb.setGeometry(299,0,31,33)
        self.pushButton_egb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_egb.clicked.connect(self.dialog_e.close)

        # 添加关闭确定按钮
        self.pushButton_Egb = QtWidgets.QPushButton(self.centralwidget_e)
        self.pushButton_Egb.setObjectName("pushButton_Egb")
        self.pushButton_Egb.setGeometry(45,200,250,45)
        self.pushButton_Egb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_Egb.clicked.connect(self.dialog_e.close)

        self.dialog_e.exec_()

    # 验证码错误
    def YZMC_Window(self):
        self.dialog_q = QtWidgets.QDialog()
        self.dialog_q.setObjectName("dialog_q")
        self.dialog_q.resize(330,300)
        zc_x = self.centralwidget.parentWidget().x()
        zc_y = self.centralwidget.parentWidget().y()
        self.dialog_q.move(zc_x + 330, zc_y + 150)

        # 设置无窗口
        self.dialog_q.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_q = QtWidgets.QWidget(self.dialog_q)
        self.centralwidget_q.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_q.setObjectName("centralwidget_q")
        self.centralwidget_q.setStyleSheet("background-image:url('D:/tongcheng/image/wj_yzmcw_bj.png');")

        # 添加标题栏
        self.page_q = QtWidgets.QWidget(self.dialog_q)
        self.page_q.setObjectName("page_q")
        self.page_q.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_q.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_Sqgb = QtWidgets.QPushButton(self.page_q)
        self.pushButton_Sqgb.setObjectName("pushButton_Sqgb")
        self.pushButton_Sqgb.setGeometry(299,0,31,33)
        self.pushButton_Sqgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_Sqgb.clicked.connect(self.dialog_q.close)

        # 添加关闭确定按钮
        self.pushButton_sqgb = QtWidgets.QPushButton(self.centralwidget_q)
        self.pushButton_sqgb.setObjectName("pushButton_sqgb")
        self.pushButton_sqgb.setGeometry(45,200,250,45)
        self.pushButton_sqgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_sqgb.clicked.connect(self.dialog_q.close)

        self.dialog_q.exec_()

# 注册界面
class Ui_MainWindow2(QtWidgets.QDialog):
    def __init__(self,zc_x,zc_y):
        super().__init__()
        self.zcc_x = zc_x
        self.zcc_y = zc_y

    def ZC_Window(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setObjectName("Dialog")
        # 设置注册界面宽高
        self.dialog.resize(500, 500)

        # 根据登录窗口移动注册窗口
        a = self.zcc_x
        b = self.zcc_y
        self.dialog.move(a+200,b+100)

        # 建立界面主框架
        self.textBrowser = QtWidgets.QTextBrowser(self.dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 33, 500, 467))
        self.textBrowser.setStyleSheet("background-image: url(D:/tongcheng/image/zc_bj.png);")
        self.textBrowser.setObjectName("textBrowser")

        # 设置dialog  无边框
        self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # 添加标题栏
        self.page = QtWidgets.QWidget(self.dialog)
        self.page.setObjectName("page")
        self.page.setGeometry(QtCore.QRect(0, 0, 500, 33))
        self.page.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/zc_btl.png');border:none}")

        # 设置关闭按钮
        self.pushButton_g = QtWidgets.QPushButton(self.page)
        self.pushButton_g.setObjectName("pushButton_g")
        self.pushButton_g.setGeometry(QtCore.QRect(468, 0, 31, 33))
        self.pushButton_g.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb.png')} QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_g.clicked.connect(self.dialog.close)

        # 设置最小化按钮
        self.pushButton_z = QtWidgets.QPushButton(self.page)
        self.pushButton_z.setObjectName("pushButton_z")
        self.pushButton_z.setGeometry(440,0,31,33)
        self.pushButton_z.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zxh.png')} QWidget:hover{background-image:url('D:/tongcheng/image/zxhhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/zxhpressed.png');border:none}")
        self.pushButton_z.clicked.connect(self.dialog.showMinimized)

        #  注册用户名文本
        self.label_6 = QtWidgets.QLabel(self.dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 110, 101, 31))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setObjectName("label_6")

        # 注册用户名文本框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 110, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setToolTip("")
        self.lineEdit_3.setStyleSheet("background: transparent;")
        # 设置最长字符为16
        self.lineEdit_3.setMaxLength(16)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("请输入用户名")

        # 密码文本框
        self.lineEdit_4 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 160, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setToolTip("")
        self.lineEdit_4.setStyleSheet("background: transparent;")
        self.lineEdit_4.setMaxLength(16)
        # 输入内容不可见
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setPlaceholderText("密码至多为16位")
        self.lineEdit_4.setObjectName("lineEdit_4")

        # 密码文本
        self.label_7 = QtWidgets.QLabel(self.dialog)
        self.label_7.setGeometry(QtCore.QRect(140, 160, 51, 31))
        self.label_7.setStyleSheet("background: transparent;")
        self.label_7.setObjectName("label_7")

        # 确认密码文本框
        self.lineEdit_5 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 210, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setToolTip("")
        self.lineEdit_5.setStyleSheet("background: transparent;")
        self.lineEdit_5.setMaxLength(16)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setPlaceholderText("请再次输入密码")
        self.lineEdit_5.setObjectName("lineEdit_5")

        # 确认密码文本
        self.label_8 = QtWidgets.QLabel(self.dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 210, 71, 31))
        self.label_8.setStyleSheet("background: transparent;")
        self.label_8.setObjectName("label_8")

        # 手机号文本
        self.label_9 = QtWidgets.QLabel(self.dialog)
        self.label_9.setGeometry(QtCore.QRect(130,260,71,31))
        self.label_9.setStyleSheet("background: transparent;")
        self.label_9.setObjectName("label_9")

        # 手机号文本框
        self.lineEdit_6 = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setGeometry(QtCore.QRect(200,260,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setToolTip("")
        self.lineEdit_6.setStyleSheet("background: transparent;")
        self.lineEdit_6.setMaxLength(16)
        self.lineEdit_6.setPlaceholderText("手机号")
        self.lineEdit_6.setObjectName("lineEdit_6")

        # 验证码文本
        self.label_yz = QtWidgets.QLabel(self.dialog)
        self.label_yz.setGeometry(QtCore.QRect(130,310,71,31))
        self.label_yz.setStyleSheet("background: transparent;")
        self.label_yz.setObjectName("label_9")

        # 验证码文本框
        self.lineEdit_yz = QtWidgets.QLineEdit(self.dialog)
        self.lineEdit_yz.setEnabled(True)
        self.lineEdit_yz.setGeometry(QtCore.QRect(200,310,200,31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_yz.setFont(font)
        self.lineEdit_yz.setToolTip("")
        self.lineEdit_yz.setStyleSheet("background:transparent;")
        self.lineEdit_yz.setMaxLength(16)
        self.lineEdit_yz.setObjectName("lineEdit_h")
        self.lineEdit_yz.setPlaceholderText("请输入验证码")

        # 验证按钮
        self.pushButton_yzs = QtWidgets.QPushButton(self.lineEdit_6)
        self.pushButton_yzs.setGeometry(QtCore.QRect(120,0,80,31))
        self.pushButton_yzs.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/fsyzman_bj.png')}")
        self.pushButton_yzs.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_yzs.setObjectName("pushButton_yzs")

        # 注册按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 360, 121, 51))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"Aharoni\";")
        self.pushButton_2.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zcan_bj.png')}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(self.dialog)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        # 窗口启动方法
        self.dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">注册用户名:</span></p></body></html>"))
        self.label_6.setStyleSheet("color:#000000")
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">密码:</span></p></body></html>"))
        self.label_7.setStyleSheet("color:#000000")
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">确认密码:</span></p></body></html>"))
        self.label_8.setStyleSheet("color:#000000")
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">手机号:</span></p></body></html>"))
        self.label_yz.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">验证码:</span></p></body></html>"))
        self.label_yz.setStyleSheet("color:#000000")

        self.pushButton_2.setText(_translate("MainWindow", ""))

        # 点击发送验证码进行一系列判断
        self.pushButton_yzs.clicked.connect(self.YZM_Window)

        # 设置点击注册之后功能
        self.pushButton_2.clicked.connect(self.ZZ_zcwindow)

        # 获取注册页面的x，y坐标
        self.zcc_x = self.dialog.x()
        self.zcc_y = self.dialog.y()

    # 发送验证码
    def YZM_Window(self):
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        password2 = self.lineEdit_5.text()
        phone = self.lineEdit_6.text()
        # 生成随机6位验证码
        n = ("1234567890")
        self.yzm = ""
        for i in range(6):
            s = random.choice(n)
            self.yzm += s
        try:
            if int(phone) is True or len(phone) != 11:
                self.CWO_Window()
            elif not username or not password or not phone:
                self.CWQ_Window()
            elif password != password2:
                self.CWJ_Window()
            else:
                apiUrl = 'http://sms_developer.zhenzikj.com'
                client = smsclient.ZhenziSmsClient(apiUrl,100003,'8c921509-3b02-4e99-a349-b54bfdea070f')
                sjh = "%s"%phone
                dx = "您的验证码为%s。"%self.yzm
                result = client.send(sjh,dx)
        except:
            self.CWO_Window()



    # 判断注册界面是否全部填写
    def ZZ_zcwindow(self):
        # 获取文本框用户输入内容
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        password2 = self.lineEdit_5.text()
        phone = self.lineEdit_6.text()
        yyzm = self.lineEdit_yz.text()
        try:
            if not username or not password or not phone or not yyzm:
                # 注册界面必须全部填写
                self.CWQ_Window()
            # 判断两次输入的密码必须保持一致 
            elif password != password2:
                self.CWJ_Window()
            # 判断输入的是否是手机号
            # elif int(phone) is True or len(phone) != 11:
            #     self.CWO_Window()
            # 判断验证码是否一致
            elif yyzm != self.yzm:
                self.CWQQ_Window()
            else:
                # 对密码进行加密处理
                s1 = sha1()
                s1.update(password.encode('utf-8'))
                password3 = s1.hexdigest()

                # 连接服务器函数
                S = ZC_function(username,password3,phone)

                if S == 'SJBZC':
                    self.CWSS_Window()
                elif S == 'CGZC':
                    self.successfully()
                elif S == 'YHYCZ':
                    self.CWH_Window()
        except:
            self.CWQQ_Window()

            # # 判断用户名是否存在
            # mysql = MysqlHelp('db4')
            # sql_select1 = 'select password from user1 where username="%s";' % username
            # result1 = mysql.getAll(sql_select1)
            # # 判断手机号是否已被注册
            # sql_select2 = 'select password from user1 where phone="%s";' % phone
            # result2 = mysql.getAll(sql_select2)
            # if len(result1) == 0:
            #     if len(result2) == 1:
            #         self.CWSS_Window()
            #         print("该手机号已被注册")
            #     else:
            #         sql_insert = 'insert into user1(username,password,phone) values("%s","%s","%s")' % (username,password3,phone)
            #         mysql.workOn(sql_insert)
            #         self.successfully()
            # else:
            #     print("用户名已存在")
            #     self.CWH_Window()
        # except:
        #     self.CWO_Window()
    
    # 验证码错误
    def CWQQ_Window(self):
        self.dialog_r = QtWidgets.QDialog()
        self.dialog_r.setObjectName("dialog_r")
        self.dialog_r.resize(330,300)
        self.dialog_r.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_r.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_r = QtWidgets.QWidget(self.dialog_r)
        self.centralwidget_r.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_r.setObjectName("centralwidget_r")
        self.centralwidget_r.setStyleSheet("background-image:url('D:/tongcheng/image/wj_yzmcw_bj.png');")

        # 添加标题栏
        self.page_r = QtWidgets.QWidget(self.dialog_r)
        self.page_r.setObjectName("page_r")
        self.page_r.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_r.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_crgb = QtWidgets.QPushButton(self.page_r)
        self.pushButton_crgb.setObjectName("pushButton_crgb")
        self.pushButton_crgb.setGeometry(299,0,31,33)
        self.pushButton_crgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_crgb.clicked.connect(self.dialog_r.close)

        # 添加关闭确定按钮
        self.pushButton_qrgb = QtWidgets.QPushButton(self.centralwidget_r)
        self.pushButton_qrgb.setObjectName("pushButton_qrgb")
        self.pushButton_qrgb.setGeometry(45,200,250,45)
        self.pushButton_qrgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qrgb.clicked.connect(self.dialog_r.close)

        self.dialog_r.exec_()
    
    # 该手机号已被注册
    def CWSS_Window(self):
        self.dialog_ss = QtWidgets.QDialog()
        self.dialog_ss.setObjectName("dialog_ss")
        self.dialog_ss.resize(330,300)
        self.dialog_ss.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_ss.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_ss = QtWidgets.QWidget(self.dialog_ss)
        self.centralwidget_ss.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_ss.setObjectName("centralwidget_ss")
        self.centralwidget_ss.setStyleSheet("background-image:url('D:/tongcheng/image/zc_sjyzc_bj.png');")

        # 添加标题栏
        self.page_ss = QtWidgets.QWidget(self.dialog_ss)
        self.page_ss.setObjectName("page_ss")
        self.page_ss.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_ss.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_csgb = QtWidgets.QPushButton(self.page_ss)
        self.pushButton_csgb.setObjectName("pushButton_csgb")
        self.pushButton_csgb.setGeometry(299,0,31,33)
        self.pushButton_csgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_csgb.clicked.connect(self.dialog_ss.close)

        # 添加关闭确定按钮
        self.pushButton_qsgb = QtWidgets.QPushButton(self.centralwidget_ss)
        self.pushButton_qsgb.setObjectName("pushButton_qsgb")
        self.pushButton_qsgb.setGeometry(45,200,250,45)
        self.pushButton_qsgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qsgb.clicked.connect(self.dialog_ss.close)

        self.dialog_ss.exec_()

    # 设置注册内容必须全部填写界面
    def CWQ_Window(self):
        self.dialog_q = QtWidgets.QDialog()
        self.dialog_q.setObjectName("dialog_q")
        self.dialog_q.resize(330,300)
        self.dialog_q.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_q.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_q = QtWidgets.QWidget(self.dialog_q)
        self.centralwidget_q.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_q.setObjectName("centralwidget_q")
        self.centralwidget_q.setStyleSheet("background-image:url('D:/tongcheng/image/zhuce_tx_bj.png');")

        # 添加标题栏
        self.page_q = QtWidgets.QWidget(self.dialog_q)
        self.page_q.setObjectName("page_q")
        self.page_q.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_q.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_cqgb = QtWidgets.QPushButton(self.page_q)
        self.pushButton_cqgb.setObjectName("pushButton_cqgb")
        self.pushButton_cqgb.setGeometry(299,0,31,33)
        self.pushButton_cqgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_cqgb.clicked.connect(self.dialog_q.close)

        # 添加关闭确定按钮
        self.pushButton_qqgb = QtWidgets.QPushButton(self.centralwidget_q)
        self.pushButton_qqgb.setObjectName("pushButton_qqgb")
        self.pushButton_qqgb.setGeometry(45,200,250,45)
        self.pushButton_qqgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qqgb.clicked.connect(self.dialog_q.close)

        self.dialog_q.exec_()

    # 设置两次输入密码不一致界面
    def CWJ_Window(self):
        self.dialog_j = QtWidgets.QDialog()
        self.dialog_j.setObjectName("dialog_j")
        self.dialog_j.resize(330,300)
        self.dialog_j.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_j.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_j = QtWidgets.QWidget(self.dialog_j)
        self.centralwidget_j.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_j.setObjectName("centralwidget_j")
        self.centralwidget_j.setStyleSheet("background-image:url('D:/tongcheng/image/zhuce_mmyz_bj.png');")

        # 添加标题栏
        self.page_j = QtWidgets.QWidget(self.dialog_j)
        self.page_j.setObjectName("page_j")
        self.page_j.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_j.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_cjgb = QtWidgets.QPushButton(self.page_j)
        self.pushButton_cjgb.setObjectName("pushButton_cjgb")
        self.pushButton_cjgb.setGeometry(299,0,31,33)
        self.pushButton_cjgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_cjgb.clicked.connect(self.dialog_j.close)

        # 添加关闭确定按钮
        self.pushButton_qjgb = QtWidgets.QPushButton(self.centralwidget_j)
        self.pushButton_qjgb.setObjectName("pushButton_qjgb")
        self.pushButton_qjgb.setGeometry(45,200,250,45)
        self.pushButton_qjgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qjgb.clicked.connect(self.dialog_j.close)

        self.dialog_j.exec_()
    
    # 设置用户名已存在界面
    def CWH_Window(self):
        self.dialog_h = QtWidgets.QDialog()
        self.dialog_h.setObjectName("dialog_h")
        self.dialog_h.resize(330,300)
        self.dialog_h.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_h.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_h = QtWidgets.QWidget(self.dialog_h)
        self.centralwidget_h.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_h.setObjectName("centralwidget_h")
        self.centralwidget_h.setStyleSheet("background-image:url('D:/tongcheng/image/shu_yhcz_bj.png');")

        # 添加标题栏
        self.page_h = QtWidgets.QWidget(self.dialog_h)
        self.page_h.setObjectName("page_h")
        self.page_h.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_h.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_chgb = QtWidgets.QPushButton(self.page_h)
        self.pushButton_chgb.setObjectName("pushButton_chgb")
        self.pushButton_chgb.setGeometry(299,0,31,33)
        self.pushButton_chgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_chgb.clicked.connect(self.dialog_h.close)

        # 添加关闭确定按钮
        self.pushButton_qhgb = QtWidgets.QPushButton(self.centralwidget_h)
        self.pushButton_qhgb.setObjectName("pushButton_qhgb")
        self.pushButton_qhgb.setGeometry(45,200,250,45)
        self.pushButton_qhgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qhgb.clicked.connect(self.dialog_h.close)

        self.dialog_h.exec_()

    # 设置请输入正确的手机号界面
    def CWO_Window(self):
        self.dialog_o = QtWidgets.QDialog()
        self.dialog_o.setObjectName("dialog_o")
        self.dialog_o.resize(330,300)
        self.dialog_o.move(self.zcc_x + 100, self.zcc_y + 100)
        # 设置无窗口
        self.dialog_o.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_o = QtWidgets.QWidget(self.dialog_o)
        self.centralwidget_o.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_o.setObjectName("centralwidget_o")
        self.centralwidget_o.setStyleSheet("background-image:url('D:/tongcheng/image/shu_sjh_bj.png');")

        # 添加标题栏
        self.page_o = QtWidgets.QWidget(self.dialog_o)
        self.page_o.setObjectName("page_o")
        self.page_o.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_o.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_cogb = QtWidgets.QPushButton(self.page_o)
        self.pushButton_cogb.setObjectName("pushButton_cogb")
        self.pushButton_cogb.setGeometry(299,0,31,33)
        self.pushButton_cogb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_cogb.clicked.connect(self.dialog_o.close)

        # 添加关闭确定按钮
        self.pushButton_qogb = QtWidgets.QPushButton(self.centralwidget_o)
        self.pushButton_qogb.setObjectName("pushButton_qogb")
        self.pushButton_qogb.setGeometry(45,200,250,45)
        self.pushButton_qogb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qogb.clicked.connect(self.dialog_o.close)

        self.dialog_o.exec_()

    # 设置注册成功界面
    def successfully(self):
        self.dialog_s = QtWidgets.QDialog()
        self.dialog_s.setObjectName("Dialog1")

        # 设置注册成功界面宽高
        self.dialog_s.resize(320, 250)
        self.dialog_s.move(self.zcc_x+130,self.zcc_y+150)

        self.textBrowser1 = QtWidgets.QWidget(self.dialog_s)
        self.textBrowser1.setGeometry(QtCore.QRect(0, 33, 320, 220))
        self.textBrowser1.setStyleSheet("background-image: url(D:/tongcheng/image/zccc_bj.png);")
        self.textBrowser1.setObjectName("textBrowser1")

        # 设置dialog_s  无边框
        self.dialog_s.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # 添加标题栏
        self.page_2 = QtWidgets.QWidget(self.dialog_s)
        self.page_2.setObjectName("page_2")
        self.page_2.setGeometry(QtCore.QRect(0, 0, 320, 33))
        self.page_2.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/zccc_btl.png');border:none}")

        # 设置立即登录按钮
        self.pushButton_s = QtWidgets.QPushButton(self.dialog_s)
        self.pushButton_s.setGeometry(QtCore.QRect(92,190,160,50))
        self.pushButton_s.setStyleSheet("font:75 12pt \"Aharoni\";")
        self.pushButton_s.setObjectName("pushButton_s")
        self.pushButton_s.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zcccan.btl.png')}")
        _translate = QtCore.QCoreApplication.translate
        self.dialog_s.setWindowTitle(_translate("Dialog","Dialog"))
        # self.pushButton_s.setText(_translate("Dialog",""))

        # 设置关闭按钮
        self.pushButton_g1 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_g1.setObjectName("pushButton_g1")
        self.pushButton_g1.setGeometry(QtCore.QRect(290, 0, 31, 33))
        self.pushButton_g1.setStyleSheet(
            "QPushButton{background-image:url('D:/tongcheng/image/gb_zccc.png')} QWidget:hover{background-image:url('D:/tongcheng/image/gb_zccchover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gb_zcccpressed.png');border:none}")
        self.pushButton_g1.clicked.connect(self.dialog_s.close)

        # 设置最小化按钮
        self.pushButton_z1 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_z1.setObjectName("pushButton_z")
        self.pushButton_z1.setGeometry(260, 0, 31, 33)
        self.pushButton_z1.setStyleSheet(
            "QPushButton{background-image:url('D:/tongcheng/image/zxh_accc.png')} QWidget:hover{background-image:url('D:/tongcheng/image/zxh_accchover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/zxh_acccpressed.png');border:none}")
        self.pushButton_z1.clicked.connect(self.page_2.showMinimized)

        # 点击按钮后连接功能界面
        self.pushButton_s.clicked.connect(self.LJ_window)
        # 显示界面
        self.dialog_s.exec_()

    # 设置点击立即登录跳转功能界面
    def LJ_window(self):
        self.dialog_s.close()
        self.dialog.close()
        self.setupUi_d()

    # 设置登录成功，注册成功后进入界面
    def setupUi_d(self):
        # 关闭注册界面以及注册成功界面

        self.dialog_d = QtWidgets.QDialog()
        self.dialog_d.setObjectName("Dialog_d")
        self.dialog_d.resize(1920, 1045)
        # 设置无窗口
        self.dialog_d.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_d = QtWidgets.QWidget(self.dialog_d)
        self.centralwidget_d.setGeometry(QtCore.QRect(0,33,1920,1015))
        self.centralwidget_d.setObjectName("centralwidget_d")
        self.centralwidget_d.setStyleSheet("background-image: url(D:/tongcheng/image/gz_bj.png);")

        # 添加标题栏
        self.page_d = QtWidgets.QWidget(self.dialog_d)
        self.page_d.setObjectName("page_d")
        self.page_d.setGeometry(QtCore.QRect(0,0,1920,33))
        self.page_d.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/gz_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_gz = QtWidgets.QPushButton(self.page_d)
        self.pushButton_gz.setObjectName("pushButton_gz")
        self.pushButton_gz.setGeometry(1890,0,31,33)
        self.pushButton_gz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_gz.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_gz.clicked.connect(self.dialog_d.close)

        # 添加最小化按钮
        self.pushButton_zz = QtWidgets.QPushButton(self.page_d)
        self.pushButton_zz.setObjectName("pushButton_zz")
        self.pushButton_zz.setGeometry(1860,0,31,33)
        self.pushButton_zz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/zxh_gz.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/zxhhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/zxhpressed.png');border:none}")
        self.pushButton_zz.clicked.connect(self.dialog_d.showMinimized)

        # 添加北京按钮
        self.pushButton_bj = QtWidgets.QPushButton(self.centralwidget_d)
        self.pushButton_bj.setObjectName("pushButton_bj")
        self.pushButton_bj.setGeometry(QtCore.QRect(120,0,100,40))

        # 添加杭州按钮
        self.pushButton_hz = QtWidgets.QPushButton(self.centralwidget_d)
        self.pushButton_hz.setObjectName("pushButton_hz")
        self.pushButton_hz.setGeometry(QtCore.QRect(230,0,100,40))

        # 添加深圳按钮
        self.pushButton_sz = QtWidgets.QPushButton(self.centralwidget_d)
        self.pushButton_sz.setObjectName("pushButton_sz")
        self.pushButton_sz.setGeometry(QtCore.QRect(340,0,100,40))

        # 添加上海按钮
        self.pushButton_sh = QtWidgets.QPushButton(self.centralwidget_d)
        self.pushButton_sh.setObjectName("pushButton_sz")
        self.pushButton_sh.setGeometry(QtCore.QRect(450,0,100,40))

        self.label_2 = QtWidgets.QLabel(self.centralwidget_d)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setObjectName("label_2")

        # 添加广州按钮
        self.pushButton_Cgz = QtWidgets.QPushButton(self.centralwidget_d)
        self.pushButton_Cgz.setObjectName("pushButton_Cgz")
        self.pushButton_Cgz.setGeometry(QtCore.QRect(560,0,100,40))

        self.retranslateUi_d()
        QtCore.QMetaObject.connectSlotsByName(self.dialog_d)

        # 添加主界面框架
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget_d)
        self.stackedWidget.setGeometry(QtCore.QRect(0,33,1920,970))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_d1 = QtWidgets.QWidget()
        self.page_dd = QtWidgets.QWidget()

        # 创建5个web界面
        self.browser_1 = QWebEngineView(self.page_d1)
        self.browser_2 = QWebEngineView(self.page_d1)
        self.browser_3 = QWebEngineView(self.page_d1)
        self.browser_4 = QWebEngineView(self.page_d1)
        self.browser_5 = QWebEngineView(self.page_d1)
        # 把5个web界面加到stackedwidget中
        self.stackedWidget.addWidget(self.browser_1)
        self.stackedWidget.addWidget(self.browser_2)
        self.stackedWidget.addWidget(self.browser_3)
        self.stackedWidget.addWidget(self.browser_4)
        self.stackedWidget.addWidget(self.browser_5)

        self.page_dd.setStyleSheet("QWidget{background-color:#FFFFFF}")
        self.stackedWidget.addWidget(self.page_dd)

        # 设置点击按钮连接相应的网页
        self.pushButton_bj.clicked.connect(self.BJinterface)
        self.pushButton_hz.clicked.connect(self.HZinterface)
        self.pushButton_sz.clicked.connect(self.SZinterface)
        self.pushButton_sh.clicked.connect(self.SHinterface)
        self.pushButton_Cgz.clicked.connect(self.GZinterface)
        self.stackedWidget.setCurrentIndex(5)
        self.dialog_d.exec_()

    # 北京地图界面
    def BJinterface(self):
        self.stackedWidget.setCurrentIndex(0)
        self.browser_1.load(QUrl('D:/tongcheng/map/北京/index.html'))
    # 杭州地图界面
    def HZinterface(self):
        self.stackedWidget.setCurrentIndex(1)
        self.browser_2.load(QUrl('D:/tongcheng/map/杭州/index.html'))
    # 深圳地图界面
    def SZinterface(self):
        self.stackedWidget.setCurrentIndex(2)
        self.browser_3.load(QUrl('D:/tongcheng/map/深圳/index.html'))
    # 上海地图界面
    def SHinterface(self):
        self.stackedWidget.setCurrentIndex(3)
        self.browser_4.load(QUrl('D:/tongcheng/map/上海/index.html'))
    # 广州地图界面
    def GZinterface(self):
        self.stackedWidget.setCurrentIndex(4)
        self.browser_5.load(QUrl('D:/tongcheng/map/广州/index.html'))

    def retranslateUi_d(self):
        _translate = QtCore.QCoreApplication.translate
        self.dialog_d.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;color:#FFFFFF\">请选择城市：</span></p></body></html>"))

        # 定义城市按钮
        self.pushButton_bj.setText(_translate("MainWindow","北京"))
        self.pushButton_bj.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/bjan_bj.png');border:none}")
        self.pushButton_hz.setText(_translate("MainWindow","杭州"))
        self.pushButton_hz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/hzan_bj.png');border:none}")
        self.pushButton_sz.setText(_translate("MainWindow","深圳"))
        self.pushButton_sz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/szan_bj.png');border:none}")
        self.pushButton_sh.setText(_translate("MainWindow","上海"))
        self.pushButton_sh.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/shan_bj.png');border:none}")
        self.pushButton_Cgz.setText(_translate("MainWindow","广州"))
        self.pushButton_Cgz.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gzan_bj.png');border:none}")

    # 账号或密码错误界面
    def CW_Window(self):
        self.dialog_c = QtWidgets.QDialog()
        self.dialog_c.setObjectName("dialog_c")
        self.dialog_c.resize(330,300)
        self.dialog_c.move(self.zcc_x + 330, self.zcc_y + 150)
        # 设置无窗口
        self.dialog_c.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget_c = QtWidgets.QWidget(self.dialog_c)
        self.centralwidget_c.setGeometry(QtCore.QRect(0,33,330,300))
        self.centralwidget_c.setObjectName("centralwidget")
        self.centralwidget_c.setStyleSheet("background-image:url('D:/tongcheng/image/cw_bj.png');")

        # 添加标题栏
        self.page_c = QtWidgets.QWidget(self.dialog_c)
        self.page_c.setObjectName("page_c")
        self.page_c.setGeometry(QtCore.QRect(0,0,330,33))
        self.page_c.setStyleSheet("QWidget{background-image:url('D:/tongcheng/image/cw_btl.png');border:none}")

        # 添加关闭按钮
        self.pushButton_cgb = QtWidgets.QPushButton(self.page_c)
        self.pushButton_cgb.setObjectName("pushButton_cgb")
        self.pushButton_cgb.setGeometry(299,0,31,33)
        self.pushButton_cgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/gb_cw.png')}  QWidget:hover{background-image:url('D:/tongcheng/image/gbhover.png');border:none} QWidget:pressed{background-image:url('D:/tongcheng/image/gbpressed.png');border:none}")
        self.pushButton_cgb.clicked.connect(self.dialog_c.close)

        # 添加关闭确定按钮
        self.pushButton_qgb = QtWidgets.QPushButton(self.centralwidget_c)
        self.pushButton_qgb.setObjectName("pushButton_qgb")
        self.pushButton_qgb.setGeometry(45,200,250,45)
        self.pushButton_qgb.setStyleSheet("QPushButton{background-image:url('D:/tongcheng/image/cwan.png')}")
        self.pushButton_qgb.clicked.connect(self.dialog_c.close)

        self.dialog_c.exec_()


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(w)
#     w.show()
#     sys.exit(app.exec_())

