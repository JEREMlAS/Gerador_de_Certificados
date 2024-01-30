from docx import Document
from docxtpl import DocxTemplate
from pathlib import Path

def posicao_em_ingles(num):
    if num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'
    elif num >= 4:
        return 'th'



def Criar_Certificado(certificado_base, nome, faixa, pasta_final):
    final = Path(pasta_final)
    certificado_base = Path(certificado_base)
    doc = DocxTemplate(certificado_base)
    faixa = int(faixa)
    ing = posicao_em_ingles(faixa)
    context = {'nome': nome, 'faixa': faixa, 'ing': ing} 
    doc.render(context)
    doc.save(final / f'Certificado de {faixa}° gub - {nome}.docx')

