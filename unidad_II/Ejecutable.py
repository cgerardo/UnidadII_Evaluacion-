import sys
from base import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
            
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        
        self.create_DB()
        self.ui.btnVer.clicked.connect(self.print_data)
        self.model = None
        self.ui.btnVer.clicked.connect(self.sql_tableview_model)
        self.ui.btnAgregar.clicked.connect(self.sql_add_row)
        self.ui.btnEliminar.clicked.connect(self.sql_delete_row)
        
        
        #-------------------------- 
       # self.init_tabs()
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tblPlantillas.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Plantilla.db')
        
        tableview = self.ui.tblPlantillas
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('Plantilla')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Cod_Plantilla")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Clasificacion")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Intencion")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "También conocido como")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Motivación")        
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Aplicabilidad")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Estructura")                          
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Participantes")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Colaboraciones")
    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'Plantilla.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'Plantilla' ORDER BY Cod_Plantilla")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Plantilla.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table Plantilla(Cod_Plantilla int primary key, "
                    "Nombre varchar(20),Clasificacion varchar(20),Intencion varchar(20),También conocido como varchar(20),Motivación varchar(20), Aplicabilidad varchar(20),Estructura varchar(20),Participantes int, Colaboraciones varchar(20))")
        query.exec_("insert into Plantilla values('1','1','1','25','2','50','21/Enero/2019','1',1,'fad')")

if __name__ == "__main__":
    MainWindow_EXEC()
