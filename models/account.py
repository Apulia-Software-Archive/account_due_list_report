# -*- coding: utf-8 -*-
# © 2019 Apulia Software (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class AccountPaymentTermType(models.Model):
    _name = 'account.payment.term.type'
    _description = 'Payment term type list'

    name = fields.Char(string='Codice', size=16)
    description = fields.Char(string='Descrizione', size=64)


class AccountPaymentTerm(models.Model):

    _inherit = 'account.payment.term'

    payment_term_type = fields.Many2one('account.payment.term.type',
                                        'Tipo di pagamento')


class AccountJournal(models.Model):

    _inherit = "account.journal"

    hide_in_due_view = fields.Boolean(string="Hide in due list view",
                                      default=False)


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    payment_term_type = fields.Many2one('account.payment.term.type',
                                        string='Tipo di pagamento',
                                        compute='_payment_type',
                                        method=True,
                                        store=True,
                                        search='_payment_term_search')

    importo = fields.Monetary(compute="_compute_importo",
                              string="Importo",
                              method=True,
                              store=True)

    hide_in_due_view = fields.Boolean(related='journal_id.hide_in_due_view',
                                      string='Hide in due list view')

    @api.multi
    @api.depends('amount_residual')
    def _compute_importo(self):
        for line in self:
            line.importo = line.amount_residual

    @api.multi
    @api.depends('payment_term_id', 'payment_term_id.payment_term_type')
    def _payment_type(self):
        for line in self:
            line.payment_term_type = \
                line.invoice_id.payment_term_id.payment_term_type

    @api.multi
    def _payment_term_search(self, args):
        if args:
            payment_obj = self.env('account.payment.term')
            payment_ids = payment_obj.search(args)
            if payment_ids:
                move_ids = self.search([
                    ('payment_term_id', 'in', payment_ids)])
                return [('id', 'in', move_ids)]
        return False
