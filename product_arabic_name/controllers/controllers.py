# -*- coding: utf-8 -*-
# from odoo import http


# class ProductArabicName(http.Controller):
#     @http.route('/product_arabic_name/product_arabic_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_arabic_name/product_arabic_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_arabic_name.listing', {
#             'root': '/product_arabic_name/product_arabic_name',
#             'objects': http.request.env['product_arabic_name.product_arabic_name'].search([]),
#         })

#     @http.route('/product_arabic_name/product_arabic_name/objects/<model("product_arabic_name.product_arabic_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_arabic_name.object', {
#             'object': obj
#         })
