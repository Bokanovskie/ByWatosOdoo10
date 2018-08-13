# -*- coding: utf-8 -*-

from odoo import models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def get_product_by_type(self, by_watos_type):

        template_obj = self.env['product.template']
        template_ids = template_obj.search([
            ('by_watos_type', '=', by_watos_type),
            ('sale_ok', '=', 'True'),
            ('active', '=', 'True'),
            ('website_published', '=', 'True')
        ])

        return template_ids
