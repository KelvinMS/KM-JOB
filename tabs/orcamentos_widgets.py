import customtkinter as ctk
from tkinter import ttk, messagebox



class OrcamentosWidgets(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frames = {}
        self.checkbox_vars = []
        self.entry_carinfo_vars = []
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame_action_buttons_orcamento()
        #self.frame_vehicle_data_entrys()


    # Criar a seção de botões de ação para o orçamento
    def frame_action_buttons_orcamento(self):
        self.frames["frame_botoes_acao_orcamentos"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_botoes_acao_orcamentos"].grid(row=0, column=0, padx=5, pady=5, sticky="new")

        botoes = [
            ("Criar Orçamento",self.criar_orcamento),
            ("Consultar Orçamento",self.forget_specific_frames),
            ("Editar Orçamento",lambda: print("Editar Orçamento Clicked")),
            ("Excluir Orçamento",lambda: print("Excluir Orçamento Clicked")),
            
        ]

        for i, (texto,funcao) in enumerate(botoes):
            ctk.CTkButton(master=self.frames["frame_botoes_acao_orcamentos"], text=texto, width=120, anchor='w',command=funcao)\
                .grid(row=i, column=0, padx=5, pady=5, sticky="ew")


    # Criar a seção de entradas para o orçamento
    def frame_vehicle_data_entrys(self):

        cliente_data_entrys = [

            ("Nome do Veículo", "entry_nome_veiculo"),
            ("Fabricante", "entry_fabricante_veiculo"),
            ("Cor do Veículo", "entry_cor_veiculo"),
            ("Placa do Veículo", "entry_placa"),
            ("Ano do Veículo", "entry_ano")
        ]
        self.frames["frame_vehicle_data_entrys"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_vehicle_data_entrys"].grid(row=0, column=1, padx=5, pady=5, sticky="nwe")
        lbl_info_veiculo = ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text="Informações do Veículo", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_veiculo.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_veiculo.rowconfigure(0, weight=1)

        # Adiciona os labels e entries para cada item na lista cliente_data_entrys
        for i, (label_text, _) in enumerate(cliente_data_entrys):
            var = ctk.StringVar() # Controla se está marcado (1) ou não (0)
            ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text=label_text + ":")\
                .grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(master=self.frames["frame_vehicle_data_entrys"], width=200, placeholder_text=label_text,textvariable=var)
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")
            self.entry_carinfo_vars.append(var)


        self.widget_car_parts_data_entrys()

        # Última linha para textbox de descrição
        ultima_linha = self.get_last_row(self.frames["frame_vehicle_data_entrys"])
        ctk.CTkLabel(master=self.frames["frame_vehicle_data_entrys"], text="Descrição:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="nw")
        descricao = ctk.CTkTextbox(master=self.frames["frame_vehicle_data_entrys"], width=200, height=100)
        descricao.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")


    def widget_car_parts_data_entrys(self):
        # Adiciona os labels e entries para cada item na lista cliente_data_entrys
        car_parts = [
            "Parachoque Dianteiro",
            "Parachoque Trasero",
            "Paralama Dianteiro Direito",
            "Paralama Dianteiro Esquerdo",
            "Paralama Trasero Direito",
            "Paralama Trasero Esquerdo",
            "Capô",
            "Porta Dianteira Direita",
            "Porta Dianteira Esquerda",
            "Porta Trasera Direita",
            "Porta Trasera Esquerda",
            "Teto"
        ]

        ultima_linha = self.get_last_row(self.frames["frame_vehicle_data_entrys"])
        self.frames['frame_choose_body_part'] = ctk.CTkFrame(self.frames["frame_vehicle_data_entrys"], width=300, height=300, fg_color="transparent")
        self.frames['frame_choose_body_part'].grid(row=ultima_linha, column=0, sticky="new",columnspan=2)
        self.frames['frame_choose_body_part'].grid_rowconfigure(0, weight=1)

        ctk.CTkLabel(master=self.frames['frame_choose_body_part'] , text="Selecionar Peças para Orçamento", font=("Arial", 16),text_color="DimGrey",anchor="center")\
            .grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="new")
        
        for i, label_text in enumerate(car_parts,start=1):
            linha = ((i - 1) % 6) + 1   
            coluna = (i - 1) // 6
            var = ctk.IntVar()  # Controla se está marcado (1) ou não (0)
            chk = ctk.CTkCheckBox(self.frames['frame_choose_body_part'], text=label_text, variable=var)
            chk.grid(row=linha, column=coluna, sticky="w", padx=10, pady=5)
            self.checkbox_vars.append(var)



    # Criar a seção de entradas para o orçamento
    def frame_client_data_entrys(self):
        #Nova implementação
        self.frames["frame_client_data_entrys"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_client_data_entrys"].grid(row=0, column=2, padx=5, pady=5, sticky="nwe")
        self.widget_existent_client_data_entrys()



    # Criar a seção de entradas para o orçamento
    def widget_existent_client_data_entrys(self):
        lbl_info_driver = ctk.CTkLabel(master=self.frames["frame_client_data_entrys"], text="Responsável Financeiro", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_driver.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_driver.rowconfigure(0, weight=1)
        
        # Adiciona os Comboboxes para selecionar um cliente existente
        clientes = ["Cliente 1", "Cliente 2", "Cliente 3"]
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entrys"])
        ctk.CTkLabel(master=self.frames["frame_client_data_entrys"], text="Selecionar Cliente:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="e")
        self.combo_clientes = ctk.CTkComboBox(master=self.frames["frame_client_data_entrys"], values=clientes, width=200)
        self.combo_clientes.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")
        self.combo_clientes.set("Selecione um cliente") 

        # Checkbox para novo cliente
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entrys"])

        self.novo_cliente_var = ctk.BooleanVar(value=False)
        self.checkbox_novo_cliente = ctk.CTkCheckBox(self.frames["frame_client_data_entrys"], text="Cadastrar novo cliente", variable=self.novo_cliente_var,command=self.widgets_new_client_data_entrys)
        self.checkbox_novo_cliente.grid(row=ultima_linha, column=0, padx=10, pady=5)

        # divider entre os widgets
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entrys"])
        divider = ctk.CTkFrame(self.frames["frame_client_data_entrys"], height=2, fg_color="DarkSlateGray")
        divider.grid(row=ultima_linha, column=0, sticky="ew", pady=5,padx=(5,5),columnspan=2)

    # Criar a seção de entradas para o orçamento
    def widgets_new_client_data_entrys(self):
        
        if not self.novo_cliente_var.get():
            print("Novo Cliente Não Selecionado")
            if "frame_add_new_client" in self.frames:
                self.frames["frame_add_new_client"].destroy()               
        else:
            print("Novo Cliente Selecionado")
            cliente_data_entrys = [
                ("Nome do Responsável", "entry_responsable"),
                ("CPF", "entry_cpf"),
                ("Telefone", "entry_phone"),
                ("Email", "entry_email")
            ]
            ultima_linha = self.get_last_row(self.frames["frame_client_data_entrys"])
            self.frames['frame_add_new_client'] = ctk.CTkFrame(self.frames["frame_client_data_entrys"], width=300, height=300, fg_color="transparent")
            self.frames['frame_add_new_client'].grid(row=ultima_linha, column=0, sticky="new",columnspan=2)
            
            self.frames['frame_add_new_client'].grid_rowconfigure(0, weight=1)
            ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text="Cadastrar Novo Cliente", font=("Arial", 16),text_color="DimGrey",anchor="center")\
                .grid(row=0, column=0, padx=10, pady=5, columnspan=2)

            for i, (label_text, _) in enumerate(cliente_data_entrys):
                ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text=label_text + ":")\
                    .grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
                entry = ctk.CTkEntry(master=self.frames['frame_add_new_client'] , width=200, placeholder_text=label_text)
                entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")

            # Última linha para textbox de descrição
            ultima_linha = self.get_last_row(self.frames["frame_client_data_entrys"])
            ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text="Descrição:")\
                .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="ne")
            descricao = ctk.CTkTextbox(master=self.frames['frame_add_new_client'] , width=200, height=100)
            descricao.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")

    # Método para obter a última linha ocupada em um frame
    def get_last_row(self,master):
        widgets = master.grid_slaves()
        if not widgets:
            return 0
        return max(widget.grid_info()['row'] for widget in widgets) + 1

    # Método para criar um orçamento
    def criar_orcamento(self):
        # Implementar a lógica para criar um orçamento
        self.frame_vehicle_data_entrys()
        self.frame_client_data_entrys()

    # Método para consultar um orçamento
    def consultar_orcamentos(self):
        # Implementar a lógica para criar um orçamento
        self.frames["frame_entrys_orcamentos"].forget()
        pass

    # Método para pegar os frames
    def get_frames(self):
        return self.frames

    # Método para esquecer os frames específicos
    def forget_specific_frames(self):
        print("Esquecendo frames específicos")
        self.frames["frame_vehicle_data_entrys"].destroy()
        self.frames["frame_client_data_entrys"].destroy()
        
        super().forget()