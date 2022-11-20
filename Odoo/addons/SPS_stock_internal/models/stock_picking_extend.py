from odoo import api,fields,models

class stock_picking_extend(models.Model):
    _name = 'stock.picking.extend'

    name = fields.Char(string="Tên Công Ty")
    address = fields.Char(string="Địa chỉ công ty")
