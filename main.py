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
        self.ui.pushButton_dalete.clicked.connect(self.delete_all)
        self.ui.pushButton_dalete.setEnabled(False)
        self.selected = None
        self.edit_state = False
        self.print_rows()
        self.ui.listWidget.installEventFilter(self)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu and
                source is self.ui.listWidget):
            context_menu = QtWidgets.QMenu()
            edit = context_menu.addAction('Edit')
            delete_row = context_menu.addAction('Delete row')
            delete_all = context_menu.addAction('Delete all')
            action = context_menu.exec_(event.globalPos())
            if action == edit:
                try:
                    if self.selected is not None:
                        self.ui.lineEdit.insert(source.itemAt(event.pos()).text())
                        self.edit_state = True
                        self.selected = None
                except AttributeError:
                    pass
            elif action == delete_row:
                if self.selected is not None:
                    self.selected = self.ui.listWidget.currentRow()
                    self.ui.listWidget.takeItem(self.selected)
                    self.selected = None
            elif delete_all == action:
                self.ui.pushButton_dalete.setEnabled(True)
            return True
        return super(App, self).eventFilter(source, event)

    def delete_all(self):
        result = QtWidgets.QMessageBox.question(self, '??????????????????', '?????????????? ?????? ?????????????',
                                                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.pushButton_dalete.setEnabled(False)
        else:
            self.ui.pushButton_dalete.setEnabled(False)

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
        # QtWidgets.QMessageBox.information(self, "??????????????????", "???????????? ???????????? ??????????????")
        file_path = QtWidgets.QFileDialog.getOpenFileNames(self, '?????????????? ????????', 'task', '*.csv')
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        path = file_path[0][0]
        read_file(path)
        self.list_1 = list_convertor(read_file(path))[0]
        self.list_2 = list_convertor(read_file(path))[1]
        self.print_rows()

    def exit_program(self):
        result = QtWidgets.QMessageBox.question(self, '??????????????????', '?????????????????? ???????????????????',
                                                QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.save_file()
            exit()
        else:
            exit()

    def enter_button(self):
        if self.edit_state:
            self.edit_state = False
            row = self.ui.listWidget.currentRow()
            insert_line = self.ui.lineEdit.text()
            self.ui.listWidget.takeItem(row)
            self.ui.listWidget.insertItem(row, insert_line)
            self.ui.lineEdit.clear()
        else:
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
            QtWidgets.QMessageBox.information(self, "????????????????", "?????? ???? ???????????? ????????!!!")

    def button_left(self):
        try:
            if self.selected is not None:
                self.ui.listWidget.insertItem(self.ui.listWidget.count(),
                                              self.ui.listWidget_2.takeItem(self.selected).text())
                self.selected = None
            else:
                pass
        except Exception:
            QtWidgets.QMessageBox.information(self, "????????????????", "?????? ???? ???????????? ????????!!!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())
