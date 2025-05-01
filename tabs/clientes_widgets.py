import customtkinter as ctk


class FrameOrcamentoButtons(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)



def createWidgetsOrcamentos(self):
    # Create a frame for the tab view
    Framedosbotoes =FrameOrcamentoButtons(master=self, width=300, height=300,fg_color="gray22")
    Framedosbotoes.grid(row=0, column=0, padx=5, pady=5,  sticky="nsew")

    #criando botões dinamicamente
    botoes = [
        "Criar Orçamento",
        "Consultar Orçamento",
        "Editar Orçamento"
    ]

    for i, texto in enumerate(botoes):
        ctk.CTkButton(master=Framedosbotoes, text=texto, width=120, anchor='w')\
            .grid(row=i, column=0, padx=5, pady=5, sticky="ew")


def 