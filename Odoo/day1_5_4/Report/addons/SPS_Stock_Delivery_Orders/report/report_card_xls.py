from odoo import models


class ReportCardXLS(models.AbstractModel):
    _name = 'report.report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        # sheet = workbook.add_worksheet('Phiếu xuất kho')
        # bold = workbook.add_format({'bold': True})
        # row = 6
        # col = 3

        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            # sheet.write(0, 0, obj.name, bold)
            sheet.set_column('B:B', 60)
            sheet.set_column('C:C', 20)
            # title
            sheet.merge_range(6,1,6,5,'PHIẾU XUẤT KHO',bold)
            # date
            ngay = str(obj.scheduled_date.day)
            thang = str(obj.scheduled_date.month)
            nam = str(obj.scheduled_date.year)
            # left
            sheet.merge_range(7,1,7,5,'Ngày'+' '+ ngay +' '+'Tháng'+' ' + thang+ ' ' + 'Năm'+ ' ' + nam)
            sheet.merge_range(8, 1, 8, 5, 'Số:' + ' ' + obj.name)
            sheet.write(10, 1, 'Khách hàng:' + ' ' + obj.partner_id.name)
            sheet.write(11, 1, 'Lý do xuất:' + ' ' + obj.operation_type.name)
            sheet.write(12, 1, 'Người vận chuyển:' + ' ' + obj.ten_nguoi_vc)
            sheet.write(13, 1,'Xuất tại kho(ngăn lô):' + ' ' + obj.location_id.location_id.name + '/' + obj.location_id.name)
            # right
            sheet.merge_range(10, 2, 10, 4, 'Xuất theo yêu cầu của bộ phận/ xưởng:' + ' ' + obj.xuat_theo_yc)
            sheet.merge_range(11, 2, 11, 4, 'Phương tiện vận chuyển:' + ' ' + obj.bien_so)
            sheet.merge_range(12, 2, 12, 4, 'Lệnh xuất kho số:' + ' ' + obj.lenh_xuat_kho)
            # table

            sheet.merge_range(15,0,16,0,'STT')
            sheet.merge_range(15,1, 16,1, 'Tên, nhãn hiệu, quy cách, phẩm chất vật tư (sản phẩm, hàng hóa)')
            sheet.merge_range(15,2, 16, 2, 'Số Lô/sê ri')
            sheet.merge_range(15, 3, 16, 3, 'ĐVT')
            sheet.merge_range(15, 4, 15, 6, 'Số lượng')
