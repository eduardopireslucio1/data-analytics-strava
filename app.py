import requests
from domain.activities import Activities
from domain.authorization import Authorization


def run():
    url = 'https://www.strava.com/api/v3'
    authorization = Authorization()
    headers = authorization.get_headers()
    activities_data = requests.get(f'{url}/athlete/activities?after=1262354647&per_page=100', headers=headers).json()

    use_case = Activities(activities_data)
    (rides_per_year,
     distance_per_year,
     elevation_gain_per_year,
     average_distance,
     moving_time_per_year,
     average_ride_distance_per_year,
     average_ride_elevation_per_year) \
        = use_case.calculate_metrics()


