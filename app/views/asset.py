# coding: utf-8

from flask import Blueprint, request, g, flash
from flask import render_template, redirect, url_for, abort
from flask.views import MethodView

from app import app
from ..models import Asset_model, Asset_idc
from ..forms import Asset_modelForm, Asset_idcForm

__all__ = ['bp']
title=u'资产管理'

bp = Blueprint('asset', __name__)


@bp.route('/model/')
def model():
    """Asset_model pages."""
    try:
        asset_model = Asset_model.query.order_by(Asset_model.id.desc()).all()
    except:
        asset_model = null
        flash(u"查询机型出错，请于管理员联系!") 
    return render_template('asset/model.html', title=title, models=asset_model)


@bp.route('/model/add', methods=['GET', 'POST'])
def model_add():
    """Add a asset_model."""
    form = Asset_modelForm()
    if form.validate_on_submit():
        #app.logger.info(asset_model)
        try:
            asset_model = form.save()
            flash(u"添加机型成功!")
        except:
            flash(u"添加机型出错，请于管理员联系!")
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
        try:
            asset_model.save()
            flash(u"修改机型成功!")
        except:
            flash(u"修改机型出错,请于管理员联系!")
    else:
        if request.method == 'POST':
            flash(u"修改机型错误!")
            #flash(u"修改机型错误!" + form.errors)
    return render_template('asset/model_edit.html', title=title, form=form, slug=id)


@bp.route('/model/del_<id>', methods=['GET'])
def model_del(id):
    """Del a asset_model."""
    try:
        asset_model = Asset_model.query.get_or_404(id)
        asset_model.delete()
        flash(u'删除机型' + id + u'成功！')
    except:
        flash(u'删除机型出错，请于管理员联系！')
    return redirect(url_for('.model'))


@bp.route('/idc/')
def idc():
    """Asset_idc pages."""
    try:
        asset_idc = Asset_idc.query.order_by(Asset_idc.id.desc()).all()
    except:
        flash(u"查询IDC出错，请于管理员联系!") 
    return render_template('asset/idc.html', title=title, idcs=asset_idc)


@bp.route('/idc/add', methods=['GET', 'POST'])
def idc_add():
    """Add a asset_idc."""
    form = Asset_idcForm()
    if form.validate_on_submit():
        #app.logger.info(asset_idc)
        try:
            asset_idc = form.save()
            flash(u"添加机型成功!")
        except:
            flash(u"添加机型出错，请于管理员联系!")
    else:
        if request.method == 'POST':
            flash(u"添加机型错误!")
            #flash(u"添加机型错误!" + form.errors)
    return render_template('asset/idc_add.html', title=title, form=form)


@bp.route('/idc/edit_<id>', methods=['GET', 'POST'])
def idc_edit(id):
    """Edit a asset_idc."""
    asset_idc = Asset_idc.query.get_or_404(id)
    form = Asset_idcForm(obj=asset_idc)
    if form.validate_on_submit():
        #app.logger.info(asset_idc)
        form.populate_obj(asset_idc)
	try:
            asset_idc.save()
            flash(u"修改机型成功!")
        except:
            flash(u"修改机型出错，请于管理员联系!")
    else:
        if request.method == 'POST':
            flash(u"修改机型错误!")
            #flash(u"修改机型错误!" + form.errors)
    return render_template('asset/idc_edit.html', title=title, form=form, slug=id)


@bp.route('/idc/del_<id>', methods=['GET'])
def idc_del(id):
    """Del a asset_idc."""
    try:
        asset_idc = Asset_idc.query.get_or_404(id)
        asset_idc.delete()
        flash(u'删除机型' + id + u'成功！')
    except:
        flash(u'删除机型出错，请于管理员联系！')
    return redirect(url_for('.idc'))
