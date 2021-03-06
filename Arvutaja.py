# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date
import urllib.request, json
import os
import datetime
import time
import matplotlib.pyplot as plt
#import datetime.strptime
#modules for graphs
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pylab as plt
import matplotlib.patches as mpatches

#kas suveaeg v6i talveaeg
NumberOfHooursUse = 0
NumberOfDaysUse = 0
WattsUsed = 0


def daylightSavingsTime():
    daylightTime = time.daylight and time.localtime().tm_isdst > 0
    if(daylightTime == True):
        return("summer")
    else:
        return("winter")
    
def timeOfWeek():  #function to see if its weekday or weekend
    dayNr = datetime.datetime.today().weekday()
    if dayNr<5:
        return('Weekday')
    else:
        return('Weekend')
        
 
today = str(date.today())
yesterday = str(date.today() - datetime.timedelta(1))

today = str(date.today())
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow1 = tomorrow.strftime('%Y-%m-%d')
yesterday = date.today() - datetime.timedelta(1)
yesterday1 = yesterday.strftime('%Y-%m-%d')
text = 'https://dashboard.elering.ee/api/nps/price?start='
text2 = '&end='
#P2ringu saime https://dashboard.elering.ee/documentation.html lehelt.
with urllib.request.urlopen(text+yesterday1+text2+tomorrow1) as url:
    #print(text+yesterday1+text2+tomorrow1)
    #v6tab eleringist stringina t2nased hinnad
    jsonstring = json.loads(url.read().decode())
    data =(jsonstring['data'])
    eesti = data['ee']
    #kirjutab andmed faili    
    with open('todaydata.txt', 'w') as outfile:

        now = datetime.datetime.now()

        for i in range (21, 45) :
            eestiajad =(eesti[i])
            kellaaeg = (eestiajad['timestamp'])
            price = (eestiajad['price'])
            time2 = datetime.datetime.fromtimestamp(kellaaeg).isoformat()
            json.dump(price, outfile)
            json.dump(time2, outfile)
            outfile.write('\n')


def splitPrices():
    cheap_times = []
    expensive_times = []
    total_sum = 0
    with open('todaydata.txt', 'r') as pricesList:
        for line in pricesList:
            count = len(open('todaydata.txt').readlines(  ))
            a, b, c = line.split('"')
            number = float(a)
            total_sum += number
            avg = total_sum/count
    pricesList.close()
    with open('todaydata.txt', 'r') as pricesList: 
        for line in pricesList:
            a, b, c = line.split('"')
            time2 = b
            time2 = time2.replace("T", " ")
            number = float(a)
            if (number < avg):
                cheap_times.append(time2)
            else:            
                expensive_times.append(time2)
        return cheap_times, expensive_times

#lugeda failist elektriandmes
f = open("clientData.txt","r")
fixed = (str((f.readline().rstrip())))
if(fixed == "fikseeritud"):
    daylightSavingTime = daylightSavingsTime()
    timeOfWeek()
    expensive_times = []
    cheap_times = []
    #fikseeritud hind erineb aastaajast ja nädalapäevast, nädalavahetustel odavam aeg puudub
    if(daylightSavingTime == 'summer'):
        if(timeOfWeek() == 'weekday'):
            #kood käivitatakse kella kahest ehk ajad on arvutatud arvestusega, et time.now on kell kaks
            for x in range(0, 6):
                normaltime = datetime.datetime.now() + timedelta(hours=x)
                sringtime = normaltime.strftime("%Y-%m-%d %H:%M:%S")
                cheap_times.append(sringtime)
            for x in range(7, 24):

                normaltime = datetime.datetime.now() + timedelta(hours=x)
                sringtime = normaltime.strftime("%Y-%m-%d %H:%M:%S")
                expensive_times.append(sringtime) 
        else:
            for x in range(0, 24):
                normaltime = datetime.datetime.now() + timedelta(hours=x)
                sringtime = normaltime.strftime("%Y-%m-%d %H:%M:%S")
                expensive_times.append(sringtime)
    if(daylightSavingTime == 'winter'):
        if(timeOfWeek() == 'summer'):
            for x in range(0, 7):
                normaltime = datetime.datetime.now() + timedelta(hours=x)
                sringtime = normaltime.strftime("%Y-%m-%d %H:%M:%S")
                cheap_times.append(sringtime)
            for x in range(8, 23):
                normaltime = datetime.datetime.now() + timedelta(hours=x)
                sringtime = normaltime.strftime("%Y-%m-%d %H:%M:%S")
                expensive_times.append(sringtime) 
        else:
            for x in range(0, 24):
                expensive_times.append(datetime.datetime.now() + timedelta(hours=x))
    day_price = (f.read())
    night_price = (f.read())
    delivery_price = (f.read())
    marginal_price = (f.read())
    f.close()
