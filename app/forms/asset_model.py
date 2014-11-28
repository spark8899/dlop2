# coding: utf-8

import os
from flask import current_app
from wtforms import Form, StringField, IntegerField, validators, SelectField, TextAreaField, BooleanField, SelectMultipleField

from ._base import BaseForm
from ..models import Asset_model, Asset_idc

class Asset_modelForm(BaseForm):
    id = StringField(u'编码', [validators.Length(min=4, max=8, message=u"需要4-8个字符")])
    type = SelectField(u'类型',
        choices=[
            ('server', 'Server'),
            ('network', 'Network'),
            ('firewall', 'Firewall')
        ],
        default='server'
    )
    manufacturer = StringField(u'厂商', [validators.Length(min=2, max=80, message=u"需要2-80个字符")])
    model = StringField(u'设备型号', [validators.Length(min=2, max=120, message=u"需要2-120个字符")])
    cpu_model = StringField(u'CPU型号')
    cpu_num = IntegerField(u'CPU数量', [validators.NumberRange(min=0, max=255, message=u"需要0-255之间数字")], default=0)
    memory_size = IntegerField(u'内存大小', [validators.NumberRange(min=0, message=u"需要数字类型")], default=0)
    netcard_num = IntegerField(u'网口数量', [validators.NumberRange(min=0, max=225, message=u"需要0-225之间数字")], default=0)
    harddisk = StringField(u'硬盘')
    flashdisk = StringField(u'闪存')
    raid = StringField(u'RAID')
    remote_manage = StringField(u'远程管理')
    virtual = StringField(u'虚拟化')
    unit = SelectField(u'高度',
        choices=[
            ('0', '0U'),
            ('1', '1U'),
            ('2', '2U'),
            ('3', '3U'),
            ('4', '4U'),
            ('5', '5U'),
            ('6', '6U')
        ],
        default='0',
    )
    desc = TextAreaField(u'备注')

    def save(self):
        asset_model = Asset_model(**self.data)
        asset_model.save()
        return asset_model

class Asset_idcForm(BaseForm):
    id = StringField(u'编码', [validators.Length(min=4, max=8, message=u"需要4-8个字符")])
    bandwidth = StringField(u'带宽')
    rack_num = StringField(u'机柜数量')
    rack_code = StringField(u'机柜编号')
    lan_ip = StringField(u'内网网段')
    wan_ip = StringField(u'外网网段')
    location = StringField(u'详细地址')
    telephone = StringField(u'电话')
    auth_code = StringField(u'验证码')
    tax = StringField(u'传真')
    desc = TextAreaField(u'备注')

    def save(self):
        asset_idc = Asset_idc(**self.data)
        asset_idc.save()
        return asset_idc
