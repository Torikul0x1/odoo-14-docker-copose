from odoo import api, fields, models, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    narration = fields.Text('Narration')

    @api.model
    def default_get(self, fields_list):
        res = super(AccountPayment, self).default_get(fields_list)
        context = dict(self.env.context)
        if context.get('narration'):
            res.update({
                'narration': context.get('narration')
            })
        return res