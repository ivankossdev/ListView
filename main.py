import sys
from ReaderCSV import read_file, list_convertor
from des import *

# pyuic5 des.ui -o des.py
# pyinstaller -F -w main.py
# pyrcc5 res.qrc -o res_rc.py
# pyinstaller -F -w -i BD.ico main.py

class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_1 = list_convertor(read_file())[0]
        self.list_2 = list_convertor(read_file())[1]
        self.ui.listWidget.addItems(self.list_1)
        self.ui.listWidget.clicked.connect(self.click_widget_1)
        self.ui.listWidget_2.clicked.connect(self.click_widget_2)
        self.ui.pushButton_right.clicked.connect(self.send_button)
        self.ui.pushButton_left.clicked.connect(self.resend_button)
        self.ui.pushButton_enter.clicked.connect(self.enter_button)
        self.selected = None

    def enter_button(self):
        if '' != self.ui.lineEdit.text():
            self.ui.listWidget.insertItem(0, self.ui.lineEdit.text())
            self.ui.lineEdit.clear()
        else:
            QtWidgets.QMessageBox.information(self, "Сообщение", "Введите строку")

    def click_widget_1(self):
        self.selected = self.ui.listWidget.currentRow()

    def click_widget_2(self):
        self.selected = self.ui.listWidget_2.currentRow()

    def send_button(self):
        try:
            if self.selected is not None:
                self.ui.listWidget_2.insertItem(self.selected,
                                                self.ui.listWidget.takeItem(self.selected).text())
                self.selected = None
            else:
                pass
        except Exception:
            QtWidgets.QMessageBox.information(self, "Внимание", "Жми на кнопку ниже!!!")

    def resend_button(self):
        try:
            if self.selected is not None:
                self.ui.listWidget.insertItem(self.selected,
                                                self.ui.listWidget_2.takeItem(self.selected).text())
                self.selected = None
            else:
                pass
        except Exception:
            QtWidgets.QMessageBox.information(self, "Внимание", "Жми на кнопку выше!!!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())