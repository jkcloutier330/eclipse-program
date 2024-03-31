from astronomy import Observer, Time, SearchLocalSolarEclipse
import subprocess
import json

def toCodeString(ss):
    with open('./shutter_speeds.txt') as f:
        raw = f.read()
    dictionary =json.loads(raw)

    return 
    

# ---------------- ~~ MODIFY THE BELOW VALUES ~~ ----------------

# Current Latitude (decimal) (should be positive)
lat = 44.1742

# Current Longitude (decimal) (should be NEGATIVE)
long = -74.9223

# Current Altitude
alt = 43.5

# Camera Model
model = "ICLE-7M4" # not currently used

# Camera Serial Number
serial = "D073205E77DE" # not currently used

# ---------------- ~~ MODIFY THE ABOVE VALUES ~~ ----------------

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

subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", "30", "35", "1", "1"])

while(True):
    p_begin = eclipse.partial_begin.time.Utc() - Time.Now().Utc()
    t_begin = eclipse.total_begin.time.Utc() - Time.Now().Utc()
    t_end = eclipse.total_end.time.Utc() - Time.Now().Utc()
    p_end = eclipse.partial_end.time.Utc() - Time.Now().Utc()

    if p_begin.total_seconds() <= 10 and p_begin.total_seconds():
        subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", toCodeString(1.0), toCodeString(0.001), "1", "1"])



