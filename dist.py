from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
def distance(l1,l2):
	R = 6373.0

	lat1 = radians(l1[0])
	lon1 = radians(l1[1])
	lat2 = radians(l2[0])
	lon2 = radians(l2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance
#print("Should be:", 278.546, "km")