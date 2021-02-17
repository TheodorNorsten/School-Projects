import re
import json
import urllib
import urllib.request
import sys

def get_data(schemaurl, data):
    ''' Funktionen hämtar data från REST API, returnerar json objekt.
    IN: endpoint + data som består av parametrar vi vill få ut
    UT: JSON objekt.'''
    schemaurl += data
    request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
    utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
    datastruktur = json.loads(utf_data)                     # lägger in i en pythonstruktur
    return datastruktur

def print_schema(datastruktur, n):
    ''' Funktionen skriver ut schemat för Json-fil
    IN: JSOn objekt och n(antalet element i Json filen)'''
    i = 0
    while i != n:
        startdata = datastruktur["entries"][i]["start"] # start parameter i JSON
        enddata = datastruktur["entries"][i]["end"] # end parameter i JSON
        enddata = enddata.strip()
        enddata = enddata.split(" ")
        enddata = enddata[1] # plocka endast ut datumet
        titledata = datastruktur["entries"][i]["title"] # typ av lektion
        locations = datastruktur["entries"][i]["locations"] # sal

        print(startdata, end="-")
        print(enddata, end=" ")
        print(titledata, end=" ")
        for x in locations:
            print(x["name"], end=" ")
        print("")
        i += 1

if __name__ == '__main__':
    schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
    pattern= re.compile(r'(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])')
    
    if len(sys.argv) == 2:# input: kursnamn
        course = sys.argv[1]
        datastruktur = get_data(schemaurl, course)
        n = datastruktur['entries']
        print("Schema för ", course)
        print_schema(datastruktur, len(n))

    elif len(sys.argv) == 3: # input kursnamn, startdatum
        course = sys.argv[1]
        start = sys.argv[2]
        
        correct= pattern.findall(start) # kolla regex
        if correct:
            data = course + "?startTime=" + start
            datastruktur = get_data(schemaurl, data)
            n = datastruktur['entries']
            print("Schema för ", course)
            print_schema(datastruktur, len(n))
        
        else:
            print("Datum är inte i rätt format YYYY-MM-DD")
            exit()
        
        


    elif len(sys.argv) == 4: # input kursnamn, start, slut
        course = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]

        correct_start= pattern.findall(start)
        correct_end= pattern.findall(end)

        if correct_start and correct_end: # kolla regex

            data = course + "?startTime=" + start + "&endTime=" + end
            datastruktur = get_data(schemaurl, data)
            n = datastruktur['entries']
            print("Schema för ", course)
            print_schema(datastruktur, len(n))


        else:
            print("Datum är inte i rätt format YYYY-MM-DD")
            exit() 
      

        
