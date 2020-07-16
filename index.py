import datetime
import os
import sys
from time import sleep
import sqlite3

from PyQt5.QtCore import QPropertyAnimation, QRect, Qt, QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QHeaderView, QMenu, QAction, QCompleter, \
    QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from time import gmtime, strftime

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
            price TEXT);
        """)
        curs.execute("""
            CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date_time TEXT, 
            product TEXT, 
            qt INTEGER, 
            total_price TEXT, 
            operation TEXT, 
            person TEXT,
            paid TEXT);
        """)
        curs.execute("""
            CREATE TABLE IF NOT EXISTS debt (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            person TEXT,
            total_price INTEGER, 
            state TEXT);
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
        self.qt.setValidator(QIntValidator())
        self.price.setValidator(QIntValidator())




class Buy(QtWidgets.QFrame):
    def __init__(self):
        super(Buy, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'src/ui/buy.ui'), self)


        self.product_name.installEventFilter(self)

        self.completer = QCompleter()
        self.model = QStringListModel()
        self.refresh()
        self.completer.setModel(self.model)
        # # self.product_name.textChanged.connect(self.product_txt_changing)
        # self.product_txt_changing()
        self.seller.setCompleter(self.completer)
        self.product_name.currentTextChanged.connect(self.product_choosen)
        self.qt_.textChanged.connect(self.qt_changing)

        self.qt_.setValidator(QIntValidator())
        self.price.setValidator(QIntValidator())
        # conn.close()
        self.qt_value = 0
        self.add.clicked.connect(self.add_row)

        self.to_buy_table.itemSelectionChanged.connect(self.table_select_event)
        self.table_header = [ 'Product', 'Code', 'Categorie', 'Quantity', 'Seller', 'Price', 'Paid', 'Total']
        self.to_buy_table.setColumnCount(len(self.table_header))
        self.to_buy_table.setHorizontalHeaderLabels(self.table_header)
        self.to_buy_table.resizeColumnsToContents()
        # self.to_buy_table.horizontalHeader().setSectionResizeMode(self.table_header.index(self.table_header[-1]), QHeaderView.Stretch)
        for i in range(len(self.table_header)):
            self.to_buy_table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.clear.setEnabled(False)
        self.clear.clicked.connect(self.del_row)
        self.buy.clicked.connect(self.save_buy)

    def save_buy(self):
        if self.to_buy_table.rowCount() < 1:
            self.err.setText('<font color="red">Add Some Products to Buy</font>')
        to_update = []
        to_add = []
        conn = sqlite3.connect(DB)
        curs = conn.cursor()
        exists_codes = [str(i[0]) for i in curs.execute('select code from products').fetchall()]

        for r in range(self.to_buy_table.rowCount()):
            if str(self.to_buy_table.item(r, 1).text()) in exists_codes:
                tmp = []
                for c in range(self.to_buy_table.columnCount()):
                    tmp.append(str(self.to_buy_table.item(r, c).text()))
                to_update.append(tmp)
            else:
                tmp = []
                for c in range(self.to_buy_table.columnCount()):
                    itm = str(self.to_buy_table.item(r, c).text())
                    tmp.append(itm)
                to_add.append(tmp)



        def add_history(i):
            curs.execute(f'''INSERT INTO history (date_time, product, qt, total_price, operation, person, paid) values(
                                                    "{str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))}", 
                                                    "{i[0]}({i[1]})", 
                                                    "{i[3]}", 
                                                    "{int(i[5]) * int(i[3])}", 
                                                    "Buy",
                                                    "{i[4]}",
                                                    "{i[6]}")''')
            conn.commit()

        for i in to_add:
            curs.execute(f'''INSERT INTO products (name, code, categorie, qt, price) values("{i[0]}", "{i[1]}", "{i[2]}", {int(i[3])}, "{i[5]}")''')
            add_history(i)

        for i in to_update:
            curs.execute(f'''
                 UPDATE products SET qt = qt + {int(i[3])} where code like "{i[1]}"
            ''')
            add_history(i)

        if not self.is_paid.isChecked():#todo add/raise the debt table
            pass



        conn.close()
        # print(f'rows : {self.to_buy_table.rowCount()} , Clolumns : {self.to_buy_table.columnCount()}')

        self.to_buy_table.clearContents()
        [self.to_buy_table.removeRow(i) for i in range(self.to_buy_table.rowCount()+1, 0, -1)]
        self.to_buy_table.removeRow(0)



    def table_select_event(self):
        # row = [str(i.text()) for i in self.to_buy_table.selectedItems()]
        self.clear.setEnabled(True) if [idx.row() for idx in self.to_buy_table.selectionModel().selectedRows()] else self.clear.setEnabled(False)
        # self.selected_rows = [idx.row() for idx in self.to_buy_table.selectionModel().selectedRows()]
        # if self.selected_rows:
        #     self.clear.setText('Delete')
        #     self.clear.clicked.connect(self.del_row)
        # else:
        #     self.clear.setText('clear')
        #     self.clear.clicked.connect(self.clear_table)

    def del_row(self):
        selected_rows = [idx.row() for idx in self.to_buy_table.selectionModel().selectedRows()]
        # [self.to_buy_table.removeRow(self.to_buy_table.indexAt(int(i)).row()) for i in selected_rows]
        [self.to_buy_table.removeRow(i) for i in selected_rows]



    def add_row(self):
        if self.product_name.currentText() == '' or len(self.product_name.currentText().split( ' - ')) < 2:
            self.err.setText('<font color="red">Invalid Product Name</font>, Hint : code - name...')
        elif self.categorie_.text() == '':
            self.err.setText('<font color="red">Invalid Categorie</font>')
        elif int(self.qt_.text()) <= 0:
            self.err.setText('<font color="red">Invalid Quantity Value</font>')
        elif self.seller.text() == '':
            self.err.setText('<font color="red">Invalid Seller Name</font>, Hint : write - if you don\'t have one')
        elif int(self.price.text() ) <= 0 :
            self.err.setText('<font color="red">Invalid Price Value</font>')
        else:
            self.err.setText('')
            # self.to_buy_table.addTableRow( [self.product_name.currentText().split(' - ')[1], self.categorie.text(), self.qt.text, self.seller.text(), self.price.text() , 'Yes' if self.paid.isChecked() else 'No'])
            row = self.to_buy_table.rowCount()
            self.to_buy_table.insertRow(0)
            col = 0
            for item in [self.product_name.currentText().split(' - ')[1], self.product_name.currentText().split(' - ')[0], self.categorie_.text(), self.qt_.text(),
                         self.seller.text(), self.price.text(), 'Yes' if self.is_paid.isChecked() else 'No', f'{int(self.qt_.text())*int(self.price.text())} DH']:

                cell = QTableWidgetItem(str(item))

                self.to_buy_table.setItem(0, col, cell)
                if col == 6 and not self.is_paid.isChecked():
                    self.to_buy_table.item(0, col).setBackground(QtGui.QColor(255, 153, 153))
                col += 1

            self.seller.setText('')
            self.product_name.setCurrentIndex(0)
            self.is_paid.setChecked(True)

        self.refresh()

    def qt_changing(self):
        if self.qt_.text():
            if self.product_name.currentText() == '':
                self.rest.setText('<font color="red">ERR :</font> Select product first')
                return

            try:
                # old = int(self.rest.text().split('*')[0])

                self.rest.setText(f'{int(self.qt_.text())+ self.qt_value}"in the stock')
            except:
                self.rest.setText('<font color="red">ERR :</font> Fill the Quantity')
            try:
                if int(self.qt_.text()) < 1:
                    self.rest.setText('<font color="red">ERR :</font> Must be > 0')
                    self.add.setEnabled(False)
                else:self.add.setEnabled(True)
            except:pass
        else:
            self.rest.setText('')
            self.add.setEnabled(False)

    def product_choosen(self):
        conn = sqlite3.connect(DB)
        curs = conn.cursor()
        code = str(self.product_name.currentText()).split("-")[0].replace(" ", "")
        print(code)
        try:
            dt = curs.execute(f'select categorie, qt, price from products where code like "{code}"').fetchone()
            self.categorie_.setText(dt[0])
            self.categorie_.setReadOnly(True)
            self.qt_value = int(dt[1])
            self.rest.setText(f'{self.qt_value}"in the stock')

            self.price.setText(str(dt[2]))

        except:
            self.categorie_.setText('')
            self.categorie_.setReadOnly(False)
            self.rest.setText('0 in the stock')
            self.price.setText('')
            self.qt_.setText('1')
            self.qt_value = 0


    def refresh(self):

        conn = sqlite3.connect(DB)
        self.curs = conn.cursor()
        # ll = list([f' - '.join(i) for i in self.curs.execute(f'select code, name from products where name like "%{self.product_name.text()}%" or code like "%{self.product_name.text()}%"').fetchall()])
        ll = list([f' - '.join(i) for i in self.curs.execute(f'select code, name from products order by name asc').fetchall()])
        ll.insert(0, '')
        # ll = ['yassine', 'baghdadi', 'guercif']

        self.model.setStringList(list(set(i[0] for i in self.curs.execute('select person from history').fetchall())))
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