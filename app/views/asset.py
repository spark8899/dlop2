# coding: utf-8

from flask import Blueprint, request, g
from flask import render_template, redirect, url_for, abort
from ..models import Asset_model
from ..forms import Asset_modelForm

__all__ = ['bp']

bp = Blueprint('asset', __name__)

@bp.route('/model/')
def model():
    """Asset_model pages."""
    Asset_model = Asset_model.query.order_by(Asset_model.updated.desc()).all()
    return render_template('asset/model.html', models=Asset_model)


@bp.route('/model/add', methods=['GET', 'POST'])
def model_add():
    """
    Add a asset_model.
    """
    form = Asset_modelForm()
    if form.validate_on_submit():
        asset_model = form.save()
        return redirect(url_for('.view', urlname=asset.urlname))
    return render_template('asset/model_add.html', form=form)
