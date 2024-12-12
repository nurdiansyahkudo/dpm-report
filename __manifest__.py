{
    'name': 'Remarks Sales Order',
    'version': '1.0',
    'summary': 'Module to show Remarks in Sales Order and Quotation',
    'description': """
        This module adds Remarks in Sales Order and Quotation.
    """,
    'category': 'Sales',
    'author': 'PT. Lintang Utama Infotek',
    'depends': ['sale', 'account', 'stock'],
    'data': [
        'views/views.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
