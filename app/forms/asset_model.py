# coding: utf-8

import os
from flask import current_app
from wtforms import Form, StringField, IntegerField, validators, SelectField, TextAreaField, BooleanField, SelectMultipleField

from ._base import BaseForm
from ..models import Asset_model

class Asset_modelForm(BaseForm):
    id = StringField(u'机型编码', [validators.Length(min=4, max=18, message=u"需要4-18个字符")])
    type = SelectField(u'机型类型',
        choices=[
            ('server', 'Server'),
            ('network', 'Network'),
            ('firewall', 'Firewall')
        ],
        default='server'
    )
    manufacturer = StringField(u'设备厂商', [validators.Length(min=2, max=80, message=u"需要2-80个字符")])
    model = StringField(u'设备型号', [validators.Length(min=2, max=120, message=u"需要2-120个字符")])
    cpu_model = StringField(u'CPU型号')
    cpu_num = IntegerField(u'CPU数量', [validators.NumberRange(min=0, max=127, message=u"需要0-127之间数字")], default=0)
    memory_model = StringField(u'内存型号')
    memory_size = IntegerField(u'内存大小', [validators.NumberRange(min=0, message=u"需要数字类型")], default=0)
    netcard_model = StringField(u'网口型号')
    netcard_num = IntegerField(u'网口数量', [validators.NumberRange(min=0, max=127, message=u"需要0-127之间数字")], default=0)
    harddisk_model = StringField(u'硬盘型号')
    harddisk_size = IntegerField(u'硬盘大小', [validators.NumberRange(min=0, message=u"需要数字类型")], default=0)
    flashdisk_model = StringField(u'闪存型号')
    flashdisk_size = IntegerField(u'闪存大小', [validators.NumberRange(min=0, message=u"需要数字类型")], default=0)
    raid_type = StringField(u'RAID类型')
    remote_manage_card = StringField(u'远程卡类型')
    virtual_type = StringField(u'虚拟机类型')
    unit = SelectField(u'机柜U数',
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
