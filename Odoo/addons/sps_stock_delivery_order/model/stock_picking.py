from odoo import models,fields,api,_

class stock_picking(models.Model):

    _inherit = 'stock.picking'
    xuat_theo_yc = fields.Char(string="Xuất theo yêu cầu của bộ phận/ xưởng")
    lenh_xuat_kho = fields.Char(string="Lệnh xuất kho số")
    bien_so = fields.Char(string="PTVC")
    ten_nguoi_vc = fields.Char(string="Người vận chuyển")

