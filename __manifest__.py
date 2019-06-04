# -*- coding: utf-8 -*-
# © 2019 Apulia Software (<info@apuliasoftware.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Payments Due list Report",
    'version': '10.0.1.1.0',
    'category': 'Generic Modules/Payment',
    'description': """
ENG: Original AgileBG addons extended with QWeb report\n
ITA: Stampa Qweb delle scadenze cliente/fornitore""",
    'author': 'Apulia Software srl',
    'website': 'http://www.apuliasoftware.it',
    'license': 'AGPL-3',
    "depends": ['account_due_list',
                'report',
                'account_invoice_supplier_ref_unique'],
    "init_xml": [],
    "data": [
        'views/account_view.xml',
        'reports/reports.xml',
        'reports/due_list_qweb.xml',
        'reports/group_by_partner_due_list_qweb.xml',
        ],
    "active": False,
    "installable": True,
}
