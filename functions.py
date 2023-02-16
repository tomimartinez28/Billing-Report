
""" file = '/Users/tomasmartinez/Documents/FACTURAS/27206517382_012_00007_00003125.pdf' """

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


