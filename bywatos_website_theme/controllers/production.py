# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class Production(http.Controller):

    @http.route('/production_my_creation', auth='public', website=True)
    def my_production(self):

        product_obj = request.env['product.template'].sudo()
        product_ids = product_obj.search(args=[], order='create_date desc')

        values = {
            'product_ids': product_ids,
        }

        response = request.render('bywatos_website_theme.my_production_template_view', values)

        return response

    @http.route(['/shop/product/<model("product.template"):product>'], auth="public", website=True)
    def product(self, product):

        values = {
            'product': product,
        }

        response = request.render('bywatos_website_theme.product_template_view', values)

        return response
