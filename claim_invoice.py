##############################################################################
#
# Copyright (c) 2011 Eynes. (http://www.eynes.com.ar) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

import tools
from osv import fields, osv
from tools.translate import _
import decimal_precision as dp
import netsvc

class res_partner(osv.osv):

    _inherit = "res.partner"

    _columns = {
        'phonecall_invoice_ids': fields.one2many('crm.phonecall', 'partner_id', 'Phonecall Invoice'),
    }

class account_invoice(osv.osv):

    _inherit = "account.invoice"

    _columns = {
        'phonecall_invoice_ids': fields.one2many('crm.phonecall', 'invoice_id', 'Phonecall Invoice'),
    }

class crm_phonecall(osv.osv):
    _inherit = "crm.phonecall"

    _columns = {
        'invoice_id': fields.many2one('account.invoice', 'Invoice', domain=[('state','=','open')]),
    }
