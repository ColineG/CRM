from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import VARCHAR, ENUM
from sqlalchemy_utils import EmailType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config, config, FlaskConfig
from app import db

# create an engine
conf = FlaskConfig()
db = create_engine(conf.DATABASE_URL)
base = declarative_base()

# configuration


class Email(base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_contact = Column(Integer, ForeignKey('contact.id'))
    email = Column(EmailType, unique=True)
    label = Column(String(100))
    id_company = Column(Integer, ForeignKey('company.id'))

    def __repr__(self):
        return '<Email {}>'.format(self.email)


class Fn(base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_contact = Column(Integer, ForeignKey('contact.id'))
    company_name = Column(String(100), unique=True)

    def __repr__(self):
        return '<Fn {}>'.format(self.company_name)


class N(base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(255))
    first_name = Column(String(255))
    prefix = Column(String(255))
    id_company = Column(Integer, ForeignKey('company.id'))
    contact_status = Column(ENUM('Client', 'Prospect', 'Churn'))

    def __repr__(self):
        return '<N {}>'.format(self.last_name)


class Note(base):
    __tablename__ = 'follow_up'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_contact = Column(Integer, ForeignKey('contact.id'))
    id_company = Column(Integer, ForeignKey('company.id'))
    note = Column(VARCHAR())
    created_at = Column(DateTime, default=unc.now())
    deleted_at = Column(DateTime)

    def __repr__(self):
        return '<Note {}>'.format(self.note)

#class Photo(base):

    #TBD


class Phone(base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_contact = Column(Integer, ForeignKey('contact.id'))
    label = Column(String(100))
    phone = Column(Integer(10))
    id_company = Column(Integer, ForeignKey('company.id'))

    def __repr__(self):
        return '<Phone {}>'.format(self.phone)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)








