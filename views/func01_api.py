# -*- coding: utf-8 -*-
from flask import request, jsonify, Blueprint
from flask.views import MethodView
from controllers.func01 import Func01

func01_bp = Blueprint("func01_bp", __name__, url_prefix="/func01")


class FunctionView(MethodView):
    def get(self):
        kwargs = request.args.to_dict()
        return self.process_request(**kwargs)

    def post(self):
        kwargs = request.form.to_dict()
        return self.process_request(**kwargs)

    def validate(self, **kwargs):
        pass

    def process_request(self, **kwargs):
        try:
            self.validate(**kwargs)
            return self.get_response(**kwargs)
        except Exception as e:
            ret = dict(code=500, errmsg=repr(e))
            return jsonify(**ret)

    @staticmethod
    def get_response(**kwargs):
        data = Func01(**kwargs).run()
        ret = dict(code=200, errmsg="ok", data=data)
        return jsonify(**ret)


func01_bp.add_url_rule("/query", view_func=FunctionView.as_view("func01_query"), methods=["GET", "POST"])
