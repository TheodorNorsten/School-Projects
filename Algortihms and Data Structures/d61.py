## LAB1
# Kopiera det här programmet, du kan markera allt med C-a och kopiera med C-c och lägg det i en fil som du döper till p1.a.py och exekvera programmet med python3 p1.a.py


############################################################
#
# Labb 1
#

# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri167499X83Z0QQ5Z16g3YZ5yQ086Y75Z0QgQY6Q5027o5p0ll55qnW67XwWa9WP16bx6ju.html"
kurs = "DD1321.htm"
info = kurs

############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request


class weektimedate:
    def __init__(self):
        self.week= ''
        self.interval= ''
        self.activities= []
        self.time= ''
        self.date= ''

    def __str__(self):
        s = "{ " + self.week + " " + self.time + " " + self.date + " " + self.interval
        if len(self.activities) > 3:
            s += " : " + self.activities[0] + " " + self.activities[1] + " " + self.activities[2] + " " + self.activities[3]
        s += " }"
        return s

    def __contains__(self, x): # added several if statement for each variable
        if x in self.week:
            return True
        elif x in self.interval:
            return True
        elif x in self.activities:
            return True
        elif x in self.time:
            return True
        elif x in self.date:
            return True
        else:
            return False


###########################################################################
##
## parse_url_file
## stores the file in qq's attributes to be stored in a string and then printed later on
##
## IN  file_content - created from imported url from the function get_file_content
##     
## OUT vek - list with all sechedule items and their place in file_content
##
def parse_url_file(file_content):
    vek = []

    reg_expr_w = re.compile('.*?td +class.*?weekColumn.*?>(v.*?)</td', re.I)
    reg_expr_d = re.compile('.*?td.*?class.*?changeDateLink.*?headline.*?>([F-T][a-zåäög]) *(.+?)</td')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)</td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)</td', re.I) 

    lines = file_content.split('\n')
    qq = weektimedate()
    
    '''initiation new local variables before for loop, week, day, weekday,time'''

    week = ""
    day = ""
    weekday = ""
    time = ""
    newEntry = False # boolean that makes us check if its the first time we enter a schema-tid
    
    for j, line in enumerate(lines):

        m = reg_expr_w.match(line)  # sets the week number of the activity
        if (m != None) :
            week = m.group(1)
            print(week)
            next

        m = reg_expr_i.match(line) 
        if (m != None) :            # sets the activity 
            qq.activities.append(m.group(1)) # the activity is stored in a list
            #print(qq.activities)
            if newEntry == False:      
                newEntry = True              # the new entry is done
                #print(qq.activities)
                next
            next
            #print(qq.activities)

        m = reg_expr_d.match(line) 
        if (m != None) :            # sets the date and the weekday for the activity
            weekday = m.group(1)
            day = m.group(2)
            next
      

        m = reg_expr_t.match(line) 
        if (m != None) :            # sets the time interval of the activity (there isn't more than one activity per time interval)

            if newEntry == True:    # new if statement
                vek.append(qq)
                qq = weektimedate()
                next
            time  = m.group(1) 
            qq.week = week
            qq.interval = time
            qq.date = day
            qq.time = weekday
            next
    vek.append(qq)
    return vek


###########################################################################
##
## get file content
## reads the file and stores it in a seperate variable infil
##
## IN  file_name - opens and reads file_name
##     
## OUT file_content - the file_name's content get stored in file_content. 
## infil.readlines() gives error because you can't split the list that is created because it isn't a string.
##
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("	python", sys.argv[0], "--update")
        sys.exit()
       
    #file_read = infil.readlines()
    file_content = infil.read()
    #file_content = ""
    #for i in file_read:
    #    file_content += i

    return file_content
    
###########################################################################
##
## usage
## shows how to use the code
##
## IN  interval
##     
## OUT interval
##
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("	updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("	checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("	prints previously downloaded schedule")
    
###########################################################################
##
## parse_command_line_args
## this function determines what to output on the terminal depedning on the command used
##
## IN  interval
##     
## OUT todo - "tells the script what to do" commandline options
##      dictionary with keys "check" and "update" with values which data type is class string
##
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
## print_schedule
## this functions prints the schedule for the user to see
##
## IN  data - the data for printing the schedule
##     
## OUT interval
##
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
## searches for data to use
##
## IN   what - what dataset contains, class string (ex. "Föreläsning")
##      dataset - dataset with items
##     
## OUT interval
##
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("interval happens", what)

###########################################################################
##
## main
## the main function that uses the other functions
##
## IN  interval
##     
## OUT interval
##
def main():

    global url

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        urllib.request.urlretrieve(url, info) 
        print ("         done")
        
    # Get schedule from disc
    filedata  = get_file_content(info)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)

    
###########################################################################

if __name__ == "__main__":
    main()
