from odoo import api,fields,models

class stock_move(models.Model):

    @api.model
    def create(self, vals_list):
        return super(stock_move, self).create(vals_list)

    _inherit = 'stock.move'
    extend_id = fields.Many2one("stock.move.extend","Extend")
    new_field = fields.Many2one("stock.move.extend.1","Số lô/sê ri")