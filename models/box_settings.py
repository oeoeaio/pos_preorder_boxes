import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class BoxSettings(models.TransientModel):
    _name = 'pos.preorder.box.settings'
    _inherit = 'res.config.settings'

    small_box_product_ids = fields.Many2many('product.product', 'box_settings_small_ids', string='Small Box Products')
    standard_box_product_ids = fields.Many2many('product.product', 'box_settings_standard_ids', string='Standard Box Products')
    large_box_product_ids = fields.Many2many('product.product', 'box_settings_large_ids', string='Large Box Products')
    fruit_box_product_ids = fields.Many2many('product.product', 'box_settings_fruit_ids', string='Fruit Box Products')
    large_fruit_box_product_ids = fields.Many2many('product.product', 'box_settings_large_fruit_ids', string='Large Fruit Box Products')

    class NullBoxIDs:
        def split(*args):
            return []

    @api.model
    def get_values(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        small_ids = ICPSudo.get_param('pos.preorder.box.small_box_product_ids') or self.NullBoxIDs()
        standard_ids = ICPSudo.get_param('pos.preorder.box.standard_box_product_ids') or self.NullBoxIDs()
        large_ids = ICPSudo.get_param('pos.preorder.box.large_box_product_ids') or self.NullBoxIDs()
        fruit_ids = ICPSudo.get_param('pos.preorder.box.fruit_box_product_ids') or self.NullBoxIDs()
        large_fruit_ids = ICPSudo.get_param('pos.preorder.box.large_fruit_box_product_ids') or self.NullBoxIDs()

        return {
            'small_box_product_ids': tuple(map(int,small_ids.split(','))),
            'standard_box_product_ids': tuple(map(int,standard_ids.split(','))),
            'large_box_product_ids': tuple(map(int,large_ids.split(','))),
            'fruit_box_product_ids': tuple(map(int,fruit_ids.split(','))),
            'large_fruit_box_product_ids': tuple(map(int,large_fruit_ids.split(','))),
        }

    def set_values(self):
        # super(BoxSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()

        small_ids = ','.join(map(lambda b: str(b.id), self.small_box_product_ids))
        standard_ids = ','.join(map(lambda b: str(b.id), self.standard_box_product_ids))
        large_ids = ','.join(map(lambda b: str(b.id), self.large_box_product_ids))
        fruit_ids = ','.join(map(lambda b: str(b.id), self.fruit_box_product_ids))
        large_fruit_ids = ','.join(map(lambda b: str(b.id), self.large_fruit_box_product_ids))

        ICPSudo.set_param('pos.preorder.box.small_box_product_ids', small_ids)
        ICPSudo.set_param('pos.preorder.box.standard_box_product_ids', standard_ids)
        ICPSudo.set_param('pos.preorder.box.large_box_product_ids', large_ids)
        ICPSudo.set_param('pos.preorder.box.fruit_box_product_ids', fruit_ids)
        ICPSudo.set_param('pos.preorder.box.large_fruit_box_product_ids', large_fruit_ids)
