# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ContactUs(http.Controller):

    @http.route('/contact-us', type='http', auth='public', website=True)
    def contact_us(self):

        response = request.render('bywatos_website_theme.contact_us_template')

        return response

    @http.route('/send-contact', type='http', auth='public', website=True)
    def send_contact(self, **post):

        mail_obj = request.env['mail.mail']

        subject_str = "Prise de contact par {0} {1}".format(request.params['civility'], request.params['name'])

        mail_values = {
            'subject': subject_str,
            'email_from': request.params['email'],
            'body_html': request.params['message'],
        }

        mail_to_send = mail_obj.sudo().create(mail_values)
        mail_to_send.send()