else:
    delivery_price = (f.read())
    marginal_price = (f.read())
    f.close()
    cheap_times, expensive_times = splitPrices()

#kasutaja sisestatud tingimused
#loeb sisse kõik tingimused
t = open("userconditions.txt","r")
how_many_minutes_in = int(t.readline())
how_many_minutes_out = int(t.readline())

how_many_minutes_in_at_once = int(t.readline())
how_many_minutes_out_at_once = int(t.readline())

max_electicity_consumption = int(t.readline())
min_electicity_consumption = int(t.readline())

tomorrownight = datetime.datetime.now() + timedelta(hours=-14)

h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_starts1 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_ends1 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_starts2 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_ends2 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_starts3 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_ends3 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_starts4 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_in_ends4 = tomorrownight + timedelta(hours=h, minutes=m)

h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_starts1 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_ends1 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_starts2 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_ends2 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_starts3 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_ends3 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_starts4 = tomorrownight + timedelta(hours=h, minutes=m)
h, m = t.readline().split(':')
h=int(h)
m=int(m)
which_timeperiod_out_ends4 = tomorrownight + timedelta(hours=h, minutes=m)

t.close()
a = open("seadme_andmed.txt","r")
name = a.readline()
appliance = int(a.readline())

def convert_min_to_hour(minutes):
    return minutes/60
    
def calculate_capacity(applience, workinghours):
    capacity = workinghours*(applience/1000)
    return capacity

def calculate_hours_from_capacity(appliance, capacity):
    hours = capacity/(appliance/1000)
    return hours

def calculate_timedifference_in_hours(starttime, endtime):
    timedifference =(endtime-starttime)
    duration_in_s = timedifference.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    totalminutes = divmod(duration_in_s, 60)[0]
    minutes = round((totalminutes-hours*60)/6, 2)
    timedifference = hours+minutes
    return timedifference

def return_existing_workingtimes(which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4, which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4):
    if(which_timeperiod_in_starts1 is 0 and which_timeperiod_in_ends1 is 0):
        return '0'
    if(which_timeperiod_in_starts2 is 0 and which_timeperiod_in_ends2 is 0):
        return '1'
    if(which_timeperiod_in_starts3 is 0 and which_timeperiod_in_ends3 is 0):
        return '2'
    if(which_timeperiod_in_starts4 is 0 and which_timeperiod_in_ends4 is 0):
        return '3'
    if(which_timeperiod_in_starts1 is not 0 and which_timeperiod_in_ends1 is not 0):
        return '4'
    
def place_missing_times_to_plan(available_times, cheap_times, expensive_times, hours_needed, turn_on_at, turn_off_at):
    u=0
    for x in range(1, available_times):
        cheap_length = (len(cheap_times))
        expensive_length = (len(expensive_times))
        if(x<cheap_length):
            cheap_times[x]=datetime.datetime.strptime(cheap_times[x] , "%Y-%m-%d %H:%M:%S")
            turn_on_at.append(cheap_times[x])
            turn_off_at.append(cheap_times[x] + timedelta(hours=hours_needed * 1.66666666667))
        elif(x<expensive_length):
            expensive_times[x]=datetime.datetime.strptime(expensive_times[x] , "%Y-%m-%d %H:%M:%S")
            turn_on_at.append(expensive_times[x])
            turn_off_at.append(expensive_times[x] + timedelta(hours=hours_needed * 1.66666666667))

    return turn_on_at, turn_off_at

