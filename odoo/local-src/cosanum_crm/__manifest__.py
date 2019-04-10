# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Cosanum CRM',
    'summary': 'Specific Sale features for Cosanum',
    'version': '12.0.1.0.0',
    'category': 'CRM',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'cosanum_contact',
        'crm',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'views/crm_lead_view.xml',
    ],
    'installable': True,
}
