from odoo import models,fields,api

class stock_move_extend_3(models.Model):

    _name = 'stock.move.extend.3'
    name = fields.Char(string='Kiểu hoạt động')