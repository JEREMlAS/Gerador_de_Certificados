import math


def limpa_entrys_de_caminho(entry):
    entry = entry.replace('"', '')
    entry = entry.strip()
    return entry

def retorna_data_por_extenso_em_pt_br(data):
    data = str(data)
    dia, mes, ano = data.split(sep='/')

    dicio_meses = {
    '01': 'Janeiro',
    '02': 'Fevereiro',
    '03': 'Março',
    '04': 'Abril',
    '05': 'Maio',
    '06': 'Junho',
    '07': 'Julho',
    '08': 'Agosto',
    '09': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
    }

    data_por_extenso = f'{dia} de {dicio_meses[mes]} de {ano}'
    
    return data_por_extenso

def get_date_in_english_format(date):
    day, month, year = date.split('/')

    months_dict = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    date_in_english = f'{months_dict[month]} {day}, {year}'

    return date_in_english

def titulo(nome_do_titulo):
    tamanho_str = len(nome_do_titulo)
    tamanho_linha = int(tamanho_str + tamanho_str * 0.2)
    print('=-' * math.ceil(tamanho_linha / 2))
    print(f'{nome_do_titulo:^{tamanho_linha}}')
    print('=-' * math.ceil(tamanho_linha / 2))

def retorna_posicao_em_ingles(num):
    if num == 1:
        return 'st'
    elif num == 2:
        return 'nd'
    elif num == 3:
        return 'rd'
    elif num >= 4:
        return 'th'
    else:
        raise KeyError('A funçao só aceita números inteiros positivos')



# Fazendo alguns testes básicos só por garantia
if __name__ == '__main__':
    titulo('Testando as funções de tratamento de datas')
    print(retorna_data_por_extenso_em_pt_br('11/11/2005'))
    print(get_date_in_english_format('11/11/2005'))

    titulo('Testando a função de limpar entrys de caminho de arquivos')
    print(limpa_entrys_de_caminho(r'"                               C:\Users\pjere\OneDrive\Estudos\top\areas de figuras planas.png      "'))

    titulo('Testando a função de posicões em inlgê')
    print(f'1{retorna_posicao_em_ingles(1)}')
    print(f'2{retorna_posicao_em_ingles(2)}')
    print(f'3{retorna_posicao_em_ingles(3)}')
    print(f'4{retorna_posicao_em_ingles(4)}')
    print(f'5{retorna_posicao_em_ingles(5)}')
    print(f'9{retorna_posicao_em_ingles(9)}')