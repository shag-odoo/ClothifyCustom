from odoo import models, fields


class ClothifyCart(models.Model):
    _name = 'clothify.cart'
    _description = 'Cart Model'

    # CUSTOMER DETAILS
    customer_name=fields.Char()
    customer_address=fields.Text()
    customer_mobile=fields.Integer()
    cart_quantity=fields.Integer()
    cart_total =fields.Integer()
    product_name=fields.Char()
    cart_price=fields.Integer()
    product_ids=fields.One2many('clothify.product','link_id')

