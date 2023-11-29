{
    'name': 'Reports Odoo',
    'version': '1.0',
    'description': 'Module Reports',
    'category': 'Other',
    'author': 'Carlos Garcia Garcia',
    'website': 'python.org',
    'license': 'OPL-1',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',  # First is the security
        'views/info.xml',
        'views/menu.xml',  # The rule is the last menu
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
