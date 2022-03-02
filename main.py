import sys
from des import *
# pyuic5 des.ui -o des.py
# pyinstaller -F -w main.py
# pyrcc5 res.qrc -o des.py
# pyinstaller -F -w -i BD.ico main.py

class App(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.listWidget.insertItem(0, 'Red')
        # self.ui.listWidget.insertItem(1, 'Orange')
        self.ui.listWidget.addItems(['красный', 'синий', 'зеленый', 'черный'])
        self.ui.listWidget.clicked.connect(self.click_widget_1)
        self.ui.listWidget_2.clicked.connect(self.click_widget_2)
        self.ui.pushButton.clicked.connect(self.send_button)
        self.ui.pushButton_2.clicked.connect(self.resend_button)
        self.selected = None

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
            QtWidgets.QMessageBox.information(self, "Облом", "Жми на кнопку ниже!!!")

    def resend_button(self):
        try:
            if self.selected is not None:
                self.ui.listWidget.insertItem(self.selected,
                                                self.ui.listWidget_2.takeItem(self.selected).text())
                self.selected = None
            else:
                pass
        except Exception:
            QtWidgets.QMessageBox.information(self, "Облом", "Жми на кнопку выше!!!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())