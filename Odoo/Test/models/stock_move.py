from odoo import models,fields,api

class stock_move(models.Model):

    @api.model
    def create(self, vals_list):
        print(vals_list)
        return super(stock_move, self).create(vals_list)

    _inherit = 'stock.move'
    #layout dưới
    extend_id = fields.Many2one("stock.move.extend","Extend")
    new_field = fields.Char("Chi tiết sản phẩm")