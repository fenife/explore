#!usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery


celery_app = Celery('celery_tasks', broker='pyamqp://guest@localhost//')


@celery_app.task
def add(x, y):
    return x + y
