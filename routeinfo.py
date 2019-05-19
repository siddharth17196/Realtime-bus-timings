import csv

with open('stop_times.csv', 'r') as f:
  reader = csv.reader(f)
  stop_time = list(reader)

with open('trips.csv', 'r') as f:
  reader = csv.reader(f)
  trips= list(reader)  

with open('routes.csv', 'r') as f:
  reader = csv.reader(f)
  route = list(reader)

with open('stops.csv', 'r') as f:
  reader = csv.reader(f)
  stops = list(reader)  

a=c='0'
rid_to_tid={}
for i in range(len(trips)):
	if(c!=a):								#	1 trip_id for same route_id 
		rid_to_tid[a]=trips[i-1][2]
		a=c
	if(i!=len(trips)-1):	
		c=trips[i+1][0] 
	else:
		rid_to_tid[a]=trips[i-1][2]		

arr={}
a=c=0
for i in range(len(stop_time)-1):
	if(c!=a):								# row number of that common trip id 
		a=c
		arr[a]=i
	c=stop_time[i+1][0] 	

rtid={}
for i in range(len(route)-1):				# route name to route_id
	rtid[route[i+1][1]]=int(route[i+1][3])

rtid.pop('745EUp', None)
rtid.pop('114+182A_D', None)				# NON-EXISTENT ROUTES
rtid.pop('182ADOWN',None)
rtid.pop('182AUP',None)
rtid.pop('460UP',None)


stop_list={}
for key in rtid:
	l=[]
	c=int(rid_to_tid[str(rtid[key])])	
	k=1		
	m=0										# list of stops corresponding to the trip_id
	while (int(rid_to_tid[str(rtid[key])])==c):
		l.append(stop_time[arr[rid_to_tid[str(rtid[key])]]+m][3])
		c=int(stop_time[arr[rid_to_tid[str(rtid[key])]]+k][0])
		k+=1
		m+=1
	stop_list[rtid[key]]=l
print(stop_list)

def give_coord (routeid):
	sel_rt=trp_id[routeid]					# list of coordinates of consecutive stops
	st_lat_lon=[]
	for i in range(len(stop_list[sel_rt])):
		tup=(stops[int(stop_list[sel_rt][i])+1][3],stops[int(stop_list[sel_rt][i])+1][4])
		st_lat_lon.append(tup)
	return st_lat_lon	