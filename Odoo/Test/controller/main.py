import datetime
from odoo import http
from odoo.http import request
import json
# from fastapi import FastAPI

# app=FastAPI();
# @app.get("/api/create/fastapi")
# async def home():
#     return "Hello World"
class test(http.Controller):
    @http.route('/quan/test')
    def quanTest(self):
        return "Hello World"

    @http.route('/api/create/stock_picking', menthod=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def createStockPicking(self):
        request.session.uid = 2
        request.uid = 2
        data = request.httprequest.data
        jData= json.loads(data)
        caSX=jData.get('caSX')
        productLot= jData.get('productLot')
        isExistPickingId= self.checkExisStockPicking(caSX,productLot)

        if not isExistPickingId:
            location_id=4
            location_dest_id=8
            move_type="direct"
            picking_type_id=1
            user_id=2
            company_id=1
            # isExistPickingId= request.env["stock.picking"].sudo().create({"caSX":caSX,
            #                                                               "productLot":productLot,
            #                                                               "location_id":location_id,
            #                                                               "location_dest_id":location_dest_id,
            #                                                               "move_type":move_type,
            #                                                               "picking_type_id":picking_type_id,
            #                                                               "user_id":user_id,
            #                                                               "company_id":company_id})
            isExistPickingId = request.env["stock.picking"].sudo().create(
                {'is_locked': True, 'immediate_transfer': True, 'picking_type_id': 1, 'location_id': 4,
                 'location_dest_id': 8, 'scheduled_date': '2022-04-06 06:20:04', 'move_type': 'direct', 'user_id': 2,
                 'company_id': 1, 'partner_id': False, 'origin': False, 'productLot': productLot, 'caSX': caSX,
                 'standard_id': 0, 'owner_id': False, 'priority': False, 'note': False, 'message_attachment_count': 0}
            )
        request.env['stock.move'].sudo().create(
            {'name': 'My Company', 'company_id': 1, 'date_expected': datetime.datetime(2022, 4, 6, 8, 25, 48),
             'product_id': 37, 'description_picking': 'My Company', 'product_uom': 1, 'location_id': 4,
             'location_dest_id': 8, 'state': 'draft', 'picking_type_id': 1, 'quantity_done': 0.0, 'additional': False,
             'extend_id': False, 'new_field': 'fdsfs', 'picking_id': isExistPickingId.id}
        )
        print(isExistPickingId)
        return data

    def checkExisStockPicking(self, caSx, productLot):
        return request.env["stock.picking"].sudo().search([("caSX","=",caSx),("productLot","=",productLot),("state","=","draft")],limit=1)
