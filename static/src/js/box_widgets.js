odoo.define('pos.preorder.box_widgets', function (require) {
"use strict";

var chrome = require('point_of_sale.chrome');

var BoxWidget = chrome.StatusWidget.extend({
    start: function(){
        var self = this;

        self.find_product_ids();
        self.count_boxes();

        self.pos.bind('preorders:updated',self.count_boxes,this);

        this.$el.click(function(){
            self.count_boxes();
        });
    },
    set_count: function(count){
        if(count){
            this.$('.js_count').html(count);
        }
        else{
            this.$('.js_count').html(0);
        }
    },
    find_product_ids: function(){
        var all_ids = Object.keys(this.pos.db.product_by_id);
        var ids = [];
        for (var i=0;i<all_ids.length;i++){
            var product = this.pos.db.product_by_id[all_ids[i]];
            if (product.display_name.startsWith(this.size + ' Box')){
                ids.push(parseInt(all_ids[i]));
            }
        }
        this.product_ids = ids;
    },
    count_boxes: function(){
        var count = 0;
        var preorders = this.pos.db.get_preorders_sorted();
        for (var i=0;i<preorders.length;i++){
            var preorder = preorders[i];
            if (preorder.state == 'to_deliver') continue;
            for (var j=0;j<preorder.lines.length;j++){
              var line = preorder.lines[j];
                if (this.product_ids.indexOf(line.product_id[0]) > -1){
                    count += line.qty;
                }
            }
        }
        this.set_count(count);
    },
});

var SmallBoxWidget = BoxWidget.extend({
    template: 'SmallBoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "Small";
    },
});
var StandardBoxWidget = BoxWidget.extend({
    template: 'StandardBoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "Standard";
    },
});
var LargeBoxWidget = BoxWidget.extend({
    template: 'LargeBoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "Large";
    },
});

chrome.Chrome.prototype.widgets.unshift({
    'name':   'large-box',
    'widget': LargeBoxWidget,
    'append':  '.pos-rightheader',
});
chrome.Chrome.prototype.widgets.unshift({
    'name':   'standard-box',
    'widget': StandardBoxWidget,
    'append':  '.pos-rightheader',
});
chrome.Chrome.prototype.widgets.unshift({
    'name':   'small-box',
    'widget': SmallBoxWidget,
    'append':  '.pos-rightheader',
});

});
