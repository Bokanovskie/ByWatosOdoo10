# -*- coding: utf-8 -*-

from odoo import models, api, fields, tools
import logging

_logger = logging.getLogger(__name__)


class MailNewsletter(models.Model):

    _name = 'mail.newsletter'
    _rec_name = 'subject'

    state = fields.Selection([
        ('draft', "Brouillon"),
        ('sent', "Envoyé")
    ], default='draft')

    subject = fields.Char(string="Titre du mail", required=True)
    body_html = fields.Html(string="Corps du mail", required=True)
    email_from = fields.Char(string="De", required=True)

    template_id = fields.Many2one(
        comodel_name='mail.template',
        string="Template de mail",
        domain=[('model_id', '=', _name)]
    )

    @api.multi
    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        self.ensure_one()

        if self.template_id:
            values = self.onchange_template_id()

            for attribute, value in values.iteritems():
                setattr(self, attribute, value)

    @api.multi
    def onchange_template_id(self):

        template = self.env['mail.template'].browse(self.template_id.id)

        if template:
            attributes = ['subject', 'body_html', 'email_from']
            values = dict((attribute, getattr(template, attribute)) for attribute in attributes if getattr(template, attribute))

            if template.user_signature and 'body_html' in values:
                signature = self.env.user.signature
                values['body_html'] = tools.append_content_to_html(values['body_html'], signature, plaintext=False)

        return values

    @api.multi
    def action_send_mail(self):

        mail_obj = self.env['mail.mail']
        mail_subscribers_obj = self.env['mail.subscribers']

        mail_subscribers_list = mail_subscribers_obj.search([]).mapped('mail')

        for mail_subscriber in mail_subscribers_list:
            mail_values = {
                'email_from': self.email_from,
                'body_html': self.body_html,
                'email_to': mail_subscriber,
                'subject': self.subject,
            }

            mail_newsletter = mail_obj.create(mail_values)
            mail_newsletter.send()

        self.update({
            'state': 'sent',
        })
