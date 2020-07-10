import datetime
import os
import sys
from time import sleep

from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtWidgets, QtCore, QtGui

# main_ui, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "src/ui/main.ui"))
#
# class Main(QWidget, main_ui):
#     def __init__(self):
#         super(Main, self).__init__()
#         QWidget.__init__(self)
#
#         # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
#         self.setupUi(self)
#         self.menu_icon.setPixmap(QPixmap('src/icons/menu.png'))
#         self.menu_icon.setScaledContents(True)

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/main.ui'), self)
        self.refresh()
        # self.menu_frame.setStyleSheet(':hover{background:#e5f1fb}')
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.sideBar.setFixedWidth(68)
        # self.resize_event()

        # self.anim = QPropertyAnimation(self.sideBar, b"geometry")
        # self.anim.setDuration(200)
        # self.anim.setStartValue(QRect(1, 1, 1, self.height()))
        # self.anim.setEndValue(QRect(1, 1, 68, self.height()))
        # self.anim.start()


        self.setWindowIcon(QtGui.QIcon('src/icons/logo.png'))
        self.setGeometry(QRect(200, 200, 855, 600))

        style = '''
            
            #sideBar{
	            border-right:1px solid black;
	            background-color:#EDEDED;
            }
            
            
            #menu_icon:hover {
                /*border:2px groove #e0e1dd;*/
                border:1px solid grey;
                background-color:#F5F5F5;
            }
            
            #home_frame:hover {
                border:1px solid grey;
            }
            
            #sell_frame:hover {
                
                border:1px solid grey;
            }
            
           #buy_frame:hover {
                border:1px solid grey;
            }
            
            
            #return_frame:hover {
                
                border:1px solid grey;
            }
            
            #debt_frame:hover {
                border:1px solid grey;
            }
            
            #statistics_frame:hover {
                border:1px solid grey;
            }
            
            #settings_frame:hover {
                border:1px solid grey;
            }
            
            
            #sell_frame{border-top:1px solid grey; border-bottom:1px solid grey;}
            #return_frame{border-top:1px solid grey; border-bottom:1px solid grey;}
            #statistics_frame{border-top:1px solid grey; }
            
            



        '''

        style1 = '''
            
            #sideBar{
	            border-right:1px solid black;
	            background-color:#00BFA5;
            }
            
            
            #sell_frame{border-top:1px solid #fff; border-bottom:1px solid #fff;}
            #return_frame{border-top:1px solid #fff; border-bottom:1px solid #fff;}
            #statistics_frame{border-top:1px solid #fff; }
            #logout_frame{border-bottom:1px solid #fff; }
            
            #menu_icon:hover {
                /*border:2px groove #e0e1dd;*/
                border:1px solid grey;
                background-color:#16e2c6;
            }
            
            #home_frame:hover {
                border:1px solid grey;
            }
            
            #sell_frame:hover {
                
                border:1px solid grey;
            }
            
           #buy_frame:hover {
                border:1px solid grey;
            }
            
            
            #return_frame:hover {
                
                border:1px solid grey;
            }
            
            #debt_frame:hover {
                border:1px solid grey;
            }
            
            #statistics_frame:hover {
                border:1px solid grey;
            }
            #logout_frame:hover {
                border:1px solid grey;
            }
            
            #settings_frame:hover {
                border:1px solid grey;
            }
            
        '''
        # self.side_bg = '#EDEDED'
        self.side_bg = '#00BFA5'
        # self.hover_color = '#F5F5F5'
        self.hover_color = '#16e2c6'
        self.setStyleSheet(style1)

        self.logo.setPixmap(QPixmap('src/icons/logo.png'))
        self.logo.setScaledContents(True)

        self.menu_icon.setPixmap(QPixmap('src/icons/menu.png'))
        self.menu_icon.setScaledContents(True)


        self.buy_icon.setPixmap(QPixmap('src/icons/buy.png'))
        self.buy_icon.setScaledContents(True)

        self.home_icon.setPixmap(QPixmap('src/icons/home.png'))
        self.home_icon.setScaledContents(True)


        self.return_icon.setPixmap(QPixmap('src/icons/return.png'))
        self.return_icon.setScaledContents(True)

        self.debt_icon.setPixmap(QPixmap('src/icons/debt.png'))
        self.debt_icon.setScaledContents(True)

        self.sell_icon.setPixmap(QPixmap('src/icons/sell.png'))
        self.sell_icon.setScaledContents(True)

        self.statistics_icon.setPixmap(QPixmap('src/icons/statics.png'))
        self.statistics_icon.setScaledContents(True)

        self.logout_icon.setPixmap(QPixmap('src/icons/logout.png'))
        self.logout_icon.setScaledContents(True)

        self.settings_icon.setPixmap(QPixmap('src/icons/settings.png'))
        self.settings_icon.setScaledContents(True)

        # self.frame.setStyleSheet('box-shadow: -1px 0px 10px 0px;')
        # self.menu_icon.mousePressEvent = lambda : self.sideBar.setFixedWidth(212)
        self.menu_icon.mousePressEvent = self.open_menu
        self.m = 0
        self.home = Home()
        self.content.addWidget(self.home)
        self.setContentsMargins(0, 0, 0, 0)

        self.sideBar.installEventFilter(self)
        self.home_frame.installEventFilter(self)
        self.sell_frame.installEventFilter(self)
        self.buy_frame.installEventFilter(self)
        self.return_frame.installEventFilter(self)
        self.debt_frame.installEventFilter(self)
        self.statistics_frame.installEventFilter(self)
        self.logout_frame.installEventFilter(self)
        self.settings_frame.installEventFilter(self)

    def refresh(self):
        self.title_label.setText(f"PARA-ELECTRO : {' - '.join(str(datetime.datetime.today().date()).split('-')[::-1])}")

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FocusOut and source is self.sideBar):
            print('eventFilter: Side bar focused out')
            if self.m:
                self.open_menu(True)

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.sell_frame):
            self.sell_frame.setStyleSheet(f'background-color: {self.hover_color}')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.sell_frame):
            self.sell_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.home_frame):
            self.home_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.home_frame):
            self.home_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.buy_frame):
            self.buy_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.buy_frame):
            self.buy_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.return_frame):
            self.return_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.return_frame):
            self.return_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.debt_frame):
            self.debt_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.debt_frame):
            self.debt_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.statistics_frame):
            self.statistics_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.statistics_frame):
            self.statistics_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.logout_frame):
            self.logout_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.logout_frame):
            self.logout_frame.setStyleSheet(f'background-color: {self.side_bg};')

        elif (event.type() == QtCore.QEvent.HoverEnter and source is self.settings_frame):
            self.settings_frame.setStyleSheet(f'background-color: {self.hover_color};')

        elif (event.type() == QtCore.QEvent.HoverLeave and source is self.settings_frame):
            self.settings_frame.setStyleSheet(f'background-color: {self.side_bg};')






        elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.home_frame):
            self.change_widget(Home())

        elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.sell_frame):
            self.change_widget(Sell())


        elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.buy_frame):
            self.change_widget(Buy())

        elif (event.type() == QtCore.QEvent.MouseButtonPress and source is self.debt_frame):
            self.dept = Debt()
            self.dept.show()



        return super(Main, self).eventFilter(source, event)

    #     self.sideBar.installEventFilter(self)
    #
    # def eventFilter(self, obj, event):
    #     if obj == self.sideBar and event.type() == QtCore.QEvent.HoverEnter:
    #         self.onHovered()
    #     return super(Main, self).eventFilter(obj, event)
    #
    # def onHovered(self):
    #     print("hovered")
    #     self.sideBar.setStyleSheet('background-color: #fff; color: #000;')

    def change_widget(self, widget):
        for i in reversed(range(self.content.count())):
            self.content.itemAt(i).widget().setParent(None)
        self.content.addWidget(widget)


    def resizeEvent(self, event):
        self.m = 0
        print(f'{self.width()} x {self.height()}')
        self.sideBar.setGeometry(QRect(0, 0, 68, self.height() ))
        self.title_frame.setGeometry(QRect(self.sideBar.width()-1, 0, self.width()-self.sideBar.width(), 70 ))
        self.frame.setGeometry(QRect(self.sideBar.width()-1, self.title_frame.height(), self.width()-self.sideBar.width()-2, self.height()-self.title_frame.height()))

    def open_menu(self, event):
        duration, w0, w1 = 200, 68, 212
        if self.m:
            self.anim = QPropertyAnimation(self.sideBar, b"geometry")
            self.anim.setDuration(duration)
            self.anim.setStartValue(QRect(0, 0, w1, self.height()))
            self.anim.setEndValue(QRect(0, 0, w0, self.height()))
            self.anim.start()
            self.m = 0
        else:
            self.anim = QPropertyAnimation(self.sideBar, b"geometry")
            self.anim.setDuration(duration)
            self.anim.setStartValue(QRect(0, 0, w0, self.height()))
            self.anim.setEndValue(QRect(0, 0, w1, self.height()))
            self.anim.start()
            self.m = 1

    # def debt(self):
    #     text, ok = QInputDialog.getText(self, 'Money Operations', 'Enter the Amount :')
    #     if ok:
    #         print(text)


class Home(QtWidgets.QFrame):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/home.ui'), self)




class Sell(QtWidgets.QFrame):
    def __init__(self):
        super(Sell, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/sell.ui'), self)




class Buy(QtWidgets.QFrame):
    def __init__(self):
        super(Buy, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/buy.ui'), self)



class Debt(QtWidgets.QDialog):
    def __init__(self):
        super(Debt, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/debt.ui'), self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('src/icons/logo.png'))
    main = Main()
    main.show()
    sys.exit(app.exec_())