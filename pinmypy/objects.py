

class PinMyPyObject(object):
    def to_json_dict(self):
        """
        Converts the object to a dict
        :return dict:
        """
        raise NotImplementedError()


class Location(PinMyPyObject):
    def __init__(self,
                 latitude=0,
                 longitude=0,
                 altitude=0,
                 epx=-1,
                 epy=-1,
                 epv=-1,
                 speed=-1,
                 gps_time=None,
                 additional=None):
        """
        :param float latitude:
        :param float longitude:
        :param int altitude:
        :param int epx:
        :param int epy:
        :param int epv:
        :param float speed:
        :param string gps_time:
        :param any additional:
        """
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.epx = epx
        self.epy = epy
        self.epv = epv
        self.speed = speed
        self.gps_time = gps_time
        self.additional = additional

    def to_json_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'epx': self.epx,
            'epy': self.epy,
            'epv': self.epv,
            'speed': self.speed,
            'gpsTime': self.gps_time,
            'additional': self.additional
        }
