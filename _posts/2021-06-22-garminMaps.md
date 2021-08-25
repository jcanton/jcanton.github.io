---
title: "Automated GPX maps"
date: 2021-06-22T21:12:57+0200
categories:
 - blog
tags:
 - coding
 - python
 - data analysis
last_modified_at: 2021-08-24T17:52:51+0200
---

As for 2020, with lockdowns extending into 2021, my girlfriend and I continue
our morning commute-substituting walks.
We got bored repeating routes we already did and so I decided to visualize our
data in some useful and fun way.

[![Walking map][1t]{: .align-center}][1]

## Other implementations

[Strava](https://www.strava.com) allows you to visualize nice heat maps, but
only for running, swimming and cycling, and I was interested in walking.
Besides, once the heat map is generated, you cannot get information on
individual activities, so the functionality is a little limited.

[Quantified Self](https://quantified-self.io) is a really cool open source
projects that can connect with Garmin or Suunto and provide most of the
functionality I was looking for.
However, the web interface is slow and somewhat buggy - and you have to
share your GPX tracks with yet another web service.

[dérive](https://erik.github.io/derive/) is a second very cool open source
project.  Differently from Quantified Self, all the processing takes place in
your browser and your tracks are not stored on their (GitHub pages) servers.
The only issue with dérive is that, besides visualising the heat map and
tracks, there is not much customisation and info on individual tracks.
The simplicity and aesthetics of this project, however, are fantastic and
inspired me to create my own.

## Implementing my own maps

I typically work with Python and have coded several side-projects with it,
enough to know that if you can think of an idea you can almost surely realise
it with Python - and somebody might have already written a package with some of
the implementation (much like with LaTeX).

I was not wrong: I found both
[garminconnect](https://github.com/cyberjunky/python-garminconnect), a neat
package that provides a Python 3 API for Garmin Connect, and
[Folium](http://python-visualization.github.io/folium/), which builds on top of
the [Leaftlet](https://leafletjs.com/) mapping library and allows to easily
create maps from within Python.

[1]:  /maps/
[1t]: /assets/images/walkingMap.gif
