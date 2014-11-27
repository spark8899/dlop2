# coding: utf-8

from flask import Blueprint, request, g, flash
from flask import render_template, redirect, url_for, abort
from flask.views import MethodView

from app import app
from ..models import Asset_model
from ..forms import Asset_modelForm

__all__ = ['bp']

bp = Blueprint('asset', __name__)
title=u'资产管理'

@bp.route('/model/')
def model():
    """Asset_model pages."""
    asset_model = Asset_model.query.order_by(Asset_model.id.desc()).all()
    return render_template('asset/model.html', title=title, models=asset_model)


@bp.route('/model/add', methods=['GET', 'POST'])
def model_add():
    """Add a asset_model."""
    form = Asset_modelForm()
    if form.validate_on_submit():
        #app.logger.info(asset_model)
        asset_model = form.save()
        flash(u"添加机型成功!")
    else:
        if request.method == 'POST':
            flash(u"添加机型错误!")
            #flash(u"添加机型错误!" + form.errors)
    return render_template('asset/model_add.html', title=title, form=form)


@bp.route('/model/edit_<id>', methods=['GET', 'POST'])
def model_edit(id):
    """Edit a asset_model."""
    asset_model = Asset_model.query.get_or_404(id)
    form = Asset_modelForm(obj=asset_model)
    if form.validate_on_submit():
        #app.logger.info(asset_model)
        form.populate_obj(asset_model)
        asset_model.save()
        flash(u"修改机型成功!")
    else:
        if request.method == 'POST':
            flash(u"修改机型错误!")
            #flash(u"修改机型错误!" + form.errors)
    return render_template('asset/model_edit.html', title=title, form=form, slug=id)


@bp.route('/model/del_<id>', methods=['GET'])
def model_del(id):
    """Del a asset_model."""
    asset_model = Asset_model.query.get_or_404(id)
    asset_model.delete()
    flash(u'删除机型' + id + u'成功！')
    return redirect(url_for('.model'))
