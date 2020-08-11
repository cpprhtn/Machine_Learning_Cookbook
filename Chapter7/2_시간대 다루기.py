#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:19:35 2020

@author: cpprhtn
"""

x = input()

import pandas as pd

pd.Timestamp('2017-05-01 06:00:00', tz='Europe/London')

date = pd.Timestamp('2017-05-01 06:00:00')

#시간대 지정
date_in_london = date.tz_localize('Europe/London')

date_in_london

# 시간대 변경
date_in_london.tz_convert('Africa/Abidjan')

#세 개의 날짜 생성
dates = pd.Series(pd.date_range('2/2/2002', periods=3, freq='M'))

#시간대 지정
dates.dt.tz_localize('Africa/Abidjan')

from pytz import all_timezones

#두 개의 시간대 확인
all_timezones[0:2]

dates.dt.tz_localize('dateutil/Aisa/Seoul')

import pytz

tz = pytz.timezone('Asia/Seoul')
dates.dt.tz_localize(tz)