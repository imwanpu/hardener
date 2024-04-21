
import time
from subprocess import Popen
from os.path import join, dirname, abspath
import os
import paramiko
import model
import metaInfo
from PySide6.QtWidgets import QTextEdit

def sayHello(word: str):
    print("hello.")
    time.sleep(2)
    print(word)


def restoreVmwareWorkstationVM():
    Popen(["powershell.exe",join(dirname(abspath(__file__)),"restoreVmStatus.ps1")]).wait()

def copy2target():
    print("start copying")
    for row in model.hostsMatrix:
        print(f"start copying to {row[0]}")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(row[0], username=row[1], password=row[2])
        for root, _, files in os.walk(metaInfo.sourceDir):
            for file in files:
                local_path = os.path.join(root, file)
                remote_path = os.path.join(metaInfo.targetDir, os.path.relpath(local_path, metaInfo.sourceDir)).replace("\\","/")
                if "\\vms\\" in local_path:
                    break
                ssh.exec_command(f"mkdir -p {os.path.dirname(remote_path)}")
                ftp_client = ssh.open_sftp()
                ftp_client.put(local_path, remote_path)
                ftp_client.close()
                print(f"将 {local_path} 复制到 {row[0]}:{remote_path}")
        ssh.close()

def testConnectivity():
    for row in model.hostsMatrix:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=row[0], username=row[1], password=row[2])
            print(f"Successfully connected to {row[0]} via SSH")
            ssh_client.close()
        except Exception as e:
            print(f"Failed to connect to {row[0]} via SSH: {str(e)}")

def addLog(logboxWidget :QTextEdit, logString: str):
    logStringWithTime = "" + time.ctime() + ": " +logString
    logboxWidget.append(logStringWithTime)