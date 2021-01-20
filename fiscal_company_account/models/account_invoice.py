# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = ['account.invoice', 'fiscal.mother.check.mixin']

    # Remove the company part of the domain
    journal_id = fields.Many2one(
        domain="""[
            ('type', 'in', {
                'out_invoice': ['sale'],
                'out_refund': ['sale'],
                'in_refund': ['purchase'],
                'in_invoice': ['purchase']
            }.get(type, []))
        ]
        """)
