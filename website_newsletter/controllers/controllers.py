# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import logging

_logger = logging.getLogger(__name__)


class WebsiteNewsletter(http.Controller):

    @http.route('/save-mail-news-letter', type='json', auth='public', website=True)
    def save_mail_news_letter(self, **post):

        news_letter_mail = request.params['email']
        mail_newsletter_obj = request.env['mail.subscribers']

        if news_letter_mail:

            mail_result = mail_newsletter_obj.sudo().search([
                ('mail', '=', news_letter_mail)
            ])

            if not mail_result:
                mail_newsletter_obj.sudo().create({
                    'mail': news_letter_mail
                })

                return "sucesss"

            return "error"
