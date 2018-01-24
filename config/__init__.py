#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

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
