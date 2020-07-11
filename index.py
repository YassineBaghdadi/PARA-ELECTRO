import datetime
import os
import sys
from time import sleep
import sqlite3

from PyQt5.QtCore import QPropertyAnimation, QRect, Qt, QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QHeaderView, QMenu, QAction, QCompleter
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
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

DB = 'src/db.db'

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

        conn = sqlite3.connect(DB)
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            code TEXT, 
            categorie TEXT, 
            qt INTEGER, 
            price INTEGER);
        """)
        curs.execute("""
            CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date_time TEXT, 
            product TEXT, 
            qt INTEGER, 
            total_price INTEGER, 
            operation TEXT, 
            person TEXT,
            paid TEXT);
        """)
        conn.commit()
        conn.close()
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
        self.search_btn.setPixmap(QPixmap('src/icons/search.png'))
        self.search_btn.setScaledContents(True)
        self.search_btn.installEventFilter(self)
        self.search_txt.installEventFilter(self)
        self.search_txt.setFixedWidth(0)
        self.history_table.itemSelectionChanged.connect(self.table_select_event)
        self.table_header = ['id', 'Date/Time', 'Product', 'Quantity', 'Total Price', 'Operation', 'Person']
        self.history_table.setColumnCount(len(self.table_header))
        self.history_table.setHorizontalHeaderLabels(self.table_header)
        self.history_table.resizeColumnsToContents()
        # self.history_table.horizontalHeader().setSectionResizeMode(self.table_header.index(self.table_header[-1]), QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.history_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.return_btn.clicked.connect(self.return_goods)

    def refresh(self, key=None):
        # conn = sqlite3.connect(DB)
        # curs = conn.cursor()
        # current_month_selld_operations = int(curs.execute('SELECT COUNT(id) FROM history where operation like "sell"').fetchone())
        # # self.sells_operations_counter.setText(f"""
        # #     {}
        # # """)
        # sql = ''
        # if key:
        #     sql = ''
        # else:
        #     pass
        #
        # self.history_table.clear()
        # self.history_table.setHorizontalHeaderLabels(self.table_header)
        pass


    def return_goods(self):
        # self.refresh()
        pass


    def table_select_event(self):
        items = self.history_table.selectedItems()
        if items:
            print([str(i.text()) for i in items])
            self.return_btn.setEnabled(True)
        else:
            self.return_btn.setEnabled(False)

    def eventFilter(self, source, event):
        if source is self.search_btn:

            if event.type() == QtCore.QEvent.MouseButtonPress:
                # self.search_txt.setText('')
                self.search_txt.setFixedWidth(311)
            elif event.type() == QtCore.QEvent.HoverEnter:
                self.search_btn.setStyleSheet('border:1px solid grey;')
            elif event.type() == QtCore.QEvent.HoverLeave :
                self.search_btn.setStyleSheet('border:0px solid grey;')

        return super(Home, self).eventFilter(source, event)


class Sell(QtWidgets.QFrame):
    def __init__(self):
        super(Sell, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/sell.ui'), self)




class Buy(QtWidgets.QFrame):
    def __init__(self):
        super(Buy, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/buy.ui'), self)
        self.refresh()

        self.product_name.installEventFilter(self)

        self.completer = QCompleter()
        self.model = QStringListModel()
        self.completer.setModel(self.model)
        # # self.product_name.textChanged.connect(self.product_txt_changing)
        # self.product_txt_changing()
        self.seller.setCompleter(self.completer)
        self.product_name.currentTextChanged.connect(self.product_choosen)
        self.qt.textChanged.connect(self.qt_changing)



        self.qt.setValidator(QIntValidator())
        # conn.close()
        self.qt_value = 0

    def qt_changing(self):
        if self.product_name.currentText() == '':
            self.rest.setText('<font color="red">ERR :</font> Select product first')
            return

        try:
            # old = int(self.rest.text().split('*')[0])
            self.rest.setText(f'{int(self.qt.text())+ self.qt_value}"in the stock')
        except:
            self.rest.setText('<font color="red">ERR :</font> Fill the Quantity')

    def product_choosen(self):
        conn = sqlite3.connect(DB)
        curs = conn.cursor()
        code = str(self.product_name.currentText()).split("-")[0].replace(" ", "")
        print(code)
        try:
            dt = curs.execute(f'select categorie, qt, price from products where code like "{code}"').fetchone()
            self.categorie.setText(dt[0])
            self.categorie.setEnabled(False)
            self.qt_value = int(dt[1])
            self.rest.setText(f'{self.qt_value}"in the stock')

            self.price.setText(str(dt[2]))

        except:
            self.categorie.setText('')
            self.categorie.setEnabled(True)
            self.rest.setText('0 in the stock')
            self.price.setText('')


    def refresh(self):

        conn = sqlite3.connect(DB)
        self.curs = conn.cursor()
        # ll = list([f' - '.join(i) for i in self.curs.execute(f'select code, name from products where name like "%{self.product_name.text()}%" or code like "%{self.product_name.text()}%"').fetchall()])
        ll = list([f' - '.join(i) for i in self.curs.execute(f'select code, name from products order by name asc').fetchall()])
        ll.insert(0, '')
        # ll = ['yassine', 'baghdadi', 'guercif']
        try:
            self.model.setStringList(self.curs.execute('select person from history where operation like "sell" order by asc').fetchall())
        except:pass
        self.product_name.clear()
        self.product_name.addItems(ll)
        conn.close()
    def eventFilter(self, source, event) :
        # if source is self.product_name or source is self.categorie:
        #     if event.type() == QtCore.QEvent.FocusIn:
        #         print(f'connecting to {DB}')
        #         self.conn = sqlite3.connect(DB)
        #         self.curs = self.conn.cursor()
        #     elif event.type() == QtCore.QEvent.FocusOut:
        #         print(f'deconnecting to {DB}')
        #         self.conn.close()

        return super(Buy, self).eventFilter(source, event)






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