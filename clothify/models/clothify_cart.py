from odoo import models, fields,api


class ClothifyCart(models.Model):
    _name = 'clothify.cart'
    _description = 'Cart Model'
    _sql_constraints = [
        ('check_quantity', 'CHECK(cart_quantity >= 0)',
         'Quantity Should be positive'),
         ('check_price','CHECK(cart_price>0)',
         'Price Should be more than zero')
    ]

    # CUSTOMER DETAILS
    customer_name=fields.Char(required=True)
    customer_address=fields.Text()
    customer_mobile=fields.Integer()
    cart_quantity=fields.Integer()
    cart_total =fields.Integer(compute='_compute_cart_total')
    product_name=fields.Many2one('clothify.product')
    cart_price=fields.Integer()
    # product_ids=fields.One2many('clothify.product','link_id')

    @api.depends('cart_quantity','cart_price')
    def _compute_cart_total(self):
        for record in self:
            record.cart_total=record.cart_quantity*record.cart_price
