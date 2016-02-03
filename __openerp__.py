# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Apulia Software srl All Rights Reserved.
#                       www.apuliasoftware.it
#                       info@apuliasoftware.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Payments Due list Report",
    'version': '0.1',
    'category': 'Generic Modules/Payment',
    'description': """
ENG: Original AgileBG addons extended with QWeb report
ITA: Stampa Qweb delle scadenze cliente/fornitore""",
    'author': 'Apulia Software srl',
    'website': 'http://www.apuliasoftware.it',
    'license': 'AGPL-3',
    "depends" : ['account_due_list', 'report'],
    "init_xml" : [],
    "update_xml" : [
        'views/account_view.xml',
        'reports/due_list_qweb.xml',
        'reports/reports.xml',
        'payment_type_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        ],
    "demo_xml" : [],
    "active": False,
    "installable": True,
    "images": ['images/image.png'],
}
