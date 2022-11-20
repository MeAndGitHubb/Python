from odoo import http

class test(http.Controller):
    @http.route('/quan/test')
    def quanTest(self):
        return "Hello World"