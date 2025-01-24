# -*- coding: utf-8 -*-
{
    'name': "ecomm_product_discounts",

    'summary': "Enable percentage-based discounts for products in the eCommerce store with dynamic pricing and cart integration.",

    'description': """
This module allows admins to set percentage discounts on products. 
        Discounted prices are displayed on the website and applied in the cart, checkout, and invoice.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '1.0.0',
    'category': 'Website/Website',
    # any module necessary for this one to work correctly

    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_template_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
