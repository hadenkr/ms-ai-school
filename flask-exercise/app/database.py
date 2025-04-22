from sqlalchemy import MetaData # Import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define the naming convention
# This is a standard convention recommended by Alembic/SQLAlchemy docs
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# Create a MetaData object with the convention
metadata = MetaData(naming_convention=convention)

# Initialize SQLAlchemy with the app AND the metadata
# Make sure 'db' is initialized *before* models are imported if they rely on 'db'
db = SQLAlchemy(metadata=metadata) # Pass metadata here

migrate = Migrate()
