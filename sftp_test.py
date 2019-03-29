# coding: utf-8
from ftplib import FTP
import time
import tarfile
import os
# !/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os


def ftpconnect(host, port, username, password):
    print('开始连接')
    sf = paramiko.Transport((host, port))
    print('开始登录')
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    return sftp

#从ftp下载文件
def downloadfile(sftp, remotepath, localpath):
    try:
        if os.path.isdir(localpath):  # 判断本地参数是目录还是文件
            for f in sftp.listdir(remotepath):  # 遍历远程目录
                sftp.get(os.path.join(remotepath + f), os.path.join(localpath + f))  # 下载目录中文件
        else:
            sftp.get(remotepath, localpath)  # 下载文件
    except Exception as e:
        print('download exception:', e)
    sftp.close()

#从本地上传文件到ftp
def uploadfile(sftp, remotepath, localpath):
    try:
        if os.path.isdir(localpath):  # 判断本地参数是目录还是文件
            for f in sftp.listdir(remotepath):  # 遍历远程目录
                sftp.get(os.path.join(remotepath + f), os.path.join(localpath + f))  # 下载目录中文件
        else:
            sftp.get(remotepath, localpath)  # 下载文件
    except Exception as e:
        print('download exception:', e)
    sftp.close()

if __name__ == "__main__":
    # ftp地址
    ftp = ftpconnect("192.168.102.184", 1111, "fmtest", "hsfundYrs04f")
    print("登录成功")
    downloadfile(ftp, "/资料/UFT代码同步工具/", "E:/Git/python/tool_box/downloads/")
    # #调用本地播放器播放下载的视频
    # os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
    # uploadfile(ftp, "C:/Users/Administrator/Desktop/test.mp4", "test.mp4")
