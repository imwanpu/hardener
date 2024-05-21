from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox, QStatusBar,QLabel,QMainWindow,QListWidget,QLineEdit,QDialog,QTextEdit
from PySide6.QtCore import Slot
from concurrent.futures import ThreadPoolExecutor

from metaInfo import projectName, version, author, githubURL, shellScriptDir
from uiSlots import sayHello, restoreVmwareWorkstationVM, testConnectivity, copy2target, addLog, modifyModel4SelectedRows, genMainShell, runMainShell
import model
import os
from typing import List


# 用于开启子线程来执行 Action
threadPool = ThreadPoolExecutor()

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.layoutUIElements()
        self.bindSlots()

    def initUI(self):
        self.resize(1500, 600)
        self.setWindowTitle(projectName + " v" + version + " By " + author + " " + githubURL)
        self.buttonHello = QPushButton("sayHello")
        self.buttonRestoreVmwareWorkstationVM = QPushButton("重置Workstation虚拟机")
        self.buttonTestConnectivity = QPushButton("测试连通性")
        self.buttonCopy2Target = QPushButton("复制文件到目标主机")
        self.buttonAddLog = QPushButton("日志测试")
        self.buttonModifyModel4SelectedRows = QPushButton("更新模型")
        self.buttonGenMainShell = QPushButton("生成加固脚本")
        self.buttonRunMainShell = QPushButton("运行加固脚本")


        self.tableWidget = QTableWidget()
        self.checkboxList: List[QCheckBox] = []


        self.logbox = QTextEdit()



    def layoutUIElements(self):

        # 按钮区
        self.buttonLayout = QHBoxLayout()
        # self.buttonLayout.addWidget(self.buttonHello)
        self.buttonLayout.addWidget(self.buttonRestoreVmwareWorkstationVM)
        self.buttonLayout.addWidget(self.buttonTestConnectivity)
        self.buttonLayout.addWidget(self.buttonCopy2Target)
        self.buttonLayout.addWidget(self.buttonAddLog)
        self.buttonLayout.addWidget(self.buttonModifyModel4SelectedRows)
        self.buttonLayout.addWidget(self.buttonGenMainShell)
        self.buttonLayout.addWidget(self.buttonRunMainShell)
        
        # 表格区
        self.buildTable()
        

        # 日志区
        self.logbox.setReadOnly(True)
        self.logbox.setFixedHeight(100)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.tableWidget)
        self.mainLayout.addWidget(self.logbox)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)
    def buildTable(self):
        self.tableWidget.setRowCount(len(model.indexMatrix))
        self.tableWidget.setColumnCount(len(model.indexMatrix[0])+1-1)
        self.tableWidget.setHorizontalHeaderLabels(["选中","编号","适用系统","加固脚本","说明","是否重启"])
        for rowIndex, row in enumerate(model.indexMatrix):
            self.checkboxList.append(QCheckBox())
            self.checkboxList[-1].setChecked(False)
            self.tableWidget.setCellWidget(rowIndex,0,self.checkboxList[-1])
            for colIndex, item in enumerate(row):
                if colIndex == 5:
                    break
                self.tableWidget.setItem(rowIndex, colIndex + 1, QTableWidgetItem(item))
                if colIndex == 2 :
                    tableItem = QTableWidgetItem("".join(open(str(os.path.join(shellScriptDir,item))).readlines()))
                    self.tableWidget.setItem(rowIndex,colIndex + 1, tableItem)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def bindSlots(self):
        self.buttonHello.clicked.connect(lambda: threadPool.submit(sayHello,"wori"))
        self.buttonRestoreVmwareWorkstationVM.clicked.connect(lambda: threadPool.submit(restoreVmwareWorkstationVM))
        self.buttonTestConnectivity.clicked.connect(lambda: threadPool.submit(testConnectivity, self.logbox))
        self.buttonCopy2Target.clicked.connect(lambda: threadPool.submit(copy2target,self.logbox))
        self.buttonAddLog.clicked.connect(lambda: threadPool.submit(addLog, self.logbox, "测试日志功能"))
        self.buttonModifyModel4SelectedRows.clicked.connect(lambda: threadPool.submit(modifyModel4SelectedRows, self.checkboxList))
        self.buttonGenMainShell.clicked.connect(lambda: threadPool.submit(genMainShell, self.logbox))
        self.buttonRunMainShell.clicked.connect(lambda: threadPool.submit(runMainShell, self.logbox))