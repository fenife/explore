#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from celery import Celery, Task
from celery.utils.log import get_task_logger
import time


app = Celery('celery_tasks',
             backend='redis://localhost:6379/1',
             broker='redis://localhost:6379/1')


# 简单的task

@app.task
def add(x, y):
    print('args: (%d, %d), running ... ' % (x, y))
    return x + y


# 根据任务状态执行不同操作

class DemoTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(DemoTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(DemoTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=DemoTask)
def sub(x, y):
    return x - y


# 绑定任务为实例方法

logger = get_task_logger(__name__)


@app.task(bind=True)
def mul(self, x, y):
    logger.info(self.request.__dict__)
    return x * y


# 获取任务状态

@app.task(bind=True)
def test_mes(self):
    for i in range(1, 11):
        time.sleep(0.1)
        self.update_state(state='PROGRESS', meta={'p': i*10})

    return 'finish'
