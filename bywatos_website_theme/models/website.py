# -*- coding: utf-8 -*-

from odoo import models, fields


class WebsiteConfig(models.TransientModel):

    _inherit = 'website.config.settings'

    url_video_configuration = fields.Char(related='website_id.url_video_configuration', string="Url vidéo")


class Website(models.Model):

    _inherit = 'website'

    url_video_configuration = fields.Char(string="Url vidéo")

