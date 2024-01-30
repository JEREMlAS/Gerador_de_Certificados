import tkinter as tk
from tkinter import messagebox

def mostrar_aviso():
    messagebox.showinfo("Aviso", """Os seguintes certificados tiveram que ter o nome original alterado:
                        Juliano
                        albertinho
                        jose rodrigues""")

janela = tk.Tk()
janela.title("Teste do Pop-up")

botao = tk.Button(janela, text="Mostrar Aviso", command=mostrar_aviso)
botao.pack(pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()

