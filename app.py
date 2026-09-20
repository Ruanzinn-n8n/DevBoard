import customtkinter as ctk

janela = ctk.CTk()
janela.title("DevBoard")
janela.geometry("700x400")
janela.maxsize(width=800, height=600)
janela.minsize(width=500, height=200)
janela.resizable(width=False, height=False)
#janela.iconify()     faz a janela fechar
#janela.deiconify()     faz ela reabrir

janela.mainloop()