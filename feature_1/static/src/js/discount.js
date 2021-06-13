odoo.define('feature_1.feature_1', function(require) {
    var core = require('web.core');
    var models = require('point_of_sale.models');
    var bankdisc = 15;
    var vbankdisc = false;
    models.Order = models.Order.extend({
        add_paymentline: function(payment_method) {
            this.assert_editable();
            var newPaymentline = new models.Paymentline({}, { order: this, payment_method: payment_method, pos: this.pos });
            var orderline = this.get_orderlines();
            if (vbankdisc) {
                vbankdisc = false;
                for (var i = 0; i < orderline.length; i++) {
                    orderline[i].set_discount(orderline[i].get_discount() - bankdisc);
                }
            }
            if (!payment_method.is_cash_count || this.pos.config.iface_precompute_cash) {
                vbankdisc = true;
                for (var i = 0; i < orderline.length; i++) {
                    orderline[i].set_discount(orderline[i].get_discount() + bankdisc);
                }
                newPaymentline.set_amount(this.get_due());
            };
            this.paymentlines.add(newPaymentline);
            this.select_paymentline(newPaymentline);
        }
    });
});