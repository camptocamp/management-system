# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class MarketingType(models.Model):
    _name = 'marketing.type'
    _description = 'Marketing Type'

    name = fields.Char(
        required="True",
    )
    sequence = fields.Integer(
        help="Gives the sequence order when"
             " displaying a list of follow-up lines."
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
    )
    color = fields.Integer()
