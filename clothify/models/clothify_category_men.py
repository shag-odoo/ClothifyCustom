from odoo import fields, models,api


class ClothifyCategoryMen(models.Model):
    _name = 'clothify.category.men'
    _description = 'Categories of Cloths in Clothify'

    name = fields.Char(required=True)
    size=fields.Integer()
    price=fields.Integer()
    quantity=fields.Integer()
    category=fields.Many2one('clothify.product')
    
    total_amount=fields.Integer(compute='_compute_total')

    @api.depends('quantity','price')
    def _compute_total(self):
        for record in self:
            record.total_amount=record.quantity*record.price
