



def get_url(schemaurl, data):
    schemaurl += data
    request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
    utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
    datastruktur = json.loads(utf_data)                     # lägger in i en pythonstruktur
    return datastruktur



def skrivut_schema():
    
