import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MinhaJanela(ctk.CTk):  #a classe cria a janela e é o pai de tudo.
    def __init__(self):   # essa função inicia e segura tudo rodando.
        super().__init__()   # isso inicia o programa

        # essa parte é responsável por informar os principais parametros
        self.title("DevBoard")
        self.geometry("500x400")
        self.resizable(False, False)

        # nessa parte criamos um texto
        self.meu_titulo = ctk.CTkLabel(self, text="Olá Dev!") # aqui é criado o objeto
        self.meu_titulo.pack(pady=10, padx=20) # e aqui é mostrado

        # essa função define oque acontece ao clicar em um botão.
        def minha_funcao():
            print("click")

        # e aqui criamos o botão
        self.btn = ctk.CTkButton(self, text="Clique aqui!", command=minha_funcao) # aqui criamos e obj
        self.btn.pack(pady=20) # e aqui fazemos aparecer no programa

app = MinhaJanela()
app.mainloop()