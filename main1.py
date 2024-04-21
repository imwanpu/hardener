from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox, QStatusBar,QLabel,QMainWindow,QListWidget,QLineEdit,QDialog
from PySide6.QtCore import Slot
from csv import reader
from typing import List
from subprocess import Popen
from os.path import abspath, dirname, join
from time import sleep
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import os

from metaInfo import projectName, author, version, indexPath, packageDir, shellScriptDir






class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.tp = ThreadPoolExecutor()
        self.setWindowTitle(projectName + " v" + version + " By " + author)
        self.resize(800, 600)

        # 按钮区
        self.button1 = QPushButton("button1")
        self.button1.clicked.connect(lambda: self.sayButtonName(self.button1))
        self.buttonRestoreVmwareWorkstationVM = QPushButton("重置Workstation虚拟机")
        self.buttonRestoreVmwareWorkstationVM.clicked.connect(lambda b=self.buttonRestoreVmwareWorkstationVM : self.tp.submit(self.restoreVmwareWorkstationVM, b))
        self.buttonPullScripstAndPackages = QPushButton("发送")
        self.buttonPullScripstAndPackages.clicked.connect(lambda hs=self.hosts, lp=[shellScriptDir,packageDir],rp="/tmp": self.tp.submit(self.pushScirptsAndPackages,hs,lp,rp))
        self.buttonInputHosts = QPushButton("输入目标主机")
        self.buttonInputHosts.clicked.connect(self.setHosts)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.button1)
        self.buttonLayout.addWidget(self.buttonRestoreVmwareWorkstationVM)
        self.buttonLayout.addWidget(self.buttonPullScripstAndPackages)
        self.buttonLayout.addWidget(self.buttonInputHosts)

        # 表格区
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.itemSelectionChanged.connect(
            lambda: self.saySeletedRow(self.table))
        self.table.setHorizontalHeaderLabels(["第一列", "第二列", "第三列"])
        csvMatrix = csv2matrix(indexPath)
        self.table.setRowCount(len(csvMatrix))
        self.table.setColumnCount(len(csvMatrix[0])+1)
        for rowIndex, row in enumerate(csvMatrix):
            checkbox = QCheckBox(str(rowIndex))
            self.table.setCellWidget(rowIndex, 0, checkbox)
            checkbox.clicked.connect(
                lambda rowIndex=rowIndex, checkbox=checkbox: self.checkboxStateChaged(checkbox, rowIndex))
            for columnIndex, element in enumerate(row):
                self.table.setItem(rowIndex, columnIndex+1,
                                   QTableWidgetItem(element))

        # 信息栏
        self.logWidget = QListWidget()
        self.logWidget.setFixedHeight(100)

        # 子窗口
        self.inputHostsWidget = InputHostsWidget(self)

        # 布局
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.table)
        self.mainLayout.addWidget(self.logWidget)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    @Slot()
    def sayButtonName(self, button: QPushButton):
        print(button.text())

    @Slot()
    def saySeletedRow(self, table: QTableWidget):
        selectedRows = []
        for item in table.selectedItems():
            selectedRows.append(item.row())
            print(item)
        print("选中的行", selectedRows)
    @Slot()
    def checkboxStateChaged(self, checkbox: QCheckBox, rowIndex: int):
        if checkbox.isChecked():
            self.scriptsNeedRun.append(rowIndex)
        else:
            self.scriptsNeedRun = [x for x in self.scriptsNeedRun if x != rowIndex]
        print(sorted(self.scriptsNeedRun))

    def restoreVmwareWorkstationVM(self,button: QPushButton):
        self.log("重置中")
        Popen(["powershell.exe",join(dirname(abspath(__file__)),"restoreVmStatus.ps1")]).wait()
        self.log("重置已完成")

        
    def afterRestoreVmwareWorkstationVM(self):
        self.statusBar.showMessage("重置完成")
    def log(self, message: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logWidget.addItem(f"{now}: {message}")
        self.logWidget.scrollToBottom()
    def pushScirptsAndPackages(self,hosts: List[Host],localPaths: List[str],remotePath:str):
        self.log("开始发送脚本和包到目标主机")
        sleep(2)
        print(localPaths,remotePath)
        for host in hosts:
            print(host.ip,host.account,host.password,host.system)
        self.log("发送完成")

    def setHosts(self):
        self.inputHostsWidget.show()

class InputHostsWidget(QWidget):
    def __init__(self,MainWindwo:MainWindow):
        super().__init__()
        self.lb = QLabel("这个是子窗口")
        self.lineEdit = QLineEdit()
        self.lineEdit.setText("这是子窗口的文本框")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEdit)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
