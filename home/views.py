from django.shortcuts import render  , redirect

import mysql.connector as sql  
std = '' 
ddt = '' 
rdt = '' 
drn = ''

nm = '' 
eml = ''
sds = ''

ctn = '' 
srv = '' 
dsc = ''








def index(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "FindDestination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into pat Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'index.html') 

    

def index(request):
    global nm , eml , sds
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml  = value 
            if key == "Destination" :
                sds = value 
            
           
            

        c = "insert into gat Values('{}' ,'{}' , '{}'  )".format(nm , eml , sds) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'index.html') 

    

def corporate(request):
    global nm , eml , ctn , srv , dsc 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml = value 
            if key == "ContactNumber" :
                ctn = value 
            
            if key == "Services" :
                srv = value 
            if key == "Description" :
                dsc = value 
            

        c = "insert into lat Values('{}' ,'{}' , '{}' , '{}' , '{}'  )".format(nm , eml , ctn , srv , dsc) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'corporate.html') 



def education(request):
    global nm , eml , ctn , srv , dsc 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml = value 
            if key == "ContactNumber" :
                ctn = value 
            
            if key == "Services" :
                srv = value 
            if key == "Description" :
                dsc = value 
            

        c = "insert into rat Values('{}' ,'{}' , '{}' , '{}' , '{}'  )".format(nm , eml , ctn , srv , dsc) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'educational.html') 


def package(request):
    global nm , eml , ctn , srv , dsc 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml = value 
            if key == "ContactNumber" :
                ctn = value 
            
            if key == "Services" :
                srv = value 
            if key == "Description" :
                dsc = value 
            

        c = "insert into jat Values('{}' ,'{}' , '{}' , '{}' , '{}'  )".format(nm , eml , ctn , srv , dsc) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'package.html') 



def social(request):
    global nm , eml , ctn , srv , dsc 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml = value 
            if key == "ContactNumber" :
                ctn = value 
            
            if key == "Services" :
                srv = value 
            if key == "Description" :
                dsc = value 
            

        c = "insert into zat Values('{}' ,'{}' , '{}' , '{}' , '{}'  )".format(nm , eml , ctn , srv , dsc) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'social.html') 


def specialevents(request):
    global nm , eml , ctn , srv , dsc 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml = value 
            if key == "ContactNumber" :
                ctn = value 
            
            if key == "Services" :
                srv = value 
            if key == "Description" :
                dsc = value 
            

        c = "insert into dft Values('{}' ,'{}' , '{}' , '{}' , '{}'  )".format(nm , eml , ctn , srv , dsc) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'special_events.html') 


def specialeventform(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Destination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into vgh  Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'special_events.html') 



def tourpackages(request):
    global nm , eml , sds
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml  = value 
            if key == "Destination" :
                sds = value 
            
           
            

        c = "insert into sed  Values('{}' ,'{}' , '{}'  )".format(nm , eml , sds) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'tourpackages.html') 


def tourpackageform(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Destination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into kpl  Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'tourpackages.html') 


def packageform(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Destination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into dfg  Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'package.html') 


def socialform(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Destination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into hjk  Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'social.html') 


def carsform(request):
    global nm , eml , sds
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Name" :
                nm = value
            if key == "Email" :
                eml  = value 
            if key == "Destination" :
                sds = value 
            
           
            

        c = "insert into ted  Values('{}' ,'{}' , '{}'  )".format(nm , eml , sds) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'cars.html') 



def carsduration(request):
    global std , ddt , rdt , drn 
    if request.method == "POST" :
        m = sql.connect(host = "localhost" , user = "root" , password = "" , database = "empl" )
        cursor = m.cursor() 
        d = request.POST 
        for key , value in d.items():
            if key == "Destination" :
                std = value
            if key == "DepartDate" :
                ddt = value 
            if key == "ReturnDate" :
                rdt = value 
            
            if key == "Duration" :
                drn = value 
            

        c = "insert into cardur  Values('{}' ,'{}' , '{}' , '{}'  )".format(std , ddt , rdt , drn) 
        cursor.execute(c) 
        m.commit() 

    return render(request , 'cars.html') 






def corporateHome(request):

    return render (request , 'index.html')

def educationHome(request):

    return render (request , 'index.html')

def packageHome(request):

    return render (request , 'index.html')

def socialHome(request):

    return render (request , 'index.html')


def specialeventsHome(request):

    return render (request , 'index.html')

def tourpackagesHome(request):

    return render (request , 'index.html')


def tourpackages(request):

    return render (request , 'package.html')

def corporateeducation(request):

    return render (request , 'educational.html')

def corporatesocial(request):

    return render (request , 'social.html')

