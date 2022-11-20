from odoo import models,fields,api,_

class stock_picking(models.Model):

    _inherit = 'stock.picking'

    @api.model
    def create(self, vals_list):
        print(vals_list)
        return super(stock_picking, self).create(vals_list)
#tạo field
    standard_reason = fields.Text(string="Lý do điều chuyển")
    lenhxuatkho = fields.Text(string="Lệnh xuất kho số")
    operation_type = fields.Many2one("stock.move.extend","Kiểu hoạt động")
    code = fields.Char("Mã phiếu")
    product_group = fields.Char(string="Nhóm sản phẩm")
    delivery_name = fields.Char(string="Họ tên người giao")
    order_code = fields.Char(string="Mã đơn đặt hàng")
    PTVC = fields.Char(string="PTVC")
    ten_nguoi_vc = fields.Char(string="Tên người vận chuyển")

    @api.model
    def test_cron_job(self):
        print("Abcd")




