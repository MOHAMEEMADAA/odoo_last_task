from odoo import models, fields


class ticket(models.Model):
    _name = 'lr.ticket'
    _description = "ticket"

    name = fields.Char(string='Name')
    tag = fields.Char(string='Tag')
    number = fields.Integer(string='Number')
    state = fields.Selection([('new', 'New'), ('done', 'Done')], string='State')

