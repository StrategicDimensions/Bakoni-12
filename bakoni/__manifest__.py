# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bakoni',
    'category': '',
    'sequence': 60,
    'summary': 'Bakoni Customization',
    'description': "Bakoni",
    'website': 'https://www.odoo.com/',
    'version': '1.0',
    'depends': ['base', 'account', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_data.xml',
        'views/res_partner_view.xml',
        'views/account_invoice_views.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'report/sale_report_templates.xml',
        'report/invoice_report_templated.xml',
    ],
    'qweb': [],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
