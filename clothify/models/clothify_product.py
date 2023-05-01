from odoo import models, fields


class ClothifyProduct(models.Model):
    _name = 'clothify.product'
    _description = 'Product Module'

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Integer()
    size = fields.Integer()
    quantity=fields.Integer()
    Active=fields.Boolean(default=True)
    color = fields.Selection(
        selection=[
            ('black', 'Black'),
            ('white', 'White'),
            ('blue', 'Blue'),
            ('grey', 'Grey')
        ],
        default='black'
    )
    state=fields.Selection(
        selection=[
            ('new','New'),
            ('cart','Add to Cart'),
            ('delivered','Delivered'),
            ('return','Return'),
        ],
        default='new',
    )
