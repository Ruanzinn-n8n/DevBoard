import customtkinter as ctk

janela = ctk.CTk()
janela.title("DevBoard")
janela.geometry("700x400")
janela.maxsize(width=800, height=600)
janela.minsize(width=500, height=200)
janela.resizable(width=False, height=False)
#janela.iconify()     faz a janela fechar
#janela.deiconify()     faz ela reabrir

def new_window():
    new_win = ctk.CTkToplevel(janela) #  fg_color="_cor_" adiciona uma cor ao fundo 
    new_win.geometry("300x150")

btn = ctk.CTkButton(master=janela, command=new_window, text="new_janela").place(x=300, y=100)

janela.mainloop()