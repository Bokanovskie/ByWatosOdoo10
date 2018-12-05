# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteNewsletter(http.Controller):
#     @http.route('/website_newsletter/website_newsletter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_newsletter/website_newsletter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_newsletter.listing', {
#             'root': '/website_newsletter/website_newsletter',
#             'objects': http.request.env['website_newsletter.website_newsletter'].search([]),
#         })

#     @http.route('/website_newsletter/website_newsletter/objects/<model("website_newsletter.website_newsletter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_newsletter.object', {
#             'object': obj
#         })