from odoo import api,fields,models

class stock_move_extend(models.Model):

    _name = 'stock.move.extend'

    info = fields.Text("Thông tin nhập")
    group = fields.Integer("Nhóm")
    note = fields.Text("Ghi chú")
    weight = fields.Float("Cân nặng sản phẩm")
    lenhxuatkho = fields.Char("lệnh xuất kho số")
    name = fields.Char("Kiểu hoạt động")
    operation_type = fields.Many2one("stock.move.extend","Kiểu hoạt động")
    text = fields.Text("Mô tả")
    reference = fields.Char(string="PDC", required=True, copy=False, readonly =True,default='New')




    
