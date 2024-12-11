from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        if 'invoice_origin' in vals:
            sale_order = self.env['sale.order'].search([('name', '=', vals['invoice_origin'])], limit=1)
            if sale_order:
                vals['narration'] = sale_order.note
        return super(AccountMove, self).create(vals)
