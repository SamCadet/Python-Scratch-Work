import time
import datetime
import threading
import subprocess
import webbrowser

# p. 398
# print(time.time())

# p. 398-399

'''
def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate' % (endTime - startTime))


# p. 399

print(time.ctime())

thisMoment = time.time()

print(time.ctime(thisMoment))

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

    time.sleep(5)



# p. 400

now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))



# p. 402-403

print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(10000000))
print(datetime.datetime.fromtimestamp(time.time()))
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

# p. 403

print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 != oct31_2019)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)

The datetime.timedelta() function
takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds. There is no month
or year keyword argument, because “a month” or “a year” is a variable amount of time depending on the
particular month or year.

print(delta.total_seconds())

print(str(delta))



# p. 404

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))



# p. 405

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# p. 405-406

print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '19", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))



# p. 407 - Multithreading

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start() # Calls the function to run the code inside it in a separate thread.

print('End of program.')

threadObj = threading.Thread(
    target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})

threadObj.start()

# p. 411 Popen() - opens programs on computer with the subproccess module

subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# You have to use print() with poll() or wait() in order to see their respective exit codes.

paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
# print(paintProc.poll() == None)

print(paintProc.wait())

print(paintProc.poll())



print(subprocess.Popen(['C:\\Windows\\notepad.exe',
                        'C:\\Users\\Sam\\My Documents\\MyGuy.txt']))


# p. 413 web browser module review

webbrowser.open('http://nba.com') # use http:// to open in default browser, going without it opens ie for some reason.



# p. 413 opening files with default applications

fileObj = open('hello.txt', 'w')
print(fileObj.write('Hello, world!'))

fileObj.close()
subprocess.Popen(['start', 'hello.txt'], shell=True)

CalcThang = open('C:\\Windows\\System32\\calc.exe')

CalcThang.close()

'''
