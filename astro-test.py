from astronomy import Observer, Time, SearchLocalSolarEclipse, LocalSolarEclipseInfo
import subprocess
import json
import time

def toCodeString(ss):
    shutter_speeds = [ 30.0, 
                    25.0,
                    20.0,
                    15.0,
                    13.0,
                    10.0,
                    8.0,
                    6.0,
                    5.0,
                    4.0,
                    3.2,
                    2.5,
                    2.0,
                    1.6,
                    1.3,
                    1.0,
                    0.8,
                    0.6,
                    0.5,
                    0.4,
                    1/3,
                    0.25,
                    0.2,
                    1/6,
                    0.125,
                    0.1,
                    1/15,
                    1/16,
                    0.05,
                    0.04,
                    1/30,
                    0.025,
                    0.02,
                    1/64,
                    0.0125,
                    0.01,
                    0.008,
                    0.00625,
                    0.005,
                    0.004,
                    0.003125,
                    0.0025,
                    0.002,
                    0.0015625,
                    0.00125,
                    0.001,
                    8e-4,
                    6.25e-4,
                    5e-4,
                    4e-4,
                    3.125e-4,
                    2.5e-4,
                    2e-4,
                    1.5625e-4,
                    1.25e-4
                    ]
    as_string = str(shutter_speeds.index(ss))
    return as_string
   

#(my current location +3deg lat to get into totality)
# lat, long, alt.
position = Observer(44.1742, -74.9223, 43.5)
t = Time.Now()

eclipse = SearchLocalSolarEclipse(t, position)

eclipse.partial_begin.time = Time('2024-04-01T22:50:00.0000Z')
eclipse.total_begin.time = Time('2024-04-01T22:55:00.0000Z')
eclipse.peak.time = Time('2024-04-01T22:56:00.0000Z')
eclipse.total_end.time = Time('2024-04-01T22:57:00.0000Z')
eclipse.partial_end.time = Time('2024-04-01T23:00:00.0000Z')

print(eclipse)

print(eclipse)
print("\n")
print(eclipse.partial_begin.time.Utc())
print(eclipse.total_begin.time.Utc())
print(eclipse.peak.time.Utc())
print(eclipse.total_end.time.Utc())
print(eclipse.partial_end.time.Utc())

delta_test = eclipse.partial_begin.time.Utc() - Time.Now().Utc()
print(delta_test)
print(delta_test.seconds)
print(delta_test)

testing = [ 30.0, 
                    25.0,
                    20.0,
                    15.0,
                    13.0,
                    10.0,
                    8.0,
                    6.0,
                    5.0,
                    4.0,
                    3.2,
                    2.5,
                    2.0,
                    1.6,
                    1.3,
                    1.0,
                    0.8,
                    0.6,
                    0.5,
                    0.4,
                    0.333,
                    0.25,
                    0.2,
                    0.167,
                    0.125,
                    0.1,
                    0.077,
                    0.067,
                    0.05,
                    0.04,
                    0.033,
                    0.025,
                    0.02,
                    0.0167,
                    0.0125,
                    0.01,
                    0.008,
                    0.00625,
                    0.005,
                    0.004,
                    0.003125,
                    0.0025,
                    0.002,
                    0.0015625,
                    0.00125,
                    0.001,
                    8e-4,
                    6.25e-4,
                    5e-4,
                    4e-4,
                    3.125e-4,
                    2.5e-4,
                    2e-4,
                    1.5625e-4,
                    1.25e-4
                    ]

#print(shutter_speeds.index(30))
#print(shutter_speeds.index(10))
#print(shutter_speeds.index(1))
#print(shutter_speeds.index(.01))
#print(shutter_speeds.index(.00625))

#subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", "30", "35", "1", "1"])

#print(toCodeString(2))
#print(type(toCodeString(2)))
#print(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/1000), toCodeString(1/10), "3", "1"])

# subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", (toCodeString(1/1000)), (toCodeString(1/10)), "1", "1"])
'''for i in range(10):
    pre = Time.Now()
    subprocess.call(["./brackets/build/RemoteCli", "27", "1", "3000", "1"])
    post = Time.Now()
    print((post.Utc() - pre.Utc()).total_seconds())

'''
p_begin = 60
t_begin = 180
t_end = 280
p_end = 340

pre = Time.Now()
# 1/2000 to 1/100
subprocess.call(["./brackets/build/RemoteCli", "42", "5", "650", "1"])
#time.sleep(0) # prevents taking too many pictures of the least eventful part of the event
print("early c1")
post = Time.Now()
print((post.Utc() - pre.Utc()).total_seconds())

pre = Time.Now()
# 1/1000 to 1/10
subprocess.call(["./brackets/build/RemoteCli", "39", "0", "1350", "1"])
#time.sleep(0) # prevents taking too many pictures of the second least eventful part of the event
print("late c1")
post = Time.Now()
print((post.Utc() - pre.Utc()).total_seconds())

pre = Time.Now()
# 1/4000 to 1/200
subprocess.call(["./brackets/build/RemoteCli", "45", "6", "1400", "1"])
# no sleep here; spamming picture hoping to get baily's beads and the diamond ring
print("c2")
post = Time.Now()
print((post.Utc() - pre.Utc()).total_seconds())

pre = Time.Now()
# 1/1000 to 5.0
subprocess.call(["./brackets/build/RemoteCli", "39", "0", "1500", "1"])
subprocess.call(["./brackets/build/RemoteCli", "22", "0", "7700", "1"])
#time.sleep(0) # totality should last around 3 minutes, so a 2 second break will help to avoid running out of storage space
print("totality")
post = Time.Now()
print((post.Utc() - pre.Utc()).total_seconds())
