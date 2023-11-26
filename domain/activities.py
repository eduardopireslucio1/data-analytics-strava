from collections import defaultdict
from datetime import datetime


class Activities:
    def __init__(self, activities):
        self.activities = activities

    def calculate_metrics(self):
        total_activities = 0
        total_distance = 0
        rides_per_year = defaultdict(int)
        distance_per_year = defaultdict(int)
        elevation_gain_per_year = defaultdict(int)
        moving_time_per_year = defaultdict(int)
        average_ride_distance_per_year = defaultdict(int)
        average_ride_elevation_per_year = defaultdict(int)
        total_activities_per_year = defaultdict(int)
        average_speed_per_year = defaultdict(int)

        for activity in self.activities:
            data_hora_obj = datetime.strptime(activity.get('start_date'), "%Y-%m-%dT%H:%M:%SZ")
            year = data_hora_obj.year

            rides_per_year[year] += 1
            distance_per_year[year] += activity.get('distance')
            elevation_gain_per_year[year] += activity.get('total_elevation_gain')
            total_distance += activity.get('moving_time')
            moving_time_per_year[year] += activity.get('moving_time')
            total_activities_per_year[year] += 1
            total_activities += 1

        for year, value in dict(distance_per_year).items():
            average_ride_distance_per_year[year] = round(value / rides_per_year[year])
        for year, value in dict(elevation_gain_per_year).items():
            average_ride_elevation_per_year[year] = round(value / rides_per_year[year])

        average_distance = total_distance / total_activities

        return (rides_per_year,
                distance_per_year,
                elevation_gain_per_year,
                average_distance,
                moving_time_per_year,
                average_ride_distance_per_year,
                average_ride_elevation_per_year)
