# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Production(http.Controller):

    @http.route('/production_my_creation', auth='public', website=True)
    def my_production(self):

        product_obj = request.env['product.template']
        product_ids = product_obj.get_product_by_type(
            by_watos_type='my_production')

        values = {
            'product_ids': product_ids,
        }

        response = request.render('bywatos_website.my_production_template_view', values)

        return response

    @http.route('/production_the_request', auth='public')
    def the_requests(self):
        product_obj = request.env['product.template']
        product_ids = product_obj.get_product_by_type(
            by_watos_type='my_production')

        values = {
            product_ids: product_ids,
        }

        response = request.render('the_requests', values)

        return response
