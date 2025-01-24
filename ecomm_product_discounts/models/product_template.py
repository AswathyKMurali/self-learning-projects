# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float(
        string="Discount Percentage",
        default=0.0,
        help="Set a discount percentage for the product. 0 means no discount."
    )
    discounted_price = fields.Float(
        string="Discounted Price",
        compute="_compute_discounted_price",
        store=True,
    )

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage > 0:
                discount = (product.list_price * product.discount_percentage) / 100
                product.discounted_price = product.list_price - discount
            else:
                product.discounted_price = product.list_price


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _onchange_product_id_set_price(self):
        super(SaleOrderLine, self)._onchange_product_id_set_price()
        if self.product_id and self.product_id.discount_percentage > 0:
            self.price_unit = self.product_id.discounted_price
