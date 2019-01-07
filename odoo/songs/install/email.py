# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import os

import anthem
from anthem.lyrics.records import create_or_update


@anthem.log
def setup_mail_servers(ctx):
    """Create incoming/outgoing mail server configurations based on the
    running environment.
    """
    if os.environ.get('RUNNING_ENV') == 'integration':
        # incoming email
        create_or_update(
            ctx, "fetchmail.server",
            "__setup__.fetchmail_server_gmail",
            {
                "name": "gmail",
                "object_id": ctx.env.ref("crm.model_crm_lead").id,
             }
        )
        # outgoing email
        create_or_update(
            ctx, "ir.mail_server",
            "__setup__.ir_mail_server_mailtrap",
            {"name": "mailtrap"}
        )


@anthem.log
def main(ctx):
    setup_mail_servers(ctx)
