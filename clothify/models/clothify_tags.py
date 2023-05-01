from odoo import fields,models

class ClothifyTags(models.Model):
    _name='clothify.tags'
    _description="Tags to differentiate products in clothify"

    name=fields.Char(required=True)