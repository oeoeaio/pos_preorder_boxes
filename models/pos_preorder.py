import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class PosPreorder(models.Model):
    _inherit = "pos.preorder"

    BOX_NAMES = {
        'small': "Small Box",
        'standard': "Standard Box",
        'large': "Large Box",
    }

    @api.depends('lines.product_id', 'lines.qty')
    def _compute_box_size(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        box_ids = self.box_ids()

        for preorder in self:
            counter = {
                'small': 0,
                'standard': 0,
                'large': 0
            }
            for line in preorder.lines:
                for size, ids in box_ids.items():
                    if line.product_id.id in ids:
                         counter[size] += line.qty
                         break

            preorder.small_count = counter['small']
            preorder.standard_count = counter['standard']
            preorder.large_count = counter['large']
            preorder.box_size = self._compute_size_text(counter)

    small_count = fields.Integer(compute=_compute_box_size, string="Small Box Count", store=True)
    standard_count = fields.Integer(compute=_compute_box_size, string="Standard Box Count", store=True)
    large_count = fields.Integer(compute=_compute_box_size, string="Large Box Count", store=True)
    box_size = fields.Char(compute=_compute_box_size, string='Box Size', store=True)

    def box_ids(self):
        box_ids = {}
        ICPSudo = self.env['ir.config_parameter'].sudo()
        small_ids = ICPSudo.get_param('pos.preorder.box.small_box_product_ids')
        standard_ids = ICPSudo.get_param('pos.preorder.box.standard_box_product_ids')
        large_ids = ICPSudo.get_param('pos.preorder.box.large_box_product_ids')
        box_ids['small'] = list(map(int,small_ids.split(','))) if small_ids else []
        box_ids['standard'] = list(map(int,standard_ids.split(','))) if standard_ids else []
        box_ids['large'] = list(map(int,large_ids.split(','))) if large_ids else []
        return box_ids

    def _compute_size_text(self, counter):
        total = sum(counter.values())
        text = ""
        for size, count in counter.items():
            if count < 1: continue
            text += "" if text == "" else ", "
            text += "" if total <= 1 else "%s × " % (int(count))
            text += self.BOX_NAMES[size]
        return text
