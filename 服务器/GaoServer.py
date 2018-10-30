from MysqlPython import *
from socket import *
import os
import time
import sys
import signal
from hashlib import sha1

# 处理登录请求
def DL_function(c,mysql):
    c.send(b"OK")
    data = c.recv(1024).decode()
    data = data.split(' ')
    mysql = MysqlHelp('db4')
    sql_select = 'select password from user1 where username="%s";' % data[0]
    result = mysql.getAll(sql_select)
    if len(result) == 0:
        c.send(b'SB')
    elif result[0][0] != data[1]:
        c.send(b'SB')
    else:
        c.send(b'TG')

# 处理注册请求
def ZC_function(c,mysql):
    c.send(b"OK")
    data = c.recv(1024).decode()
    data = data.split(' ')
    # 判断用户名是否存在
    sql_select1 = 'select password from user1 where username="%s";' % data[0]
    result1 = mysql.getAll(sql_select1)
    print(result1)
    # 判断手机号是否已被注册
    sql_select2 = 'select password from user1 where phone="%s";' % data[2]
    result2 = mysql.getAll(sql_select2)
    if len(result1) == 0:
        if len(result2) == 1:
            c.send(b'SJBZC')
        else:
            sql_insert = 'insert into user1(username,password,phone) values("%s","%s","%s")' % (data[0],data[1],data[2])
            mysql.workOn(sql_insert)
            c.send(b'CGZC')
    else:
        c.send(b'YHYCZ')

# 处理客户端点击忘记密码发送验证码是否有该手机号
def WJY_function(c,mysql):
    c.send(b'OK')
    data = c.recv(1024).decode()
    data = data.split(' ')
    sql_select = 'select phone from user1 where username="%s"' % data[0]
    result = mysql.getAll(sql_select)
    if len(result) == 0:
        c.send(b'YHBCZ')
    elif result[0][0] != data[1]:
        c.send(b'SJCW')
    else:
        c.send(b'CG')

# 处理客户端忘记密码中的　设置新的密码
def WJX_function(c,mysql):

    c.send(b'OK')
    data = c.recv(1024).decode()
    data = data.split(' ')
    sql_select = 'select phone from user1 where username="%s"' % data[0]
    result = mysql.getAll(sql_select)
    sql_update = 'update user1 set password = "%s" where username="%s"'%(data[1],data[0])
    if len(result) == 0:
        c.send(b'YHBCZ')
    elif result[0][0] != data[2]:
        c.send(b'SJCW')
    else:
        mysql.workOn(sql_update)
        c.send(b'MMCG')


def main():
    # 连接数据库
    mysql = MysqlHelp("db4")

    # 创建TCP 套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(("0.0.0.0",8888))
    s.listen(3)

    # 忽略子进程退出信号
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        print("已连接",addr)

        pid = os.fork()

        if pid == 0:
            s.close()
            print("子进程准备处理请求")
            while True:
                try:
                    data = c.recv(1024)
                except:
                    break
                if data.decode() == 'D':
                    DL_function(c,mysql)
                elif data.decode() == 'Z':
                    ZC_function(c,mysql)
                # 忘记密码发送验证码
                elif data.decode() == 'WF':
                    WJY_function(c,mysql)
                elif data.decode() == 'XG':
                    WJX_function(c,mysql)
            # 关闭数据库
            # mysql.close()
            sys.exit()

        else:
            # 关闭客户端套接字
            c.close()
            continue
if __name__ == '__main__':
    main()