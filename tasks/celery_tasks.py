#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from celery import Celery


app = Celery('celery_tasks', backend='redis://localhost:6379/1', broker='redis://localhost:6379/1')


@app.task
def add(x, y):
    return x + y


