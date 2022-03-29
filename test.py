from riotapiutilities.api import RiotApi
from riotapiutilities.consts import REGIONS

key = 'RGAPI-ef3247df-953a-4361-80f7-f3f2c255b5d0'
na1_api = RiotApi(key, REGIONS['north_america'])
americas_api = RiotApi(key, REGIONS['americas'])