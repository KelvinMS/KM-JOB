import customtkinter as ctk


# class VehiclesFunctions():

#     # Get entry values from frame
#     def entryCarVariables(self):
#         self.cod = self.entry_cod.get()   
#         self.marca = self.entry_marca.get()
#         self.modelo = self.entry_modelo.get().upper()
#         self.placa = self.entry_placa.get().upper()
#         self.combustivel = self.entry_combustivel.get()   
#         self.quilometragem = self.entry_quilometragem.get()
#         self.ano = self.entry_ano.get()
#         self.data_ulti_revisao = self.calendar.get_date()
#         if not self.marca or not self.modelo or not self.placa or not self.ano:
#            return False
        
#     #Clean form Entrys
#     def cleanFormCarEntry(self):
#         self.entry_cod.delete(0,END)
#         self.entry_marca.delete(0,END)
#         self.entry_modelo.delete(0,END)
#         self.entry_placa.delete(0,END)
#         self.entry_quilometragem.delete(0,END)
#         self.entry_ano.delete(0,END)
#         self.entry_combustivel.delete(0,END)
#         self.lbl_lastRevision_date.config(text="")
        

#     #Add vehicle to db and update treeview
#     def addVehiclesDB(self):       
#             result = self.entryCarVariables()
#             if result == False:
#                 messagebox.showerror("Erro", "Preencha todos os campos necessários para adicionar veículo!")
#                 return
#             vehicle_data.VehicleDataFuntionsDB.addVehiclesDB(self,self.marca,self.modelo,self.placa,self.quilometragem,self.ano,self.combustivel,self.data_ulti_revisao,self.motorista_associado)
#             self.updateVehiclesInTreeView()
#             messagebox.showinfo("Sucesso", "Veículo adicionado com sucesso!")
    
#     #Delete vehicle to db and update treeview
#     def deleteVehicleDB(self):
#         result = self.entryCarVariables()
#         if result==False and not self.cod:
#             messagebox.showerror("Erro", "Preencha o código do veículo!")
#             return
#         vehicle_data.VehicleDataFuntionsDB.deleteVehicleDB(self,self.cod)
#         self.cleanFormCarEntry()
#         self.updateVehiclesInTreeView()
#         messagebox.showinfo("Sucesso", "Veículo removido com sucesso!")
  
#     #Update vehicle into db and update treeview
#     def updateVehicleDB(self):
#         result = self.entryCarVariables()
#         if result==False and not self.cod:
#             messagebox.showerror("Erro", "Preencha o código do veículo!")
#             return
#         vehicle_data.VehicleDataFuntionsDB.updateVehicleDB(self,self.marca,self.modelo,self.placa,self.quilometragem,self.ano,self.combustivel,self.data_ulti_revisao,self.motorista_associado,self.cod)
#         self.cleanFormCarEntry()
#         self.updateVehiclesInTreeView()
#         messagebox.showinfo("Sucesso", "Informações do Veículo alteradas com sucesso!")

#     #Update treeview with all vehicles from db
#     def updateVehiclesInTreeView(self):
#         self.treeView_table.delete(*self.treeView_table.get_children())
#         cursorList = vehicle_data.VehicleDataFuntionsDB.getVehiclesDB(self)
#         for i in cursorList:
#             self.treeView_table.insert("",END, values=i)
#         self.cleanFormCarEntry()
    
    
#     def updateDriversInTreeView(self):
#         self.treeView_table.delete(*self.treeView_table.get_children())
#         cursorList = drivers_data.DriverDataFuntionsDB.getDriversDB(self)
#         for i in cursorList:
#             self.treeView_table.insert("",END, values=i)
#         self.cleanFormDriverEntry()

#     #Search vehicle in db and update treeview
#     def searchVehicle(self):
#         self.treeView_table.delete(*self.treeView_table.get_children())
#         self.entry_marca.insert(END,'%') 
#         marca = self.entry_marca.get()
#         cursorList = vehicle_data.VehicleDataFuntionsDB.searchVehicleDB(self,marca)
#         for i in cursorList:
#             self.treeView_table.insert("",END, values=i)
#         self.cleanFormCarEntry()
    
