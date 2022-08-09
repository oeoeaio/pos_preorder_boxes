odoo.define('point_of_sale.add_boxes', ['point_of_sale.models', 'pos.preorders'], function (require) {

var models = require('point_of_sale.models');

// Add box size fields to the field list for preorders
models.load_fields('pos.preorder', [
  'box_size',
  'small_count',
  'standard_count',
  'large_count',
  'fruit_count',
  'large_fruit_count',
])

});
