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
        'views/assets.xml',
        'views/box_settings.xml',
        'views/preorder_views.xml',
        'wizard/box_summary.xml',
    ],
    'qweb': [
        'static/src/xml/box_widgets.xml',
        'static/src/xml/preorder_templates.xml',
    ],
    'images': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
