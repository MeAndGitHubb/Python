from odoo import models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        self.ensure_one()
        if self._context.get('open_stock_picking_backdate_wizard', False)\
            and not self._context.get('manual_validate_date_time', False)\
            and self.env.user.has_group('to_backdate.group_backdate'):
            view = self.env.ref('to_stock_picking_backdate.view_stock_picking_backdate_form')
            ctx = dict(self._context or {})
            ctx.update({'default_picking_id': self.id})
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'stock.picking.backdate',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': ctx,
            }
        return super(StockPicking, self).button_validate()

    def action_done(self):
        res = super(StockPicking, self).action_done()
        manual_validate_date_time = self._context.get('manual_validate_date_time', False)
        if manual_validate_date_time:
            self.filtered(lambda x: x.state == 'done').write({'date_done': manual_validate_date_time})
        return res
