from odoo import fields,models

class ClothifyCategory(models.Model):
    _name='clothify.category'
    _description='Categories of Cloths in Clothify'

    name=fields.Char(required=True)
