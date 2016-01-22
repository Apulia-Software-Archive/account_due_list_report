# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
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

import time
from report import report_sxw
import inspect
import os
from datetime import datetime
from osv import osv
from osv import fields


class account_due_list_webkit(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(account_due_list_webkit, self).__init__(cr, uid, name,
                                                      context=context)
        file_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
        self.localcontext.update({
            'datetime': datetime,
            'time': time,
            'cr': cr,
            'uid': uid,
            'file_path': file_path,
        })

report_sxw.report_sxw('report.account_due_list.scadenzario',
                      'account.move.line',
                      'account_due_list_extended/reports/scadenzario.mako',
                      parser=account_due_list_webkit)
