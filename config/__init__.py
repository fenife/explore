#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from .base import *
from .apscheduler_config import *


FLASK_CONFIG = os.getenv('FLASK_CONFIG')

if FLASK_CONFIG == 'production':
    from .production import *
elif FLASK_CONFIG == 'release':
    from .release import *
elif FLASK_CONFIG == 'dev':
    from .dev import *
else:
    from .dev import *


# 自定义的 init_app
def init_app(app):
    # 日志系统管理
    handler = logging.FileHandler(os.path.join(basedir, 'log/app.log'), encoding='UTF-8')
    logging_format = logging.Formatter(
        '[%(asctime)s]-[%(levelname)s]-[%(module)s/%(filename)s-%(funcName)s()-%(lineno)s] - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
