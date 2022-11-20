from odoo import models,fields,api
class stock_move(models.Model):

    _inherit = 'stock.move'

    @api.model
    def create(self, val_list):
        print(val_list)
        return super(stock_move, self).create(val_list)

    Extend = fields.Many2one("stock.move.extend", "Mở rộng")

    fieldThongTin = fields.Char(string="Thông tin sản phẩm")
    fieldQuocGia = fields.Char(string="Quốc gia")