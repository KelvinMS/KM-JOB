import customtkinter as ctk

class TelaConsultaOrcamentos(ctk.CTkFrame):
    def __init__(self, master, frames):
        super().__init__(master)
        self.frames = frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.mostrar_tela_consultar_orcamentos()

    def mostrar_tela_consultar_orcamentos(self):
        

        # Mantém apenas o frame de botões
        for nome, frame in list(self.frames.items()):
            if nome != "frame_botoes_acao_orcamentos":
                frame.destroy()
        self.frames = {"frame_botoes_acao_orcamentos": self.frames.get("frame_botoes_acao_orcamentos")}

        print("frames na TESTE:", self.frames.keys())
        # Cria novo frame de consulta
        frame_consulta = ctk.CTkFrame(master=self, fg_color="gray20")
        frame_consulta.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frames["frame_consulta_orcamentos"] = frame_consulta

        # Título
        ctk.CTkLabel(
            master=frame_consulta, text="Consulta de Orçamentos",
            font=("Arial", 18, "bold"), text_color="white"
        ).grid(row=0, column=0, pady=(10, 5))

        # Scrollable Frame para "Tabela"
        scroll_frame = ctk.CTkScrollableFrame(master=frame_consulta, width=900, height=400)
        scroll_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Cabeçalhos
        headers = ["ID", "Cliente", "Veículo", "Data", "Valor"]
        for col, text in enumerate(headers):
            ctk.CTkLabel(
                master=scroll_frame, text=text, font=("Arial", 14, "bold"),
                text_color="white"
            ).grid(row=0, column=col, padx=10, pady=5)

        # Dados simulados
        dados_exemplo = [
            (1, "João Silva", "Uno", "01/01/2025", "R$ 1.200,00"),
            (2, "Maria Lima", "Civic", "02/01/2025", "R$ 2.300,00"),
            (3, "Pedro Souza", "Corolla", "03/01/2025", "R$ 3.400,00"),
        ]

        for row, item in enumerate(dados_exemplo, start=1):
            for col, valor in enumerate(item):
                ctk.CTkLabel(
                    master=scroll_frame, text=str(valor), text_color="white"
                ).grid(row=row, column=col, padx=10, pady=2, sticky="w")
