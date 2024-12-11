from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        if vals.get('sale_id'):
            sale_order = self.env['sale.order'].browse(vals['sale_id'])
            vals['note'] = sale_order.note
        return super(StockPicking, self).create(vals)

    def write(self, vals):
        if vals.get('sale_id'):
            sale_order = self.env['sale.order'].browse(vals['sale_id'])
            vals['note'] = sale_order.note
        return super(StockPicking, self).write(vals)
