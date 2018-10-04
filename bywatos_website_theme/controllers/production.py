# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Production(http.Controller):

    @http.route('/production_my_creation', auth='public', website=True)
    def my_production(self):

        product_obj = request.env['product.template'].sudo()
        product_ids = product_obj.search([])

        values = {
            'product_ids': product_ids,
            'html_test': '<h1>TEST TEST<h1>'
        }

        response = request.render('bywatos_website_theme.my_production_template_view', values)

        return response
