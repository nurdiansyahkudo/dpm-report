from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        if res.sale_id:
            res.note = res.sale_id.note
        return res
