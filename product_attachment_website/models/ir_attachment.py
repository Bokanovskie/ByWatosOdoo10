# -*- coding: utf-8 -*-

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from PIL import Image
from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class IrAttachment(models.Model):

    _inherit = 'ir.attachment'
    _order = 'sequence, id'

    sequence = fields.Integer('Sequence', default=1)

    website_image = fields.Boolean(string="Image pour SiteWeb", default=False)
    website_portfolio_image = fields.Boolean(string="Image pour portefolio", default=False)
    website_product_details = fields.Boolean(string="Image pour page produit", default=False)

    compress_image_file = fields.Boolean(string="Compresser l'image", default=False)
    compress_rate = fields.Float(string="Taux de compression", default=50)

    image_size = fields.Selection([
        ('width_and_long', "Image longueur"),
        ('width_and_height', "Image haute"),
        ('width_and_small', "Image petite"),
    ])

    @api.model
    def create(self, values):
        # remove computed field depending of datas
        for field in ('file_size', 'checksum'):
            values.pop(field, False)

        values = self._check_contents(values)
        self.browse().check('write', values=values)

        if values.get('compress_image_file'):
            values = self.handle_image(values, values.get('compress_rate'), values.get('compress_image_file'))

        return super(IrAttachment, self).create(values)

    @api.multi
    def write(self, vals):
        self.check('write', values=vals)

        # remove computed field depending of datas
        for field in ('file_size', 'checksum'):
            vals.pop(field, False)

        if 'mimetype' in vals or 'datas' in vals:
            vals = self._check_contents(vals)

        if vals.get('compress_image_file') or self.compress_image_file:
            compress_image = vals.get('compress_image_file') if 'compress_image_file' in vals else self.compress_image_file
            quality = int(vals.get('compress_rate') if 'compress_rate' in vals else self.compress_rate)

            vals = self.handle_image(vals, quality, compress_image)

        return super(IrAttachment, self).write(vals)

    def handle_image(self, vals, quality, compress_image):
        if vals.get('datas') and compress_image:
            image_stream = StringIO.StringIO(vals.get('datas').decode('base64'))

            image = Image.open(image_stream)
            background_stream = StringIO.StringIO()

            image.save(background_stream, "Jpeg", optimize=True, quality=quality)

            vals.update(
                {
                    'datas': background_stream.getvalue().encode('base64')
                }
            )

        return vals

    @api.onchange('website_portfolio_image', 'image_size')
    def _check_unique_website_portfolio_image(self):

        if self.website_portfolio_image and self.image_size:
            attachment_id = self.search([
                ('res_model', '=', self.res_model),
                ('res_id', '=', self.res_id),
                ('website_portfolio_image', '=', True),
                ('website_image', '=', True),
                ('image_size', '=', self.image_size)
            ])

            if attachment_id:
                warning_mess = {
                    'title': _("Image portefolio déja existante !"),
                    'message': _(""),
                }

                self.website_portfolio_image = False
                self.image_size = False

                return {'warning': warning_mess}
