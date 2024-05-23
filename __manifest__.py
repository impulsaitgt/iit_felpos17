# -*- coding: utf-8 -*-
{
    'name' : 'Especializacion para POS de Factura Electronica Impulsa IT',
    'summary':"""
        Implementacion Factura Electronica FEL con Infile, especialiacion para POS
    """,
    'author':'Alexander Paiz',
    'category': 'General',
    'version' : '1.0.0',
    'depends': [
        "account",
        "account_debit_note",
        "contacts",
        "iit_fel"
    ],

    'data': [
        "views/assets.xml"
    ],

     'qweb': ['static/src/xml/client_fel_nombre_sat.xml',
              'static/src/xml/captura_cambio_vat.xml'],

}