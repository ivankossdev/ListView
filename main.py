import sys
from ReaderCSV import read_file, list_convertor, write_file
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
        read_file()
        self.list_1 = list_convertor(read_file())[0]
        self.list_2 = list_convertor(read_file())[1]
        self.ui.listWidget.clicked.connect(self.click_widget_1)
        self.ui.listWidget_2.clicked.connect(self.click_widget_2)
        self.ui.lineEdit.editingFinished.connect(self.enter_button)
        self.ui.pushButton_right.clicked.connect(self.right_button)
        self.ui.pushButton_left.clicked.connect(self.button_left)
        self.ui.pushButton_enter.clicked.connect(self.enter_button)
        self.ui.pushButton_exit.clicked.connect(self.exit_program)
        self.ui.pushButton_open.clicked.connect(self.open_file)
        self.ui.pushButton_save.clicked.connect(self.save_file)
        self.ui.pushButton_dalete.clicked.connect(self.delete_row)
        self.ui.pushButton_dalete.setHidden(True)
        self.ui.pushButton_edit.setHidden(True)
        self.ui.pushButton_delete_row.setHidden(True)
        self.selected = None
        self.edit_state = False
        self.print_rows()
        self.ui.listWidget.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu and
                source is self.ui.listWidget):
            menu = QtWidgets.QMenu()
            menu.addAction('Edit')
            if menu.exec_(event.globalPos()):
                # self.selected = source.itemAt(event.pos()).text()
                # source.takeItem(self.ui.listWidget.currentRow()).text()
                self.edit()
            return True
        return super(App, self).eventFilter(source, event)

    def edit(self):
        self.ui.pushButton_dalete.setHidden(False)

    def delete_row(self):
        print(self.ui.listWidget.takeItem(self.ui.listWidget.currentRow()).text())

    def delete_all(self):
        result = QtWidgets.QMessageBox.question(self, 'Внимаение', 'Удалить все записи?',
                                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # write_file([])
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            # self.save_file()

    def print_rows(self):
        for x in self.list_1:
            if "" != x:
                 self.ui.listWidget.addItem(x)
        for x in self.list_2:
            if "" != x:
                self.ui.listWidget_2.addItem(x)

    def save_file(self):
        li_1 = []
        li_2 = []
        for x in range(self.ui.listWidget.count()):
            li_1.append(self.ui.listWidget.item(x).text())
        for y in range(self.ui.listWidget_2.count()):
            li_2.append(self.ui.listWidget_2.item(y).text())
        write_file(li_1, li_2)

    def open_file(self):
        QtWidgets.QMessageBox.information(self, "Сообщение", "Нажата кнопка открыть")

    def exit_program(self):
        result = QtWidgets.QMessageBox.question(self, 'Внимаение', 'Сохранить изменения?',
                                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.save_file()
            exit()
        else:
            exit()

    def enter_button(self):
        if '' != self.ui.lineEdit.text():
            self.ui.listWidget.insertItem(self.ui.listWidget.count(), self.ui.lineEdit.text())
            self.ui.lineEdit.clear()

    def click_widget_1(self):
        self.selected = self.ui.listWidget.currentRow()

    def click_widget_2(self):
        self.selected = self.ui.listWidget_2.currentRow()

    def right_button(self):
        try:
            if self.selected is not None:
                self.ui.listWidget_2.insertItem(self.ui.listWidget_2.count(),
                                                self.ui.listWidget.takeItem(self.selected).text())
                self.selected = None
            else:
                pass
        except Exception:
            QtWidgets.QMessageBox.information(self, "Внимание", "Жми на кнопку ниже!!!")

    def button_left(self):
        try:
            if self.selected is not None:
                self.ui.listWidget.insertItem(self.ui.listWidget.count(),
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
