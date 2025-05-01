import customtkinter as ctk
from tkinter import ttk, messagebox


class OrcamentosWidgets(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frames = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.FrameOrcamentoButtons()
        #self.frame_vehicle_data_entrys()


    # Criar a seção de botões de ação para o orçamento
    def FrameOrcamentoButtons(self):
        self.frames["frame_botoes_acao_orcamentos"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_botoes_acao_orcamentos"].grid(row=0, column=0, padx=5, pady=5, sticky="new")
        print('FrameOrcamentoButton FUNCTION: ',self.frames["frame_botoes_acao_orcamentos"])

        botoes = [
            ("Criar Orçamento",self.criar_orcamento),
            ("Consultar Orçamento", lambda: print("Consultar Orçamento Clicked")),
            ("Editar Orçamento",lambda: print("Editar Orçamento Clicked")),
            ("Excluir Orçamento",lambda: print("Excluir Orçamento Clicked")),
            
        ]

        for i, (texto,funcao) in enumerate(botoes):
            ctk.CTkButton(master=self.frames["frame_botoes_acao_orcamentos"], text=texto, width=120, anchor='w',command=funcao)\
                .grid(row=i, column=0, padx=5, pady=5, sticky="ew")


    # Criar a seção de entradas para o orçamento
    def frame_vehicle_data_entrys(self):
        self.frames["frame_vehicle_data_entrys"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_vehicle_data_entrys"].grid(row=0, column=1, padx=5, pady=5, sticky="nwe")
        #self.frames["frame_vehicle_data_entrys"].grid_columnconfigure(1, weight=1)


        cliente_data_entrys = [

            ("Nome do Veículo", "entry_nome_veiculo"),
            ("Fabricante", "entry_fabricante_veiculo"),
            ("Cor do Veículo", "entry_cor_veiculo"),
            ("Placa do Veículo", "entry_placa"),
            ("Ano do Veículo", "entry_ano")
        ]

        lbl_info_veiculo = ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text="Informações do Veículo", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_veiculo.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_veiculo.rowconfigure(0, weight=1)
        # Adiciona os labels e entries para cada item na lista cliente_data_entrys
        for i, (label_text, _) in enumerate(cliente_data_entrys):
            ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text=label_text + ":")\
                .grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(master=self.frames["frame_vehicle_data_entrys"], width=200, placeholder_text=label_text)
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")

        # Última linha para textbox de descrição
        ultima_linha = self.get_ultima_linha(self.frames["frame_vehicle_data_entrys"])
        ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text="Descrição:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="ne")
        descricao = ctk.CTkTextbox(master=self.frames["frame_vehicle_data_entrys"], width=200, height=100)
        descricao.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")




    # Criar a seção de entradas para o orçamento
    def frame_client_data_entrys(self):
        #Nova implementação
        self.frames["frame_client_data_entrys"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_client_data_entrys"].grid(row=0, column=1, padx=5, pady=5, sticky="nwe")
        #self.frames["frame_entrys_orcamentos"].grid_columnconfigure(1, weight=1)


        cliente_data_entrys = [

            ("Nome do Veículo", "entry_nome_veiculo"),
            ("Fabricante", "entry_fabricante_veiculo"),
            ("Cor do Veículo", "entry_cor_veiculo"),
            ("Placa do Veículo", "entry_placa"),
            ("Ano do Veículo", "entry_ano")
        ]

        lbl_info_veiculo = ctk.CTkLabel(master=self.frames["frame_client_data_entrys"], text="Informações do Veículo", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_veiculo.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_veiculo.rowconfigure(0, weight=1)
        # Adiciona os labels e entries para cada item na lista cliente_data_entrys
        for i, (label_text, _) in enumerate(cliente_data_entrys):
            ctk.CTkLabel(master=self.frames["frame_client_data_entrys"], text=label_text + ":")\
                .grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(master=self.frames["frame_client_data_entrys"], width=200, placeholder_text=label_text)
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")

        # Última linha para textbox de descrição
        ultima_linha = self.get_ultima_linha(self.frames["frame_client_data_entrys"])
        ctk.CTkLabel(master=self.frames["frame_client_data_entrys"], text="Descrição:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="ne")
        descricao = ctk.CTkTextbox(master=self.frames["frame_client_data_entrys"], width=200, height=100)
        descricao.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")






    def get_ultima_linha(self,master):
        widgets = master.grid_slaves()
        if not widgets:
            return 0
        return max(widget.grid_info()['row'] for widget in widgets) + 1

    def criar_orcamento(self):
        # Implementar a lógica para criar um orçamento
        self.frame_vehicle_data_entrys()
        pass

    def consultar_orcamentos(self):
        # Implementar a lógica para criar um orçamento
        print("Consultar Orçamento Clicked")
        self.frames["frame_entrys_orcamentos"].forget()
        pass

    def get_frames(self):
        return self.frames
