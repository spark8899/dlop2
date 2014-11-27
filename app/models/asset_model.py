# coding: utf-8

import hashlib
from datetime import datetime
from werkzeug import security
from ._base import db, DlopQuery, SessionMixin

__all__ = ['Asset_model']

class Asset_model(db.Model, SessionMixin):
    __tablename__ = "asset_model"
    query_class = DlopQuery

    id = db.Column(db.String(8), primary_key=True)
    type = db.Column(db.String(80))
    manufacturer = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(120), nullable=False)
    cpu_model = db.Column(db.String(80))
    cpu_num = db.Column(db.Integer)
    memory_model = db.Column(db.String(80))
    memory_size = db.Column(db.Integer)
    netcard_model = db.Column(db.String(80))
    netcard_num = db.Column(db.Integer)
    harddisk_model = db.Column(db.String(80))
    harddisk_size = db.Column(db.Integer)
    flashdisk_model = db.Column(db.String(80))
    flashdisk_size = db.Column(db.Integer)
    raid_type = db.Column(db.String(80))
    remote_manage_card = db.Column(db.String(80))
    virtual_type = db.Column(db.String(80))
    unit = db.Column(db.Integer)
    desc = db.Column(db.String(120))

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<ID '{:s}'>".format(self.id)
