#!/usr/bin/env python
kmh = int(input("Enter km/h: "))
mph =  0.6214 * kmh
print("Speed:", kmh, "KM/H = ", mph, "MPH")
print("{:.2f}".format(mph))