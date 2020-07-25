#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:26:44 2020

@author: liuweikai
"""

import mysql.connector

cnx = mysql.connector.connect(user='robot', password='Robot#123456', host='vicliu.i234.me', database='robot')
mycursor = cnx.cursor()
my_cmd_sql = "select * from tbl_qa"
a=mycursor.execute(my_cmd_sql)
for a in mycursor:
    print(a)
mycursor.close()
cnx.close()
