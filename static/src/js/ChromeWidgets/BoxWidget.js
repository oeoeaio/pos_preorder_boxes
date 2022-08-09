odoo.define('point_of_sale.BoxWidget', function(require) {
    'use strict';

    const { useState } = owl;
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class BoxWidget extends PosComponent {
        constructor() {
            super(...arguments);

            this.state = useState({
              count: 0,
            });

            this.updateCount();

            this.env.pos.on('preorders:updated',this.updateCount,this);
        }
        updateCount() {
            var newCount = 0;
            var preorders = this.env.pos.db.get_preorders_sorted();
            var count_property = this.props.size+'_count';
            for (var i=0;i<preorders.length;i++){
                var preorder = preorders[i];
                if (preorder.state == 'to_deliver') continue;
                newCount += preorder[count_property];
            }
            this.state.count = newCount;
        }
    }
    BoxWidget.template = 'BoxWidget';

    Registries.Component.add(BoxWidget);

    return BoxWidget;
});