#     #Load the values of treeview selection on Entrys
#     def onDoubleClickVehicleTreeView(self,event):
#         self.cleanFormCarEntry()
#         self.treeView_table.selection()
#         for entry in self.treeView_table.selection():
#             col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = self.treeView_table.item(entry,'values')
#             self.entry_cod.insert(END,col1)
#             self.entry_marca.insert(END,col2)
#             self.entry_modelo.insert(END,col3)
#             self.entry_placa.insert(END,col4)
#             self.entry_quilometragem.insert(END,col5)
#             self.entry_ano.insert(END,col6)
#             self.entry_combustivel.insert(END,col7)
#             self.lbl_lastRevision_date.config(text="Data da última revisão: "+col9)
#         #if col10 != '':
            

#     #Load the values of treeview selection on Entrys
#     def onDoubleClickDriverTreeView(self,event):
#         self.cleanFormDriverEntry()
#         self.treeView_table.selection()
#         for entry in self.treeView_table.selection():
#             col1,col2,col3,col4,col5,col6,col7 = self.treeView_table.item(entry,'values')
#             self.entry_cod_driver.insert(END,col1)
#             self.entry_name_driver.insert(END,col2)
#             self.entry_cpf_driver.insert(END,col3)
#             self.entry_cnh_driver.insert(END,col4)
#             self.entry_email_driver.insert(END,col5)
#             self.entry_phone_driver.insert(END,col6)
#             self.label_attachment.config(text=col7)
                        
#     #Action on tab change
#     def onTabChange(self,event):
#         tab = event.widget.tab('current')['text']
#         if tab == 'Veículos':	
#             self.treeView_table.delete(*self.treeView_table.get_children())
#             self.createTreeViewDataVehicles()
#             self.updateVehiclesInTreeView()
#         elif tab == 'Motoristas':
#             self.treeView_table.delete(*self.treeView_table.get_children())
#             self.createTreeViewDataDrivers()
#             self.updateDriversInTreeView()

#     # Open Calaendar and bind the event to select a date
#     def abrir_calendario(self):
#         self.calendar.place(relx=0.5, rely=0.5, anchor='center')
#         self.calendar.bind("<<CalendarSelected>>", self.selecionar_data)        
    
#     # Action when selecting a date in the calendar
#     def selecionar_data(self, event):
#         self.data_ulti_revisao = self.calendar.get_date()  # formato: yyyy-mm-dd
#         self.calendar.place_forget()
#         self.lbl_lastRevision_date.config(text="Data da última revisão: "+self.data_ulti_revisao)
#         #self.lbl_lastRevision_date =Label(self.tab_car_data, text="Data da última revisão"+col9).grid(row=7, column=5,sticky="W",padx=5,pady=5)

# class DriversFunctions():

#     # Get entry values from frame
#     def entryDriverVariables(self):
#         self.cod_driver = self.entry_cod_driver.get()   
#         self.name_driver = self.entry_name_driver.get()
#         self.cpf_driver = self.entry_cpf_driver.get().upper()
#         self.cnh_driver = self.entry_cnh_driver.get().upper()
#         self.email_driver = self.entry_email_driver.get()   
#         self.phone_driver = self.entry_phone_driver.get()
#         self.cnh_path = self.label_attachment.cget("text")
        
#         if not self.name_driver or not self.cpf_driver or not self.cnh_driver:
#            return False

#     #Clean form Entrys
#     def cleanFormDriverEntry(self):
#         self.entry_cod_driver.delete(0,END)
#         self.entry_name_driver.delete(0,END)
#         self.entry_cpf_driver.delete(0,END)
#         self.entry_cnh_driver.delete(0,END)
#         self.entry_email_driver.delete(0,END)
#         self.entry_phone_driver.delete(0,END)
#         self.label_attachment.config(text="")

