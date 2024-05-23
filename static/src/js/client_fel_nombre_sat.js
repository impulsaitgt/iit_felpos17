odoo.define('producto_type.producto_brand_order_line', function(require) {
    "use strict";
        var models = require("point_of_sale.models")
        var _super_order = models.Order.prototype;
        models.load_fields('res.partner', 'fel_nombre_sat')
        models.Order = models.Order.extend({
            initialize:function(attr,options){
                var order=_super_order.initialize.apply(this,arguments);
                try {
                    this.fel_nombre_sat = this.attributes.client.fel_nombre_sat;
                }
                catch (error) {
                    this.fel_nombre_sat = ""

                }
            }
        })


})