#kõikide aegade vahe tundides
timeIn1 = calculate_timedifference_in_hours(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
timeIn2 = calculate_timedifference_in_hours(which_timeperiod_in_starts2, which_timeperiod_in_ends2)
timeIn3 = calculate_timedifference_in_hours(which_timeperiod_in_starts3, which_timeperiod_in_ends3)
timeIn4 = calculate_timedifference_in_hours(which_timeperiod_in_starts4, which_timeperiod_in_ends4)
timeOut1 = calculate_timedifference_in_hours(which_timeperiod_out_starts1, which_timeperiod_out_ends1)
timeOut2 = calculate_timedifference_in_hours(which_timeperiod_out_starts2, which_timeperiod_out_ends2)
timeOut3 = calculate_timedifference_in_hours(which_timeperiod_out_starts3, which_timeperiod_out_ends3)
timeOut4 = calculate_timedifference_in_hours(which_timeperiod_out_starts4, which_timeperiod_out_ends4)

hours_working = timeIn1 + timeIn2 + timeIn3 + timeIn4
hours_not_working = timeOut1 + timeOut2 + timeOut3 + timeOut4

#algab kontroll
def check_timedifference(starttime, endtime):
    timedifference = calculate_timedifference_in_hours(starttime, endtime)
    if(timedifference < 0):
        print("Time can not be negative")
        return False;
    elif (timedifference > 24):
        print("Time difference can not be over 24 hours")
        return False
    else:
        return True;

def check_workinghours(minutes_working, minutes_not_working, timeIn1, timeIn2, timeIn3, timeIn4, timeOut1, timeOut2, timeOut3, timeOut4):
    hours_must_be_working = convert_min_to_hour(minutes_working)
    hours_must_not_be_working = convert_min_to_hour(minutes_not_working)
    working_time_total = hours_working + hours_not_working
    
    if(hours_must_be_working !=0 and hours_working>hours_must_be_working):
        print("The working times entered are bigger than the working time allowance entered")
        return False
    if(hours_must_not_be_working !=0 and hours_not_working>hours_must_not_be_working):
        print("The shutdown times entered are bigger than the shutdown time allowance entered")
        return False
    if(working_time_total > 24):
        print("Device can not work more than 24 hours")
        return False
    else:
        print("Total working time: ")
        return(working_time_total)
    
def check_capacity(appliance, max_capacity, min_capacity, hours_working):
    capacity = calculate_capacity(appliance, hours_working)
    maxcapacity = calculate_capacity(appliance, 24)
    if(capacity>max_capacity):
        print('Entered working timees are crossing the capacity limit entered')
        return False
    if(maxcapacity<min_capacity):
        print('The minimum capacity can not be reached by your device')
        return False
    else:
        missing_capacity = min_capacity - capacity
        print('missing')
        print(missing_capacity)
        return(missing_capacity)
    
def check_if_hours_fit_to_limit(hours, limit_in_hours):
    if(hours <= limit_in_hours):
        return True
    else:
        return False
    
#kas kõik ajavahemikud klapivad
check1 = check_timedifference(which_timeperiod_in_starts1, which_timeperiod_in_ends1)
check2 = check_timedifference(which_timeperiod_in_starts2, which_timeperiod_in_ends2)
check3 = check_timedifference(which_timeperiod_in_starts3, which_timeperiod_in_ends3)
check4 = check_timedifference(which_timeperiod_in_starts4, which_timeperiod_in_ends4)
check5 = check_timedifference(which_timeperiod_out_starts1, which_timeperiod_out_ends1)
check6 = check_timedifference(which_timeperiod_out_starts2, which_timeperiod_out_ends2)
check7 = check_timedifference(which_timeperiod_out_starts3, which_timeperiod_out_ends3)
check8 = check_timedifference(which_timeperiod_out_starts4, which_timeperiod_out_ends4)
check9 = check_workinghours(how_many_minutes_in, how_many_minutes_out, timeIn1, timeIn2, timeIn3, timeIn4, timeOut1, timeOut2, timeOut3, timeOut4)
check10 = check_capacity(appliance, max_electicity_consumption, min_electicity_consumption, hours_working)

def check_final(check1, check2, check3, check4, check5, check6, check7, check8, check9, check10):
    if(check1 is not False and check2 is not False and check3 is not False and check4 is not False and check5 is not False and check6 is not False and check7 is not False and check8 is not False and check9 is not False and check10 is not False):
        print('Everything is correct')
        return True;
    else:
        print('Please fix your mistakes')
        return False;
#hakkame moodustama graafikut

if(check_final(check1, check2, check3, check4, check5, check6, check7, check8, check9, check10)==True):
    turn_device_on=[]
    turn_device_off=[]
    how_many_times = return_existing_workingtimes(which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4, which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4)
    if(how_many_times == '0'):
        turn_device_on=[]
        turn_device_off=[]
    elif(how_many_times == '1'):
        turn_device_on=[which_timeperiod_in_starts1]
        turn_device_off=[which_timeperiod_in_ends1]
    elif(how_many_times == '2'):
        turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2]
        turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2]
    elif(how_many_times == '3'):
        turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3]
        turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3]
    elif(how_many_times == '4'):
        turn_device_on=[which_timeperiod_in_starts1, which_timeperiod_in_starts2, which_timeperiod_in_starts3, which_timeperiod_in_starts4]
        turn_device_off=[which_timeperiod_in_ends1, which_timeperiod_in_ends2, which_timeperiod_in_ends3, which_timeperiod_in_ends4]
    #kui pole vaja lisaaegu kuna kasutaja sisestatud aegadest piisab
    if(check10<=0):
        text_file1 = open("WorkingTimes.txt", "w")
        text_file2 = open("TurnOffTimes.txt", "w")
        for item in turn_device_on:
          text_file1.write("%s\n" % item)
        for item in turn_device_off:
          text_file2.write("%s\n" % item)
        text_file1.close()
        text_file2.close()
    else:
        missing_power = round(check10, 1)
        missing_hours = round(calculate_hours_from_capacity(appliance, missing_power), 1)
        maxlimit = convert_min_to_hour(how_many_minutes_in_at_once)
        i=1
        while(check_if_hours_fit_to_limit(missing_hours, maxlimit) is False):
          i=i*2
          missing_hours = missing_hours/2
        place_missing_times_to_plan(i, cheap_times, expensive_times, missing_hours, turn_device_on, turn_device_off)
        print('Korras, jagasime aja', i, 'Ajajupid on', missing_hours, 'pikkused')
        text_file1 = open("WorkingTimes.txt", "w")
        text_file2 = open("TurnOffTimes.txt", "w")
        for item in turn_device_on:
          text_file1.write("%s\n" % item)
        for item in turn_device_off:
          text_file2.write("%s\n" % item)
        text_file1.close()
        text_file2.close()
