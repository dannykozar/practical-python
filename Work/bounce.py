# bounce.py
#
# Exercise 1.5

peak = 100 # initial drop height [m]
bounce_f = 3/5 # bounce height as proportion of previous bounce [unitless]

i = 1
while i <= 10:
    peak = bounce_f * peak
    print(i, peak)
    i = i + 1
