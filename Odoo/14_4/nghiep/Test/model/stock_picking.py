from odoo import models,fields,api
class stock_picking(models.Model):

    _inherit = 'stock.picking'

    @api.model
    def create(self,val_list):
        print(val_list)
        return super(stock_picking,self).create(val_list)

    @api.model
    def edit(self, val_list):
        print(val_list)
        return super(stock_picking, self).edit(val_list)

    fieldNhan =fields.Char(string="Mã nhận")
    fieldLyDoNhap=fields.Char(string="Lý do nhập")
    fieldCaSX=fields.Char(string="Ca sản xuất")
    fieldMaLo=fields.Char(string="Mã lô")
    fieldSoLuong=fields.Integer(string="Số lượng")