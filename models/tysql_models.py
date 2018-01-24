#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

""" 
《SQL必知必会》中的样例表 
More details: doc/tysql/
"""


from . import db


class Vendors(db.Model):
    """ 供应商信息 """
    __bind_key__ = 'tysql'
    __tablename__ = 'vendors'
    vend_id = db.Column(db.String(10), primary_key=True, nullable=False, comment='供应商ID')
    vend_name = db.Column(db.String(50), nullable=False, comment='供应商名称')
    vend_address = db.Column(db.String(50), nullable=True, comment='供应商地址')
    vend_city = db.Column(db.String(50), nullable=True, comment='供应商所在城市')
    vend_state = db.Column(db.String(5), nullable=True, comment='供应商所在州')
    vend_zip = db.Column(db.String(10), nullable=True, comment='供应商地址邮政编码')
    vend_country = db.Column(db.String(50), nullable=True, comment='供应商所在国家')

    # 此供应商的所有产品
    products = db.relationship('Products', backref='vendor', lazy='dynamic')

    def __repr__(self):
        return '<Vendor %r>' % self.vend_name


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

    # 此顾客的所有订单
    orders = db.relationship('Orders', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer %r>' % self.cust_name


class Products(db.Model):
    """ 产品信息 """
    __bind_key__ = 'tysql'
    __tablename__ = 'products'
    prod_id = db.Column(db.String(10), primary_key=True, nullable=False, comment='产品ID')
    prod_name = db.Column(db.String(255), nullable=False, comment='产品名')
    prod_price = db.Column(db.DECIMAL(8, 2), nullable=False, comment='产品价格')
    prod_desc = db.Column(db.Text, nullable=True, comment='产品描述')

    # 产品供应商ID（关联到Vendors表的vend_id）
    vend_id = db.Column(db.String(10), db.ForeignKey('vendors.vend_id'), comment='产品供应商ID')

    # 此商品关联的条目
    orderitems = db.relationship('OrderItems', backref='product', lazy='dynamic')

    def __repr__(self):
        return '<Product %r>' % self.prod_name


class Orders(db.Model):
    """ 订单表 """
    __bind_key__ = 'tysql'
    __tablename__ = 'orders'
    order_num = db.Column(db.Integer, primary_key=True, nullable=False, comment='唯一的订单号')
    order_date = db.Column(db.Date, nullable=False, comment='订单日期')

    # 订单顾客ID（关联到Customers表的cust_id）
    cust_id = db.Column(db.String(10), db.ForeignKey('customers.cust_id'), comment='订单顾客ID')

    # 此订单的所有物品条目
    orderitems = db.relationship('OrderItems', backref='order', lazy='dynamic')

    def __repr__(self):
        return '<Order %r>' % self.order_num


class OrderItems(db.Model):
    """ 订单物品条目 """
    __bind_key__ = 'tysql'
    __tablename__ = 'orderitems'
    order_item = db.Column(db.Integer, nullable=False, comment='订单物品号（订单内的顺序）')
    quantity = db.Column(db.Integer, nullable=False, comment='物品数量')
    item_price = db.Column(db.DECIMAL(8, 2), nullable=False, comment='物品价格')

    # 订单号（关联到Orders表的order_num）
    order_num = db.Column(db.Integer, db.ForeignKey('orders.order_num'), comment='订单号')

    # 产品ID（关联到Products表的prod_id）
    prod_id = db.Column(db.String(10), db.ForeignKey('products.prod_id'), comment='产品ID')

    __table_args__ = (
        db.PrimaryKeyConstraint('order_num', 'order_item'),
    )

    def __repr__(self):
        return '<Item %r>' % self.order_item



