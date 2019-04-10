# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class CustomerValue(models.Model):
    _name = 'customer.value'
    _description = 'Customer Value'

    name = fields.Char(
        required="True",
    )
    sequence = fields.Integer(
        help="Gives the sequence order when"
             " displaying a list of follow-up lines."
    )
