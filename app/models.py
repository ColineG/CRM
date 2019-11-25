from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.types import DateTime, Numeric
from sqlalchemy.dialects.postgresql import VARCHAR, ENUM
from sqlalchemy_utils import EmailType
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config, config, FlaskConfig
from vcf_extractor import  CustomerExtractor
from app import db

# create an engine
conf = FlaskConfig()
db = create_engine(conf.DATABASE_URL)
base = declarative_base()

# configuration to file db
conf = Config(config)
x = CustomerExtractor(conf.clients)


class Email(base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    label = Column(String(100))
    email = Column(EmailType, unique=True)
    company_id = Column(Integer, ForeignKey('company.id'))

    def __repr__(self):
        return '<Email {}>'.format(self.contact_id, self.label, self.email, self.company_id)


class Fn(base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    company_name = Column(String(100), unique=True)

    def __repr__(self):
        return '<Fn {}>'.format(self.contact_id, self.company_name)


class N(base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String(255))
    first_name = Column(String(255))
    job_position = Column(String(255))
    company_id = Column(Integer, ForeignKey('company.id'))
    contact_status = Column(ENUM('Client', 'Prospect', 'Churner', 'Prestataire', 'Reperage', name='contact_status'))
    start_date = Column(DateTime, server_default=func.now())
    stop_date = Column(DateTime, default=None)

    def __repr__(self):
        return '<N {}>'.format(self.last_name, self.first_name, self.job_position, self.company_id, self.contact_status)


class Note(base):
    __tablename__ = 'follow_up'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    note = Column(VARCHAR())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return '<Note {}>'.format(self.contact_id, self.company_id, self.note, self.created_at)

#class Photo(base):

    #TBD


class Phone(base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    label = Column(String(100))
    phone = Column(Integer())
    company_id = Column(Integer, ForeignKey('company.id'))

    def __repr__(self):
        return '<Phone {}>'.format(self.phone)


class Devis(base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ref_quote = Column(String)
    quote_status = Column(ENUM('Signé', 'Envoyé', 'Retard', 'Refusé', name='quote_status'))
    company_id = Column(Integer, ForeignKey('company.id'))
    created_at = Column(DateTime, server_default=func.now())
    signed_at = Column(DateTime)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    amount_id = Column(Integer, ForeignKey('amount.id'))


class Prestation(base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    services = Column(ENUM('3D', 'Photo', 'Vidéo', 'Réalité Augmentée', 'Drône', 'Photo sur site',
                               'Surcyclage', 'Photo avec location lieux', 'Production', 'Direction artistique',
                               name='quote_status'))
    quote_id = Column(Integer, ForeignKey('quote.id'))
    amount_id = Column(Integer, ForeignKey('amount.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    contractor = Column(Integer, ForeignKey('contractor.id'))


class Prestataire(base):
    __tablename__ = 'contractor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey('contact.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    expensess = Column(Numeric(5, 2))
    contractor_payment_ht = Column(Numeric(5, 2))
    contractor_payment_ttc = Column(Numeric(5, 2))


class Facture(base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ref_invoice = Column(String)
    invoice_type = Column(ENUM("Facture d'accompte", "Facture intermédiaire", "Facture", "Facture solde",
                               name='invoice_type'))
    quote_id = Column(Integer, ForeignKey('quote.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    created_at = Column(DateTime, server_default=func.now())
    amount_id = Column(Integer, ForeignKey('amount.id'))


class Amount(base):
    __tablename__ = 'amount'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quote_id = Column(Integer, ForeignKey('quote.id'))
    ht_amount = Column(Numeric(5, 2))
    ttc_amount = Column(Numeric(5, 2))
    payment_status = Column(ENUM('Payé', 'En attente', name='payment_status'))
    paid_at = Column(DateTime)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)








