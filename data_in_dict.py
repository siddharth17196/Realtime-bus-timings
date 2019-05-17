#store/print in readable format

from google.transit import gtfs_realtime_pb2
import urllib.request

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.request.urlopen("https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=vNWztvpuYoe0dwaUpPTgEFrYNfS0hetR")
feed.ParseFromString(response.read())

rt_trips={}
lg=len(feed.entity)
print(lg)
for entity in feed.entity:
  #if entity.HasField('trip_update'):
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
	print(bid,rt_trips[bid])
  #break
#print(rt_trips)