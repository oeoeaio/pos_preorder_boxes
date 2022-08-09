# -*- coding: utf-8 -*-
{
    'name': 'POS Preorder Boxes',
    'version': '1.0.0',
    'category': 'Point Of Sale',
    'author': 'Rob Harrington',
    'sequence': 10,
    'summary': 'Allow tracking of box sizes within preorders',
    'description': "",
    'depends': ['pos_preorders'],
    'data': [
        'views/box_settings.xml',
        'views/preorder_views.xml',
        'wizard/box_summary.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_preorder_boxes/static/src/js/**/*',
            ('after', 'point_of_sale/static/src/css/pos.css', 'pos_preorder_boxes/static/src/css/box_widgets.css'),
        ],
        'web.assets_qweb': [
            'pos_preorder_boxes/static/src/xml/**/*',
        ],
    },
    'images': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
