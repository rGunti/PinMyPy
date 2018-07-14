from urllib.parse import urlencode
from urllib.request import Request, urlopen
from .objects import PinMyPyObject, Location


class PinMyPyClient(object):
    def __init__(self, host, api_key):
        """
        Creates a new client
        :param string host: Base URL (including protocol) of the PinMyPi installation (e.g. "https://example.com/")
        :param string api_key: API Key to authenticate the request
        """
        self.host = host
        self.api_key = api_key

    def _get_url(self, route):
        """
        Returns a URL that combines the given route with the Base URL and the API key
        :param string route: Route
        :return string:
        """
        return self.host + route + "?apikey=" + self.api_key

    def _post(self, route, data):
        """
        Issues a POST request to the given route with the given data
        :param string route: Route to POST to
        :param PinMyPyObject data: Data to POST
        :return:
        """
        url = self._get_url(route)
        request = Request(url, urlencode(data.to_json_dict()).encode())
        response = urlopen(request).read().decode()
        return response

    def post_location_update(self, data):
        """
        Posts location updates
        :param Location data:
        :return:
        """
        return self._post("/api/device/update", data)
