import pdfquery
import pandas as pd
import os




def pdfscrape(pdf):

    
    # Extract each relevant information individually               
    date        = pdf.pq('LTTextLineHorizontal:overlaps_bbox("428.0, 724.36, 478.02, 734.36")').text()
    period      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("265.0, 654.61, 315.02, 664.61")').text()
    os_cuit     = pdf.pq('LTTextLineHorizontal:overlaps_bbox("102.51, 635.52, 102.513, 644.52")').text().split(sep=':')[1]
    doc_type    = pdf.pq('LTTextLineHorizontal:overlaps_bbox("341.0, 760.89, 427.94, 778.89")').text()
    punto_venta = pdf.pq('LTTextLineHorizontal:overlaps_bbox("417.0, 739.86, 444.8, 749.86")').text()
    doc_number  = pdf.pq('LTTextLineHorizontal:overlaps_bbox("517.0, 739.86, 561.48, 749.86")').text()
    total       = pdf.pq('LTTextLineHorizontal:overlaps_bbox("531.31, 177.36, 573.0, 187.36")').text()
    detail      = pdf.pq('LTTextLineHorizontal:overlaps_bbox("57.0, 500.98, 174.32, 560.98")').text()


    
    print('fecha  => ', date)
    print('period  => ', (period))
    print('Cuit  => ', os_cuit)
    print('punto de venta  => ', punto_venta)
    print('tipo  => ', doc_type)
    print('Numero de Compro.  => ', doc_number)
    print('Monto  => ', total)
    print('detail  => ', detail)
    
# Combined all relevant information into single observation
    page = pd.DataFrame({
        'Fecha de Emision': date,
        'Periodo': period,
        'Obra Social': os_cuit,
        'Tipo de Comprobante': doc_type,
        'Punto de Venta': punto_venta,
        'Numero de Comprobante': doc_number,
        'Total': total,
        'Detalle': detail,
        }, index=[0])
    return(page)


directory = '/Users/tomasmartinez/Documents/FACTURAS' 

master = pd.DataFrame()




for file in os.listdir(directory):
    try:
        print(file)
        pdf = pdfquery.PDFQuery(os.path.join (directory, file))
        pdf.load(1)
        page = pdfscrape(pdf)
        master = master.append(page, ignore_index=True)
        master.to_excel(f'/Users/tomasmartinez/Desktop/Archivo de Facturacion.xlsx',sheet_name='new_sheet_name', index= False)
    except:
        print(f'Error en {file}')

