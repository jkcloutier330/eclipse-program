from astronomy import Observer, Time, SearchLocalSolarEclipse

#(my current location +3deg lat to get into totality)
# lat, long, alt.
position = Observer(44.1742, -74.9223, 43.5)
time = Time.Now()

eclipse = SearchLocalSolarEclipse(time, position)

print(eclipse)