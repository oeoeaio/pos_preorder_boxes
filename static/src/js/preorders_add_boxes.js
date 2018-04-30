odoo.define('pos.preorders.add_boxes', function (require) {

var models = require('point_of_sale.models');

// Find the model request for preorders
// and add box size fields to the field list
var model_list = models.PosModel.prototype.models;
for (var i=0;i < model_list.length;i++){
    if (model_list[i].model === 'pos.preorder'){
        model_list[i].fields.push('box_size');
        model_list[i].fields.push('small_count');
        model_list[i].fields.push('standard_count');
        model_list[i].fields.push('large_count');
    }
}

});
