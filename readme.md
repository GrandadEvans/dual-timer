[![Build Status](https://travis-ci.org/GrandadEvans/dual-timer.svg?branch=master)](https://travis-ci.org/GrandadEvans/dual-timer)
# Dual Timer
This project is here because I couldn't find a solution to what I wanted

## Features (not yet complete)

*  2 Separate Timers. 1 for the time spent on a project & 1 for the billable time
*  Store Projects and tasks locally or sync with Freeagent
*  Monitor the title of the active window & if 1 or more keywords are found in the title the timer starts

## Features (complete)
If you want to check out the DualTimer tag this was me playing around with Python and it has a GUI which has 2 timers as described above. They can be controlled independently but currently there is no persistence layer so make sure that you note the times down before you exit the application

### Freeagent

*  Add timesheets to Freeagent
*  Sync projects & tasks

This project (once complete) will be brilliant for freelancers like me.
If you are working on a project called "GrandadEvans" you could add this word to a list of keywords containing things like "PHPStorm".
You could either start/stop the timer manually from the docking utility or you could rely on the window title feature.
When a window changes and the title (or application) is not recognised it will add a few buttons to the dock.

*  Add to the watch list
*  Ignore this window

All of this information would either be stored in files or synced to your Freeagent account.

I have all the knowledge to do this & it is now just finding the time to get it all coded and working.

## TDD
The project is built using Test Driven Design methodology using py.test.

## Newbie
Please take into account that Python is not my primary programming language of choice & I normally use PHP