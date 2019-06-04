# -*- coding: utf-8 -*-
# © 2019 Apulia Software (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class AccountJournal(models.Model):

    _inherit = "account.journal"

    hide_in_due_view = fields.Boolean(string="Hide in due list view",
                                      default=False)


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    hide_in_due_view = fields.Boolean(related='journal_id.hide_in_due_view',
                                      string='Hide in due list view')
