from json import loads
from requests import Session
from datetime import datetime as dt

API_URL = 'http://www.netcodepool.org/oldapi.php?api_key={0}'


class NetCodePoolAPI:
    def __init__(self, key):
        self.key = key
        self.sesh = Session()

    def refresh(self):
        """Updates the internal data"""
        content = loads(self.sesh.get(API_URL.format(self.key)).content)
        self.data = {
            'stats': {
                'username': content['username'],
                'rewards': content['username'],
                'hashrate': content['total_hashrate'],
                'history': content['payout_history'],
                'estimate': content['round_estimate']
            },
            'workers': {}
        }

        for k, v in content['workers'].items():
            self.data['workers'][k] = {
                'alive': int(v['alive']) == 1,
                'hashrate': int(v['hashrate']),
                'last_share': dt.fromtimestamp(int(v['last_share_timestamp']))
            }

    def get_stat(self, stat):
        """Returns the specific stat specified"""
        return self.data['stats'][stat] if stat in self.data['stats'] else None

    def get_stats(self):
        """Returns a dict of the user stats"""
        return self.data['stats']

    def get_workers(self):
        """Lists the workers as of the last request"""
        return self.data['workers']

    def get_worker(self, name):
        """Gets the worker stats by name"""
        if not name in self.data['workers']:
            return None

        return self.data['workers'][name]


if __name__ == '__main__':
    print 'You have to implement the API yourself!'
