import pandas as pd


class CalculateMetricsPerYear:
    def __init__(self, activities):
        self.activities = activities

    def execute(self):
        df = pd.DataFrame(self.activities)
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['year'] = df['start_date'].dt.year

        total_activities = len(df)
        total_distance = df['distance'].sum()
        total_moving_time = df['moving_time'].sum()
        rides_per_year = df.groupby('year')['distance'].count()
        distance_per_year = df.groupby('year')['distance'].sum()
        moving_time_per_year = df.groupby('year')['moving_time'].sum()

        average_ride_distance_per_year = distance_per_year / rides_per_year
        average_ride_elevation_per_year = df.groupby('year')['total_elevation_gain'].mean()
        average_speed_per_year = df.groupby('year')['average_speed'].mean()
        elevation_gain_per_year = df.groupby('year')['total_elevation_gain'].sum()

        average_distance = total_distance / total_activities

        df_metrics = pd.DataFrame({
            'rides_per_year': rides_per_year,
            'distance_per_year': distance_per_year,
            'elevation_gain_per_year': elevation_gain_per_year,
            'moving_time_per_year': moving_time_per_year,
            'average_ride_distance_per_year': average_ride_distance_per_year,
            'average_ride_elevation_per_year': average_ride_elevation_per_year,
            'average_speed_per_year': average_speed_per_year
        })
        metrics = df_metrics.to_dict()
        return metrics
