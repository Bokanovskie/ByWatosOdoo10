# -*- coding: utf-8 -*-

from odoo import models


class ProductTemplate(models.Model):

    _inherit = 'product.template'
    _order = "sequence"

    def get_product_by_type(self, by_watos_type):

        template_ids = self.search([
            ('by_watos_type', '=', by_watos_type),
            ('sale_ok', '=', 'True'),
            ('active', '=', 'True'),
        ])

        return template_ids
