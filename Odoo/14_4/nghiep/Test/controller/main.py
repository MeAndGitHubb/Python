from odoo import http
from odoo.http import request
import json, datetime

class test(http.Controller):
    @http.route('/nghiep/test', menthods=['GET'], auth='none', csrf=False)
    def nghiepTest(self):
        return "Hello World"

    @http.route('/api/select/stock_picking', menthos=['GET'], auth='none', csrf=False, save_session=False)
    def selectStockPicking(self):
        request.session.uid = 2
        request.uid = 2
        item ={}
        data = request.httprequest.data
        jData = json.loads(data)
        select_data = jData.get('select_id')
        if (request.env["stock.picking"].sudo().search([("fieldCaSX", "=", select_data)], limit=1)):
            item = {'is_locked': True, 'immediate_transfer': True, 'picking_type_id': 1, 'location_id': 4,
                 'location_dest_id': 8, 'scheduled_date': '2022-04-12 09:16:26', 'move_type': 'direct', 'user_id': 2,
                 'company_id': 1, 'partner_id': False, 'origin': False, 'fieldSoLuong': 0, 'fieldMaLo': False,
                 'fieldCaSX': False, 'fieldLyDoNhap': False, 'fieldNhan': False, 'owner_id': "", 'priority': False,
                 'note': False, 'message_attachment_count': 0}
        print (item)
        iData=json.dumps(item)
        return iData

    @http.route('/api/create/stock_picking', menthods=['POST'], auth='none', csrf=False, save_session=False)
    def createStockPicking(self):
        request.session.uid = 2
        request.uid = 2
        data = request.httprequest.data
        jData = json.loads(data)
        caSX = jData.get('caSX')
        maLo = jData.get('maLo')
        isExistPickingId = self.checkExistStockPicking(caSX, maLo)

        if not isExistPickingId:
            isExistPickingId = request.env["stock.picking"].sudo().create(
                {'is_locked': True, 'immediate_transfer': True, 'picking_type_id': 1, 'location_id': 4,
                 'location_dest_id': 8, 'scheduled_date': '2022-04-12 09:16:26', 'move_type': 'direct', 'user_id': 2,
                 'company_id': 1, 'partner_id': False, 'origin': False, 'fieldSoLuong': 0, 'fieldMaLo': maLo,
                 'fieldCaSX': caSX, 'fieldLyDoNhap': False, 'fieldNhan': False, 'owner_id': False, 'priority': False,
                 'note': False, 'message_attachment_count': 0}
            )
        elif isExistPickingId:
            request.env['stock.move'].sudo().create(
                {'name': 'đèn', 'company_id': 1, 'date_expected': datetime.datetime(2022, 4, 13, 3, 15, 55),
                 'product_id': 2, 'description_picking': 'đèn', 'product_uom': 1, 'location_id': 4,
                 'location_dest_id': 8, 'state': 'draft', 'picking_type_id': 1, 'quantity_done': 100.0,
                 'additional': False, 'extend_id': 1, 'fieldThongTin': 'Công suất 20W', 'fieldQuocGia': 'Việt Nam',
                 'picking_id': isExistPickingId.id}
            )
        print(isExistPickingId)
        return data

    def checkExistStockPicking(self, caSX, maLo):
        return request.env["stock.picking"].sudo().search([("fieldCaSX", "=", caSX), ("fieldMaLo", "=", maLo), ("state", "=", "draft")], limit=1)

    @http.route('/api/create/product', menthods=['POST'], auth='none', csrf=False, save_session=False)
    def createProduct(self):
        request.session.uid = 2
        request.uid = 2
        data = request.httprequest.data
        jData = json.loads(data)
        tenSanPham = jData.get('tenSanPham')
        loaiSanPham = jData.get('loaiSanPham')
        isExistSanPham = request.env["product.template"].sudo().search([("name", "=", tenSanPham), ("type", "=", loaiSanPham),], limit=1)

        if not isExistSanPham:
            isExistSanPham = request.env["product.template"].sudo().create(
                {'sale_ok': True, 'purchase_ok': True, 'active': True, 'type': loaiSanPham, 'categ_id': 1,
                 'list_price': 100000, 'uom_id': 1, 'uom_po_id': 1, 'sale_delay': 0, 'tracking': 'none',
                 'property_stock_production': 15, 'property_stock_inventory': 14, 'responsible_id': 2,
                 'image_1920': False, '__last_update': False, 'name': tenSanPham, 'default_code': False, 'barcode': False,
                 'standard_price': 50000, 'company_id': False, 'description': 'nón sơn', 'description_sale': False,
                 'route_ids': [[6, False, []]], 'weight': 0, 'volume': 0, 'description_pickingout': False,
                 'description_pickingin': False, 'description_picking': False, 'message_attachment_count': 0}
            )
            print(isExistSanPham)
        return data
