# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
import logging

_logger = logging.getLogger(__name__)


class WebsiteInherited(Website):

    @http.route()
    def index(self, **kw):

        response = request.render('bywatos_website_theme.homepage_template')

        return response

    @http.route('/get_video', type="json", auth="public", website=True)
    def get_iframe(self):

        website_config = request.env['website'].sudo().search([])

        url = website_config.url_video_configuration

        return url
