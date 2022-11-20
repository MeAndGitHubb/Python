# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Test',
    'version' : '1.1',
    'summary': 'Test & Test',
    'sequence': 15,
    'category': 'Accounting/Accounting',
    'depends' : ['base','stock'],
    'data': [
        'views/stock_picking_views.xml', 'security/ir.model.access.csv'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
