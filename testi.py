#store/print in readable format
from multiprocessing import Process,Pool
from google.transit import gtfs_realtime_pb2
import urllib.request
import time
from routeinfo import give_coord,getrouteid
from geopy.distance import geodesic


tt={}
rname=(input())
st_lat_lon=give_coord(rname)
rid=getrouteid(rname)
def loop_a():
	for i in range(4,len(st_lat_lon)//2-1):
		start=st_lat_lon[i]
		stop=st_lat_lon[i+1]
		print(start)
		print(stop)
		flag=0
		kid='yo'
		ch='y'
		s1=s2=0
		while (ch=='y'):	
			feed = gtfs_realtime_pb2.FeedMessage()
			response = urllib.request.urlopen("https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=vNWztvpuYoe0dwaUpPTgEFrYNfS0hetR")
			feed.ParseFromString(response.read())	
			rt_trips={}
			lg=len(feed.entity)
			print(lg)
			for entity in feed.entity:
				ot = {}
				t = {}
				t['trip_id'] = entity.vehicle.trip.trip_id
				t['route_id'] = entity.vehicle.trip.route_id
				ot['trip'] = t
				p = {}
				p['lat'] = entity.vehicle.position.latitude
				p['long'] = entity.vehicle.position.longitude
				ot['position'] = p
				ot['timestamp'] = entity.vehicle.timestamp
				bid=entity.vehicle.vehicle.id
				rt_trips[bid] = ot
				st=[]
				if(entity.vehicle.trip.route_id==rid):#and entity.vehicle.position.speed!=0)	
					l2=(entity.vehicle.position.latitude,entity.vehicle.position.longitude)
					st.append(bid)
					if(flag==1 and kid==bid):
						if((geodesic(stop,l2).km)<=0.03):
							s2=entity.vehicle.timestamp
							ch='n'
							kid='yo'
							flag=0
							tt[i]=s2-s1
							s1=s2=0
							print(tt)
							break
						else:
							break	
					elif ((geodesic(start,l2).km)<=0.03 and flag==0):
						kid=bid
						flag=1
						s1=entity.vehicle.timestamp
					print(bid,rt_trips[bid])
			# if ((kid not in st) and flag==1):
			# 	kid='yo'
			# 	print('k',st)
			# 	s1=0
			# 	flag=0
			print(s2,s1,'loop1')
			print(s2-s1)		
			time.sleep(10)					
print(tt)
def loop_b():
	for i in range(len(st_lat_lon)//2+4,len(st_lat_lon)-1):
		start=st_lat_lon[i]
		stop=st_lat_lon[i+1]
		print(start)
		print(stop)
		flag=0
		kid='yo'
		ch='y'
		s1=s2=0
		while (ch=='y'):	
			feed = gtfs_realtime_pb2.FeedMessage()
			response = urllib.request.urlopen("https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=vNWztvpuYoe0dwaUpPTgEFrYNfS0hetR")
			feed.ParseFromString(response.read())	
			rt_trips={}
			lg=len(feed.entity)
			print(lg)
			for entity in feed.entity:
				ot = {}
				t = {}
				t['trip_id'] = entity.vehicle.trip.trip_id
				t['route_id'] = entity.vehicle.trip.route_id
				ot['trip'] = t
				p = {}
				p['lat'] = entity.vehicle.position.latitude
				p['long'] = entity.vehicle.position.longitude
				ot['position'] = p
				ot['timestamp'] = entity.vehicle.timestamp
				bid=entity.vehicle.vehicle.id
				rt_trips[bid] = ot
				st=[]
				if(entity.vehicle.trip.route_id==rid):#and entity.vehicle.position.speed!=0)	
					l2=(entity.vehicle.position.latitude,entity.vehicle.position.longitude)
					st.append(bid)
					if(flag==1 and kid==bid):
						if((geodesic(stop,l2).km)<=0.03):
							s2=entity.vehicle.timestamp
							ch='n'
							kid='yo'
							flag=0
							tt[i]=s2-s1
							s1=s2=0
							print(tt)
							break
						else:
							break	
					elif ((geodesic(start,l2).km)<=0.03 and flag==0):
						kid=bid
						flag=1
						s1=entity.vehicle.timestamp
					print(bid,rt_trips[bid])
			# if ((kid not in st) and flag==1):
			# 	kid='yo'
			# 	print('k',st)
			# 	s1=0
			# 	flag=0
			print(s2,s1,'loop2')
			print(s2-s1)		
			time.sleep(10)	
print(tt)

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
