# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Cosanum Contact',
    'summary': 'Specific Contact features for Cosanum',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'partner_company_group',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'views/contact_view.xml',
        'views/customer_value_view.xml',
        'views/marketing_type_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
