# -*- coding: utf-8 -*-

from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def get_portefolio_img(self, size=False):

        ir_attachment_obj = self.env['ir.attachment']

        ir_attachment_id = ir_attachment_obj.search([
            ('res_model', '=', self._name),
            ('res_id', '=', self.id),
            ('website_portfolio_image', '=', True),
            ('website_image', '=', True),
            ('image_size', '=', size)
        ])

        return ir_attachment_id.id

    def get_images_product(self):

        ir_attachment_obj = self.env['ir.attachment']

        ir_attachment_ids = ir_attachment_obj.search([
            ('res_model', '=', self._name),
            ('res_id', '=', self.id),
            ('website_image', '=', True),
            ('website_product_details', '=', True)
        ])

        return ir_attachment_ids

    @api.multi
    def action_open_attachments(self):
        self.ensure_one()
        return {
            'name': "",
            'domain': [('res_model', '=', self._name), ('res_id', '=', self.id)],
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'view_type': 'form',
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (
                self._name, self.id),
        }
