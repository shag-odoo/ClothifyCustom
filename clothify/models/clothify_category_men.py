from odoo import fields, models


class ClothifyCategoryMen(models.Model):
    _name = 'clothify.category.men'
    _description = 'Categories of Cloths in Clothify'

    name = fields.Char(required=True)
    size=fields.Integer()
    price=fields.Integer()
    quantity=fields.Integer()
    category=fields.Many2one('clothify.product')
    newCategory=fields.Selection(
        related='category.category_type'
    )
