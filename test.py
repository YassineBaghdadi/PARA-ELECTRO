# # from PyQt5 import Qt
# # from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
# # from PyQt5.QtCore import QRect, QPropertyAnimation
# # import sys
# #
# #
# # class Example(QWidget):
# #
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.initUI()
# #         self.setWindowFlags(Qt.Popup)
# #
# #     def initUI(self):
# #         self.button = QPushButton("Start", self)
# #         self.button.clicked.connect(self.doAnim)
# #         self.button.move(30, 30)
# #
# #         self.frame = QFrame(self)
# #         self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
# #         self.frame.setGeometry(150, 30, 100, 200)
# #
# #         self.setGeometry(300, 300, 380, 300)
# #         self.setWindowTitle('Animation')
# #         self.show()
# #
# #     def doAnim(self):
# #         self.anim = QPropertyAnimation(self.frame, b"geometry")
# #         self.anim.setDuration(300)
# #         self.anim.setStartValue(QRect(150, 30, 100, 200))
# #         self.anim.setEndValue(QRect(150, 30, 200, 200))
# #         self.anim.start()
# #
# #
# # if __name__ == "__main__":
# #     app = QApplication([])
# #     ex = Example()
# #     ex.show()
# #     app.exec_()
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import sys
#
# #
# BUTTON_HEIGHT = 30
# # button width
# BUTTON_WIDTH = 30
# # title bar height
# TITLE_HEIGHT = 30
#
#
# class TitleWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         # self.setStyleSheet("background-color:blue")
#         titleIcon = QPixmap(".\icon.png")
#         Icon = QLabel()
#         Icon.setPixmap(titleIcon.scaled(25, 25))
#         titleContent = QLabel("title content")
#         titleContent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         titleContent.setFixedHeight(TITLE_HEIGHT)
#         titleContent.setObjectName("TitleContent")
#         self.ButtonMin = QPushButton()
#         self.ButtonMin.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
#         self.ButtonMin.setObjectName("ButtonMin")
#         self.ButtonMax = QPushButton()
#         self.ButtonMax.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
#         self.ButtonMax.setObjectName("ButtonMax")
#         self.ButtonRestore = QPushButton()
#         self.ButtonRestore.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
#         self.ButtonRestore.setObjectName("ButtonRestore")
#         self.ButtonRestore.setVisible(False)
#         self.ButtonClose = QPushButton()
#         self.ButtonClose.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
#         self.ButtonClose.setObjectName("ButtonClose")
#         mylayout = QHBoxLayout()
#         mylayout.setSpacing(0)
#         mylayout.setContentsMargins(0, 0, 0, 0)
#         mylayout.addWidget(Icon)
#
#         mylayout.addWidget(titleContent)
#         mylayout.addWidget(self.ButtonMin)
#         mylayout.addWidget(self.ButtonMax)
#         mylayout.addWidget(self.ButtonRestore)
#         mylayout.addWidget(self.ButtonClose)
#
#         self.setLayout(mylayout)
#         # QSS can be written in the file. Read the file. It is convenient for everyone to use it directly in the code.
#         Qss = '''
#
#             QLabel#TitleContent
#             {
#                 color: #FFFFFF;
#             }
#
#             QPushButton#ButtonMin
#             {
#                 border-image:url(./min.png) 0 81 0 0 ;
#
#             }
#
#             QPushButton#ButtonMin:hover
#             {
#                 border-image:url(./min.png) 0 54 0 27 ;
#             }
#
#             QPushButton#ButtonMin:pressed
#             {
#                 border-image:url(./min.png) 0 27 0 54 ;
#             }
#
#             QPushButton#ButtonMax
#             {
#                 border-image:url(./max.png) 0 81 0 0 ;
#             }
#
#             QPushButton#ButtonMax:hover
#             {
#                 border-image:url(./max.png) 0 54 0 27 ;
#             }
#
#             QPushButton#ButtonMax:pressed
#             {
#                 border-image:url(./max.png) 0 27 0 54 ;
#             }
#
#             QPushButton#ButtonRestore
#             {
#                 border-image:url(./restore.png) 0 81 0 0 ;
#             }
#
#             QPushButton#ButtonRestore:hover
#             {
#                 border-image:url(./restore.png) 0 54 0 27 ;
#             }
#
#             QPushButton#ButtonRestore:pressed
#             {
#                 border-image:url(./restore.png) 0 27 0 54 ;
#             }
#
#             QPushButton#ButtonClose
#             {
#                 border-image:url(./close.png) 0 81 0 0 ;
#                 border-top-right-radius:3 ;
#             }
#
#             QPushButton#ButtonClose:hover
#             {
#                 border-image:url(./close.png) 0 54 0 27 ;
#                 border-top-right-radius:3 ;
#             }
#
#             QPushButton#ButtonClose:pressed
#             {
#                 border-image:url(./close.png) 0 27 0 54 ;
#                 border-top-right-radius:3 ;
#             }
#
#         '''
#         self.setStyleSheet(Qss)
#
#         self.restorePos = None
#         self.restoreSize = None
#         self.startMovePos = None
#
#     def saveRestoreInfo(self, point, size):
#         self.restorePos = point
#         self.restoreSize = size
#
#     def getRestoreInfo(self):
#         return self.restorePos, self.restoreSize
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
#         self.resize(800, 600)
#         AllWidget = QWidget()
#         # AllWidget.setStyleSheet("background-color:red")
#         Alllayout = QVBoxLayout()
#         Alllayout.setSpacing(0)
#         Alllayout.setContentsMargins(0, 0, 0, 0)
#         AllWidget.setLayout(Alllayout)
#         self.title = TitleWidget()
#         self.title.setFixedWidth(self.width())
#         self.title.setFixedHeight(TITLE_HEIGHT)
#         self.title.ButtonMin.clicked.connect(self.ButtonMinSlot)
#         self.title.ButtonMax.clicked.connect(self.ButtonMaxSlot)
#         self.title.ButtonRestore.clicked.connect(self.ButtonRestoreSlot)
#         self.title.ButtonClose.clicked.connect(self.ButtonCloseSlot)
#         centerWidget = QWidget()
#         # centerWidget can add any control you want to use
#         # centerWidget.setStyleSheet("background-color:red")
#         Qss = '''
#             QMainWindow{
#                 background:qlineargradient(spread:pad,x1:1,y1:0,x2:0,y2:1,stop:0 rgba(51,146,255,255),stop:1 rgba(255,255,255,255));
#
#             }
#         '''
#
#         Alllayout.addWidget(self.title)
#         Alllayout.addWidget(centerWidget)
#         self.setCentralWidget(AllWidget)
#         self.setStyleSheet(Qss)
#
#     def ButtonMinSlot(self):
#         self.showMinimized()
#
#     def ButtonMaxSlot(self):
#         self.title.ButtonMax.setVisible(False)
#         self.title.ButtonRestore.setVisible(True)
#         self.title.saveRestoreInfo(self.pos(), QSize(self.width(), self.height()))
#         desktopRect = QApplication.desktop().availableGeometry()
#         FactRect = QRect(desktopRect.x() - 3, desktopRect.y() - 3, desktopRect.width() + 6, desktopRect.height() + 6)
#         print(FactRect)
#         self.setGeometry(FactRect)
#         self.setFixedSize(desktopRect.width() + 6, desktopRect.height() + 6)
#
#     def ButtonRestoreSlot(self):
#         self.title.ButtonMax.setVisible(True)
#         self.title.ButtonRestore.setVisible(False)
#         windowPos, windowSize = self.title.getRestoreInfo()
#         # print(windowPos,windowSize.width(),windowSize.height())
#         self.setGeometry(windowPos.x(), windowPos.y(), windowSize.width(), windowSize.height())
#         self.setFixedSize(windowSize.width(), windowSize.height())
#
#     def ButtonCloseSlot(self):
#         self.close()
#
#     def paintEvent(self, event):
#         self.title.setFixedWidth(self.width())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mw = MainWindow()
#     mw.show()
#     sys.exit(app.exec_())


