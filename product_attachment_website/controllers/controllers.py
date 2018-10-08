# -*- coding: utf-8 -*-
from odoo import http

# class ProductAttachmentWebsite(http.Controller):
#     @http.route('/product_attachment_website/product_attachment_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_attachment_website/product_attachment_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_attachment_website.listing', {
#             'root': '/product_attachment_website/product_attachment_website',
#             'objects': http.request.env['product_attachment_website.product_attachment_website'].search([]),
#         })

#     @http.route('/product_attachment_website/product_attachment_website/objects/<model("product_attachment_website.product_attachment_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_attachment_website.object', {
#             'object': obj
#         })