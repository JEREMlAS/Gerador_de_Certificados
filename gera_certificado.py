from docx import Document
from docxtpl import DocxTemplate
from pathlib import Path
from facilidades import retorna_posicao_em_ingles

def gera_certificado(certificado_base, nome, faixa, data_pt, data_ing, nome_do_arquivo):
    certificado_base = Path(certificado_base)

    doc = DocxTemplate(certificado_base)

    posicao_em_ingles = retorna_posicao_em_ingles(faixa)

    context = {'nome': nome, 'faixa': faixa, 'ing': posicao_em_ingles, 'data_pt': data_pt, 'data_ing': data_ing} 
    doc.render(context)
    doc.save(nome_do_arquivo)
