from odoo import models,fields,api

class product(models.Model):

    _inherit = 'product.template'

    @api.model
    def create(self, val_list):
        print(val_list)
        return super(product, self).create(val_list)

    # fieldThuocTinh = fields.Char("Thuộc tính")
    # fieldMauSac = fields.Char("Màu sắc")