#teeme visuaalse graafiku


def visulize_timedata():
    #function that visulizes todays data as a linegraph
    #must install Matplotlib
    price = []
    time = []
    workingtimes = []
    notworkingtimes = []
    with open('todaydata.txt', 'r') as pricesList, open('WorkingTimes.txt','r') as workingTimes, open('WorkingOfftimes.txt','r') as notWorkingTimes:
        for line in pricesList:
	    #taking the times and prices from todaydata.txt and making a linegraph
            a, b, c = line.split('"')
            priceA = float(a) #a - taking the prices from todays data
            timeB = b #b - taking the dates from todays data
            timeB = timeB.replace("T", " ")
            timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
            d, e = str(timeB).split(" ")

            price.append(priceA)
            time.append(timeB)
            
        indexx=1
        for line in workingTimes:
            #taking the times from workingtimes.txt and adding them to the table as dots
            uu = line.strip()
            if(indexx < 5):
                uu, oo = uu.split('.')
                indexx = indexx+1
            timeB2 = datetime.datetime.strptime(uu , "%Y-%m-%d %H:%M:%S")
            f, g = line.split(' ')
            timeG = g #g - taking the times from working times
            #workingtimes.append(timeG)
            workingtimes.append(timeB2)
        indexx=1
        for line in notWorkingTimes:
            ee = line.strip()
            if(indexx < 5):
                ee, oo = ee.split('.')
                indexx = indexx+1
            #taking the times from notworkingtimes.txt and adding them to the table as dots
            timeB3 = datetime.datetime.strptime(ee , "%Y-%m-%d %H:%M:%S")
            h, i = line.split(' ')
            timeI = i #i - taking the times from not working times
            notworkingtimes.append(timeB3)

    workline = [40 for aeg in workingtimes]
    endline = [40 for aeg in workingtimes]
    green_patch = mpatches.Patch(color='aqua', label='Device started working')
    red_patch = mpatches.Patch(color='black', label='Device ended working')
    plt.plot(time, price, color='hotpink')
    plt.scatter(workingtimes, workline, color='aqua')
    plt.scatter(notworkingtimes, endline, color='black')
    plt.xlabel("time(date, hour)")
    plt.ylabel("Electricity price(€/MWh)")
    plt.title("Today's electricity prices(24h), includes device's Working timetable")
    plt.gcf().autofmt_xdate()
    plt.legend(handles=[green_patch, red_patch])
    plt.savefig('24h.png')
    #plt.show()
    
