{
    'name' : 'SPS Stock Internal',
    'version' : '1.1',
    'summary': 'SPS_Stock_Internal',
    'sequence': 15,
    'description': """SPS_Stock_Internal""",
    'category': 'Inventory',
    'website': '',
    'depends' : ['base','stock','product'],
    'data': [
        'views/stock_picking_views.xml','security/ir.model.access.csv',
        'reports/report.xml','reports/report_card.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}