def corporatespecial(request):

    return render (request , 'special_events.html')


def educationcorporate(request):

    return render (request , 'corporate.html')

def educationsocial(request):

    return render (request , 'social.html')

def educationspecial(request):

    return render (request , 'special_events.html')

def socialspecial(request):

    return render (request , 'special_events.html')


def socialeducation(request):

    return render (request , 'educational.html')

def socialsocial(request):

    return render (request , 'social.html')

def specialcorporate(request):

    return render (request , 'corporate.html')

def specialeducation(request):

    return render (request , 'educational.html')

def specialsocial(request):

    return render (request , 'social.html')

def specialspecial(request):

    return render (request , 'special_events.html')

def corporatecorporate(request):

    return render (request , 'corporate.html')

def educationeducation(request):

    return render (request , 'educational.html')

def cars(request):

    return render (request , 'select.html')

def Buses(request):

    return render (request , 'select2.html')


def Trains(request):

    return render (request , 'select3.html')


def Flights(request):

    return render (request , 'select4.html')

def Flightscars(request):

    return render (request , 'select.html')

def FlightsBuses(request):

    return render (request , 'select.html')

def FlightsTrains(request):

    return render (request , 'select.html')

def FlightsFlights(request):

    return render (request , 'select.html')

def carsFlights(request):

    return render (request , 'select.html')

def carscars(request):

    return render (request , 'select.html')


def carsBuses(request):

    return render (request , 'select.html')


def carsTrains(request):

    return render (request , 'select.html')

def BusesBuses(request):

    return render (request , 'Buses.html')

def Busescars(request):

    return render (request , 'select.html')

def BusesTrains(request):

    return render (request , 'select.html')

def BusesFlights(request):

    return render (request , 'select.html')


def Trainscars(request):

    return render (request , 'train.html')

def TrainsBuses(request):

    return render (request , 'select.html')

def TrainsTrains(request):

    return render (request , 'select.html')

def TrainsFlights(request):

    return render (request , 'select.html') 

def Flightscars(request):

    return render (request , 'select.html') 

def FlightsBuses(request):

    return render (request , 'select.html') 

def FlightsTrains(request):

    return render (request , 'select.html') 


def FlightsFlights(request):

    return render (request , 'select.html') 


def corporatemeeting(request):

    return render (request , 'corporate_board_meeting.html') 


def corporatemeetingcorporate(request):

    return render (request , 'corporate.html') 


def corporateconfrence(request):

    return render (request , 'corporate_conference.html') 

def corporatenetwork(request):

    return render (request , 'corporate_social_networking_event.html') 

def corporatewebinar(request):

    return render (request , 'corporate_webinar.html') 

def corporateworkshop(request):

    return render (request , 'corporate_workshop.html') 

def corporatepackage(request):

    return render (request , 'package.html') 

def educationcamp(request):

    return render (request , 'educational_camp.html') 

def educationtrip(request):

    return render (request , 'educational_educational_tour_trip.html') 


def educationseminar(request):

    return render (request , 'educational_seminar.html') 


def educationsummit(request):

    return render (request , 'educational_summit.html') 


def socialanniversary(request):

    return render (request , 'social_anniversary.html') 


def socialfamily(request):

    return render (request , 'social_family_reunion.html') 



def socialphoto(request):

    return render (request , 'social_pre_wedding_photoshoot.html') 

def socialreception(request):

    return render (request , 'social_reception.html') 


def socialtrip(request):

    return render (request , 'social_tour_trip.html') 

def socialwedding(request):

    return render (request , 'social_wedding.html') 

def specialaward(request):

    return render (request , 'special_events_award_show.html') 


def specialdance(request):

    return render (request , 'special_events_dance_event.html') 






def specialexhibition(request):

    return render (request , 'special_events_exhibition.html') 

def specialretreat(request):

    return render (request , 'special_events_retreat.html') 


def specialreligious(request):

    return render (request , 'special_events_spiritual_and_religious.html') 


def specialtournament(request):

    return render (request , 'special_events_sports_event_tournament.html') 

def educationpackage(request):

    return render (request , 'package.html') 

def educationeducational(request):

    return render (request , 'educational.html') 





def select(request):

    return render (request , 'select.html') 

def  carscars(request):

    return render (request , 'cars.html') 

def  Busbus(request):

    return render (request , 'Buses.html') 

def  traintrain(request):

    return render (request , 'trains.html') 

def  flightflight(request):

    return render (request , 'flights.html') 


def  tpgs(request):

    return render (request , 'package.html') 





def  tcrs(request):

    return render (request , 'trains.html') 

def  fcrs(request):

    return render (request , 'flights.html') 