#visulize_timedata()


def visulize_timedata_fixed():
    #lists of times for different times
    weekdayprice = ["night","night","day","day","night"]
    weekendprice = ["price","price","price","price","price"]
    summertimeweekday = [00.00, 08.00, 08.00, 24.00, 24.00]    
    summertimeweekend = [00.00, 08.00, 08.00, 24.00, 24.00]
    wintertimeweekday = [00.00, 07.00, 07.00, 23.00, 23.00]
    wintertimeweekend = [00.00, 07.00, 07.00, 23.00, 23.00]             
    with open('clientData.txt','r') as fixedPriceslist:
        
        #for line in pricesList:     #taking the times from todaydata.txt
         #  a, b, c = line.split('"')
           
          # if i in pricesList:
           #    timeB = b #b - taking the dates from todays data
            #   timeB = timeB.replace("T", " ")
             #  timeB = datetime.datetime.strptime(timeB , "%Y-%m-%d %H:%M:%S")
              # d, e = str(timeB).split(" ")			
               #time.append(timeB)               

        for line in fixedPriceslist:
            priceday, pricenight = line.split("\n")
            print(priceday)
            lines = fixedPriceslist.readlines()
            fPrice = lines #a - taking the prices from clientData.txt					
            #price.append(fPrice)
            if(daylightSavingsTime() == "summer" and timeOfWeek() == "Weekday"):
                plt.figure()
                plt.scatter(summertimeweekday, weekdayprice)
                plt.plot(summertimeweekday, weekdayprice)	 
            elif(daylightSavingsTime() == "summer" and timeOfWeek() == "Weekend"):
                plt.figure()
                plt.scatter(summertimeweekend, weekendprice)
                plt.plot(summertimeweekend, weekendprice)
            elif(daylightSavingsTime() == "winter" and timeOfWeek() == "Weekday"):
                plt.figure()
                plt.scatter(wintertimeweekday, weekdayprice)
                plt.plot(wintertimeweekday, weekdayprice)
            elif(daylightSavingsTime() == "winter" and timeOfWeek() == "Weekend"):
                plt.figure()
                plt.scatter(wintertimeweekend, weekendprice)
                plt.plot(wintertimeweekend, weekendprice)
            else:
                print("broken")
        
    plt.xlabel("time(date, hour)")
    plt.ylabel("Electricity price(€/MWh)")
    plt.title("Today's electricity prices(24h), includes device's Working timetable")
    plt.savefig('24h.png')
    


def chooseGraph():
    with open('clientData.txt','r') as fixedPriceslist:
        for line in fixedPriceslist:
            if(fixedPriceslist.readline()=="fikseeritud"):
                visulize_timedata()
            else:
                visulize_timedata_fixed()
            
chooseGraph()
