# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
#
#
# class Main(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QtWidgets.QHBoxLayout()
#         self.choice_questions = QtWidgets.QTreeWidget(self)
#         self.choice_questions.setFixedSize(850, 400)
#         self.choice_questions.setHeaderLabels(["№", "1", "2"])
#         item = QtWidgets.QTreeWidgetItem(["1", "пример1", "пример2"])
#         self.choice_questions.addTopLevelItem(item)
#         self.choice_questions.setFont(QtGui.QFont('Times New Roman', 13))
#         self.choice_questions.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#         self.choice_questions.customContextMenuRequested.connect(self.context)
#         layout.addWidget(self.choice_questions)
#         self.setLayout(layout)
#
#     def context(self, point):
#         menu = QtWidgets.QMenu()
#         if self.choice_questions.itemAt(point):
#             edit_question = QtWidgets.QAction('Редактировать вопрос', menu)
#             edit_question.triggered.connect(lambda: print("Текст в первой ячейке: " +
#                                                           self.choice_questions.itemAt(point).text(1)))
#             menu.addAction(edit_question)
#         else:
#             pass
#         menu.exec(self.choice_questions.mapToGlobal(point))
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main = Main()
#     main.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())