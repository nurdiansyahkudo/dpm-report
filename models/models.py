# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderRemarks(models.Model):
    
    _inherit = 'sale.order'

  # Untuk Brand
    brand = fields.Char(
        string='Brand',
        compute="_compute_brand",
        search="_search_brand",  # Menambahkan fungsi pencarian 
        store=True,  # Store is set to True for better performance
    )

    @api.depends('order_line')
    def _compute_brand(self):
        for record in self:
            brands = []
            
            # Cek setiap baris di Sales Order
            for sale_line in record.order_line:
                if sale_line.product_id:
                    # Ambil brand dari atribut produk pada sale.order.line
                    brand_value = sale_line.product_id.product_tmpl_id.attribute_line_ids.filtered(
                        lambda x: x.attribute_id.name == 'Brand'
                    ).mapped('value_ids.name')
                    brands.extend(brand_value)  # Tambahkan brand ke dalam daftar     

            # Menggabungkan daftar brand menjadi string unik
            record.brand = ', '.join(set(brands)) if brands else 'No Brand'
