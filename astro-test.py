from astronomy import Observer, Time, SearchLocalSolarEclipse
import subprocess
import json

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
    return str(shutter_speeds.index(ss))
   

#(my current location +3deg lat to get into totality)
# lat, long, alt.
position = Observer(44.1742, -74.9223, 43.5)
time = Time.Now()

eclipse = SearchLocalSolarEclipse(time, position)

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

print(shutter_speeds.index(30))
print(shutter_speeds.index(10))
print(shutter_speeds.index(1))
print(shutter_speeds.index(.01))
print(shutter_speeds.index(.00625))

# subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", "30", "35", "1", "1"])

p_begin = 60
t_begin = 180
t_end = 280
p_end = 340

while(True):

    # partial phase 1, most of disk visible
    # starting 1 minute before C1 and ending 10 minutes before C2
    if p_begin <= 60 and p_begin > 600:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/2000), toCodeString(1/100), "3", "1"])
        time.sleep(100) # prevents taking too many pictures of the least eventful part of the event
    
    # partial phase 1, less of disk visible
    # starting 10 minutes before C2 and ending 1 minute before C2
    if t_begin <= 600 and t_begin > 60:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/1000), toCodeString(1/10), "3", "1"])
        time.sleep(5) # prevents taking too many pictures of the second least eventful part of the event

    # REMOVE CAMERA FILTER HERE!

    # start of totality, fast shutter speeds for beads and ring
    # starting 1 minute before C2 and ending 15 seconds after C2
    if t_begin <= 60 and t_begin > 15:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/4000), toCodeString(1/200), "2", "1"])
        # no sleep here; spamming picture hoping to get baily's beads and the diamond ring
    
    # totality, full specturm of shutter speeds for corona HDRs
    # starting 15 seconds after C2 and ending 15 seconds before C3
    if t_begin <= 15 and t_end > 15:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/1000), toCodeString(5), "2", "1"])
        time.sleep(2) # totality should last around 3 minutes, so a 2 second break will help to avoid running out of storage space

    # end of totality, fast shutter speeds for beads and ring
    # starting 15 seconds after C3 and ending 1 minute after C3
    if t_end <= 15 and t_end > 15:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/4000), toCodeString(1/200), "2", "1"])
        # no sleep here; spamming picture hoping to get baily's beads and the diamond ring

    # REPLACE CAMERA FILTER HERE!
        
    # partial phase 2, less of disk visible
    # starting 1 minute after C3 and ending 10 minutes after C3
    if t_end >= 60 and p_begin < 600:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/1000), toCodeString(1/10), "3", "1"])
        time.sleep(5) # prevents taking too many pictures of the second least eventful part of the event
        
    # partial phase 2, most of disk visible
    # starting 10 minutes after C3 and ending 1 minute after C4
    if p_end >= 600 and p_end < 60:
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1/2000), toCodeString(1/100), "3", "1"])
        time.sleep(100) # prevents taking too many pictures of the least eventful part of the event

    p_begin -= 1
    t_begin -= 1
    t_end -= 1
    p_end -= 1