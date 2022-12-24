#from UI.Login import Ui_LoginWindow

import sys
#Libraraies imported to embed the graph in the form
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import random
#----------------------------------------------
from Stacked_DesignUI1 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox,QPushButton
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)
import re
from Core import User, InventorySupervisor, Rider , SaleAgent, Vehicle
from DL.UserCRUD import UserCRUD
from DL.AttendenceCRUD import AttendenceCRUD
from DL.VehicleCRUD import VehicleCRUD
from DL.NotificationDL import Notifications

from random import randint
from datetime import date , datetime



class ManaMainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.userDL = UserCRUD()
        self.userDL.readFromTable()
        self.vehicleDL=VehicleCRUD()
        self.vehicleDL.loadFromTable()
        self.AttendanceDL = AttendenceCRUD()
        self.AttendanceDL.readData()

        self.noti=Notifications()
        self.noti.GetNotification()
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card1.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card2.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card3.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Card4.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_TopClients.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_TableWhatsNew.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_GoalsCompleted.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Account_Widget.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Input_Widget.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.HeaderFrame_3.setGraphicsEffect(self.shadow)

        #--------------Shadow Add Vehicle--------------
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_17.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.widget_12.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.frame_34.setGraphicsEffect(self.shadow)
        #----------------------------------------------

        #----------Create a horizontal Layout----------
        
        self.ui.horizontalLayout_107=QtWidgets.QHBoxLayout(self.ui.frame_34)
        self.ui.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.ui.figure7=plt.figure()
        self.ui.canvas7=FigureCanvas(self.ui.figure7)
        self.ui.horizontalLayout_107.addWidget(self.ui.canvas7)

        Days=['Monday','Tuesday','Wednesday','Thursday']
        values=[123,1,333,2]
        plt.plot(Days,values,color='red')
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas7.draw()
        self.ui.txt_Salaries.setText("1234")
        
        #----------------------------------------------
        now1 = date.today()
        dateTime = now1.strftime("%Y-%m-%d")
        day = dateTime.split("-")
        if(day[2]=="30"): #MakeEveryone Un Paid
            self.Make_Everyone_Unpaid()
        
        #self.ui.btnUpdateStock.clicked.connect(lambda: self.OpenUpdatePage())
        #self.ui.btnBuyStock.clicked.connect(lambda: self.OpenBuyStockPage())
        #self.ui.btn_Report_Cost.clicked.connect(lambda: self.OpenReportCostPage())
        self.ui.menuBtn.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_2.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_3.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_4.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.menuBtn_5.clicked.connect(lambda: self.slideLeftMenu())
        self.ui.accountBtn.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_2.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_3.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_4.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.accountBtn_5.clicked.connect(lambda: self.SlideRightMenu())
        self.ui.btnAddEmployee.clicked.connect(lambda: self.OpenAddEmployee())
        self.ui.btnDashboard.clicked.connect(lambda: self.OpenDashboardManager())
        self.ui.btnUpdateEmployee.clicked.connect(lambda: self.OpenUpdateEmployee())
        self.ui.btn_AddVehicle.clicked.connect(lambda: self.OpenAddVehicleManager())
        self.ui.btnCheckAttendance.clicked.connect(lambda: self.OpenCheckattendance())
        self.ui.btn_CompanyAccount.clicked.connect(lambda: self.OpenCompanyAccountManager())
        self.ui.btn_AddEmployee.clicked.connect(lambda: self.Add_Employee())
        self.ui.btn_GenerateID.clicked.connect(lambda: self.generate_userID())
        self.ui.btn_GeneratePassword.clicked.connect(lambda: self.generate_password(8,self.ui.txt_Passsword))
        self.ui.btn_UpdateDetails.clicked.connect(lambda: self.ShowToUpdateEmployee())
        self.ui.btn_Delete.clicked.connect(lambda: self.deleteEmployee(self.updateEmpObj))
        self.ui.btn_Update.clicked.connect(lambda: self.update_employee(self.updateEmpObj))
        self.ui.Update_tableWidget.verticalHeader().sectionClicked.connect(lambda: self.getTableRow())
        self.ui.btn_AddVehicle_2.clicked.connect(lambda: self.addVehicle())
        self.ui.btn_SalaryBonus.clicked.connect(lambda: self.OpenSalaryPage())
        self.ui.btn_paySalary.clicked.connect(lambda: self.Pay_Salary())
        self.ui.btnNotification.clicked.connect(lambda: self.Open_NotificationPage())
        
        
        self.show()
    def Open_NotificationPage(self):
        self.ui.mainBody.setCurrentIndex(8)
        self.LoadNotificationTable()
    def LoadNotificationTable(self):
        row=0
        self.ui.table_Notification.setRowCount(5)
        for i in range(5):
            btn_Edit = QPushButton()
            btn_Edit.setText("Confirm")
            self.ui.table_Notification.setCellWidget(row,2,btn_Edit)
            btn_Delete=QPushButton()
            btn_Delete.setText("Reject")
            self.ui.table_Notification.setCellWidget(row,3,btn_Delete)
            row+=1
    def OpenSalaryPage(self):
        self.ui.mainBody.setCurrentIndex(6)
        self.Load_SalaryTable()
        
    def Load_SalaryTable(self):    
        row = 0
        unPaid=[]
        self.ui.tableWidget_4.setRowCount(self.Get_Table_Row_Length())
        for i in self.userDL.getHashTable():
            for j in i :
                if(j!=None):
                    if(j[1].getUserRole()!= 0):
                        self.ui.tableWidget_4.setItem(row, 0, QtWidgets.QTableWidgetItem(str(j[0])))
                        self.ui.tableWidget_4.setItem(row, 1, QtWidgets.QTableWidgetItem(str(j[1].getName())))
                        if (j[1].getUserRole() == 1) :
                            self.ui.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem("Inventory Supervisor"))
                        elif (j[1].getUserRole() == 2) :
                            self.ui.tableWidget_4.setItem(row, 2, QtWidgets.QTableWidgetItem("Sales Agent"))
                        self.ui.tableWidget_4.setItem(row, 3, QtWidgets.QTableWidgetItem(str(j[1].getSalary())))
                        print(j[1].get_s_status())
                        if (j[1].get_s_status() != 0):
                            pass
                            self.ui.tableWidget_4.setItem(row, 4, QtWidgets.QTableWidgetItem("Paid"))
                        else:
                            self.ui.tableWidget_4.setItem(row, 4, QtWidgets.QTableWidgetItem("Un Paid"))
                            unPaid.append(j[1].getName())
                        
                        #self.ui.tableWidget_4.setCellWidget(row,4,btn)
                        
                        row+=1
        self.Select_Employee(unPaid)
        
    def Select_Employee(self,unPaid):
        self.ui.cmb_Employee_3.clear()
        self.ui.cmb_Employee_3.addItems(unPaid)

    def Pay_Salary(self):
        
        employee=self.ui.cmb_Employee_3.currentText()
        if(employee!=""):
            bonus=self.ui.txt_Bonus.text()
            if(bonus=="" or bonus==None):
                bonus="0"
            if(bonus.isdigit()):
                isFound=False


                for i in self.userDL.getHashTable():
                    for j in i :
                        if(j!=None):
                            if(j[1].getUserRole()!= 0 and j[1].getName()==employee):
                                j[1].set_s_status(1)
                                isFound=True
                                self.Load_SalaryTable()
                                self.ui.txt_Bonus.clear()
                                break
                    if(isFound):
                        break
            else:
                self.ui.txt_Bonus.clear()
                QMessageBox.warning(self , "Error","Bonus must be integer and greater than zero")
        else:
            self.ui.txt_Bonus.clear()
            QMessageBox.warning(self , "Error","Employee must be selected")


    def Make_Everyone_Unpaid(self):
        for i in self.userDL.getHashTable():
            for j in i :
                if(j!=None):
                    if(j[1].getUserRole()!= 0):
                        j[1].set_s_status(0)
    def Get_Table_Row_Length(self):
        count=0
        for i in self.userDL.getHashTable():
            for j in i:
                if(j!=None and j[1].getUserRole()!= 0):
                    count+=1
        return count
        
    def getTableRow(self):
       
        tableRow=self.ui.Update_tableWidget.currentRow()
        userName=self.ui.Update_tableWidget.item(tableRow,7)
        self.updateEmpObj=self.userDL.getUserReturn(userName.text())
        if(self.updateEmpObj!=None):
            self.ui.btn_UpdateDetails.setEnabled(1)
            self.ui.btn_Delete.setEnabled(1)
        
            
    def OpenCompanyAccountManager(self):
        
        #self.PlotGraph2()
        self.ui.mainBody.setCurrentIndex(7)
        self.PlotGraph()
        
    def PlotGraph(self):
        self.ui.horizontalLayout_100=QtWidgets.QHBoxLayout(self.ui.frame_15)
        self.ui.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.ui.figure1=plt.figure()
        self.ui.canvas1=FigureCanvas(self.ui.figure1)
        self.ui.horizontalLayout_100.addWidget(self.ui.canvas1)

        Days=['Monday','Tuesday','Wednesday','Thursday']
        values=random.randint(50,size=(4))
        plt.bar(Days,values,color='red',width=0.4)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas1.draw()
        self.ui.txt_Salaries.setText("1234")

        self.ui.horizontalLayout_101=QtWidgets.QVBoxLayout(self.ui.frame_17)
        self.ui.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.ui.figure2=plt.figure()
        self.ui.canvas2=FigureCanvas(self.ui.figure2)
        self.ui.horizontalLayout_101.addWidget(self.ui.canvas2)

        Dayss=['Monday','Tuesday','Wednesday','Thursday']
        valuses=[1,2,3,4]
        plt.plot(Dayss,valuses)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas2.draw()
        self.ui.txt_FuelConsumption.setText("1234")


        self.ui.horizontalLayout_102=QtWidgets.QHBoxLayout(self.ui.frame_18)
        self.ui.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.ui.figure3=plt.figure()
        self.ui.canvas3=FigureCanvas(self.ui.figure3)
        self.ui.horizontalLayout_102.addWidget(self.ui.canvas3)

        Dayss=['Monday','Tuesday','Wednesday','Thursday']
        valuses=[1,2,3,4]
        plt.scatter(Dayss,valuses)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas3.draw()
        self.ui.txt_Bonuses.setText("1234")

        self.ui.horizontalLayout_103=QtWidgets.QHBoxLayout(self.ui.frame_19)
        self.ui.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.ui.figure4=plt.figure()
        self.ui.canvas4=FigureCanvas(self.ui.figure4)
        self.ui.horizontalLayout_103.addWidget(self.ui.canvas4)

        Dayss=['Monday','Tuesday','Wednesday','Thursday','Friday']
        valuses=[1,21231,222,10,123]
        plt.plot(Dayss,valuses)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas4.draw()
        self.ui.txt_WarehouseExpense.setText("1234")

        self.ui.horizontalLayout_104=QtWidgets.QHBoxLayout(self.ui.frame_31)
        self.ui.horizontalLayout_104.setObjectName("horizontalLayout_103")
        self.ui.figure5=plt.figure()
        self.ui.canvas5=FigureCanvas(self.ui.figure5)
        self.ui.horizontalLayout_104.addWidget(self.ui.canvas5)

        Dayss=['Monday','Tuesday','Wednesday','Thursday','Friday']
        valuses=[1,0,222,10,123]
        plt.plot(Dayss,valuses)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas5.draw()
        self.ui.txt_WarehouseExpense.setText("1234")

        self.ui.horizontalLayout_105=QtWidgets.QHBoxLayout(self.ui.frame_32)
        self.ui.horizontalLayout_105.setObjectName("horizontalLayout_103")
        self.ui.figure6=plt.figure()
        self.ui.canvas6=FigureCanvas(self.ui.figure6)
        self.ui.horizontalLayout_105.addWidget(self.ui.canvas6)

        Dayss=['Monday','Tuesday','Wednesday','Thursday','Friday']
        valuses=[1,0,222,10,123]
        plt.plot(Dayss,valuses)
        plt.xlabel('Weak Dayz')
        plt.ylabel('Values')
        plt.title("Profit")
        self.ui.canvas6.draw()
        self.ui.txt_WarehouseExpense.setText("1234")
        
        #self.ui.figure2.clear()
        #self.ui.figure3.clear()

    def OpenAddVehicleManager(self):
        self.ui.mainBody.setCurrentIndex(1)
        self.loadVehicle_tableWidget()   
    def OpenCheckattendance(self) :
        self.ui.mainBody.setCurrentIndex(5)  
        self.loadAttendance_tableWidget()  
    def OpenUpdateEmployee(self ):
        self.ui.mainBody.setCurrentIndex(2) 
        self.loadUpdate_tableWidget()   
    def OpenUpdateEmployeeManager(self ,n):
        self.ui.mainBody.setCurrentIndex(n)
    def OpenDashboardManager(self):
        self.ui.mainBody.setCurrentIndex(0)
    def ShowToUpdateEmployee(self):
        self.ui.mainBody.setCurrentIndex(3)
        self.EditToUpdate_employee(self.updateEmpObj)
    def SpecificldReturnUI(self,n):
        self.ui.mainBody.setCurrentIndex(n)
        
    def OpenAddEmployee(self):
        self.ui.mainBody.setCurrentIndex(4)
    
    def slideLeftMenu(self):
        width=self.ui.LeftMenu.width()
        if(width==0):
            newWidth=220
            #self.ui.menuBtn_2.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/chevron-left.svg"))
        else:
            newWidth=0
            #self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/align-left.svg"))
        self.animation = QPropertyAnimation(self.ui.LeftMenu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def SlideRightMenu(self):
        width=self.ui.profileCont.width()
        if(width==0):
            newWidth=105
        else:
            newWidth=0
        self.animation = QPropertyAnimation(self.ui.profileCont, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()
    def generate_password (self,n,a) :
        start = 10**(n-1)
        end = (10**n)-1
        code = randint(start,end)
        a.setText(str(code))
    def generate_userID(self) :
        userID=0
        for bucket in self.userDL.getHashTable():
            for user in bucket:
                if(user!=None):
                    userID +=1
        self.Employee_userID=userID+1 
        self.ui.txt_GenerateId.setText(str(self.Employee_userID))
                  
                    
    def clear_screen (self) :
        self.ui.txt_Name.clear()
        self.ui.txt_Name.clear()
        self.ui.txt_Age.clear()
        self.ui.txt_Cnic.clear()
        self.ui.txt_Email.clear()
        self.ui.txt_PhoneNumber.clear()
        self.ui.txt_BankAccount.clear()
        self.ui.spinBox_Salary.clear()
        self.ui.txt_Passsword.clear()
    def validate_date (self,name) :
        date_format = '%Y-%m-%d'
        try: 
            birth_date = datetime.datetime.strptime(name, date_format)
            return True
        except:
            QMessageBox.warning(self , "Error","Invalid format of Date")
            return False
    def validate_email(self,email) :
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex,email)):
            return True
        else:
            QMessageBox.warning(self,"Error","Invalid format of email")
            return False
    def validate_number (self,number,n):
        if re.search("([189])[\d]+", number) and len(number) == n :
            return True
        else :
            QMessageBox.warning(self,"Error","Invalid format of Number")
            return False
    def Add_Employee(self):
        flag = False
        Employee_Name =self.ui.txt_Name.text()
        if (Employee_Name != "") :
            if Employee_Name.isalpha() :
                flag = True
            else :
                QMessageBox.warning(self , "Error","Invalid format of Name")
                flag = False
        else :
                QMessageBox.warning(self , "Error","Name cannot be empty")
                flag = False
        Employee_username = self.ui.txt_Name.text()
        Employee_Age =self.ui.txt_Age.text() #Employee birth date
        if (Employee_Age != "") :
            flag = self.validate_date(Employee_Age)
            
        else:
            QMessageBox.warning(self , "Error","Date cannot be empty")
            flag = False
        Employee_CNIC =self.ui.txt_Cnic.text()
        if (Employee_CNIC != "") :
            pass
        else:
            QMessageBox.warning(self , "Error","CNIC cannot be empty")
            flag = False
        Employee_Email =self.ui.txt_Email.text()
        if (Employee_Email != ""):
            flag = self.validate_email(Employee_Email)
            
        else :
            QMessageBox.warning(self , "Error","Email cannot be empty")
            flag = False
        Employee_PhoneNo =self.ui.txt_PhoneNumber.text()
        if (Employee_PhoneNo != ""):
            flag = self.validate_number(Employee_PhoneNo , 11)
        else:
            QMessageBox.warning(self , "Error","Phone Number cannot be empty")
            flag = False
        Employee_BankAccount =self.ui.txt_BankAccount.text()
        if (Employee_BankAccount != ""):
            flag = self.validate_number(Employee_BankAccount,12)
            
        else:
            QMessageBox.warning(self,"Error","Invalid format of Bank Account")
            flag = False
        Employee_Status =self.ui.cmb_Employee.currentIndex()+1
        Employee_Salary =self.ui.spinBox_Salary.text()
        if (Employee_Salary != ""):
            if (Employee_Salary.isdigit() and int(Employee_Salary) > 5000):
                flag= True
            else:
                QMessageBox.warning(self,"Error","Invalid format of Salary")
                flag = False
        else:
            QMessageBox.warning(self,"Error","Salary cannot be empty")
        Employee_password = self.ui.txt_Passsword.text()
        Employee_createDate = date.today()
        Employee_updateDate = date.today()
        if (flag == True):
            my_user = (self.Employee_userID ,Employee_username,Employee_password,Employee_Status,Employee_Name,Employee_Age,Employee_PhoneNo,Employee_Email,Employee_CNIC,Employee_BankAccount,Employee_createDate , Employee_updateDate)
            if(Employee_Status==1):
                inventory_supervisor = InventorySupervisor.InventorySupervisor(my_user,Employee_Salary,Employee_createDate)
                self.userDL.setUser(Employee_username,inventory_supervisor)
                QMessageBox.information(self,"ADDED" ,"Employee Added")
                self.clear_screen()
            if(Employee_Status==3):
                rider = Rider.Rider(my_user,Employee_Salary)
                self.userDL.setUser(Employee_username,rider)
                QMessageBox.information(self,"ADDED" ,"Employee Added")
                self.clear_screen()
            if(Employee_Status==2):
                sales_agent = SaleAgent.SaleAgent(my_user,Employee_Salary,Employee_createDate)
                self.userDL.setUser(Employee_username,sales_agent)
                QMessageBox.information(self,"ADDED" ,"Employee Added")
                self.clear_screen()
    def EditToUpdate_employee (self, employee) :
        self.ui.txt_Name_2.setText(employee.name) 
        self.ui.txt_CNIC.setText(str(employee.CNIC))
        self.ui.txt_Age_2.setText(str(employee.age))
        self.ui.txt_Email_2.setText(employee.Email)
        self.ui.txt_PhonoNumber.setText(str(employee.contactNum))
        self.ui.txt_BankAccount_2.setText(str(employee.BankAccount))
        self.ui.lineEdit_7.setText(str(employee.getSalary())) 
    def update_employee (self,employee) :
        flag = False
        employee.name = self.ui.txt_Name_2.text() 
        if (employee.name != "") :
            if employee.name.isalpha() :
                flag = True
            else :
                QMessageBox.warning(self , "Error","Invalid format of Name")
                flag = False
        else :
                QMessageBox.warning(self , "Error","Name cannot be empty")
                flag = False
        employee.CNIC = self.ui.txt_CNIC.text()
        employee.age = self.ui.txt_Age_2.text()
        if (employee.age != "") :
            flag = self.validate_date(employee.age)
            
        else:
            QMessageBox.warning(self , "Error","Date cannot be empty")
            flag = False
        employee.Email = self.ui.txt_Email_2.text()
        if (employee.Email != ""):
            flag = self.validate_email(employee.Email)
            
        else :
            QMessageBox.warning(self , "Error","Email cannot be empty")
            flag = False
        employee.contactNum = self.ui.txt_PhonoNumber.text()
        if (employee.contactNum != ""):
            flag = self.validate_number(employee.contactNum , 11)
        else:
            QMessageBox.warning(self , "Error","Phone Number cannot be empty")
            flag = False
        employee.BankAccount = self.ui.txt_BankAccount_2.text()
        if (employee.BankAccount != ""):
            flag = self.validate_number(employee.BankAccount,12)
        else:
            QMessageBox.warning(self,"Error","Invalid format of Bank Account")
            flag = False
        employee.setSalary(self.ui.lineEdit_7.text())
        if (employee.getSalary() != ""):
            if (employee.getSalary().isdigit() and int(employee.getSalary()) > 5000):
                flag = True
            else:
                QMessageBox.warning(self,"Error","Invalid format of Salary")
                flag = False
        if (flag == True) :
            employee.updatedDate = date.today()
            self.OpenUpdateEmployee()
    
    def deleteEmployee(self,employee):
        self.userDL.deleteUser(employee.getUsername(),employee)
        self.OpenUpdateEmployee()
    def loadUpdate_tableWidget(self):
        self.ui.btn_UpdateDetails.setEnabled(0)
        self.ui.btn_Delete.setEnabled(0)
        self.ui.Update_tableWidget.clear()
        hashtable=self.userDL.getHashTable()
        row=0
        userRole=""
        for bucket in hashtable:
            for user in bucket:
                if(user!=None and user[1].userRole!=0):
                    self.ui.Update_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[1].userId)))
                    self.ui.Update_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1].name))
                    self.ui.Update_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[1].CNIC))
                    if(user[1].userRole==1):
                        userRole="Inventory Supervisor"
                    elif(user[1].userRole==2):
                        userRole="Sales Agent"
                    elif(user[1].userRole==3):
                        userRole="Rider"
                    self.ui.Update_tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(userRole))
                    self.ui.Update_tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(user[1].contactNum))
                    self.ui.Update_tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(user[1].age)))
                    self.ui.Update_tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[1].Email))
                    self.ui.Update_tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(user[1].userName))
                    row=row+1
                    
    def loadVehicle_tableWidget(self):
        self.ui.btn_Edit.setEnabled(0)
        self.ui.btn_Delete_2.setEnabled(0)
        DLinkList=self.vehicleDL.getList()
        self.ui.tableWidget_3.clearSpans()
        row=0
        for data in DLinkList:
            self.ui.tableWidget_3.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data.model)))
            self.ui.tableWidget_3.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data.number)))
            self.ui.tableWidget_3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data.fuelAverage)))
            row=row+1
    def loadAttendance_tableWidget(self) :
        listt = self.AttendanceDL.getAttendancelist()
        self.ui.table_CheckAttendance.setColumnCount(31)
        import pandas as pd
        import datetime
        t=date.today()
        base = pd.to_datetime(str(t))
        date_list = [datetime.datetime.strftime(pd.to_datetime(base + datetime.timedelta(days=x)),"%Y-%m-%d") for x in range(31)]
        date_list.insert(0,"Employee")
        self.ui.table_CheckAttendance.setHorizontalHeaderLabels(date_list)
        self.ui.table_CheckAttendance.setRowCount(len(listt))
        row = 0
        column = 1
        for data in listt:
            self.ui.table_CheckAttendance.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data.getname())))
            for i in data.getAttendenceList():
                print(i)
                #for j in range(1, len(date_list)-1):
                if (date_list[column] == i) :
                    self.ui.table_CheckAttendance.setItem(row, column, QtWidgets.QTableWidgetItem("P"))
                elif ():
                    self.ui.table_CheckAttendance.setItem(row, column, QtWidgets.QTableWidgetItem("A"))
                column = column + 1
            column = 1
            row = row+1
    def addVehicle(self):
        model=self.ui.txt_VehicleModel.text()
        number=self.ui.txt_VehicleNumber.text()
        fuelAverage=self.ui.txt_FuelAverage.text()
        if(model!="" and model!="" and model!=""):
            self.ui.txt_VehicleModel.clear()
            self.ui.txt_VehicleNumber.clear()
            self.ui.txt_FuelAverage.clear()
            vehicle=Vehicle.Vehicle(model,number,fuelAverage)
            self.vehicleDL.addToList(vehicle)
            self.loadVehicle_tableWidget()
    #def pay_salary (self) :
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=ManaMainWindow()
    window.show()
    sys.exit(app.exec_())