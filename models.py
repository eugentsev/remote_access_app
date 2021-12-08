from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    password_hash = Column(String(128))
    ip_address_mac = Column(String(25), unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

