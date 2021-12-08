from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = 'postgresql://origin:hasd4YDG7@localhost/user_auth'

connection = create_engine(SQLALCHEMY_DATABASE_URI)
