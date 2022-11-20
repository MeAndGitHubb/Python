{
    'name' : 'SPS_product_template',
    'version' : '1.1',
    'summary': 'SPS_product_template',
    'sequence': 15,
    'description': """SPS_product_template""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends' : ['base','stock','product'],
    'data': [
        'views/product_template.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}