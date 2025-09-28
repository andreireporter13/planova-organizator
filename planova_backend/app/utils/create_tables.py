from app.models.user import Base
from app.core.database import engine


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_db_and_tables()
    print("Tables created successfully!")
