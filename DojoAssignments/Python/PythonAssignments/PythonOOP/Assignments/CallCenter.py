from datetime import datetime, date, time, tzinfo, timedelta
import itertools
import operator
import uuid
from decimal import *
from collections import deque


class Call(object):
    new_id = itertools.count().next
    current = datetime.today()

    def __init__(self, name, phone, reason):
        call_id = Call.new_id() + 1
        unique_id = (id(call_id))
        id_length = len(str(unique_id))
        getcontext().prec = id_length + 1
        call_date = Call.current
        call_day = datetime.date(call_date)
        call_time = datetime.time(call_date)
        self.id = call_id + Decimal(Decimal(unique_id) * Decimal(0.00000001))
        self.name = name
        self.phone = phone
        self.day = call_day
        self.time = call_time
        self.reason = reason
        return

    def call(self):
        id = self.id
        name = self.name
        phone = self.phone
        day = self.day
        time = self.time
        reason = self.reason
        call = [id, name, phone, day, time, reason]
        return call

    def display(self):
        print(
            "The call's attributes include:\n  The call's id is: {}.\n  The caller's name is: {}.\n  The caller's phone number is: {}.\n  The call was recieved on: {} at {}.\n  The reason for the call is: {}.".format(
                self.id, self.name, self.phone, self.day, self.time, self.reason))
        return self

c1 = Call('bob dylan', '817-555-1212', 'my guitar does not work')
call = c1.call()
# c2 = Call()
# c3 = Call()
# c4 = Call()
# c5 = Call()
# c6 = Call()
# c7 = Call()
class CallCenter(object):
    def __init__(self):
        self.calls = []
        print('self.calls')
        print(self.calls)
        self.queue = list.__len__(self.calls)
        return

    def add(self):
        newCall = c1.call()
        for i, v in enumerate(newCall):
            print(i, v)
        print(type(newCall))
        print(newCall)
        print(type(self.calls))
        return

    def remove(self):
        return

    def info(self):
        return

    def find(self):
        return

    def sort(self):

        return



print(c1.display())
print(c1.call())
# print(c2.call())
# print(c3.call())
# print(c4.call())
# print(c5.call())
# print(c6.call())
# print(c7.call())

center = CallCenter()
print(center.add())
