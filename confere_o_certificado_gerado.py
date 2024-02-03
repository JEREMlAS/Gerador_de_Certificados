from win32com.client import Dispatch

def confere_qualidade_do_certificado(caminho_certificado):
    '''
    Essa função, através do win32, abre o certificado no word e o força a repaginá-lo, 
    após isso ela verifica se a propriedade referente ao número de páginas do documento
    é diferente que um, o que não deveria ser, então se for ela retorna False, mas se
    o certificado tiver apenas uma página, o que é o esperado, ela retorna True.
    '''
    
    word = Dispatch('Word.Application')
    word.Visible = False
    word = word.Documents.Open(caminho_certificado)

    word.Repaginate()
    numero_de_paginas = word.ComputeStatistics(2)

    word.Close()

    if numero_de_paginas != 1:
        return False
    else:
        return True
 



if __name__ == '__main__':
    if confere_qualidade_do_certificado(r'C:\Users\pjere\OneDrive\Projetos Python\Github\Gerador_de_Certificados\certificados_teste\Certificado de 8° gub - enzo da silva junior.docx'):
        print('Deu certo')
