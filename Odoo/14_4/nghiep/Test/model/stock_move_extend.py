from odoo import models,fields,api
class stock_move_extend(models.Model):

    _name = 'stock.move.extend'

    fieldNhom = fields.Char("Nhóm")
    fieldHoTen = fields.Char("Họ Tên ")
    fieldNgaySinh = fields.Date("Ngày Sinh")