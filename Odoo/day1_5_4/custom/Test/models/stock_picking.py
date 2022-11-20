from odoo import models,fields,api

class stock_picking(models.Model):

    _inherit = 'stock.picking'

    test = fields.Char(string="test")

    @api.model
    def create(self, vals_list):
        print(vals_list)
        return super(stock_picking,self).create(vals_list)