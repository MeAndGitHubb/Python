from odoo import models,fields,api

class stock_move_extend(models.Model):

    _name = 'stock.move.extend'


    name = fields.Char("Tên công ty")
    info= fields.Char("Thông tin")
    group= fields.Char("Nhóm")