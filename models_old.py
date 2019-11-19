from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_utils import PhoneNumber
from app import routes, models
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.username)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    job_title_0 = db.Clumn(db.String(64), index=True, unique=True)
    job_title_1 = db.Clumn(db.String(64), index=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.PhoneNumberType())
    status = db.Column(db.String(20))
    note = db.Column(db.String)

    def __repr__(self):
        return '<Contact {}>'.format(self.last_name)


class ContactDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    email_0 = db.Column(db.String(120), index=True, unique=True)
    email_1 = db.Column(db.String(120), index=True, unique=True)
    email_2 = db.Column(db.String(120), index=True, unique=True)
    phone_0 = db.Column(db.PhoneNumberType())
    phone_1 = db.Column(db.PhoneNumberType())
    phone_2 = db.Column(db.PhoneNumberType())
    phone_3 = db.Column(db.PhoneNumberType())

    def __repr__(self):
        return '<ContactDetails {}>'.format(self.email_0)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), index=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    url_0 = db.Column(db.String(200))
    url_1 = db.Column(db.String(200))
    url_2 = db.Column(db.String(200))

    def __repr__(self):
        return '<Company {}>'.format(self.company)


class Localization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    adr_0_street = db.Column(db.String(200))
    adr_1_street = db.Column(db.String(200))
    adr_0_city = db.Column(db.String(200))
    adr_1_city = db.Column(db.String(200))
    adr_0_cp = db.Column(db.String(200))
    adr_1_cp = db.Column(db.String(200))
    adr_0_country = db.Column(db.String(200))
    adr_1_country = db.Column(db.String(200))

    def __repr__(self):
        return '<Localization {}>'.format(self.adr_0_street)


class Historic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    desc = db.Column(db.String(255))
    delete_at = db.Column(db.DateTime)
    modify_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<Historic {}>'.format(self.desc)


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    label_0 = db.Column(db.String(120))
    label_1 = db.Column(db.String(120))
    label_2 = db.Column(db.String(120))
    label_3 = db.Column(db.String(120))

