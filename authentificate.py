from werkzeug.security import check_password_hash
from models import User
from sqlalchemy.orm import sessionmaker
from database import connection


def check_user(info_auth):
    Session = sessionmaker()
    Session.configure(bind=connection)
    session = Session()
    user = session.query(User).filter_by(username=info_auth['username']).first()
    if user is None or not check_password_hash(user.password_hash, info_auth['password']):
        return 'Невірне ім`я або пароль'
    if info_auth['ip_address_mac'] != user.ip_address_mac:
        return 'Невірна IP або MAC адреса'
    return 'Автентифікація пройшла успішно'





