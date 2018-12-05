# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class MailNewsLetter(models.Model):

    _name = 'mail.newsletter'

    mail = fields.Char(string="Adresse mail", required=True)
