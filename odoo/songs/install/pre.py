# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import os

# from base64 import b64encode
# from pkg_resources import resource_string

import anthem

# from ..common import req

MAIN_LANG = "de_DE"
OPT_LANG = ""
ALL_LANG = [MAIN_LANG] + (OPT_LANG.split(';') if OPT_LANG else [])


@anthem.log
def setup_company(ctx):
    """ Setup company """
    # load logo on company
    # logo_content = resource_string(req, 'data/images/company_main_logo.png')
    # b64_logo = b64encode(logo_content)

    values = {
        'name': "Cosanum",
        'street': "",
        'zip': "",
        'city': "",
        'country_id': ctx.env.ref('base.ch').id,
        'phone': "+41 00 000 00 00",
        'fax': "+41 00 000 00 00",
        'email': "contact@cosanum.ch",
        'website': "http://www.cosanum.ch",
        'vat': "VAT",
        # 'logo': b64_logo,
        'currency_id': ctx.env.ref('base.CHF').id,
    }
    ctx.env.ref('base.main_company').write(values)


@anthem.log
def setup_language(ctx):
    """ Installing language and configuring locale formatting """
    for code in ALL_LANG:
        ctx.env['base.language.install'].create({'lang': code}).lang_install()
    # TODO check your date format
    ctx.env['res.lang'].search([]).write({
        'grouping': [3, 0],
        'date_format': '%d/%m/%Y',
    })


@anthem.log
def set_default_partner_language(ctx):
    """Define default partner language"""
    Default = ctx.env['ir.default']
    Default.set('res.partner', 'lang', MAIN_LANG, condition=False)


@anthem.log
def admin_user_password(ctx):
    """ Changing admin password """
    if os.environ.get('RUNNING_ENV') == 'dev':
        ctx.log_line('Not changing password for dev RUNNING_ENV')
        return
    ctx.env.user.password_crypt = (
        '$pbkdf2-sha512$25000$OIfQei9FyBmD8L6XknIuRQ$rvsse96ZvjG9KO2sBrXb.'
        'iQZLKWMM4mQol3o4dHHpjCPw1tvh80mMVsxvddpdSGhbrStUa8Z75p.dsWMt08.wQ'
    )


@anthem.log
def main(ctx):
    """ Main: creating base config """
    setup_company(ctx)
    setup_language(ctx)
    set_default_partner_language(ctx)
    admin_user_password(ctx)
