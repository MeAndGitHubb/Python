from odoo import models,fields,api
import requests
import json
class stock_picking(models.Model):

    _inherit = 'stock.picking'

    test = fields.Char(string="test")
    
    @api.model
    def create(self, vals_list):
        # print(vals_list)
        # return super(stock_picking,self).create(vals_list)
        print(vals_list)
        picking_id= super(stock_picking, self).create(vals_list)
        url = "https://reqres.in/api/users"

        payload = json.dumps({
            "name": "quan",
            "job": "daaaa"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        print(response.text)
        return picking_id

    standard_id = fields.Integer(string="field_test")

    caSX=fields.Char(string="Ca sản xuất")
    productLot=fields.Char(string="Mã lô")