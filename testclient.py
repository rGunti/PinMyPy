from pinmypy.client import PinMyPyClient
from pinmypy.objects import Location

client = PinMyPyClient(host="http://localhost:3000",
                       api_key="8Ofntqayo2pgzyTyPiHRara2VI56FmTNlTblXgP52xCaZp774AmbYj30oIDdZmIw")
print(
    client.post_location_update(
        Location(latitude=51.547987000,
                 longitude=7.046349000,
                 altitude=45,
                 gps_time="2018-07-14T15:00:00.000Z")
    )
)
