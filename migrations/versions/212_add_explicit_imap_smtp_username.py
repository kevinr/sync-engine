"""add explicit imap/smtp username

Revision ID: 915e0d84527
Revises: 31aae1ecb374
Create Date: 2016-01-25 23:00:51.807888

"""

# revision identifiers, used by Alembic.
revision = '915e0d84527'
down_revision = '31aae1ecb374'

from alembic import op
from sqlalchemy import Column, String
from inbox.models.constants import MAX_INDEXABLE_LENGTH


def upgrade():
    op.add_column('imapaccount', Column('_imap_server_user', String(MAX_INDEXABLE_LENGTH), nullable=True))
    op.add_column('imapaccount', Column('_smtp_server_user', String(MAX_INDEXABLE_LENGTH), nullable=True))


def downgrade():
    op.drop_column('imapaccount', '_imap_server_user')
    op.drop_column('imapaccount', '_smtp_server_user')
