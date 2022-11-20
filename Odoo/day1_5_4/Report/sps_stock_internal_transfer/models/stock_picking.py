from odoo import models,fields,api,_
import json
import requests

class stock_picking(models.Model):

    _inherit = 'stock.picking'

    # @api.model
    # def create(self, vals_list):
    #     print(vals_list)
    #     return super(stock_picking, self).create(vals_list)

    @api.model
    def create(self, vals_list):
        print(vals_list)
        picking_id = super(stock_picking, self).create(vals_list)
        url = "https://assets.vinhhoan.com.vn/api/warehouse.php?type=export&token=23j8kn28fjulcbam8@82f78ik2"

        payload = json.dumps({
            "1": {
                "Resquest": "",
                "Code": "",
                "Name": "",
                "Unit": "",
                "Quantity": "",
                "Note": "",
                "Time": ""
            },
            "2": {
                "Resquest": "",
                "Code": "",
                "Name": "",
                "Unit": "",
                "Quantity": "",
                "Note": "",
                "Time": ""
            }
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        print(response.text)
        return picking_id
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






