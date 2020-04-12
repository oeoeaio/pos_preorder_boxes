from odoo import models, fields, api
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)

class BoxCount(models.TransientModel):
    _name = 'pos.preordered_box.count'

    size = fields.Selection(
        [('small', 'Small'), ('standard', 'Standard'), ('large', 'Large'),
        ('fruit', 'Fruit'), ('large_fruit', 'Large Fruit')],
        'Box Type', copy=False, default='small')
    uncollected_count = fields.Integer(string='Uncollected', default=0)
    to_deliver_count = fields.Integer(string='To Deliver', default=0)
    summary = fields.Many2one('pos.preordered_box.summary')

class BoxSummary(models.TransientModel):
    _name = 'pos.preordered_box.summary'

    counts = fields.One2many('pos.preordered_box.count', 'summary')

    def _get_records(self):
        context = dict(self._context or {})
        active_model = context.get('active_model', False)
        active_ids = context.get('active_ids', [])
        records = self.env[active_model].browse(active_ids)
        return records

    def _box_sizes(self):
        return {
            'small': 0,
            'standard': 0,
            'large': 0,
            'fruit': 0,
            'large_fruit': 0
        }

    @api.model
    def default_get(self, fields):
        result = super(BoxSummary, self).default_get(fields)
        records = self._get_records()

        counter = {
            'uncollected': self._box_sizes(),
            'to_deliver': self._box_sizes(),
        }

        for preorder in records:
            for size in self._box_sizes():
                if preorder.state not in ['uncollected', 'to_deliver']:
                    continue
                counter[preorder.state][size] += preorder[size + '_count']

        result['counts'] = []
        for size in self._box_sizes():
            fields = {
              'size': size,
              'uncollected_count': counter['uncollected'][size],
              'to_deliver_count': counter['to_deliver'][size],
            }
            result['counts'].append((0,0,fields))

        _logger.info(result)

        return result
