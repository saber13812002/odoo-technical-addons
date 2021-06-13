# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': "feature_1",
    'category': 'Uncategorized',
    'version': '0.1',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'description': """
        Long description of module's purpose
    """,
    'depends': ['base','point_of_sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml'
    ],
    'qweb': [
        'static/src/xml/discount_templates.xml',
    ],
    'installable': True,
}
