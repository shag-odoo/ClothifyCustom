# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Clothify Module",
    'version': '1.0',
    'category': 'Fashion',
    'summary': 'An Online Cloth Store',
    'description': 'Dealing in Clothes',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/clothify_product_views.xml',
        'views/clothify_category_views.xml',
        'views/clothify_menus.xml',


    ],
    'application': True,

}
