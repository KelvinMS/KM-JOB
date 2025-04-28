import customtkinter as ctk



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





Application()
