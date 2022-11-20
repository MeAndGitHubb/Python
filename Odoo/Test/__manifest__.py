# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Test',
    'version': '1.1',
    'summary': 'Test & Test',
    'sequence': 15,
    'category': 'Accounting/Accounting',
    'depends': ['base', 'stock','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/product_view.xml',
        'reports/report.xml',
        'reports/report_card.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
