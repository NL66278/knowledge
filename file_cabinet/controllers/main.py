# -*- coding: utf-8 -*-
# Copyright 2017 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.http import request


class Main(http.Controller):
    @http.route('/file_cabinet/files', type='http', auth='user')
    def files(self):
        """Serve files from file cabinet."""
        result = (
            "<html><body>"
            "<h1>List of files</h1>"
            "<p>Files</p>"
            "</body></html>")
        return result
