import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter.filedialog import askopenfilename





# Criando janela
janela = tk.Tk()
janela.title('Gerador de Certificados')
#Criando titlo
label_titulo = tk.Label(text='GERADOR DE CERTIFICADOS', font=('Aptos', 30))
label_titulo.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='nswe')
# Criando label planilha alunos
label_planilha_alunos = tk.Label(text='Planilha de Alunos:', anchor='w', font=('Aptos', 12))
label_planilha_alunos.grid(row=1, column=0, padx=15, pady=15, sticky='nswe')
# Criando entry planilha alunos
entry_planilha_alunos = tk.Entry(font=('Aptos', 10))
entry_planilha_alunos.grid(row=1, column=1, padx=15, pady=15, sticky='we')
# Botao pesquisar arquivo
def procurar_arquivo():
    arquivo = tk.StringVar()
    arquivo.set(askopenfilename())
    entry_planilha_alunos['text'] = arquivo

btt_procurar_arquivo = tk.Button(text='Buscar', font=('Aptos', 12), fg='white', bg='#156082', command=procurar_arquivo)
btt_procurar_arquivo.grid(row=1, column=3, padx=15, pady=15, sticky='nswe')
# Label entrada de data do exame
label_data = tk.Label(text='Data do Exame:', anchor='w', font=('Aptos', 12))
label_data.grid(row=2, column=0, sticky='nswe', padx=15, pady=15)
# Entrada de data do exame
dateentry_data_exame = DateEntry(locale='pt_br')
dateentry_data_exame.grid(row=2, column=1, sticky='nswe', padx=15, pady=15)
# Botao para gerar os certificados
btt_gerar_certificados = tk.Button(text='GERAR CERTIFICADOS', font=('Aptos', 14), fg='white', bg='#156082')
btt_gerar_certificados.grid(row=3, column=1, padx=15, pady=15, sticky='nswe')
# Label de progresso
label_progresso = tk.Label(text='0/0', font=('Aptos', 12), fg='red')
label_progresso.grid(row=4, column=1, padx=15, pady=15, sticky='nswe')



janela.mainloop()
