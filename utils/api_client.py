import requests
from config.config import BASE_URL, API_KEY

# class APIClient:

#     def __init__(self) -> None:
#         self.base_url = BASE_URL
#         self.headers = {
#             "x-api-key" : API_KEY
#         }

#     def get(self, endpoint):
#         return requests.get(f"{self.base_url}{endpoint}", headers = self.headers)
    
#     def post(self, endpoint, payload):
#         return requests.post(f"{self.base_url}{endpoint}", json=payload, headers = self.headers)
    
#     def put(self, endpoint, payload):
#         return requests.put(f"{self.base_url}{endpoint}", json=payload, headers = self.headers)
    
#     def delete(self, endpoint):
#         return requests.delete(f"{self.base_url}{endpoint}", headers = self.headers)

    


class APIClient:

    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key" : API_KEY
        })

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}{endpoint}")
    
    def post(self, endpoint, payload):
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)
    
    def put(self, endpoint, payload):
        return self.session.put(f"{self.base_url}{endpoint}", json=payload)
    
    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}")