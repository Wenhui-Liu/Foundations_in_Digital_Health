import threading

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QGroupBox,QVBoxLayout,QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QSize, QThread
import UI_model
import UMLS_CONNECT
from queue import Queue

global result
result_queue = Queue()

global result_solr
result_solr = Queue()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = UI_model.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.movie.start()
        self.ui.loading_label.hide()
        self.ui.pushButton.clicked.connect(self.Serach_function)
        self.ui.cleanButton.clicked.connect(self.clearAll)

    def clearAll(self):
        a = self.ui.verticalLayout.count()
        for i in reversed(range(self.ui.verticalLayout.count())):
            self.ui.verticalLayout.itemAt(i).widget().setParent(None)
        self.ui.Expired_button_group.setExclusive(False)
        self.ui.Synonyms_button_group.setExclusive(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.Expired_button_group.setExclusive(True)
        self.ui.Synonyms_button_group.setExclusive(True)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()


        return

    def Serach_function(self):
        self.ui.loading_label.show()
        try:
            KeyWord = self.ui.lineEdit.text()
            FromDate = self.ui.lineEdit_2.text()
            ToDate = self.ui.lineEdit_3.text()
            DiagnosesNum = self.ui.lineEdit_4.text()
        except Exception as e:
            print(e)

        try:
            Expired = self.ui.Expired_button_group.checkedButton().text()
        except Exception as e:
            Expired = None
        try:
            Synonyms = self.ui.Synonyms_button_group.checkedButton().text()
        except Exception as e:
            Synonyms = None

        UMLS_key = None
        if Synonyms == "Yes":
            search_thread = threading.Thread(target= UMLS_CONNECT.UMLS_SEARCH,args = (KeyWord,result_queue))
            search_thread.start()
            UMLS_key = result_queue.get()
            KeyWord = UMLS_key
            print(UMLS_key)

        solr_Thread = threading.Thread(target=UMLS_CONNECT.solr_search,args = (KeyWord,FromDate,ToDate,DiagnosesNum,Expired,result_solr))
        solr_Thread.start()

        solr_result = result_solr.get()
        totalnum = result_solr.get()

        KeyWord = self.ui.lineEdit.text()
        FromDate = self.ui.lineEdit_2.text()
        ToDate = self.ui.lineEdit_3.text()
        DiagnosesNum = self.ui.lineEdit_4.text()
        u_input = KeyWord + FromDate + ToDate+ DiagnosesNum

        self.addBox(u_input,solr_result,UMLS_key,totalnum)

        self.ui.movie.stop()
        return

    def addBox(self,u_input,res,UMLS_key,totalnum):
        # Create a new group box and add it to the scroll widget layout
        group_box = QGroupBox(f'User Input:{str(u_input)}')
        group_box_layout = QVBoxLayout(group_box)

        if UMLS_key != None:
            b = QLabel()
            b.setText(f"Similar Word for input:{UMLS_key[1:]}")
            b.setWordWrap(True)
            group_box_layout.addWidget(b)



        a = QLabel()
        a.setText(f"This is the result ID:{res}")
        a.setWordWrap(True)
        c = QLabel()
        c.setText(f"\n***************************************\nTotal number of matching documents:{totalnum}\n")
        c.setWordWrap(True)
        group_box_layout.addWidget(a)
        group_box_layout.addWidget(c)
        self.ui.verticalLayout.addWidget(group_box)


if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.show()


    sys.exit(app.exec_())
