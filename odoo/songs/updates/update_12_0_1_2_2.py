# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem


@anthem.log
def cleanup_mail_servers(ctx):
    """Cleanup wrongly configured mail servers"""
    ctx.env['fetchmail.server'].search([]).unlink()
    ctx.env['ir.mail_server'].search([]).unlink()


@anthem.log
def full(ctx):
    cleanup_mail_servers(ctx)
