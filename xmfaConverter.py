'''
Copyright (C) 2015 by Astha Jaiswal
astha421@gmail.com
 
This file is part of xmfaGenerator.

    xmfaGenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    xmfaGenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with xmfaGenerator. If not, see <http://www.gnu.org/licenses/>.

'''

from PyQt4 import QtCore, QtGui
import sys
import webbrowser
import Tkinter
import tkFileDialog
import urllib
import fc
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.out_file = None
        self.in_file = None
        self.currentPath = None
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("xmfaConvertor"))
        Form.resize(485, 334)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 221))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.lineEdit = QtGui.QLineEdit(self.tab1)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 241, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.tab1)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 30, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 341, 16))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 241, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 401, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(300, 300, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)       
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(300, 250, 25, 19))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 221, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 270, 23))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        

        # send signal
        self.tabWidget.currentChanged.connect(self.eventResponseTab)
        self.pushButton_3.clicked.connect(self.eventResponseButton)
        self.pushButton_2.clicked.connect(self.eventResponseButton)
        self.buttonBox.accepted.connect(self.eventResponseButtonBoxOK)
        self.buttonBox.rejected.connect(self.eventResponseButtonBoxCancel)
        self.toolButton.clicked.connect(self.eventResponsetoolButton)
        
        # call the other funtion
        self.retranslateUi(Form)
        self.currentIndex=0
        self.tabWidget.setCurrentIndex(self.currentIndex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("xmfaConvertor", "xmfaConvertor", None))
        self.lineEdit.setText(_translate("xmfaConvertor", "http://www.ebi.ac.uk/Tools/msa/clustalw2/", None))
        self.pushButton_3.setText(_translate("xmfaConvertor", "Go", None))
        self.lineEdit_2.setText(_translate("xmfaConvertor", "", None))
        self.label.setText(_translate("xmfaConvertor", "Visit ClustalW from here", None))
        self.label_2.setText(_translate("xmfaConvertor", "Paste the URL of alignment results here", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("xmfaGenerator", "Web", None))
        self.pushButton_2.setText(_translate("xmfaConvertor", "Input File", None))
        self.label_4.setText(_translate("xmfaConvertor", "Choose an input file with multiple sequence alignment results (e.g., in.fas).", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("xmfaConvertor", "File", None))
        self.toolButton.setText(_translate("xmfaConvertor", "...", None))
        self.label_3.setText(_translate("xmfaConvertor", "Choose an output file (e.g., out.xmfa)", None))
        self.label_5.setText(_translate("xmfaConvertor", "See logs here", None))

    
    def eventResponseTab(self):
        sender = self.sender()
        if(self.tabWidget.currentIndex() == 0):
           self.label_5.setText(_translate("xmfaConvertor", "Web choosen", None))
           self.currentIndex = 0
        elif(self.tabWidget.currentIndex() == 1):
           self.label_5.setText(_translate("xmfaConvertor", "File choosen", None))
           self.currentIndex = 1
        

    def eventResponseButton(self):
        sender = self.sender()
        if(sender.text() == "Go"):
            self.label_5.setText(_translate("xmfaConvertor", "Opening the Browser", None))
            webbrowser.open(self.lineEdit.text())
        if(sender.text() == "Input File"):
            Tkinter.Tk().withdraw() 
            self.in_file = tkFileDialog.askopenfilename()
            self.label_5.setText(_translate("xmfaConvertor", "Input file: "+self.in_file, None))

    def eventResponseButtonBoxOK(self):
        sender = self.sender()
        if(self.currentIndex == 0):
            self.in_file = open(self.currentPath+"/tmp.fas", 'w')
            link = self.lineEdit_2.text()
            url = str(link)
            f = urllib.urlopen(url)           
            myfile = f.read()
            self.in_file.write(myfile)
            self.in_file.close()
            if(self.out_file == None):
                self.label_5.setText(_translate("xmfaConvertor", "Please choose an output file", None))
            else:
                status=fc.convertFiles(self.currentPath+"/tmp.fas", self.out_file)
                # reset everything
                os.remove(self.currentPath+"/tmp.fas")
                self.out_file = None
                self.currentPath = None
                if(status=="done"):
                    self.label_5.setText(_translate("xmfaConvertor", "Successfully Done", None))
        else:
            if(self.in_file == None):
                self.label_5.setText(_translate("xmfaConvertor", "Please choose an input file", None))
            elif(self.out_file == None):
                self.label_5.setText(_translate("xmfaConvertor", "Please choose an output file", None))
            else:
                status=fc.convertFiles(self.in_file, self.out_file)
                # reset everything
                self.in_file = None
                self.out_file = None
                self.currentPath = None
                if(status=="done"):
                    self.label_5.setText(_translate("xmfaConvertor", "Successfully Done", None))
            
    def eventResponseButtonBoxCancel(self):
        self.close()
        
    def eventResponsetoolButton(self):
        Tkinter.Tk().withdraw() 
        self.out_file = tkFileDialog.asksaveasfilename(defaultextension=".xmfa", filetypes=(("xmfa file", "*.xmfa"),("All Files", "*.*") ))
        self.currentPath = os.path.split(self.out_file)[0]
        self.label_5.setText(_translate("xmfaConvertor", "Output file: "+self.out_file, None))
        
def main():
    print "Copyright (C) 2015 Astha Jaiswal\
        \n astha421@gmail.com \
        \n This file is part of xmfaGenerator.\
        \n \
        \n    xmfaGenerator is free software: you can redistribute it and/or modify\
        \n    it under the terms of the GNU General Public License as published by\
        \n    the Free Software Foundation, either version 3 of the License, or\
        \n    (at your option) any later version.\
        \n \
        \n    xmfaGenerator is distributed in the hope that it will be useful,\
        \n    but WITHOUT ANY WARRANTY; without even the implied warranty of\
        \n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
        \n    GNU General Public License for more details.\
        \n \
        \n    You should have received a copy of the GNU General Public License\
        \n    along with xmfaGenerator. If not, see <http://www.gnu.org/licenses/>."                               

    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
