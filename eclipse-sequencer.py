from astronomy import Observer, Time, SearchLocalSolarEclipse
import subprocess
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
    return str(shutter_speeds.index(ss))
    
# ---------------- ~~ MODIFY THE BELOW VALUES ~~ ----------------

# Current Latitude (decimal) (should be positive)
lat = 44.1742

# Current Longitude (decimal) (should be NEGATIVE)
long = -74.9223

# Current Altitude
alt = 43.5

# ---------------- ~~ MODIFY THE ABOVE VALUES ~~ ----------------

# Camera Model
model = "ICLE-7M4" # not currently used

# Camera Serial Number
serial = "D073205E77DE" # not currently used

position = Observer(lat, long, alt)
temp_time = Time.Now()

eclipse = SearchLocalSolarEclipse(temp_time, position)

print(eclipse)
print("\n")
print("Partial begins: " + eclipse.partial_begin.time.Utc())
print("Total begins:   " + eclipse.total_begin.time.Utc())
print("Total peaks:    " + eclipse.peak.time.Utc())
print("Total ends:     " + eclipse.total_end.time.Utc())
print("Partial ends:   " + eclipse.partial_end.time.Utc())

delta_test = eclipse.partial_begin.time.Utc() - Time.Now().Utc()
print(delta_test)
print(delta_test.seconds)

#subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", "30", "35", "1", "1"])

while(True):
    p_begin = eclipse.partial_begin.time.Utc() - Time.Now().Utc()
    t_begin = eclipse.total_begin.time.Utc() - Time.Now().Utc()
    t_end = eclipse.total_end.time.Utc() - Time.Now().Utc()
    p_end = eclipse.partial_end.time.Utc() - Time.Now().Utc()

    # partial phase 1, most of disk visible
    # starting 1 minute before C1 and ending 10 minutes before C2
    if p_begin.total_seconds() <= 60 and t_begin.total_seconds() > 600:
        # 1/2000 to 1/100
        subprocess.call(["./brackets/build/RemoteCli", "42", "5", "650", "1"])
        time.sleep(120) # prevents taking too many pictures of the least eventful part of the event
    
    # partial phase 1, less of disk visible
    # starting 10 minutes before C2 and ending 1 minute before C2
    if t_begin.total_seconds() <= 600 and t_begin.total_seconds() > 60:
        # 1/1000 to 1/10
        subprocess.call(["./brackets/build/RemoteCli", "39", "0", "1350", "1"])
        time.sleep(30) # prevents taking too many pictures of the second least eventful part of the event

    # REMOVE CAMERA FILTER HERE!

    # start of totality, fast shutter speeds for beads and ring
    # starting 1 minute before C2 and ending 15 seconds after C2
    if t_begin.total_seconds() <= 60 and t_begin.total_seconds() > -15:
        # 1/4000 to 1/200
        subprocess.call(["./brackets/build/RemoteCli", "45", "6", "1400", "1"])
        # no sleep here; spamming picture hoping to get baily's beads and the diamond ring
    
    # totality, full specturm of shutter speeds for corona HDRs
    # starting 15 seconds after C2 and ending 15 seconds before C3
    if t_begin.total_seconds() <= -15 and t_end.total_seconds() > 15:
        # 1/1000 to 5.0
        subprocess.call(["./brackets/build/RemoteCli", "39", "0", "1500", "1"])
        subprocess.call(["./brackets/build/RemoteCli", "22", "0", "7700", "1"])
        time.sleep(2) # totality should last around 3 minutes, so a 2 second break will help to avoid running out of storage space

    # end of totality, fast shutter speeds for beads and ring
    # starting 15 seconds before C3 and ending 1 minute after C3
    if t_end.total_seconds() <= 15 and t_end.total_seconds() > -15:
        # 1/4000 to 1/200
        subprocess.call(["./brackets/build/RemoteCli", "45", "6", "1400", "1"])
        # no sleep here; spamming picture hoping to get baily's beads and the diamond ring

    # REPLACE CAMERA FILTER HERE!
        
    # partial phase 2, less of disk visible
    # starting 1 minute after C3 and ending 10 minutes after C3
    if t_end.total_seconds() <= -60 and t_end.total_seconds() > -600:
        # 1/1000 to 1/10
        subprocess.call(["./brackets/build/RemoteCli", "39", "0", "1350", "1"])
        time.sleep(5) # prevents taking too many pictures of the second least eventful part of the event
        
    # partial phase 2, most of disk visible
    # starting 10 minutes after C3 and ending 1 minute after C4
    if p_end.total_seconds() >= 600 and p_end.total_seconds() > -60:
        # 1/2000 to 1/100
        subprocess.call(["./brackets/build/RemoteCli", "42", "5", "650", "1"])
        time.sleep(100) # prevents taking too many pictures of the least eventful part of the event
    
