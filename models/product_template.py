from odoo import fields, models

class ProductTemplate(models.Model):
  _inherit = "product.template"

  list_price = fields.Float(
        'Sales Price', default=1.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.",
        groups="account.group_account_manager, sale.group_sale_manager",
    )
  standard_price = fields.Float(
        'Cost', compute='_compute_standard_price',
        inverse='_set_standard_price', search='_search_standard_price',
        digits='Product Price', groups="stock.group_stock_manager, account.group_account_manager",
        help="""Value of the product (automatically computed in AVCO).
        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
        Used to compute margins on sale orders.""",
        invisible="1")