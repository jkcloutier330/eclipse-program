from astronomy import Observer, Time, SearchLocalSolarEclipse
import subprocess
import json

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
print(delta_test.total_seconds())

with open('./shutter_speeds.txt') as f:
    raw = f.read()
dictionary =json.loads(raw)

print(dictionary)

# subprocess.call(["./pi export 20240324/sonyapp/build/RemoteCli", "30", "35", "1", "1"])