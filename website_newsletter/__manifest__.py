# -*- coding: utf-8 -*-
{
    'name': "website_newsletter",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website',
                'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mail_subscribers_news_letter_view.xml',
        'views/mail_news_letter_view.xml',
        'views/action_news_letter.xml',
    ],
}