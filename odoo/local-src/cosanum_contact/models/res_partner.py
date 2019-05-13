# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class Contact(models.Model):
    _inherit = 'res.partner'

    spitex_center_id = fields.Many2one(
        comodel_name='res.partner',
        string='Spitex Center',
        domain=[('is_company', '=', True)]
    )

    insurance_id = fields.Many2one(
        comodel_name='res.partner',
        string='Insurance',
        domain=[('is_company', '=', True)]
    )
    company_name_suffix1 = fields.Char(
        string='Company Name Suffix 1',
    )
    company_name_suffix2 = fields.Char(
        string='Company Name Suffix 2',
    )
    customer_value_id = fields.Many2one(
        comodel_name='customer.value',
        string='Customer Value',
        ondelete='restrict',
    )
    marketing_type_ids = fields.One2many(
        comodel_name='marketing.type',
        inverse_name='partner_id',
        string='Contact marketing type',
        ondelete='restrict',
    )
    customer_fte_number = fields.Float(
        digits=(16, 2),
        string='Customer number of FTE',
    )

    @api.depends('ref', 'company_name_suffix1')
    def _compute_display_name(self):
        # override to inject dependency on fields
        return super()._compute_display_name()

    def _get_name(self):
        name = super()._get_name()
        if self.is_company and self.company_name_suffix1 and self.ref:
            return '{} {} ({})'.format(
                self.name, self.company_name_suffix1, self.ref
            )
        elif self.is_company and self.ref:
            return '{} ({})'.format(self.name, self.ref)
        return name
