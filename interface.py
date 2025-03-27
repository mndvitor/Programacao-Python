import tkinter as tk

janela = tk.Tk()
janela.geometry("500x500")
janela.title("Teste")

texto_label = tk.Label(janela,text = 'Isso é um texto')
texto_label.pack()

btn = tk.Button(janela,text='clique aqui')
btn.pack()

janela.mainloop()