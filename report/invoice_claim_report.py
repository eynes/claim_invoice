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
from openerp import tools

class invoice_claim_stat(osv.osv):
    _name = "invoice_claim.stat"
    _description = "Invoice claim Statistics"
    _rec_name = 'partner_id'
    _auto = False
    _columns = {
        'partner_id': fields.many2one('res.partner', 'Partner', readonly=True),
        'date':fields.date('Date', readonly=True),
        'user_id': fields.many2one('res.users', 'Responsible', required=True),
        'description': fields.text('Description'),
        'name': fields.char('Call Summary', size=64, required=True),
        'partner_phone': fields.char('Phone', size=32),
        'invoice_id': fields.many2one('account.invoice', 'Invoice'),
        'period_id': fields.many2one('account.period', 'Period', readonly=True),
    }
    _order = 'date'

    #~ def search(self, cr, uid, args, offset=0, limit=None, order=None,
                #~ context=None, count=False):
        #~ for arg in args:
            #~ if arg[0] == 'period_id' and arg[2] == 'current_year':
                #~ current_year = self.pool.get('account.fiscalyear').find(cr, uid)
                #~ ids = self.pool.get('account.fiscalyear').read(cr, uid, [current_year], ['period_ids'])[0]['period_ids']
                #~ args.append(['period_id','in',ids])
                #~ args.remove(arg)
        #~ return super(account_followup_stat, self).search(cr, uid, args=args, offset=offset, limit=limit, order=order,
            #~ context=context, count=count)
#~ 
    #~ def read_group(self, cr, uid, domain, *args, **kwargs):
        #~ for arg in domain:
            #~ if arg[0] == 'period_id' and arg[2] == 'current_year':
                #~ current_year = self.pool.get('account.fiscalyear').find(cr, uid)
                #~ ids = self.pool.get('account.fiscalyear').read(cr, uid, [current_year], ['period_ids'])[0]['period_ids']
                #~ domain.append(['period_id','in',ids])
                #~ domain.remove(arg)
        #~ return super(account_followup_stat, self).read_group(cr, uid, domain, *args, **kwargs)

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'invoice_claim_stat')
        cr.execute("""
            create or replace view invoice_claim_stat as (
                SELECT
                    cp.id as id,
                    cp.partner_id AS partner_id,
                    cp.date AS date,
					cp.user_id AS user_id,
					cp.description AS description,
					cp.name AS name,
					cp.partner_phone AS partner_phone,
					cp.invoice_id AS invoice_id
                FROM
                    crm_phonecall cp
                WHERE
					cp.invoice_id is not null
            )""")
invoice_claim_stat()

#~ WHERE
                    #~ a.active AND
                    #~ a.type = 'receivable' AND
                    #~ l.reconcile_id is NULL AND
                    #~ l.partner_id IS NOT NULL
                #~ GROUP BY
                    #~ l.id, l.partner_id, l.company_id, l.blocked, l.period_id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