import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        css = """
        QWidget{
            Background: #AA00AA;
            color:white;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            Background-image:url('img/titlebar bg.png');
            font-size:12px;
            color: black;

        }
        QToolButton{
            Background:#AA00AA;
            font-size:11px;
        }
        QToolButton:hover{
            Background: #FF00FF;
            font-size:11px;
        }
        """
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)
        self.minimize=QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon('img/min.png'))
        self.maximize=QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon('img/max.png'))
        close=QtWidgets.QToolButton(self)
        close.setIcon(QtGui.QIcon('img/close.png'))
        self.minimize.setMinimumHeight(10)
        close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)
        label=QtWidgets.QLabel(self)
        label.setText("Window Title")
        self.setWindowTitle("Window Title")
        hbox=QtWidgets.QHBoxLayout(self)
        hbox.addWidget(label)
        hbox.addWidget(self.minimize)
        hbox.addWidget(self.maximize)
        hbox.addWidget(close)
        hbox.insertStretch(1,500)
        hbox.setSpacing(0)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
        self.maxNormal=False
        close.clicked.connect(self.close)
        self.minimize.clicked.connect(self.showSmall)
        self.maximize.clicked.connect(self.showMaxRestore)

    def showSmall(self):
        box.showMinimized()

    def showMaxRestore(self):
        if(self.maxNormal):
            box.showNormal()
            self.maxNormal= False
            self.maximize.setIcon(QtGui.QIcon('img/max.png'))
            print('1')
        else:
            box.showMaximized()
            self.maxNormal=  True
            print('2')
            self.maximize.setIcon(QtGui.QIcon('img/max2.png'))

    def close(self):
        box.close()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True
            box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)


class Frame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.m_mouse_down= False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
        QFrame{
            Background:  #D700D7;
            color:white;
            font:13px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.m_titleBar= TitleBar(self)
        self.m_content= QtWidgets.QWidget(self)
        vbox=QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.m_content)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(0)
        vbox.addLayout(layout)
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button()== Qt.LeftButton

    def mouseMoveEvent(self,event):
        x=event.x()
        y=event.y()

    def mouseReleaseEvent(self,event):
        m_mouse_down=False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    box = Frame()
    box.move(60,60)
    l=QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    edit=QtWidgets.QLabel("""I would've did anything for you to show you how much I adored you
But it's over now, it's too late to save our loveJust promise me you'll think of me
Every time you look up in the sky and see a star 'cuz I'm  your star.""")
    l.addWidget(edit)
    box.show()
    app.exec_()