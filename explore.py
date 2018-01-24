#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from flask import Flask
from flask_apscheduler import APScheduler

import config


scheduler = APScheduler()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    from models import db
    db.app = app
    db.init_app(app)

    scheduler.init_app(app)
    print scheduler.get_jobs()

    return app


app = create_app()


@app.route('/')
def hello_world():
    app.logger.info('Hello World')
    return 'Hello World!'


if __name__ == '__main__':
    # scheduler.start()
    app.run(debug=True)


