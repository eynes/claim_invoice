# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import netsvc
from openerp import pooler
import time

class account_invoice_claim(osv.osv_memory):
    """
    This wizard will generate claim form selected invoice
    """

    _name = "account.invoice.claim"
    _description = "Claim the selected invoices"

    _columns = {
        'user_id': fields.many2one('res.users', 'Responsible', required=True),
        'partner_id': fields.many2one('res.partner', 'Contact'),
        'description': fields.text('Description'),
        'name': fields.char('Call Summary', size=64, required=True),
        'date': fields.datetime('Date', required=True),
        'partner_phone': fields.char('Phone', size=32),
    }
    
    _defaults = {
        'user_id': lambda self,cr,uid,c: self.pool.get('res.users').browse(cr, uid, uid, c).id,
        'date': lambda *a: time.strftime('%Y-%m-%d'),
    }
    
    def invoice_claim(self, cr, uid, ids, context=None):
        invoice_obj = self.pool.get('account.invoice')
        phonecall_obj = self.pool.get('crm.phonecall')
        data_inv = invoice_obj.read(cr, uid, context['active_ids'], context=context)
        for form in self.browse(cr, uid, ids, context=None):
            for record in data_inv:
                phonecall_obj.create(cr, uid, {
                    'user_id': form.user_id.id,
                    'partner_id': record['partner_id'][0],
                    'description': form.description,
                    'name': form.name,
                    'date': form.date,
                    'partner_phone': form.partner_phone,
                    'invoice_id': record['id']
                    }, context=context)
                    
            return {'type': 'ir.actions.act_window_close'}
