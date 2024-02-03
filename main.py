import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
import pandas as pd
from threading import Thread
from pathlib import Path
import os
from gera_certificado import gera_certificado
from facilidades import limpa_entrys_de_caminho, retorna_data_por_extenso_em_pt_br, get_date_in_english_format
from confere_o_certificado_gerado import confere_qualidade_do_certificado

from time import sleep


class AppGeradorDeCertificados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Gerador de Certificados')
        self.janela.iconbitmap(r'imagens/logo.ico')
        self.janela.geometry('+650+200')

        self.cria_widgets()

        self.janela.mainloop()

    def cria_widgets(self):
        self.label_titulo = tk.Label(text='GERADOR DE CERTIFICADOS', font=('Aptos', 30))
        self.label_titulo.grid(row=0, column=0, padx=15, pady=15, columnspan=4, sticky='nswe')

        self.label_planilha_alunos = tk.Label(text='Planilha de Alunos:', anchor='w', font=('Aptos', 12))
        self.label_planilha_alunos.grid(row=1, column=0, padx=15, pady=15, sticky='nswe')

        self.entry_planilha_alunos = tk.Entry(font=('Aptos', 10))
        self.entry_planilha_alunos.grid(row=1, column=1, padx=15, pady=15, sticky='we')

        self.btt_procurar_planilha = tk.Button(text='Buscar', font=('Aptos', 12), fg='white', bg='#156082', command=self.procura_arquivo_planilha)
        self.btt_procurar_planilha.grid(row=1, column=3, padx=15, pady=15, sticky='nswe')

        self.label_pasta_final = tk.Label(text='Pasta Final:', anchor='w', font=('Aptos', 12))
        self.label_pasta_final.grid(row=2, column=0, padx=15, pady=15, sticky='nswe')

        self.entry_pasta_final = tk.Entry(font=('Aptos', 10))
        self.entry_pasta_final.grid(row=2, column=1, padx=15, pady=15, sticky='we')

        self.btt_procurar_pasta_final = tk.Button(text='Buscar', font=('Aptos', 12), fg='white', bg='#156082', command=self.procura_pasta_final)
        self.btt_procurar_pasta_final.grid(row=2, column=3, padx=15, pady=15, sticky='nswe')

        self.label_data = tk.Label(text='Data do Exame:', anchor='w', font=('Aptos', 12))
        self.label_data.grid(row=3, column=0, sticky='nswe', padx=15, pady=15)

        self.dateentry_data_exame = DateEntry(locale='pt_br')
        self.dateentry_data_exame.grid(row=3, column=1, sticky='nswe', padx=15, pady=15)

        self.btt_gerar_certificados = tk.Button(text='GERAR CERTIFICADOS', font=('Aptos', 14), fg='white', bg='#156082', command=self.roda_a_funcao_de_gerar_certificados_em_segundo_plano)
        self.btt_gerar_certificados.grid(row=4, column=1, padx=15, pady=15, sticky='nswe')

        self.label_progresso = tk.Label(text='', font=('Aptos', 12), fg='red')
        self.label_progresso.grid(row=5, column=1, padx=15, pady=15, sticky='nswe')

    def procura_arquivo_planilha(self):
        self.caminho_planilha = askopenfilename()
        if self.caminho_planilha:
            self.entry_planilha_alunos.delete(0, 'end')
            self.entry_planilha_alunos.insert(0, self.caminho_planilha)

    def procura_pasta_final(self):
        self.caminho_pasta = askdirectory()
        if self.caminho_pasta:
            self.entry_pasta_final.delete(0, 'end')
            self.entry_pasta_final.insert(0, self.caminho_pasta)

    def _cria_os_certificados(self):

        if self.pega_as_entrys_e_confere_se_estao_preenchidas():
            self.data_do_exame_por_extenso_ptbr = retorna_data_por_extenso_em_pt_br(self.data_do_exame)
            self.data_do_exame_por_extenso_ing = get_date_in_english_format(self.data_do_exame)

            df_planilha_de_alunos = pd.read_excel(self.caminho_planilha_alunos)
            numero_total_de_alunos = len(df_planilha_de_alunos)
            certificados_defeituosos = 'Os cetificados dos seguintes alunos NÃO conseguiram ser criados:'
            for num, aluno in df_planilha_de_alunos.iterrows():
                self.label_progresso['text'] = f'Criando certificados... {num + 1} / {numero_total_de_alunos}'

                nome = aluno['Aluno']
                faixa = int(aluno['GUB'])
                nome_do_arquivo = self.caminho_pasta_final / Path(f'Certificado de {faixa}° gub - {nome}.docx')
                gera_certificado(
                    certificado_base = 'Modelo_falso_para_testes.docx',
                    nome = nome, 
                    faixa = faixa, 
                    data_ing = self.data_do_exame_por_extenso_ing, 
                    data_pt = self.data_do_exame_por_extenso_ptbr,
                    nome_do_arquivo = nome_do_arquivo 
                    )

                nome_completo_do_arquivo = Path(os.getcwd()) / nome_do_arquivo # Para a funcao abaixo funcionar eh necessario o nome completo)
                if confere_qualidade_do_certificado(fr'{nome_completo_do_arquivo}'):
                    pass
                else:
                    certificados_defeituosos += f'\n-->{nome}'
                    os.remove(nome_completo_do_arquivo)

            if certificados_defeituosos != 'Os cetificados dos seguintes alunos NÃO conseguiram ser criados:':
                messagebox.showwarning('Certificados NÃO criados', certificados_defeituosos)

                

    def pega_as_entrys_e_confere_se_estao_preenchidas(self):
        self._pega_as_informacoes_preenchidas()

        for item in [self.caminho_planilha_alunos, self.data_do_exame, self.caminho_pasta_final]:
            if item == '' or item == None:
                messagebox.showerror('Erro', 'Preencha todos os campos antes de continuar,\ne lembre-se de conferir se a data está correta')
                return False
        return True


    def _pega_as_informacoes_preenchidas(self):
        self.data_do_exame = self.dateentry_data_exame.get()

        self.caminho_planilha_alunos = self.entry_planilha_alunos.get()
        self.caminho_planilha_alunos = limpa_entrys_de_caminho(self.caminho_planilha_alunos)

        self.caminho_pasta_final = self.entry_pasta_final.get()
        self.caminho_pasta_final = Path(limpa_entrys_de_caminho(self.caminho_pasta_final))
       

    def roda_a_funcao_de_gerar_certificados_em_segundo_plano(self):
        thread_gerar_certificados = Thread(target=self._cria_os_certificados)
        thread_gerar_certificados.start()
    
    



if __name__ == '__main__':
    janela = AppGeradorDeCertificados()
