import datetime

from odoo import http
from odoo.http import request
import json
import requests


class custom_inventory_controller(http.Controller):
    @http.route('/vu/test', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def vuTest(self):
        url ="http://fsd.fast.com.vn/FEED1/categories"
        payload = json.dumps({
            "items"[
                {
                    "controller" : "setCustomer"
                    "data"[
                    {
                        "wms_id":"",
                        "code":"",
                        "name": "",
                        "is_vendor":"",
                        "is_customer":"",
                        "billing_address":"",
                        "delivery_address":"",
                        "tax_code": "",
                        "email": "",
                        "phone": "",
                        "active": "",
                    }
                ]
            }
            ]
        })
        headers = {
            "Token": "K5191cfe497d075fb41c07a668eb506k",
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        print(response.text)
        return json.dumps(response.requests)

    @http.route('/vu/test', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def vuTest(self):
        url = "http://fsd.fast.com.vn/FEED1/categories"
        payload = json.dumps({
            "items"[
                {
                    "controller": "setCustomer"
                    "data"[
                        {
                            "wms_id": "",
                            "code": "",
                            "name": "",
                            "address":"",
                            "active": ""
                        }
                    ]
                }
            ]
        })
        headers = {
            "Token": "K5191cfe497d075fb41c07a668eb506k",
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        print(response.text)
        return json.dumps(response.requests)

    @http.route('/vu/test', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def checkExistResPartner(self,wms_id,code,name,is_vendor,is_customer,billing_address,delivery_address,tax_code,email,phone,active):
        return request.env['res.partner'].sudo().search(
            [("wms_id", "=", wms_id), ("code", "=", code), ("name", "=", name),("is_vendor", "=", is_vendor),("is_customer", "=", is_customer)],
            limit=1)




    @http.route('/api/create/stock_picking', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def createStockPicking(self):
        request.session.uid = 2
        request.uid = 2
        data = request.httprequest.data
        jData = json.loads(data)
        lot_number = jData.get('lot_number')
        material_number = jData.get('material_number')

        isExistPickingId = self.checkExistStockPicking(lot_number, material_number)
        # limit = 1, order = "id desc"])
        recordset = request.env['stock.picking'].sudo().search([('id', '!=', False)],  limit=1, order = "id desc")
        print("recordset")
        print(recordset)
        if not isExistPickingId:
            location_id = 4
            location_dest_id = 8
            move_type = "direct"
            picking_type_id = 1
            user_id = 2
            company_id = 1
            # isExistPickingId = request.env['stock.picking'].sudo().create(
            #     {"caSX": caSX, "productLot": productLot, "location_id": location_id,
            #      "location_dest_id": location_dest_id,
            #      "move_type": move_type,
            #      "picking_type_id":picking_type_id,
            #      "user_id":user_id,
            #      "company_id":company_id
            #      })

            isExistPickingId = request.env['stock.picking'].sudo().create(
                {'is_locked': True, 'immediate_transfer': True, 'picking_type_id': 1, 'location_id': location_id,
                 'location_dest_id': location_dest_id, 'scheduled_date': '2022-02-22 15:11:59', 'move_type': 'direct', 'user_id': 2,
                 'company_id': 1, 'partner_id': False, 'form_code': False, 'delivery_name': False, 'reason': False,
                 'caSX': material_number, 'productLot': lot_number, 'origin': False, 'owner_id': False, 'priority': False,
                 'note': False, 'message_attachment_count': 0})

        request.env['stock.move'].sudo().create(
            {'name': 'aaaaaaa', 'company_id': 1, 'date_expected': datetime.datetime(2022, 2, 22, 15, 22, 30),
             'product_id': 1, 'description_picking': 'test', 'product_uom': 1, 'location_id': 4,
             'location_dest_id': 8, 'state': 'draft', 'picking_type_id': 1, 'quantity_done': 0.0, 'additional': False,
             'extend_id': False, 'new_field': False, 'picking_id': isExistPickingId.id})
        object_response = {
            "wms_id": recordset.id+1
        }
        print(isExistPickingId)
        return json.dumps(object_response)

    @http.route('/api/customSPS/UpdateWeightDataToStock', methods=['POST'], type='http', auth='none', csrf=False, save_session=False)
    def update_weight_data_stock(self):
        request.session.uid = 2
        request.uid = 2
        data = request.httprequest.data
        print(data)
        jData = json.loads(data)
        lotNumber = jData.get('lotNumber')

        object_response = {
            "wms_id": 1
        }
        return json.dumps(object_response)

    def checkExistStockPicking(self, caSX, productLot):
        return request.env['stock.picking'].sudo().search([("caSX", "=", caSX), ("productLot", "=", productLot), ("state", "=", "draft")],
                                                          limit=1)
