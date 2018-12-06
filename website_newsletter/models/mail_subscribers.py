# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
import logging

_logger = logging.getLogger(__name__)


class MailSubscribers(models.Model):

    _name = 'mail.subscribers'

    mail = fields.Char(string="Adresse mail", required=True)
