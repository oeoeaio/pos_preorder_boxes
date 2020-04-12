odoo.define('pos.preorder.box_widgets', function (require) {
"use strict";

var chrome = require('point_of_sale.chrome');

var BoxWidget = chrome.StatusWidget.extend({
    start: function(){
        var self = this;

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
    count_boxes: function(){
        var count = 0;
        var preorders = this.pos.db.get_preorders_sorted();
        var count_property = this.size+'_count';
        for (var i=0;i<preorders.length;i++){
            var preorder = preorders[i];
            if (preorder.state == 'to_deliver') continue;
            count += preorder[count_property];
        }
        this.set_count(count);
    },
});

var SmallBoxWidget = BoxWidget.extend({
    template: 'BoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "small";
    },
});
var StandardBoxWidget = BoxWidget.extend({
    template: 'BoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "standard";
    },
});
var LargeBoxWidget = BoxWidget.extend({
    template: 'BoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "large";
    },
});
var FruitBoxWidget = BoxWidget.extend({
    template: 'BoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "fruit";
    },
});
var LargeFruitBoxWidget = BoxWidget.extend({
    template: 'BoxWidget',
    init: function(parent, options) {
        this._super(parent, options);
        this.size = "large_fruit";
    },
});

chrome.Chrome.prototype.widgets.unshift({
    'name':   'large-fruit-box',
    'widget': LargeFruitBoxWidget,
    'append':  '.pos-rightheader',
});
chrome.Chrome.prototype.widgets.unshift({
    'name':   'fruit-box',
    'widget': FruitBoxWidget,
    'append':  '.pos-rightheader',
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
