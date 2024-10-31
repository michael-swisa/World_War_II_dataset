from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db import Base

connection_url = 'postgresql://admin:1234@localhost:5437/missions_db'
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))



