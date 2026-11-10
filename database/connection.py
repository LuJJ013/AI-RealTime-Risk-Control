"""Database engine and lightweight connection checks."""

import os

from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root@localhost:3306/ai_bigdata",
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


def check_database_connection() -> bool:
    """Return whether the configured database can execute a simple query."""
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True
