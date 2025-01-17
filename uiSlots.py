
import time
from subprocess import Popen
from os.path import join, dirname, abspath
import os
import paramiko
import model
import metaInfo
from PySide6.QtWidgets import QTextEdit, QCheckBox
from typing import List


def sayHello(word: str):
    print("hello.")
    time.sleep(2)
    print(word)


def restoreVmwareWorkstationVM():
    Popen(["powershell.exe", join(
        dirname(abspath(__file__)), "restoreVmStatus.ps1")]).wait()


def copy2target(logboxWidget):
    print("start copying")
    for row in model.hostsMatrix:
        print(f"start copying to {row[0]}")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(row[0], username=row[1], password=row[2])
        for root, _, files in os.walk(metaInfo.sourceDir):
            for file in files:
                local_path = os.path.join(root, file)
                remote_path = os.path.join(metaInfo.targetDir, os.path.relpath(
                    local_path, metaInfo.sourceDir)).replace("\\", "/")
                if "\\vms\\" in local_path:
                    break
                ssh.exec_command(f"mkdir -p {os.path.dirname(remote_path)}")
                ftp_client = ssh.open_sftp()
                ftp_client.put(local_path, remote_path)
                ftp_client.close()
                addLog(logboxWidget,
                       f"将 {local_path} 复制到 {row[0]}:{remote_path}")
        ssh.close()


def testConnectivity(logboxWidget):
    for row in model.hostsMatrix:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(
                hostname=row[0], username=row[1], password=row[2])
            addLog(logboxWidget, f"Successfully connected to {row[0]} via SSH")
            ssh_client.close()
        except Exception as e:
            addLog(logboxWidget,
                   f"Failed to connect to {row[0]} via SSH: {str(e)}")


def addLog(logboxWidget: QTextEdit, logString: str):
    logStringWithTime = "" + time.ctime() + ": " + logString
    logboxWidget.append(logStringWithTime)


def modifyModel4SelectedRows(checkboxList: List[QCheckBox]):
    for idx, checkbox in enumerate(checkboxList):
        if checkbox.isChecked():
            model.indexMatrix[idx][5] = "执行"
        else:
            model.indexMatrix[idx][5] = "不执行"
    print(model.indexMatrix)


def genMainShell(logboxWidget: QTextEdit):
    with open(os.path.join(metaInfo.shellScriptDir, "main.sh"), "wb") as f:
        isReboot = False
        f.write(bytes("#!/usr/bin/bash\n", encoding='utf-8'))
        for row in model.indexMatrix:
            if row[5] == "执行":
                f.write(
                    bytes(f"{metaInfo.targetDir}/shellScript/{row[2]}\n", encoding='utf-8'))
                if row[4] == "需要重启":
                    isReboot = True
                print(row[4])
        if isReboot:
            f.write(bytes("reboot\n", encoding='utf-8'))
        f.write(bytes("\n", encoding='utf-8'))
    addLog(logboxWidget, "加固脚本生成完毕")


def runMainShell(logboxWidget: QTextEdit):
    for row in model.hostsMatrix:
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(
                hostname=row[0], username=row[1], password=row[2])
            _ = ssh_client.exec_command("chmod a+rx -R /tmp/hardener/")
            stdout, _, _ = ssh_client.exec_command(
                "/tmp/hardener/shellScript/main.sh")
            while not stdout.channel.exit_status_ready():
                pass
            ssh_client.close()
            addLog(logboxWidget, f"{row[0]}: 执行main.sh成功")
        except Exception as e:
            addLog(logboxWidget, f"{row[0]} {str(e)}: 执行main.sh失败")
