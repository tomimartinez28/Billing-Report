from datetime import datetime


def doc_type_function(file):
    doc_type_cod = file.split('_')[1]
    if doc_type_cod == '211':
        return 'FACTURA DE CREDITO ELECTRONICA MIPYMES'
    elif doc_type_cod == '011':
        return 'FACTURA'
    elif doc_type_cod == '013':
        return 'NOTA DE CREDITO'
    elif doc_type_cod == '012':
        return 'NOTA DE DEBITO'


def date_converter(date_string):
    return datetime.strptime(date_string, '%d/%m/%Y').date()

    
print(date_converter('22/10/2023'))

