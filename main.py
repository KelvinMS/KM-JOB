import customtkinter as ctk
from pprint import pprint
from tkinter import ttk, messagebox
from tabs.orcamentos_widgets import OrcamentosWidgets




class NotebookTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
        
        # create tabs
        self.add("Orçamento")
        self.add("Clientes")
        self.add("Relatórios")
        self.add("Materiais")
        self.add("Registros Freelancer")
        self.set("Orçamento")  # set currently visible tab




class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.frames = {}
        self.mainPage()
        self.createWidgets()
        self.mainloop()

        
    #Creates the main page of the application and notebook tabs
    def mainPage(self):
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.title('KMJob - Management System')
        self.iconbitmap('images\\icon.ico')
        self.configure(background='RoyalBlue4')
        self.geometry('1200x820')
        self.resizable(True,True)
        self.minsize(width=1200,height=720)




    def createWidgets(self):
        
        self.tab_view = NotebookTabView(master=self, corner_radius=10,command=self.on_tab_change)
        self.tab_view.grid(row=0, column=0, padx=5, pady=15,sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        # Create the tabs and their widgets
        self.widgets_orcamento = OrcamentosWidgets(master=self.tab_view.tab("Orçamento"))
        self.widgets_orcamento.grid(row=0, column=0, sticky="nsew")
        self.widgets_orcamento.columnconfigure(0, weight=1)
        self.widgets_orcamento.columnconfigure(1, weight=1)
        self.widgets_orcamento.columnconfigure(2, weight=1)
        #self.treeView_table = ttk.Treeview(self, height=1,columns=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10'),show='headings')



        #createWidgetsClientes()
        # self.createWidgetsRelatorios()
        # self.createWidgetsMateriais()
        # self.createWidgetsRegistrosFreelancer()



    def on_tab_change(self):
        print(f"\n\nTab changed to: {self.tab_view.get()}")
        self.frames = self.widgets_orcamento.get_frames()

        pprint(f"\nFrames: {self.widgets_orcamento.get_frames()}")
        if self.tab_view.get() == "Orçamento":
            print("Orcamentos tab selected")
            if "frame_vehicle_data_entrys" in self.frames:
                print("Frame das Entrys do Orcamentos Existe")
                self.frames["frame_vehicle_data_entrys"].destroy()
                self.frames["frame_client_data_entrys"].destroy()



if __name__ == "__main__":
    Application()
