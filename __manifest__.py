{
    'name': 'Customer Audio Files',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Automatically import and link audio files to customers',
    'description': 'This module imports audio files, links them to customers, and displays them in the customer module.',
    'depends': ['base', 'contacts'],
    'Author': 'Julian Pokorny',
    'data': [
        'views/res_partner_view.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': False,
}