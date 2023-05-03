import psutil

battery = psutil.sensors_battery()

if battery is None:
    print("Unable to retrieve battery information.")
else:
    # print(battery)
    plugged = battery.power_plugged
    percent = battery.percent
    time = battery.secsleft
    # power_usage = battery.power_now / 1000  # Convert mW to W


    if plugged:
        print("Power Source: Plugged in")
        print("Battery Percentage:", percent)
        print(f"Remaining time left: N.A")
    else:
        print("Power Source: Battery")
        print("Battery Percentage:", percent)
        print(f"Remaining time left: {time}s")

    # print("Power Consumption:", power_usage, "W")
