from odoo import models,fields,api,_
import json
import requests

class res_partner(models.Model):
    _inherit = 'res.partner'
    @api.model
    def create(self, vals_list):
        print(vals_list)
        return super(res_partner, self).create(vals_list)