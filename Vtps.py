import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import urllib.request
import json
import csv
import APISingle
import APIBatch
import struct

class Vtps(QWidget):
    def __init__(self):


        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Voter Turnout Prediction System')
        self.setGeometry(300, 250, 500, 125)

        batchbtn = QPushButton('Batch Request', self)
        batchbtn.clicked.connect(self.activateBatch)
        batchbtn.resize(200,100)
        batchbtn.move(250, 15)

        singlebtn = QPushButton('Single Request', self)
        singlebtn.clicked.connect(self.activateSingle)
        singlebtn.resize(200,100)
        singlebtn.move(40, 15)

        app_icon = QtGui.QIcon()
        app_icon.addFile('icon.jpg')
        app.setWindowIcon(app_icon)

        self.show()

    def activateSingle(self):

        self.singleGui = VtpsSingle()
        self.hide()
        self.singleGui.show()

    def activateBatch(self):
        self.batchGui = VtpsBatch()
        self.hide()
        self.batchGui.show()

class VtpsBatch(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.inputFile = QLineEdit(self)
        self.inputFile.setGeometry(40, 30, 400, 25)

        self.outputDir = QLineEdit(self)
        self.outputDir.setGeometry(40, 77, 400, 25)

        self.stdOut = QTextEdit(self)
        self.stdOut.setGeometry(40,155,450,75)
        self.stdOut.setReadOnly(True)

        self.calcbtn = QPushButton('Calculate', self)
        self.calcbtn.clicked.connect(self.do_the_big_thing)
        self.calcbtn.resize(self.calcbtn.sizeHint())
        self.calcbtn.move(350, 115)

        app_icon = QtGui.QIcon()
        app_icon.addFile('icon.jpg')
        app.setWindowIcon(app_icon)

        brsbtn1 = QPushButton('Browse', self)
        brsbtn1.clicked.connect(self.browse_file)
        brsbtn1.resize(brsbtn1.sizeHint())
        brsbtn1.move(450, 28)

        brsbtn2 = QPushButton('Browse', self)
        brsbtn2.clicked.connect(self.showDialog)
        brsbtn2.resize(brsbtn2.sizeHint())
        brsbtn2.move(450, 75)

        extbtn = QPushButton('Exit', self)
        extbtn.clicked.connect(QCoreApplication.instance().quit)
        extbtn.resize(extbtn.sizeHint())
        extbtn.move(450, 115)

        bkbtn = QPushButton('Back', self)
        bkbtn.clicked.connect(self.goBack)
        bkbtn.resize(extbtn.sizeHint())
        bkbtn.move(275, 115)

        lblinput = QLabel('Input File:', self)
        lblinput.move(15, 10)

        lbloutput = QLabel('Output Directory:', self)
        lbloutput.move(15, 60)

        lbloutputlog = QLabel('Output Log:', self)
        lbloutputlog.move(15,125)

        self.setGeometry(300, 300, 550, 250)
        self.setWindowTitle('Voter Turnout Prediction System')

    def goBack(self):
        self.hide()
        gui.show()

    def showDialog(self):
        outputLoc = QFileDialog.getExistingDirectory(options=QFileDialog.DontUseNativeDialog)

        if outputLoc is not None:
            self.outputDir.setText(outputLoc)
            self.stdOut.insertPlainText('Output directory selected.\n')
            self.stdOut.moveCursor(11)

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(options=QFileDialog.DontUseNativeDialog)

        if file_name[1]:
            self.inputFile.setText(file_name[0])
            self.stdOut.insertPlainText('File selected.\n')
            self.stdOut.moveCursor(11)

    def do_the_big_thing(self):    
        if self.inputFile.text() is '':
            self.stdOut.insertPlainText('No input file detected. Operation Aborted.\n')
            self.stdOut.moveCursor(11)
        elif self.outputDir.text() is '':
            self.stdOut.insertPlainText('No output directory selected. Please select an output directory.\n ')
            self.stdOut.moveCursor(11)
        else:
            self.stdOut.insertPlainText('Beginning Analysis.\n')
            self.stdOut.moveCursor(11)
            outpath = self.outputDir.text() + '/'
            APIBatch.invokeBatchExecutionService(self.inputFile.text(),outpath)
            self.stdOut.insertPlainText('Analysis complete. \nSee output directory for results.\n')


class VtpsSingle(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        sendbtn = QPushButton('Send', self)
        sendbtn.clicked.connect(self.send_request)
        sendbtn.resize(sendbtn.sizeHint())
        sendbtn.move(300, 30)

        bkbtn = QPushButton('Back', self)
        bkbtn.clicked.connect(self.goBack)
        bkbtn.resize(bkbtn.sizeHint())
        bkbtn.move(300, 70)

        extbtn = QPushButton('Exit', self)
        extbtn.clicked.connect(QCoreApplication.instance().quit)
        extbtn.resize(extbtn.sizeHint())
        extbtn.move(300, 110)

        app_icon = QtGui.QIcon()
        app_icon.addFile('icon.jpg')
        app.setWindowIcon(app_icon)

        lbloutput = QLabel('Are you on the do not call list?', self)
        lbloutput.move(20, 365)
        self.dontPhonecombo = QComboBox(self)
        self.dontPhonecombo.addItem("I'm on the do not call list.")
        self.dontPhonecombo.addItem("I'm not on the do not call list.")
        self.dontPhonecombo.addItem("Unsure.")
        self.dontPhonecombo.move(20,380)
        self.dontPhonecombo.resize(200,30)
        self.dontPhonetext = self.dontPhonecombo.currentText()

        lbloutput = QLabel('How many elections have you been elegible to vote?', self)
        lbloutput.move(20, 445)
        self.cntEligibleLineEdit = QLineEdit(self)
        self.cntEligibleLineEdit.move(20,460)
        self.cntEligibleLineEdit.resize(200,20)
        self.cntEligibletext = self.cntEligibleLineEdit.displayText()

        lbloutput = QLabel('What is your gender?', self)
        lbloutput.move(20, 5)
        self.gendercombo = QComboBox(self)
        self.gendercombo.addItem("Male")
        self.gendercombo.addItem("Female")
        self.gendercombo.move(20,20)
        self.gendercombo.resize(200,30)
        self.gendertext = self.gendercombo.currentText()

        lbloutput = QLabel('What is your preferred party?', self)
        lbloutput.move(20, 45)
        self.partyAffiliationcombo = QComboBox(self)
        self.partyAffiliationcombo.addItem("Democrats")
        self.partyAffiliationcombo.addItem("Republicans")
        self.partyAffiliationcombo.addItem("Other")
        self.partyAffiliationcombo.move(20,60)
        self.partyAffiliationcombo.resize(200,30)
        self.partyAffiliationtext = self.partyAffiliationcombo.currentText()

        lbloutput = QLabel('Are you the head of your family?', self)
        lbloutput.move(20, 85)
        self.householdHeadcombo = QComboBox(self)
        self.householdHeadcombo.addItem("Head")
        self.householdHeadcombo.addItem("Member")
        self.householdHeadcombo.move(20,100)
        self.householdHeadcombo.resize(200,30)
        self.householdHeadtext = self.householdHeadcombo.currentText()

        lbloutput = QLabel('Where do you rank in your household?', self)
        lbloutput.move(20, 125)
        self.householdRankcombo = QComboBox(self)
        self.householdRankcombo.addItem("1 (Highest)")
        self.householdRankcombo.addItem("2")
        self.householdRankcombo.addItem("3+")
        self.householdRankcombo.move(20,140)
        self.householdRankcombo.resize(200,30)
        self.householdRanktext = self.householdRankcombo.currentText()

        lbloutput = QLabel('Do you ever postal vote?', self)
        lbloutput.move(20, 165)
        self.mailOrdercombo = QComboBox(self)
        self.mailOrdercombo.addItem("I often postal vote.")
        self.mailOrdercombo.addItem("I never postal vote.")
        self.mailOrdercombo.move(20,180)
        self.mailOrdercombo.resize(200,30)
        self.mailOrdertext = self.mailOrdercombo.currentText()

        lbloutput = QLabel('What is your average income?', self)
        lbloutput.move(20, 205)
        self.incomecombo = QComboBox(self)
        self.incomecombo.addItem("Under $15,000")
        self.incomecombo.addItem("$15,000-$24,999")
        self.incomecombo.addItem("$25,000-$34,999")
        self.incomecombo.addItem("$35,000-$49,999")
        self.incomecombo.addItem("$50,000-$74,999")
        self.incomecombo.addItem("$75,000-$99,999")
        self.incomecombo.addItem("$100,000-$124,999")
        self.incomecombo.addItem("$125,000-$149,999")
        self.incomecombo.addItem("$150,000-$174,999")
        self.incomecombo.addItem("$175,000-$199,999")
        self.incomecombo.addItem("$200,000-$249,999")
        self.incomecombo.addItem("More than $250,000")
        self.incomecombo.move(20,220)
        self.incomecombo.resize(200,30)
        self.incometext = self.incomecombo.currentText()

        lbloutput = QLabel('Do you own the home you live in?', self)
        lbloutput.move(20, 245)
        self.homeOwnercombo = QComboBox(self)
        self.homeOwnercombo.addItem("Renter")
        self.homeOwnercombo.addItem("Probable Renter")
        self.homeOwnercombo.addItem("Probable Homeowner")
        self.homeOwnercombo.addItem("Homeowner")
        self.homeOwnercombo.move(20,260)
        self.homeOwnercombo.resize(200,30)
        self.homeOwnertext = self.homeOwnercombo.currentText()

        lbloutput = QLabel('Do you own a computer?', self)
        lbloutput.move(20, 285)
        self.compOwnercombo = QComboBox(self)
        self.compOwnercombo.addItem("I  own a computer")
        self.compOwnercombo.addItem("I don't own a computer")
        self.compOwnercombo.move(20,300)
        self.compOwnercombo.resize(200,30)
        self.compOwnertext = self.compOwnercombo.currentText()

        lbloutput = QLabel('What is your education level?', self)
        lbloutput.move(20, 325)
        self.educationLevelcombo = QComboBox(self)
        self.educationLevelcombo.addItem("1 (Highest)")
        self.educationLevelcombo.addItem("2")
        self.educationLevelcombo.addItem("3")
        self.educationLevelcombo.addItem("4")
        self.educationLevelcombo.addItem("5")
        self.educationLevelcombo.addItem("6")
        self.educationLevelcombo.addItem("7 (Lowest)")
        self.educationLevelcombo.move(20,340)
        self.educationLevelcombo.resize(200,30)

        lbloutput = QLabel("How many elections have you voted in?", self)
        lbloutput.move(20, 405)
        self.cntLineEdit = QLineEdit(self)
        self.cntLineEdit.move(20,420)
        self.cntLineEdit.resize(200,20)
        self.cnttext = self.cntLineEdit.displayText()

        lbloutput = QLabel("Probability of voting:", self)
        lbloutput.move(240, 245)
        self.results = QLineEdit(self)
        self.results.move(240,265)

        self.setGeometry(400, 100, 400, 500)


    def goBack(self):
        self.hide()
        gui.show()


    def send_request(self):
        self.cntEligibletext        = self.cntEligibleLineEdit.displayText()[0:1]
        self.gendertext             = self.gendercombo.currentText()
        self.partyAffiliationtext   = self.partyAffiliationcombo.currentText()
        self.householdHeadtext      = self.householdHeadcombo.currentText()
        self.householdRanktext      = self.householdRankcombo.currentText()
        self.mailOrdertext          = self.mailOrdercombo.currentText()
        self.incometext             = self.incomecombo.currentText()
        self.compOwnertext          = self.compOwnercombo.currentText()
        self.homeOwnertext          = self.homeOwnercombo.currentText()
        self.cnttext                = self.cntLineEdit.displayText()[0:2]
        self.educationLeveltext     = self.educationLevelcombo.currentText()
        self.dontPhonetext          = self.dontPhonecombo.currentText()

        result = APISingle.SummonAzure(self.cntEligibletext,
                                       self.gendertext,
                                       self.partyAffiliationtext,
                                       self.householdHeadtext,
                                       self.householdRanktext,
                                       self.mailOrdertext,
                                       self.incometext,
                                       self.compOwnertext,
                                       self.homeOwnertext,
                                       self.cnttext,
                                       self.educationLeveltext,
                                       self.dontPhonetext)
        if result is None:
            result = 'ERROR'
        else:
            result = str(result)

        self.results.setText(result)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = Vtps()
    sys.exit(app.exec_())
