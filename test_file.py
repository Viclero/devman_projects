import datetime
now = datetime.datetime.now()
 
then = datetime.datetime(2023, 1, 29, 13,15,30)

d = now-then

t = datetime.timedelta(hours=2, minutes=30)
print(now)
print(then)
h = int(d/datetime.timedelta(hours=1)) 
m = int(d/datetime.timedelta(minutes=1) - h*60) 

#print( f'{h}ч {m}мин' )

stay =  now-then

def  get_duration():
    stay =  now-then
    print(stay)

def  format_duration(td):
    h = int(td/datetime.timedelta(hours=1)) 
    m = int(td/datetime.timedelta(minutes=1) - h*60) 

    print(f'{h}ч {m}мин')


#get_duration()
#format_duration(stay)


def is_visit_long(  minutes=60):
    duration = now-then 

    if duration.total_seconds()/60 > minutes:      
        return True
    # TODO пишите код здесь
    else: 
        return False


print(  is_visit_long() )