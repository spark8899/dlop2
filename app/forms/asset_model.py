# coding: utf-8

import os
from flask import current_app
from wtforms import Form, StringField, validators, SelectField, TextAreaField, BooleanField, SelectMultipleField

from ._base import BaseForm
from ..models import asset_model

class Asset_modelForm(BaseForm):
    id = StringField(u'机型编码', [validators.Required(), validators.Length(min=4, max=18)])
    type = SelectField(u'机型类型',
        choices=[
            ('server', 'Server'),
            ('network', 'Network'),
            ('firewall', 'Firewall')
        ],
        default='server',
    )
    manufacturer = StringField(u'设备厂商', [validators.Required(), validators.Length(min=2, max=80)])
    model = StringField(u'设备型号', [validators.Required(), validators.Length(min=2, max=120)])
    cpu_model = StringField(u'CPU型号')
    cpu_num = StringField(u'CPU数量')
    memory_model = StringField(u'内存型号')
    memory_size = StringField(u'内存大小')
    netcard_model = StringField(u'网口型号')
    netcard_port = StringField(u'网口数量')
    harddisk_model = StringField(u'硬盘型号')
    harddisk_size = StringField(u'硬盘大小')
    flashdisk_model = StringField(u'闪存型号')
    flashdisk_size = StringField(u'闪存大小')
    raid_type = StringField(u'RAID类型')
    remote_manage_card = StringField(u'远程卡类型')
    virtual_type = StringField(u'虚拟机类型')
    unit = SelectField(u'机柜U数',
        choices=[
            ('0U', '0U'),
            ('1U', '1U'),
            ('2U', '2U'),
            ('3U', '3U'),
            ('4U', '4U'),
            ('5U', '5U'),
            ('6U', '6U')
        ],
        default='0U',
    )
    desc = TextAreaField(u'备注')

    def save(self):
        asset_model = Asset_model(**self.data)
        asset_model.save()
        return device_model
