from odoo import models, fields, api



class product(models.Model):
    _inherit = 'product.template'

    def create(self, vals_list):
        print(vals_list)
        return super(product,self).create(vals_list)

    luong_ton_an_toan = fields.Char(string="Thời gian Sử dụng Sản phẩm")
    luong_su_dung_toi_thieu_1_ngay = fields.Char(string="Tuổi thọ sản phẩm")
    luong_to_canh_bao = fields.Char(string="Thời gian Loại bỏ Sản Phẩm")
    luong_to_du = fields.Char(string="Thời gian Cảnh báo Sản phẩm")
