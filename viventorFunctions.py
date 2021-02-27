import requests, json

class viventor:

    def __init__(self, username, password):
       self.username = username
       self.password = password
       self.base_url = 'https://api.viventor.com/api/ia'
       self.token = self.login()

    def login (self,):
        failureKeys = ['BAD_CREDENTIALS', 'NOT_EMPTY']
        data = {"email": self.username, "password": self.password, "web": True}
        endpoint = '/clients/authentication'

        resp = requests.post(self.base_url + endpoint, json=data)

        if any(failureKey in resp.text for failureKey in failureKeys):
            return 'login failed'

        jsn = json.loads(resp.text)
        print (jsn['token'])
        return jsn['token']


    def outstanding_balance(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/outstanding-balance'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text

    def investor (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/investor'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text

    def all_time_transaction_summary (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/all-time-transaction-summary'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text

    #def fit_summary (self):
    #    pass

    def strategies (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/strategies'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text

    def originators (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/originators'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text

    def investment_summary_by_loan_type (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-loan-type'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text


    def investment_summary_by_country (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-country'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text


    def investment_summary_by_maturity (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-maturity'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text


    def investment_summary_by_loan_status (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-loan-status'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text

    def investment_summary_by_interest (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-interest'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text

    def investment_summary_by_loan_originator (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-loan-originator'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text

    def investment_summary_by_rating (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/accounts/investment-summary-by-rating'
        data = {"outstanding_only": True, "portfolios": [], "originators": [], "graph_type": "AMOUNT"}
        resp = requests.post(self.base_url + endpoint, json=data, headers=headers)
        return resp.text


    #def expected_cash_flows (self):
    #    pass

    def loan_configuration (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        endpoint = '/loan-configuration'
        resp = requests.get(self.base_url + endpoint, headers=headers)
        return resp.text


    def refresh_token (self):
        headers = {"Authorization": f"Bearer {self.token}"}
        url = 'https://api.viventor.com/api/refreshtoken'
        resp = requests.get(url, headers=headers)
        return resp.text


