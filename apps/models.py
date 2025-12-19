# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Safety_Metrics(db.Model):

    __tablename__ = 'Safety_Metrics'

    id = db.Column(db.Integer, primary_key=True)

    #__Safety_Metrics_FIELDS__
    lta = db.Column(db.Integer, nullable=True)
    skador = db.Column(db.Integer, nullable=True)
    tillbud = db.Column(db.Integer, nullable=True)
    osakra_forhallande = db.Column(db.Integer, nullable=True)
    kommentar = db.Column(db.Text, nullable=True)

    #__Safety_Metrics_FIELDS__END

    def __init__(self, **kwargs):
        super(Safety_Metrics, self).__init__(**kwargs)


class Quality(db.Model):

    __tablename__ = 'Quality'

    id = db.Column(db.Integer, primary_key=True)

    #__Quality_FIELDS__
    problemsolving = db.Column(db.Text, nullable=True)
    problems = db.Column(db.Text, nullable=True)
    op9_kommentar = db.Column(db.Text, nullable=True)
    op9_antal = db.Column(db.Integer, nullable=True)

    #__Quality_FIELDS__END

    def __init__(self, **kwargs):
        super(Quality, self).__init__(**kwargs)


class People(db.Model):

    __tablename__ = 'People'

    id = db.Column(db.Integer, primary_key=True)

    #__People_FIELDS__
    bemanning = db.Column(db.Boolean, nullable=True)
    kompetens = db.Column(db.Boolean, nullable=True)
    kommentar = db.Column(db.Text, nullable=True)

    #__People_FIELDS__END

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)


class Other(db.Model):

    __tablename__ = 'Other'

    id = db.Column(db.Integer, primary_key=True)

    #__Other_FIELDS__
    utrustning = db.Column(db.Boolean, nullable=True)
    reservdelar = db.Column(db.Boolean, nullable=True)
    annat = db.Column(db.Text, nullable=True)
    oppna_ao = db.Column(db.Integer, nullable=True)
    sena_fu_antal = db.Column(db.Integer, nullable=True)
    sena_fu = db.Column(db.Text, nullable=True)

    #__Other_FIELDS__END

    def __init__(self, **kwargs):
        super(Other, self).__init__(**kwargs)


class Cost(db.Model):

    __tablename__ = 'Cost'

    id = db.Column(db.Integer, primary_key=True)

    #__Cost_FIELDS__
    produktions_loss = db.Column(db.Integer, nullable=True)

    #__Cost_FIELDS__END

    def __init__(self, **kwargs):
        super(Cost, self).__init__(**kwargs)


class Delivery(db.Model):

    __tablename__ = 'Delivery'

    id = db.Column(db.Integer, primary_key=True)

    #__Delivery_FIELDS__
    ct = db.Column(db.Integer, nullable=True)
    bm = db.Column(db.Integer, nullable=True)
    cbm = db.Column(db.Integer, nullable=True)
    balk = db.Column(db.Integer, nullable=True)
    maskin_kalibrering = db.Column(db.Integer, nullable=True)
    maskin_maskindata = db.Column(db.Integer, nullable=True)

    #__Delivery_FIELDS__END

    def __init__(self, **kwargs):
        super(Delivery, self).__init__(**kwargs)



#__MODELS__END
