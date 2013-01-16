BartFinder
==========

Finds BART trips given start and end stations, and a time.  Uses BeautifulSoup.

Usage
=====

<pre>python bart.py departure_station arrival_station (time) (number_of_queries)</pre>

<b>departure_station</b>: The station where you will be starting from.  Input a string a characters without spaces -- either the station name ("downtownberkeley" -- some abbreviations work such as "dtwnberkeley"), or the known 4-letter BART abbreviation (DBRK).  Case does not matter.

<b>arrival_station</b>: Identical to <b>departure_station</b>, except it will be the station where you wish to arrive.  For trips involving train transfers, this is your final destination.

<b>time</b>: The time you wish to depart.  Acceptible formats are without spaces: "5:05pm", "5:05PM", or "now."  This is an optional argument that will be set to the current time ("now") on default.

<b>number_of_queries</b>: The number of soonest trips you would like to see.  This is an optional argument that defaults to 3.
