from shared.database import SessionLocal

from sqlalchemy import text


def test_connection():
    with SessionLocal() as session:
        result = session.execute(text("SELECT 1"))
        print(result.fetchone())

