# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'SPS Stock Delivery Orders',
    'version' : '1.1',
    'summary': 'Delivery and report',
    'sequence': 15,
    'description': """SPS_stock_delivery_orders""",
    'category': 'Inventory',
    'depends' : ['base','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'report/report.xml',
        'report/report_card.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
