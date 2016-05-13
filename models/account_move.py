# -*- coding: utf-8 -*-
from openerp import api, models, fields


class AccountMove(models.Model):

    _inherit = 'account.move'

    @api.one
    def _get_invoice_origin(self):
        self.invoice_origin = self.invoice_ids and self.invoice_ids[0].origin or '-'

    # Core already has a many2one relationship defined from account.invoice
    # to account.move. Add the counterpart one2many link so that the invoice
    # can be accessed from the journal entry.
    # Note that even though the relationship is o2m, there is just a single
    # invoice linked to the journal entry.

    invoice_ids = fields.One2many('account.invoice', 'move_id', 'Invoices')
    invoice_origin = fields.Char(compute='_get_invoice_origin', string='Invoice Origin')
