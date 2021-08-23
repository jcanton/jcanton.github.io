---
permalink: /maps/
title: "Autometed maps"
---

As for 2020, with lockdowns extending into 2021, my girlfriend and I continue
our morning commute-substituting walks.

<iframe title="Walking map" src="map_walking.html" height="500"
width="100%"></iframe>

The map is interactive: you can move around and get info on each track by
simply clicking on it. You can also change the aesthetics and visualise a heat
map by opening the layers menu.

This map is updated daily by my Raspberry Pi with code from my
[garminMaps](https://github.com/jcanton/garminMaps) repository.
The code interfaces with the Garmin Connect API, gathers, filters and processes
the data, and generates the map employing the Folium library.
