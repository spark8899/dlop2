# coding: utf-8

import os
from flask import current_app
from wtforms import Form, TextField, validators, SelectField, TextAreaField, BooleanField, SelectMultipleField

from ._base import BaseForm
from ..models import asset_model

class Asset_modelForm(BaseForm):
    id = TextField(u'机型', [validators.Required(), validators.Length(min=4, max=18)])
    type = SelectField(u'机型类型',
        choices=[
            ('server', 'Server'),
            ('network', 'Network'),
            ('firewall', 'Firewall')
        ],
        default='server',
    )
    manufacturer = TextAreaField(u'厂商')
    model = TextAreaField(u'设备型号')
    cpu_name = TextAreaField(u'CPU型号')
    clock_speed = TextAreaField(u'CPU频率')
    cpu_num = TextAreaField(u'CPU数量')
    memory_type = TextAreaField(u'内存型号')
    memory_size = TextAreaField(u'内存大小')
    network_port = TextAreaField(u'网口数量')
    harddisk_name = TextAreaField(u'硬盘名称')
    harddisk_size = TextAreaField(u'硬盘大小')
    flashdisk_size = TextAreaField(u'闪存大小')
    raid_type = TextAreaField(u'raid类型')
    remote_manage_card = TextAreaField(u'远程卡类型')
    virtual_type = TextAreaField(u'虚拟机类型')
    unit = TextAreaField(u'机柜U数')
    desc = TextAreaField(u'备注')

    def save(self):
        asset_model = Asset_model(**self.data)
        asset_model.save()
        return device_model
