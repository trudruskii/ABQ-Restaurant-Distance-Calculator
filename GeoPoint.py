import math

# Create a class to manage geographic points and calculate distances
class GeoPoint:
    def __init__(self, lat=0, lon=0, description='TBD'):
        """Initialize GeoPoint with latitude, longitude, and description."""
        self.__lat = lat
        self.__lon = lon
        self.__description = description

    # Property for the point coordinates for latitude and longitude
    @property
    def Point(self):
        """Get or set the point coordinates"""
        return self.__lat, self.__lon

    # Set the latitude and longitude of the GeoPoint
    @Point.setter
    def Point(self, coords):
        """Set the point coordinates using a sequence"""
        self.__lat, self.__lon = coords

    # Calculate and return the distance between the GeoPoint and given coordinates
    def Distance(self, to_point):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1 = math.radians(self.__lat), math.radians(self.__lon)
        lat2, lon2 = math.radians(to_point.Point[0]), math.radians(to_point.Point[1])

        # Spherical law of cosines formula
        dist = 6371.01 * math.acos(
            math.sin(lat1) * math.sin(lat2) +
            math.cos(lat1) * math.cos(lat2) *
            math.cos(lon1 - lon2)
        )
        return dist

    @property
    def Description(self):
        """Get or set the description"""
        return self.__description
    @Description.setter
    def Description(self, description):
        """Set the description."""
        self.__description = description


