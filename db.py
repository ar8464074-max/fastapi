from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:9019194535@localhost:5434/telusko"

engine = create_engine(db_url)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)