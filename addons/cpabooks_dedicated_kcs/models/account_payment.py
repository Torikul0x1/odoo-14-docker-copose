from odoo import api, models, fields, _


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    so_id = fields.Many2one('sale.order', 'Sales Order')
    signatory_id = fields.Many2one(
        'res.users',
        string='Signatory',
        default=lambda self: self.env.user
    )
