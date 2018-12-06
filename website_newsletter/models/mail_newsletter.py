# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class MailNewsletter(models.Model):

    _name = 'mail.newsletter'

    state = fields.Selection([
        ('draft', "Brouillon"),
        ('sent', "Envoyée")
    ], default='draft')

    name = fields.Char(string="Titre du mail")

    mail_body = fields.Html(string="Corps du mail")

    @api.multi
    def action_send_mail(self):
        pass
