from socket import *
import time
from hashlib import sha1

s = socket()
HOST = ("172.88.4.145")
PORT = 8888
ADDR = (HOST,PORT)
try:
    s.connect(ADDR)
except Exception as e:
    print('连接服务器失败',e)

# 把登录信息发送给服务器
def DL_funtcion(name,password):
    s.send("D".encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        s.send(('%s %s'%(name,password)).encode())
        data = s.recv(1024).decode()
        if data == "SB":
            return "SB"
        elif data == 'TG':
           return "TG"

# 把注册信息发送给服务器
def ZC_function(username,password,phone):
    s.send("Z".encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        s.send(('%s %s %s'%(username,password,phone)).encode())
        data = s.recv(1024).decode()
        if data == 'SJBZC':
            return 'SJBZC'
        elif data == 'CGZC':
            return 'CGZC'
        elif data == 'YHYCZ':
            return 'YHYCZ'

# 把忘记密码中的手机号发送给服务器，查找是否存在该手机号
def WJY_function(username,phone):
    s.send("WF".encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        s.send(('%s %s'%(username,phone)).encode())
        data = s.recv(1024).decode()
        if data == 'YHBCZ':
            return 'YHBCZ'
        elif data == 'SJCW':
            return 'SJCW'
        elif data == 'CG':
            return 'CG'

# 忘记密码中把修改密码发送给服务器
def WJX_function(username,password,phone):
    s.send("XG".encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        s.send(('%s %s %s'%(username,password,phone)).encode())
        data = s.recv(1024).decode()
        if data == 'YHBCZ':
            return 'YHBCZ'
        elif data == 'SJCW':
            return 'SJCW'
        elif data == 'MMCG':
            return 'MMCG'