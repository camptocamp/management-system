# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    company_name_suffix1 = fields.Char(
        related='partner_id.company_name_suffix1',
        string='Company Name Suffix 1',
    )
    company_name_suffix2 = fields.Char(
        related='partner_id.company_name_suffix2',
        string='Company Name Suffix 2',
    )
