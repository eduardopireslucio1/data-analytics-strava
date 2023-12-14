import pandas as pd


class CalculateEvolutionOfYear:
    def __init__(self, activities, year, year_comparation):
        self.activities = activities
        self.year = year
        self.year_comparation = year_comparation

    def execute(self):
        df = pd.DataFrame(self.activities)
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['year'] = df['start_date'].dt.year
        df['month'] = df['start_date'].dt.month

        activities_year = df[df['year'] == self.year]
        activities_year_comparation = df[df['year'] == self.year_comparation]

        distance_by_month_year = activities_year.groupby(['year', 'month'])['distance'].sum()
        distance_by_month_comparation = activities_year_comparation.groupby(['year', 'month'])['distance'].sum()

        # result_dict = {
        #     f"{year}-{month}": distance
        #     for (year, month), distance in distance_by_month_year.to_dict().items()
        # }
        #
        # return result_dict





