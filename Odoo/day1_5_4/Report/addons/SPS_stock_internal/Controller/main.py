from odoo import http
from odoo.http import request
import json
class test(http.Controller):
   @http.route('/vu/test')
   def vuTest(self):
        return "Hello World"

   @http.route('/api/create/stock_picking', methods = ['POST'], type='http', auth='none', csrf=False, save_session=False)
   def createStockPicking(self):
       request.session.uid = 2
       request.uid = 2
       data = request.httprequest.data
       jData = json.loads(data)
       caSX = jData.get('caSX')
       productLot = jData.get('productLot')

   #     isExistPickingId = self.checkExistStockPicking(caSX,productLot)
   #     if not isExistPickingId:
   #         location_id = 4
   #         location_dest_id = 8
   #         move_type ="direct"
   #         picking_type_id = 1
   #         user_id = 2
   #         company_id = 1
   #         isExistPickingId = request.env['stock.picking'].sudo().create(
   #             {'is_locked':True,'immediate_transfer':True,'picking_type_id':1,'location_id':4,
   #              'location_dest_id':8,'scheduled_date':'2022-03-17 15:11:59','move_type':'direct','user_id':2,
   #              'company_id':1,'partner_id':False,'form_code':False,'delivery_name':False,'reason':False,'caSX':caSX,
   #              'productLot':productLot,'origin':False,'owner_id':False,'priority':False,
   #              'note':False,'message_attachment_count':0})
   def checkExistStockPicking(self, caSX, productLot):

    return request.env['stock.picking'].sudo().search([("caSX","=",caSX),("productLot","=",productLot)],limit = 1)

