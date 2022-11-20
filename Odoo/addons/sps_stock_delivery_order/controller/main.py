from odoo import http
from odoo.http import request
import json
import datetime

class custom_warehouse(http.Controller):
    @http.route('/my/test')
    def mytest(selfs):
        return "Hello World"

    # @http.route('/api/create/stock_picking', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    # def createStockPicking(self):
    #     request.session.uid = 2
    #     request.uid = 2
    #     data = request.httprequest.data
    #     jData = json.loads(data)
    #     caSX = jData.get('caSX')
    #     productLot = jData.get('productLot')
    #
    #     isCheck = self.checkExitStockPicking(caSX,productLot)
    #     if not isCheck:
    #         isCheck = request.env['stock.picking'].sudo().create(
    #             {'is_locked': True, 'immediate_transfer': True, 'picking_type_id': 1, 'location_id': 4,
    #              'location_dest_id': 8, 'scheduled_date': '2022-03-17 14:27:28', 'move_type': 'direct',
    #              'user_id': 2, 'company_id': 1, 'partner_id': 14, 'productLot': productLot, 'origin': 'PO321',
    #              'caSX': caSX, 'owner_id': False, 'priority': False, 'note': False, 'message_attachment_count': 0})
    #     request.env['stock.move'].sudo().create(
    #         {'name': '[E-COM09] Large Desk', 'company_id': 1, 'date_expected':
    #             datetime.datetime(2022, 3, 17, 14, 39, 56), 'product_id': 19, 'description_picking': 'Large Desk',
    #          'product_uom': 1, 'location_id': 4, 'location_dest_id': 8, 'state': 'assigned', 'picking_type_id': 1,
    #          'quantity_done': 1.0, 'additional': True, 'test1': '111', 'test2': '111', 'test3': False, 'test4': False,
    #          'picking_id': isCheck.id})
    #     print(isCheck)
    #     return data
    #
    # def checkExitStockPicking(self, caSX, productLot):
    #     return request.env['stock.picking'].sudo().search([("caSX","=",caSX),("productLot","=",productLot)],limit = 1)