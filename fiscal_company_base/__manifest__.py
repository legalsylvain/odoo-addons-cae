# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "CAE - Base",
    "version": "12.0.1.2.2",
    "category": "CAE",
    "summary": "Manage CAE (Cooperatives of Activities and Employment)",
    "author": "GRAP",
    "website": "https://github.com/grap/odoo-addons-cae",
    "license": "AGPL-3",
    "post_init_hook": "post_install_set_fiscal_company",
    "depends": [
        "base",
        # GRAP
        "technical_partner_access",
    ],
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/view_res_company.xml",
    ],
    "demo": [
        "demo/res_partner_company.xml",
        "demo/res_partner_users.xml",
        "demo/res_partner.xml",
        "demo/res_groups.xml",
    ],
    "installable": True,
}
