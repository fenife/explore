#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

base_dir = os.path.abspath('.')
database_dir = os.path.join(base_dir, 'data.sqlite')

DB = dict(
    host="",
    port=3306,
    username="",
    password="",
    dbname=""
)