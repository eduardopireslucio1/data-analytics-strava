import requests
import os


class StravaGatewayHttp:
    token = ''
    headers = {}
    STRAVA_API_URL = 'https://www.strava.com/api/v3'
    PARAM_AFTER = '1262354647'
    PARAM_PER_PAGE = '100'

    def __init__(self):
        self.set_headers()

    def get_activities(self):
        return requests.get(
            f'{self.STRAVA_API_URL}/athlete/activities?after={self.PARAM_AFTER}&per_page={self.PARAM_PER_PAGE}',
            headers=self.headers).json()

    def set_headers(self):
        access_token = os.environ['ACCESS_TOKEN']
        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }

    @staticmethod
    def get_token():
        data = {
            'client_id': os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET'],
            'code': os.environ['AUTHORIZATION_CODE'],
            'grant_type': 'authorization_code'
        }

        try:
            response = requests.post('https://www.strava.com/oauth/token', data=data).json()
            access_token = response.get('access_token')
            if access_token:
                return access_token
        except Exception as e:
            print(f"Erro na solicitação {e}")
        return None
