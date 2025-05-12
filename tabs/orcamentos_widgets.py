import customtkinter as ctk
from tkinter import ttk, messagebox
from tabs.teste import TelaConsultaOrcamentos


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, width=0.2):
        super().__init__(master=parent)
        self.width = width
        self.hidden_pos = -self.width
        self.visible_pos = 0.0
        self.pos = self.hidden_pos
        self.in_start_pos = True  # Está escondido inicialmente
        self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
        #self.configure(fg_color="gray33")

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos < self.visible_pos:
            self.pos += 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.pos = self.visible_pos
            self.in_start_pos = False
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate_backwards(self):
        if self.pos > self.hidden_pos:
            self.pos -= 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.pos = self.hidden_pos
            self.in_start_pos = True
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
                
# Global variable to control the button position

class OrcamentosWidgets(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frames = {}
        self.master = master
        self.checkbox_car_parts_vars = {}
        self.entry_carinfo_vars = {}
        self.entry_novo_cliente_var = {}
        self.entry_payments_var = {}
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_sidebar()
        
        
    def move_btn(self,CtkButton):
        global button_x
        button_x += 0.001
        CtkButton.place(relx = button_x, rely = 0.5, anchor = 'center')
        
        if button_x < 0.9:
            
            self.after(10, self.move_btn)

        # configure 
        # colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
        # color = choice(colors)
        # button.configure(fg_color = color)

    def infinite_print(self):
        global button_x
        button_x += 0.5
        if button_x < 10:
            print('infinite')
            print(button_x)
            self.after(100, self.infinite_print)



    def create_sidebar(self):
        self.animated_panel = SlidePanel(self.master, width=0.1)
        button_x = 0.5
        toggle_button = ctk.CTkButton(self, text = 'Menu', width=300,command = self.animated_panel.animate)
        #toggle_button.place(x=10, y=10)
        toggle_button.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        #self.frames["frame_botoes_acao_orcamentos"] = animated_panel
        self.frame_action_buttons_orcamento(self.animated_panel)
        
        
        

    # Criar a seção de botões de ação para o orçamento
    def frame_action_buttons_orcamento(self,parent):

        self.frames["frame_botoes_acao_orcamentos"] = ctk.CTkFrame(master=parent, fg_color="gray33")
        self.frames["frame_botoes_acao_orcamentos"].grid(row=0, column=0, padx=5, pady=5, sticky="new")
        self.frames["frame_botoes_acao_orcamentos"].grid_columnconfigure(0, weight=1)

        botoes = [
            ("Criar Orçamento",self.create_widgets_orcamento),
            ("Consultar Orçamento",self.create_widgets_consultar_orcamento),
            ("Botao de teste",self.get_all_entrys),
            ("Excluir Orçamento",lambda: print("Excluir Orçamento Clicked")),
            
        ]
        for i, (texto,funcao) in enumerate(botoes):
            button = ctk.CTkButton(master=self.frames["frame_botoes_acao_orcamentos"], text=texto, width=100, anchor='center',command=funcao)
            button.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            


    def create_widgets_consultar_orcamento(self):
        self.animated_panel.animate()
        self.limpar_frames_dinamicos()
        self.btn_salvar_orcamento.destroy()
        self.frames["frame_consult_budgets"] = TelaConsultaOrcamentos(master=self,frames=self.frames)
        self.frames["frame_consult_budgets"].grid(row=0, column=1, sticky="nsew")
        print("Frames existentes Consultar orcamento:", self.frames.keys())

    # Métodos para criar um orçamento
    def create_widgets_orcamento(self):
        #recua o slide panel e limpa os frames dinâmicos
        self.animated_panel.animate()
        self.limpar_frames_dinamicos()
        
        
        # Implementar a lógica para criar um orçamento
        self.frame_vehicle_data_entries()
        self.frame_client_data_entries()
        self.frame_payment_data_entries()
        self.btn_salvar_orcamento = ctk.CTkButton(master=self, text="Salvar Orçamento", width=200,height=50, anchor='center',command=self.get_all_entrys)
        self.btn_salvar_orcamento.grid(row=1, column=1, padx=5, pady=5, sticky="ew",columnspan=3,rowspan=2)
        print("Frames existentes Criar Orçamento:", self.frames.keys())

    # Criar o Frame para as entradas de dados do veículo e chamar o método de widgets
    def frame_vehicle_data_entries(self):
        #self.rowconfigure(1, weight=1)
        #self.columnconfigure(0, weight=1)
        self.frames["frame_vehicle_data_entries"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_vehicle_data_entries"].grid(row=0, column=1, padx=5, pady=5, sticky="nwe")
        self.widgets_vehicle_orcamento()
        

    # Criar os widgets de entradas para os dados do veículo na criação de orçamento
    def widgets_vehicle_orcamento(self):

        vehicle_data_entrys = [

            ("Nome do Veículo", "entry_nome_veiculo"),
            ("Fabricante", "entry_fabricante_veiculo"),
            ("Cor do Veículo", "entry_cor_veiculo"),
            ("Placa do Veículo", "entry_placa"),
            ("Ano do Veículo", "entry_ano")
        ]

        lbl_info_veiculo = ctk.CTkLabel(master=self.frames["frame_vehicle_data_entries"], text="Informações do Veículo", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_veiculo.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_veiculo.rowconfigure(0, weight=1)

        # Adiciona os labels e entries para cada item na lista cliente_data_entrys
        for i, (label_text, entry_name) in enumerate(vehicle_data_entrys):
            var = ctk.StringVar()
            ctk.CTkLabel(master=self.frames["frame_vehicle_data_entries"], text=label_text + ":")\
                .grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(master=self.frames["frame_vehicle_data_entries"], width=200, placeholder_text=label_text,textvariable=var)
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")
            self.entry_carinfo_vars[entry_name] = var
                    
        self.widgets_car_parts_data()

        # Última linha para textbox de descrição
        ultima_linha = self.get_last_row(self.frames["frame_vehicle_data_entries"])
        ctk.CTkLabel(master=self.frames["frame_vehicle_data_entries"], text="Descrição:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="nw")
        self.txtbox_vehicle_descrition = ctk.CTkTextbox(master=self.frames["frame_vehicle_data_entries"], width=200, height=100)
        self.txtbox_vehicle_descrition.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")

    
    # Criar a seção de entradas para as partes do veículo na criacao de orçamento
    def widgets_car_parts_data(self):
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

        ultima_linha = self.get_last_row(self.frames["frame_vehicle_data_entries"])
        self.frames['frame_choose_body_part'] = ctk.CTkFrame(self.frames["frame_vehicle_data_entries"], width=300, height=300, fg_color="transparent")
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
            self.checkbox_car_parts_vars[label_text] = var


    # Criar a seção de entradas a selecao ou criacao de cliente na criacao de orçamento
    def frame_client_data_entries(self):

        self.frames["frame_client_data_entries"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_client_data_entries"].grid(row=0, column=2, padx=5, pady=5, sticky="nwe")
        self.widgets_responsible_client_data()


    # Criar a seção de entradas para selecionar um cliente existente ou criar um novo cliente na criacao de orçamento
    def widgets_responsible_client_data(self):
        lbl_info_driver = ctk.CTkLabel(master=self.frames["frame_client_data_entries"], text="Responsável Financeiro", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_driver.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_driver.rowconfigure(0, weight=1)
        
        # Adiciona os Comboboxes para selecionar um cliente existente
        clientes = ["Cliente 1", "Cliente 2", "Cliente 3"]
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entries"])
        ctk.CTkLabel(master=self.frames["frame_client_data_entries"], text="Selecionar Cliente:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="e")
        self.combo_clientes = ctk.CTkComboBox(master=self.frames["frame_client_data_entries"], values=clientes, width=200)
        self.combo_clientes.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")
        self.combo_clientes.set("Selecione um cliente") 

        # Checkbox para novo cliente
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entries"])

        self.novo_cliente_var = ctk.BooleanVar(value=False)
        self.checkbox_novo_cliente = ctk.CTkCheckBox(self.frames["frame_client_data_entries"], text="Cadastrar novo cliente", variable=self.novo_cliente_var,command=self.widgets_new_client_data_entrys)
        self.checkbox_novo_cliente.grid(row=ultima_linha, column=0, padx=10, pady=5)

        # divider entre os widgets
        ultima_linha = self.get_last_row(self.frames["frame_client_data_entries"])
        divider = ctk.CTkFrame(self.frames["frame_client_data_entries"], height=2, fg_color="DarkSlateGray")
        divider.grid(row=ultima_linha, column=0, sticky="ew", pady=5,padx=(5,5),columnspan=2)

    # Criar a seção de entradas para um novo cliente no orçamento
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
            ultima_linha = self.get_last_row(self.frames["frame_client_data_entries"])
            self.frames['frame_add_new_client'] = ctk.CTkFrame(self.frames["frame_client_data_entries"], width=300, height=300, fg_color="transparent")
            self.frames['frame_add_new_client'].grid(row=ultima_linha, column=0, sticky="new",columnspan=2)
            
            self.frames['frame_add_new_client'].grid_rowconfigure(0, weight=1)
            ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text="Cadastrar Novo Cliente", font=("Arial", 16),text_color="DimGrey",anchor="center")\
                .grid(row=0, column=0, padx=10, pady=5, columnspan=2)

            for i, (label_text, entry_name) in enumerate(cliente_data_entrys):
                var = ctk.StringVar()
                ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text=label_text + ":")\
                    .grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
                entry = ctk.CTkEntry(master=self.frames['frame_add_new_client'] , width=200, placeholder_text=label_text,textvariable=var)
                entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="ew")
                self.entry_novo_cliente_var[entry_name] = var

            # Última linha para textbox de descrição
            ultima_linha = self.get_last_row(self.frames["frame_client_data_entries"])
            ctk.CTkLabel(master=self.frames['frame_add_new_client'] , text="Descrição:")\
                .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="ne")
            self.txtbox_new_client_descrition = ctk.CTkTextbox(master=self.frames['frame_add_new_client'] , width=200, height=100)
            self.txtbox_new_client_descrition.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")
            


    def frame_payment_data_entries(self):
        self.frames["frame_payment_data_entries"] = ctk.CTkFrame(master=self, width=300, height=300, fg_color="gray22")
        self.frames["frame_payment_data_entries"].grid(row=0, column=3, padx=5, pady=5, sticky="nwe")
        self.widgets_payment_data()

    
    # Criar a seção de entradas para os dados de pagamento na criação de orçamento
    def widgets_payment_data(self):
        parcelamento = ['1','2','3','4','5','6','7','8','9','10','11','12']
        var_valor_entrada = ctk.StringVar()
        var_valor_total = ctk.StringVar()
        var_payment_method = ctk.StringVar()
        var_payment_parcel = ctk.StringVar()


        lbl_info_payment = ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text="Dados de Pagamento", font=("Arial", 16),text_color="DimGrey",anchor="center")
        lbl_info_payment.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        lbl_info_payment.rowconfigure(0, weight=1)

        # Entry para o valor de entrada
        ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text='Valor de Entrada:')\
                .grid(row=1, column=0, padx=10, pady=5, sticky="e")
        ctk.CTkEntry(master=self.frames["frame_payment_data_entries"], width=200, placeholder_text='Valor Total',textvariable=var_valor_entrada)\
                .grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.entry_payments_var['entry_valor_entrada'] = var_valor_entrada

        # Entry para o valor total
        ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text='Valor Total:')\
            .grid(row=2, column=0, padx=10, pady=5, sticky="e")
        ctk.CTkEntry(master=self.frames["frame_payment_data_entries"], width=200, placeholder_text='Valor Total',textvariable=var_valor_total)\
            .grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.entry_payments_var['entry_valor_total'] = var_valor_total
        
        # Combo box para selecionar o método de pagamento
        ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text='Método de Pagamento')\
            .grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.btn_payment_method = ctk.CTkSegmentedButton(master=self.frames["frame_payment_data_entries"], values=["Pix", "Débito", "Crédito", "Dinheiro"],variable=var_payment_method)\
            .grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.entry_payments_var['entry_metodo_pagamento'] = var_payment_method
        
        # Combo box para selecionar parcelamento
        ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text='Parcelamento')\
                .grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.combo_payment_method = ctk.CTkComboBox(master=self.frames["frame_payment_data_entries"], values=parcelamento, variable=var_payment_parcel)
        self.combo_payment_method.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.combo_payment_method.set("Nº de Parcelas")
        self.entry_payments_var['entry_parcelamento'] = var_payment_parcel
        
        # Última linha para textbox de descrição
        ultima_linha = self.get_last_row(self.frames["frame_payment_data_entries"])
        ctk.CTkLabel(master=self.frames["frame_payment_data_entries"], text="Descrição:")\
            .grid(row=ultima_linha, column=0, padx=10, pady=5, sticky="nw")
        self.txtbox_payment_description = ctk.CTkTextbox(master=self.frames["frame_payment_data_entries"], width=200, height=100)
        self.txtbox_payment_description.grid(row=ultima_linha, column=1, padx=10, pady=5, sticky="ew")

        

    # Método para obter a última linha ocupada em um frame
    def get_last_row(self,master):
        widgets = master.grid_slaves()
        if not widgets:
            return 0
        return max(widget.grid_info()['row'] for widget in widgets) + 1


    # Método para consultar um orçamento
    def consultar_orcamentos(self):
        
        self.frames["frame_entrys_orcamentos"].forget()
        pass

    # Método para pegar os frames
    def get_frames(self):
        return self.frames

    # Método para esquecer os frames específicos
    def forget_specific_frames(self):
        print("Esquecendo frames específicos")
        self.frames["frame_vehicle_data_entries"].destroy()
        self.frames["frame_client_data_entries"].destroy()
        self.frames["frame_choose_body_part"].destroy()
        
        super().forget()

    # Método para obter todos os valores dos Entry
    def get_all_entrys(self):
        # Retorna todos os valores dos Entry
        print("\n\nValores dos Entry:")
        print("\n=============Dados do carro=============\n")
        self.entry_carinfo_vars['vehicle_description'] = self.txtbox_vehicle_descrition.get("0.0", "end")
        for key, var in self.entry_carinfo_vars.items():
            if key != 'vehicle_description':
                print(f"{key}: {var.get()}")
            else:
                print(f"{key}: {self.entry_carinfo_vars['vehicle_description']}")
        print("=============Partes do carro a trabalhar=============")
        for key, var in self.checkbox_car_parts_vars.items():
            print(f"{key}: {var.get()}") 
        print("=============Dados de pagamento=============")
        self.entry_payments_var['payment_description'] = self.txtbox_payment_description.get("0.0", "end")
        for key, var in self.entry_payments_var.items():
            if key != 'payment_description':
                print(f"{key}: {var.get()}")
            else:
                print(f"{key}: {self.entry_payments_var['payment_description']}")
        if self.novo_cliente_var.get():
            self.entry_novo_cliente_var['new_client_description'] = self.txtbox_new_client_descrition.get("0.0", "end")
            for key, var in self.entry_novo_cliente_var.items():
                if key != 'new_client_description':
                    print(f"{key}: {var.get()}")
                else:
                    print(f"{key}: {self.entry_novo_cliente_var['new_client_description']}")
        print("=========================================")
        self.validate_all_entrys()
   
    # Método para limpar todos os Entry
    def clean_all_entrys(self):
        # Limpa todos os valores dos Entry
        for key, var in self.entry_carinfo_vars.items():
            var.set("")    
        for key, var in self.checkbox_car_parts_vars.items():
            var.set(0)
        if self.novo_cliente_var.get():
            for key, var in self.entry_novo_cliente_var.items():
                var.set("")
        
    # Método para validar todos os Entry
    def validate_all_entrys(self):
        errors = []

        # Valida os campos de dados do carro
        for key, var in self.entry_carinfo_vars.items():
            if key != 'vehicle_description' and not var.get().strip():
                errors.append(f"Campo '{key}' não preenchido.")

        # Valida os campos de pagamento
        for key, var in self.entry_payments_var.items():
            if key != 'payment_description' and not var.get().strip():
                errors.append(f"Campo de pagamento '{key}' não preenchido.")

        # Valida os campos de novo cliente, se selecionado
        if self.novo_cliente_var.get():
            for key, var in self.entry_novo_cliente_var.items():
                if key != 'new_client_description' and not var.get().strip():
                    errors.append(f"Dados do novo cliente '{key}' não preenchido.")

        # Exibe os erros ou retorna True se tudo estiver válido
        if errors:
            print("\nErros encontrados:")
            for error in errors:
                print(f"- {error}")
            messagebox.showerror("Erro de Validação", "\n".join(errors))
            return False
        else:
            print("Todos os campos foram preenchidos corretamente.")
            return True
        
    def limpar_frames_dinamicos(self):
        print(f"\n\n*********Limpeza de framedinamicos*********")
        print(f"Frames antes da limpeza: {self.frames.keys()}")
        for nome, frame in self.frames.items():
            if nome != "frame_botoes_acao_orcamentos":
                print(f"Destruindo frame: {nome}\n")  
                frame.destroy()
                super().forget()
        self.frames = {"frame_botoes_acao_orcamentos": self.frames["frame_botoes_acao_orcamentos"]}
        print(f"Frames após limpeza: {self.frames.keys()}")