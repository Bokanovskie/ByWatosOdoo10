# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
import logging

_logger = logging.getLogger(__name__)


class WebsiteInherited(Website):

    @http.route()
    def index(self, **kw):

        response = request.render('bywatos_website.homepage_template')

        return response
