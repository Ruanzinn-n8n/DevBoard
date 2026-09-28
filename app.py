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

btn = ctk.CTkButton(master = janela, text= "new_janela", command = new_window).place(x=280, y=100)

# Frames
#frame = ctk.CTkFrame(master = janela, width = 60, height = 40).place(x=320, y=100)


tabview = ctk.CTkTabview(master = janela, width = 400, corner_radius = 30, border_width = 2, border_color = "purple")
tabview.pack()
tabview.add("Nomes")
tabview.add("Profissões")
tabview.add("Salarios")
tabview.tab("Nomes").grid_columnconfigure(0, weight = 1)
tabview.tab("Profissões").grid_columnconfigure(10, weight = 10)
tabview.tab("Salarios").grid_columnconfigure(0, weight = 1)

name = ctk.CTkLabel(tabview.tab("Nomes"), text = "Ruan\nLiz\nSamira\nAnna")
name.pack()

prof = ctk.CTkLabel(tabview.tab("Profissões"), text = "predero\narquiteto\ncaminhao")
prof.pack()


janela.mainloop()