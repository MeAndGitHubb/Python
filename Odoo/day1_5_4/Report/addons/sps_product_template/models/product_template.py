from odoo import models, fields, api
class product_template(models.Model):

    _inherit = 'product.template'

    @api.model
    def create(self, vals_list):
        return super(product_template, self).create(vals_list)

    luongsudungtoithieu = fields.Char(string="Lượng dùng tối thiếu 1 ngày")
    luongtoncanhbao = fields.Char(string="Lượng tồn cảnh báo")
    luongtondu = fields.Char(string = "Lượng tồn dư")