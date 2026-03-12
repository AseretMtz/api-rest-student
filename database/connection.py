from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:%p4n1cButt0n_?@panic-db-prod.cknyi4i083fx.us-east-1.rds.amazonaws.com:5432/panicbtn"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # recomendado para RDS
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()