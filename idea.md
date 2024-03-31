pre-conditions:
1. RemoteCli.exe is built from David's files
    a. must have correct serial number for your camera
    b. must have correct model type
2. shutter speed code list is compilated and formatted into LUT
3. shutter speed sequences for each timeframe are entered into python script
4. GPS coordinates are obtained (thru phone) and entered into python script

python script process:
1. get next eclipse position based on entered coordinates, save eclipse_event for later use
2. main loop
    a. calculate deltas between current time and each event (in seconds)
    # calcualte each iteration

    # chose which looping sequence to execute based on current time deltas
    # 10 seconds is just a placeholder. real intervals will be determined based on research/ripping off other people
    b. if delta_partial_begin =< 10 and delta_total_begin > 10
        i. execute partial eclipse sequence
        # sequences arguments: starting shutter speed, ending shutter speed, increment (?), loop count
        # shutter speeds will be described here as floats, converted with function in line
    c. elif delta_total_begin =< 10 and delta_total_begin > -10
        ii. execute baily's beads & diamond ring sequence
    d. elif delta_total_begin >= -10 and delta_total_end <10
        iii. execute corona sequence
    e. elif delta_total_end =< 10 and delta_total_end > -10
        iv. execute baily's beads & diamond ring sequence
    f. elif delta_total_end >= -10 and delta_partial_end > -10
        v. execute partial eclipse sequence

functions:
- convert numeric shutter speed to coded shutter speed
    - shutter speeds in the script are given as floats
        - 1.000 is 1", 8.000" is 8", .01 is 1/100", .00025 is 1/4000", etc.
    - codes must be pre-obtained by running the stock version of RemoteCli
    - do something like a switch-case thing, but smarter and less dumb
