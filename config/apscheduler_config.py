#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from apscheduler.jobstores.memory import MemoryJobStore


JOBS = [
    {
        'id': 'job_tasks_job1',
        'func': 'tasks:job1',
        'args': (1, 2),
        'trigger': 'interval',
        'seconds': 10
    },
    {
        'id': 'job_tasks_task2',
        'func': 'tasks:task2',
        'args': None,
        'trigger': 'interval',
        'seconds': 10
    },
]

SCHEDULER_JOBSTORES = {
    'default': MemoryJobStore()
}

SCHEDULER_API_ENABLED = False










