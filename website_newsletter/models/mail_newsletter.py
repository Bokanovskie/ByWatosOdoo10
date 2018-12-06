# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class MailNewsletter(models.Model):

    _name = 'mail.newsletter'

    title = fields.Char(string="Titre du mail")

    mail_body = fields.Html(string="Corps du mail")