#     #Add vehicle to db and update treeview
#     def addDriverDB(self):       
#             result = self.entryDriverVariables()
#             if result == False:
#                 messagebox.showerror("Erro", "Preencha todos os campos necessários para adicionar Motorista!")
#                 return
#             drivers_data.DriverDataFuntionsDB.addDriveToDB(self,self.name_driver,self.cpf_driver,self.cnh_driver,self.email_driver,self.phone_driver,self.cnh_path)
#             self.updateDriversInTreeView()
#             messagebox.showinfo("Sucesso", "Motorista adicionado com sucesso!")
    
#     #Delete driver to db and update treeview
#     def deleteDriverDB(self):
#         result = self.entryDriverVariables()
#         if result==False and not self.cod_driver:
#             messagebox.showerror("Erro", "Preencha o código do Motorista!")
#             return
#         drivers_data.DriverDataFuntionsDB.deleteDriverToDB(self,self.cod_driver)
#         self.cleanFormDriverEntry()
#         self.updateDriversInTreeView()
#         messagebox.showinfo("Sucesso", "Motorista removido com sucesso!")
  
#     #Update vehicle into db and update treeview
#     def updateDriverDB(self):
#         result = self.entryDriverVariables()
#         if result==False and not self.cod_driver:
#             messagebox.showerror("Erro", "Preencha o código do motorista!")
#             return
#         drivers_data.DriverDataFuntionsDB.updateDriversDB(self,self.name_driver,self.cpf_driver,self.cnh_driver,self.email_driver,self.phone_driver,self.cnh_path,self.cod_driver)
#         self.cleanFormDriverEntry()
#         self.updateDriversInTreeView()
#         messagebox.showinfo("Sucesso", "Informações do Motorista alteradas com sucesso!")

#     #Search vehicle in db and update treeview
#     def searchDriver(self):
#         self.treeView_table.delete(*self.treeView_table.get_children())
#         self.entry_name_driver.insert(END,'%') 
#         name = self.entry_name_driver.get()
#         cursorList = drivers_data.DriverDataFuntionsDB.searchDriverDB(self,name)
#         for i in cursorList:
#             self.treeView_table.insert("",END, values=i)
#         self.cleanFormDriverEntry()
    
#     #Update treeview with all vehicles from db
#     def updateDriversInTreeView(self):
#         self.treeView_table.delete(*self.treeView_table.get_children())
#         cursorList = drivers_data.DriverDataFuntionsDB.getDriversDB(self)
#         for i in cursorList:
#             self.treeView_table.insert("",END, values=i)
#         self.cleanFormDriverEntry()

#     #Attachement logic
#     def saveAttachment(self):
#         self.attachment_path = filedialog.askopenfilename(title='Selecione um arquivo')
#         self.label_attachment.config(text=self.attachment_path)
        
#         return self.attachment

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = ctk.CTkCheckBox(self, text="checkbox 3")
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_4 = ctk.CTkCheckBox(self, text="checkbox 4")
        self.checkbox_4.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_5 = ctk.CTkCheckBox(self, text="checkbox 5")
        self.checkbox_5.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.root = ctk.CTk()
        self.mainPage()
        self.root.mainloop()

        
    def mainPage(self):
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.root.title('KMJob - Management System')
        self.root.iconbitmap('images\\icon.ico')
        self.root.configure(background='RoyalBlue4')
        self.root.geometry('1200x720')
        self.root.resizable(True,True)
        self.root.minsize(width=1200,height=720)

    # def mainPage(self):
    #     ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    #     ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    #     self.root.title('KMJob - Funilaria e Pintura')
    #     self.root.iconbitmap('images\\icon.ico')
    #     self.root.configure(background='RoyalBlue4')
    #     self.root.geometry('1200x720')
    #     self.root.resizable(True,True)
    #     self.root.minsize(width=1200,height=720)

    #     self.checkbox_frame = MyCheckboxFrame(self.root)
    #     self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

    #     self.button = ctk.CTkButton(self.root, text="my button", command=self.button_callback)
    #     self.button.grid(row=7, column=0, padx=10, pady=10, sticky="ew") # como nao tem nada na row 1 ela colapsa e fica na row 1

    def button_callback(self):
        print("button pressed")

Application()
