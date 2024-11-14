from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from app.database.psql_connect import session_maker
from app.models import User, HostageSentence, ExplosiveSentence


def get_user_by_email(email):
    try:
        with session_maker() as session:
            user = (
                session.query(User)
                .options(joinedload(User.hostage_sentences), joinedload(User.explosive_sentences), joinedload(User.location), joinedload(User.device_info))
                .filter_by(email=email)
                .first()
            )
        return user
    except SQLAlchemyError as e:
        raise e

def get_all_sentences():
    try:
        with session_maker() as session:
            all_sentences = (
                session.query(HostageSentence.sentence)
                .union(session.query(ExplosiveSentence.sentence))
                .all()
            )
        return all_sentences
    except SQLAlchemyError as e:
        raise e
