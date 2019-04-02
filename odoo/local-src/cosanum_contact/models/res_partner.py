from odoo import models, fields


class Contact(models.Model):
    _inherit = 'res.partner'

    spitex_center_id = fields.Many2one(
        'res.partner',
        'Spitex Center',
        domain=[('is_company', '=', True)]
    )

    insurance_id = fields.Many2one(
        'res.partner',
        'Insurance',
        domain=[('is_company', '=', True)]
    )
