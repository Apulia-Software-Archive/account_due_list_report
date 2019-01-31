# -*- coding: utf-8 -*-
# © 2019 Apulia Software (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class DueListQweb(models.AbstractModel):

    _name = 'report.account_due_list_report.group_by_date_qweb'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(
            'account_due_list_report.group_by_date_qweb')
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'company': False,
            'docs': self.env[report.model].browse(self._ids),
        }
        return report_obj.render(
            'account_due_list_report.group_by_date_qweb',
            docargs)


class DueListPartnerQweb(models.AbstractModel):

    _name = 'report.account_due_list_report.group_by_partner_qweb'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(
            'account_due_list_report.group_by_partner_qweb')
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'company': False,
            'docs': self.env[report.model].browse(self._ids),
        }
        return report_obj.render(
            'account_due_list_report.group_by_partner_qweb',
            docargs)
