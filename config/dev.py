#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
from .base import basedir


# Flask config
DEBUG = True


# SQLAlchemy config
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')


# APScheduler
SCHEDULER_API_ENABLED = True

