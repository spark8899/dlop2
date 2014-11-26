import time
import base64
import hashlib
import functools
from flask import g, request, session, current_app
from flask import flash, url_for, redirect, abort
from flask.ext.babel import lazy_gettext as _
from .models import Asset_model


def force_int(value, default=1):
    try:
        return int(value)
    except:
        return default
