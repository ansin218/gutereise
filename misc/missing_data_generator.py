#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:57:51 2020

@author: ankurs
"""

import pandas as pd

df = pd.read_csv('../dataset/_2020-07-16_muc_in.csv')

df['from_date'] = pd.to_datetime(df['from_date'])
df['to_date'] = pd.to_datetime(df['to_date'])
df['crawl_date'] = pd.to_datetime(df['crawl_date'])

df['from_date'] = df['from_date'] + pd.Timedelta(days = 1)
df['to_date'] = df['to_date'] + pd.Timedelta(days = 1)
df['crawl_date'] = df['crawl_date'] + pd.Timedelta(days = 1)

df['from_date'] = df['from_date'].dt.strftime('%Y-%m-%d')
df['to_date'] = df['to_date'].dt.strftime('%Y-%m-%d')
df['crawl_date'] = df['crawl_date'].dt.strftime('%Y-%m-%d')

df.to_csv('../dataset/_2020-07-17_muc_in.csv', index = False)