#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from apscheduler.jobstores.memory import MemoryJobStore


JOBS = [
    {
        'id': 'job_tasks_task_1',
        'func': 'tasks:task_1',
        'args': (1, 2),
        'trigger': 'interval',
        'seconds': 10
    },
    {
        'id': 'job_tasks_task_2',
        'func': 'tasks:task_2',
        'args': None,
        'trigger': 'interval',
        'seconds': 10
    },
]

SCHEDULER_JOBSTORES = {
    'default': MemoryJobStore()
}

SCHEDULER_API_ENABLED = False










