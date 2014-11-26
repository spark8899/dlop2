# coding: utf-8

from flask import Blueprint, request, g, flash
from flask import render_template, redirect, url_for, abort
from flask.views import MethodView

from app import app
from ..models import Asset_model
from ..forms import Asset_modelForm

__all__ = ['bp']

bp = Blueprint('asset', __name__)

@bp.route('/model/')
def model():
    """Asset_model pages."""
    Asset_model = Asset_model.query.order_by(Asset_model.updated.desc()).all()
    return render_template('asset/model.html', models=Asset_model)


class model_add(MethodView):
    """
    Add a asset_model.
    """
    def get(self):
        form = Asset_modelForm()
        return render_template('asset/model_add.html', form=form)

    def post(self):
        form = Asset_modelForm(request.form)
        app.logger.info(form.errors)
        if form.validate_on_submit():
            app.logger.info(form.id.data)
            asset_model = form.save()
            return redirect(url_for('.view', urlname=asset.urlname))
        else:
            #flash(u"添加机型错误!")
            flash(u"添加机型错误!" + form.errors)
        return render_template('asset/model_add.html', form=form)

bp.add_url_rule('/model/add', view_func=model_add.as_view('model_add'))
