import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStatusBar

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置主窗口标题
        self.setWindowTitle("QStatusBar 示例")

        # 添加一个标签到主窗口
        label = QLabel("这是一个主窗口")
        self.setCentralWidget(label)

        # 创建状态栏
        self.statusBar = self.statusBar()

        # 在状态栏中显示一条消息
        self.statusBar.showMessage('准备就绪')

        # 将状态栏添加到主窗口
        self.setStatusBar(self.statusBar)

        # 创建按钮
        self.button = QPushButton("运行任务", self)
        self.button.setGeometry(100, 100, 100, 30)
        self.button.clicked.connect(self.runTask)

    def runTask(self):
        # 在按钮点击时设置状态栏消息为 "运行中"
        self.statusBar.showMessage('运行中')

        # 创建一个定时器，在3秒后更新状态栏消息为 "已完成"
        self.timer = QTimer()
        self.timer.timeout.connect(self.taskCompleted)
        self.timer.start(3000)

    def taskCompleted(self):
        # 更新状态栏消息为 "已完成"
        self.statusBar.showMessage('已完成')
        self.timer.stop()

if __name__ == "__main__":
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建主窗口实例
    mainWindow = MyMainWindow()
    mainWindow.show()

    # 运行应用程序
    sys.exit(app.exec())
