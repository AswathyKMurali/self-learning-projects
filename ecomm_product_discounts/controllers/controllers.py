# -*- coding: utf-8 -*-
# from odoo import http


# class EcommProductDiscounts(http.Controller):
#     @http.route('/ecomm_product_discounts/ecomm_product_discounts', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecomm_product_discounts/ecomm_product_discounts/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecomm_product_discounts.listing', {
#             'root': '/ecomm_product_discounts/ecomm_product_discounts',
#             'objects': http.request.env['ecomm_product_discounts.ecomm_product_discounts'].search([]),
#         })

#     @http.route('/ecomm_product_discounts/ecomm_product_discounts/objects/<model("ecomm_product_discounts.ecomm_product_discounts"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecomm_product_discounts.object', {
#             'object': obj
#         })

