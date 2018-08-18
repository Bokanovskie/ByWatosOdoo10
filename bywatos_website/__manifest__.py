# -*- coding: utf-8 -*-
{
    'name': "bywatos_website",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website',
                'bywatos_product_extended',
                'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_template/layout_main_website.xml',
        'views/website_template/layout_header_website.xml',
        'views/website_template/layout_footer_website.xml',
        'views/website_template/my_production_template.xml',
        'views/website_template/production_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}