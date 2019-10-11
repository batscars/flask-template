# -*- coding: utf-8 -*-
import gevent.monkey
gevent.monkey.patch_all()

import os
import sys
from flask import Flask
src_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, src_root)

from views.func01_api import func01_bp


app = Flask(__name__)
app.register_blueprint(func01_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
