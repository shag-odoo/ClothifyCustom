from odoo import fields, models


class ClothifyCategoryWomen(models.Model):
    _name = 'clothify.category.women'
    _description = 'Categories of Cloths in Clothify'

    name = fields.Char(required=True)
    