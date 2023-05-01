from odoo import fields, models


class ClothifyCategoryKid(models.Model):
    _name = 'clothify.category.kid'
    _description = 'Categories of Cloths in Clothify'

    name = fields.Char(required=True)
