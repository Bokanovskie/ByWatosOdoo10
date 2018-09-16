# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ContactUs(http.Controller):
    @http.route('/contact-us', type='http', auth='public', website=True)
    def contact_us(self):
        values = {

        }

        response = request.render('website.contactus', values)

        return response
