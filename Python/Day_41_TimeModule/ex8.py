import time
localtime=time.localtime()
t2= time.strftime('%B',localtime)
print(t2)

t2= time.strftime('%b',localtime)
print(t2)

t = time.strftime("%H", localtime)
print(t)
# 10
t = time.strftime("%I", localtime)
print(t)
# 10
t = time.strftime("%j", localtime)
print(t)
# 100
t = time.strftime("%m", localtime)
print(t)
# 04
t = time.strftime("%p", localtime)
print(t)
# AM
t = time.strftime("%w", localtime)
print(t)
# 1
t = time.strftime("%x", localtime)
print(t)
# 04/10/23
t = time.strftime("%X", localtime)
print(t)
# 10:32:33
t = time.strftime("%c", localtime)
print(t)
# Mon Apr 10 10:32:33 2023
t = time.strftime("%y", localtime)
print(t)
# 23
t = time.strftime("%Y", localtime)
print(t)
# 2023
t = time.strftime("%Z", localtime)
print(t)
# India Standard Time


# time.struct_time(tm_year=2023, tm_mon=4, tm_mday=10, tm_hour=10, tm_min=25, tm_sec=33, tm_wday=0, tm_yday=100, tm_isdst=0)

# %a	This directive will return locale weekday in its abbreviated form.
# %A	This directive will return locale weekday in its complete form.
# %b	This directive will return the locale month in its shortened form.
# %B	This directive will return the locale month in its full form.
# %c	This format will return the appropriate locale date and time.
# %d	This format represents the day of the month in the form of a corresponding decimal number [0, 31].
# %H	This format represents the time in the form of a 24-hour format decimal number [01, 24].
# %I	This format means the time in the 12-hour format decimal number [01, 12].
# %j	This format represents the year's day in decimal numbers [01, 366].
# %m	This will represent the month as a decimal number [01, 12].
# %M	This will represent the minutes as a decimal number [00, 59].
# %p	This format will give the corresponding locale AM or PM.
# %S	This represents the seconds as a decimal number [00, 61].
# %U	This format will return the year's week as a decimal number ranging from [00, 53]. The convention uses Sunday as the first day of the week, and every day of a new year that comes before the first Sunday is regarded as being in week 0.
# %w	This format returns the locale day of the week as a decimal number ranging from [0, 6]. The convention uses Sunday as the 0th day of the week.
# %W	This format returns the year's week number as a decimal number ranging from [00, 53]. The convention uses Monday as the first of the week, and week 0 of a new year is defined as all days before the first Monday.
# %x	This will return the correct date representation according to the locale date.
# %X	This will return the proper time representation according to the locale used.
# %y	This format will