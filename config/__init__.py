#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .dev import *

# SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8'.format(**ZZHW_STSC_DB)
SQLALCHEMY_DATABASE_URI = "sqlite:///" + database_dir

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
