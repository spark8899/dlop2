# coding: utf-8

import hashlib
from datetime import datetime
from werkzeug import security
from ._base import db, DlopQuery, SessionMixin

__all__ = ['Asset_model', 'Asset_idc']

class Asset_model(db.Model, SessionMixin):
    __tablename__ = "asset_model"
    query_class = DlopQuery

    id = db.Column(db.String(8), primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    manufacturer = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    cpu_model = db.Column(db.String(80))
    cpu_num = db.Column(db.Integer)
    memory_size = db.Column(db.Integer)
    netcard_num = db.Column(db.Integer)
    harddisk = db.Column(db.String(80))
    flashdisk = db.Column(db.String(80))
    raid = db.Column(db.String(80))
    remote_manage = db.Column(db.String(80))
    virtual = db.Column(db.String(80))
    unit = db.Column(db.Integer)
    desc = db.Column(db.String(240))

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<ID '{:s}'>".format(self.id)

class Asset_idc(db.Model, SessionMixin):
    __tablename__ = "asset_idc"
    query_class = DlopQuery

    id = db.Column(db.String(8), primary_key=True)
    bandwidth = db.Column(db.String(120))
    rack_num = db.Column(db.Integer)
    rack_code = db.Column(db.String(120))
    lan_ip = db.Column(db.String(120))
    wan_ip = db.Column(db.String(120))
    location = db.Column(db.String(120))
    telephone = db.Column(db.String(20))
    auth_code = db.Column(db.String(120))
    tax = db.Column(db.String(20))
    desc = db.Column(db.String(240))

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<ID '{:s}'>".format(self.id)
