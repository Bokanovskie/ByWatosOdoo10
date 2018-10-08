# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class IrAttachment(models.Model):

    _inherit = 'ir.attachment'

    website_image = fields.Boolean(string="Image pour SiteWeb", default=False)
    website_portfolio_image = fields.Boolean(string="Image pour portefolio", default=False)

    @api.onchange('website_portfolio_image')
    def _check_unique_website_portfolio_image(self):

        if self.website_portfolio_image:
            attachment_id = self.search([
                ('res_model', '=', self.res_model),
                ('res_id', '=', self.res_id),
                ('website_portfolio_image', '=', True),
                ('website_image', '=', True)
            ])

            if attachment_id:
                warning_mess = {
                    'title': _("Image portefolio déja existante !"),
                    'message': _(""),
                }

                self.website_portfolio_image = False
                return {'warning': warning_mess}
