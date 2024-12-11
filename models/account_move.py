from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        if vals.get('order_id'):
            sale_order = self.env['sale.order'].browse(vals['order_id'])
            vals['narration'] = sale_order.note
        return super(AccountMove, self).create(vals)

    def write(self, vals):
        if vals.get('order_id'):
            sale_order = self.env['sale.order'].browse(vals['order_id'])
            vals['narration'] = sale_order.note
        return super(AccountMove, self).write(vals)
