# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderRemarks(http.Controller):
#     @http.route('/sale_order_remarks/sale_order_remarks', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_remarks/sale_order_remarks/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_remarks.listing', {
#             'root': '/sale_order_remarks/sale_order_remarks',
#             'objects': http.request.env['sale_order_remarks.sale_order_remarks'].search([]),
#         })

#     @http.route('/sale_order_remarks/sale_order_remarks/objects/<model("sale_order_remarks.sale_order_remarks"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_remarks.object', {
#             'object': obj
#         })

