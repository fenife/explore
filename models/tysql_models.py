#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

""" 
《SQL必知必会》中的样例表 
More details: doc/tysql/
"""


from . import db


class Customers(db.Model):
    """ 顾客信息 """
    __bind_key__ = 'tysql'
    __tablename__ = 'customers'
    cust_id = db.Column(db.String(10), primary_key=True, nullable=False, comment='顾客ID')
    cust_name = db.Column(db.String(50), nullable=False, comment='顾客名称')
    cust_address = db.Column(db.String(50), nullable=True, comment='顾客地址')
    cust_city = db.Column(db.String(50), nullable=True, comment='顾客所在城市')
    cust_state = db.Column(db.String(5), nullable=True, comment='顾客所在州')
    cust_zip = db.Column(db.String(10), nullable=True, comment='顾客地址邮政编码')
    cust_country = db.Column(db.String(50), nullable=True, comment='顾客所在国家')
    cust_contact = db.Column(db.String(50), nullable=True, comment='顾客联系名')
    cust_email = db.Column(db.String(255), nullable=True, comment='顾客的电子邮件')
