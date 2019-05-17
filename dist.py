#sampele code for calculating diatance between 2 geolocations

from geopy.distance import geodesic

l1=(28.704118728637695, 77.21355438232422)
l2=(28.705001, 77.212055)

print(geodesic(l1,l2).km)
