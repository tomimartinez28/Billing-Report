import pdfquery
import pandas as pd
import os
from functions import doc_type_function, date_converter



def pdfscrape(pdf):
    # Extract each relevant information individually
    



    if doc_type_function(file) == 'FACTURA DE CREDITO ELECTRONICA MIPYMES':
        date        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("428.0, 750.36, 478.02, 760.36")').text()
        period      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("531.77, 681.61, 531.78, 691.61")').text().split('Hasta: ')[1]
        os_cuit     = pdf.pq('LTTextLineHorizontal:overlaps_bbox("21.0, 638.52, 102.513, 647.52")').text().split(sep=': ')[1]
        doc_type    = doc_type_function(file)
        punto_venta = pdf.pq('LTTextLineHorizontal:overlaps_bbox("417.0, 765.86, 444.8, 775.86")').text()
        doc_number  = pdf.pq('LTTextLineHorizontal:overlaps_bbox("517.0, 765.86, 561.48, 775.86")').text()
        if doc_type == 'NOTA DE CREDITO':
            total       = '-' + pdf.pq('LTTextLineHorizontal:overlaps_bbox("525.75, 208.36, 573.0, 218.36")').text()
        else:
            total       = pdf.pq('LTTextLineHorizontal:overlaps_bbox("525.75, 208.36, 573.0, 218.36")').text()
        detail      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("57.0, 515.59, 188.128, 541.98")').text()
    else:
        date        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("428.0, 724.36, 478.02, 734.36")').text()
        period      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("265.0, 654.61, 315.02, 664.61")').text()
        os_cuit     = pdf.pq('LTTextLineHorizontal:overlaps_bbox("102.51, 635.52, 102.513, 644.52")').text().split(sep=': ')[1]
        doc_type    = doc_type_function(file)
        punto_venta = pdf.pq('LTTextLineHorizontal:overlaps_bbox("417.0, 739.86, 444.8, 749.86")').text()
        doc_number  = pdf.pq('LTTextLineHorizontal:overlaps_bbox("517.0, 739.86, 561.48, 749.86")').text()
        if doc_type == 'NOTA DE CREDITO':
            total       = '-' + pdf.pq('LTTextLineHorizontal:overlaps_bbox("531.31, 177.36, 573.0, 187.36")').text()
        else:
            total       = pdf.pq('LTTextLineHorizontal:overlaps_bbox("531.31, 177.36, 573.0, 187.36")').text()
        detail      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("57.0, 500.98, 174.32, 560.98")').text()

    '''
    print('====================================================================================================================================')
    print('fecha  => ', date)
    print('period  => ', (period))
    print('Cuit  => ', os_cuit)
    print('punto de venta  => ', punto_venta)
    print('tipo  => ', doc_type)
    print('Numero de Compro.  => ', doc_number)
    print('Monto  => ', total)
    print('detail  => ', detail)
    print('====================================================================================================================================')
    '''
# Combined all relevant information into single observation
    page = pd.DataFrame({
        'Fecha de Emision': date_converter(date),
        'Periodo': date_converter(period),
        'Obra Social': int(os_cuit),
        'Tipo de Comprobante': doc_type,
        'Punto de Venta': int(punto_venta),
        'Numero de Comprobante': int(doc_number),
        'Total': total,
        'Detalle': detail,
        }, index=[0])
    return(page)




directory = '/Users/tomasmartinez/Documents/FACTURAS' 
master = pd.DataFrame()




for file in os.listdir(directory):
    try:
        pdf = pdfquery.PDFQuery(os.path.join (directory, file))
        if doc_type_function(file) == 'FACTURA DE CREDITO ELECTRONICA MIPYMES':
            pdf.load()
        else:
            pdf.load(1)
        page = pdfscrape(pdf)
        #pasar a excel
        master = master.append(page, ignore_index=True)
        master.to_excel(f'/Users/tomasmartinez/Desktop/Archivo de Facturacion.xlsx',sheet_name='new_sheet_name', index= False)
    except:
        print('========================================================================================================================')
        print(f'{file} NO PUDO SER REGISTRADA. CARGARLA MANUALMENTE.')
        print('========================================================================================================================')

