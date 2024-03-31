from astronomy import Observer, Time, SearchLocalSolarEclipse
import subprocess

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

subprocess.check_call([r"./RemoteCli.exe", 30, 35, 1, 1])