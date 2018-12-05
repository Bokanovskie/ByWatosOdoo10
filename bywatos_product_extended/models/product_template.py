# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    by_watos_type = fields.Selection(
        [('my_production', "Mes productions"),
         ('the_requests', "Les demandes")],
        string="Types By Watos"
    )

    website_description = fields.Html(string="Description website")
