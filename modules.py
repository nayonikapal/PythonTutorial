import module1 as m1
import math 
import datetime
# import json

"""MODULE1"""
res=m1.greets()
print(res)

"""MATH MODULE"""
x,y=5.25,4.01
a,b=3,2
o=-8.32
p,q=121,225

print(math.ceil(x),math.ceil(y))                          #ceiling func
print(math.floor(x),math.floor(y))                        #floor func
print(math.comb(a,b))                                     #combination
print("MINIMUM:",min(x,y,a,b),"MAXIMUM:",max(x,y,a,b))    #min and max
print("ABSOLUTE:",abs(o),abs(x))                          #absolute
print(pow(a,b))                                           #power
print(math.sqrt(p),math.sqrt(q))                          #square root
print(math.pi)                                            #pi
print(math.factorial(a))                                  #factorial
print(math.gcd(a,b,p,q),math.gcd(a,q))                    #greatest common divisor
print(math.lcm(a,b,p,q),math.lcm(a,q))                    #least common multiple
print(math.sin(b))                                        #sine func

"""DATETIME MODULE"""
t=datetime.datetime.now()
tm=datetime.datetime(2003,9,26)
print(t)                                                  #today's date and time
print(t.strftime("%x"))                                   #local version of today's date
print(t.strftime("%j"))                                   #day of the year
print(t.strftime("%a"))                                   #weekday short version
print(t.strftime("%A"))                                   #weekday long version
print(tm.strftime("%j"))                                  #set date trial
print(t.strftime("%y"))                                   #year short ver
print(t.strftime("%Y"))                                   #year long ver
print(t.strftime("%H"))                                   #24 hour clock hour
print(t.strftime("%I"))                                   #12hr clock hour
print(t.strftime("%p"))                                   #am/pm
print(t.strftime("%d"))                                   #day of the month

"""JSON MODULE"""