from odoo import api,fields,models

class stock_move_extend_1(models.Model):

    _name = 'stock.move.extend.1'

    name = fields.Char("Tên Lô")
    info = fields.Text("Thông tin lô/sêri")
    group = fields.Integer("Nhóm")
#thông tin thêm ở extend