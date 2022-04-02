# -*- coding: utf-8 -*-
{
    'name': 'POS Enlarge Image',
    'category': 'Point of Sale',
    'summary': 'This module allows user to see large product image in POS and also in Inventory.',
    'description': """
""",
    'author': 'V2Logic Systems Pvt. Ltd.',
    'website': 'https://v2logicsystems.com/',
    'currency': 'EUR',
    'version': '1.0.1',
    'depends': ['base', 'point_of_sale','product'],
    "data": [
        'views/point_of_sale.xml',
        'views/pos_image_enlarge.xml',
        'views/product_template_views.xml',
    ],
    'qweb': [
        'static/src/xml/Screens/ProductScreen/ProductItem.xml',
        'static/src/xml/Popups/ImagePopup.xml'
    ],
    'installable': True,
    'auto_install': False,
}

