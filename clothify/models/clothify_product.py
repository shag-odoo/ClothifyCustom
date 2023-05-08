from odoo import models, fields,api


class ClothifyProduct(models.Model):
    _name = 'clothify.product'
    _description = 'Product Module'
    _sql_constraints = [
        ('check_quantity', 'CHECK(quantity >= 0)',
         'Quantity Should be positive'),
         ('check_price','CHECK(price>0)',
         'Price Should be more than zero')
    ]
    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Integer()
    size = fields.Integer()
    quantity = fields.Integer(default=2)
    Active = fields.Boolean(default=True)
    color = fields.Selection(
        selection=[
            ('black', 'Black'),
            ('white', 'White'),
            ('blue', 'Blue'),
            ('grey', 'Grey')
        ],
        default='black'
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('cart', 'Add to Cart'),
            ('delivered', 'Delivered'),
            ('return', 'Return'),
        ],
        default='new',
    )
    category_type = fields.Selection(
        selection=[
            ("mens","Mens"),
            ("women","Women"),
            ("kids","Kids"),
        ]
    )
    
    # MANY2MANY RELATIONSHIPS
    tag_ids = fields.Many2many("clothify.tags")
    # MANY2ONE RELATIONSHIP
    # link_id=fields.Many2one('clothify.product')
    @api.depends('state')
    def add_to_cart(self):
        for record in self:
            record.state='cart'
            record.link_id.product_name=record.name
            record.link_id.cart_price=record.price
        

    def cancel(self):
        self.state='new'
   