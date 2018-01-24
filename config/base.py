#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os


basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.split(basedir)[0]

# Flask config
SECRET_KEY = os.urandom(24)

# SQLAlchemy config
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
