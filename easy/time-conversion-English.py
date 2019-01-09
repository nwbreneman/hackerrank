def timeConversion(s):
    time = s.split(":")

    pm = False
    if time[-1].endswith("PM"):
        pm = True
        time[-1] = time[-1].rstrip("PM")
    else:
        time[-1] = time[-1].rstrip("AM")

    if time[0] == "12" and not pm:
        time[0] = "00"
    elif time[0] != "12" and pm:
        time[0] = str(int(time[0]) + 12)

    return ":".join(time)

