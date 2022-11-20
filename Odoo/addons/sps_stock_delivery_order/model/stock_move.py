from odoo import models,fields,api

class stock_move(models.Model):

    _inherit = 'stock.move'

    @api.model
    def create(self, vals_list):
        print(vals_list)
        return super(stock_move, self).create(vals_list)

    can_xe = fields.Char(string="Cân xe")
    bao_bi = fields.Char(string="Bao bì")
    luong_thuc_xuat = fields.Char(string="Lượng thực xuất")