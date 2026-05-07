import os
import random

from locust import HttpUser, task, between

#simulate many users searching 
class TunifySearchStressUser(HttpUser):
    host = "https://tunify.duckdns.org"

    wait_time = between(0.5, 2)

    EMAIL = os.getenv("TUNIFY_EMAIL", "softwaretestacc198@gmail.com")
    PASSWORD = os.getenv("TUNIFY_PASSWORD", "Farah@123")

    SEARCH_PARAM = os.getenv("TUNIFY_SEARCH_PARAM", "q")

    GLOBAL_SEARCH_TERMS = [
        "Farah",
        "Yara",
        "dreamin",
        "505",
        "night",
        "quality time",
        "zzzznotfound123",
    ]

    TRACK_SEARCH_TERMS = [
        "dreamin",
        "505",
        "night",
        "quality time",
        "A Million Dreams",
        "zzzznotfound123",
    ]

    PEOPLE_SEARCH_TERMS = [
        "Farah",
        "Yara",
        "farahjnn",
        "farahelhebeishy",
        "Farahs_Demon",
        "randomnomatch999",
    ]

    COLLECTION_SEARCH_TERMS = [
        "yaraaaa",
        "album1",
        "TEST",
        "Try A",
        "randomnomatch999",
    ]

    def on_start(self):#login and store access token
        self.auth_headers = {}

        login_payload = {
            "email": self.EMAIL,
            "password": self.PASSWORD,
        }

        with self.client.post(
            "/api/auth/login",
            json=login_payload,
            name="Login for search stress",
            catch_response=True,
        ) as response:

            if response.status_code not in [200, 201]:
                response.failure(
                    f"Login failed with status code {response.status_code}: {response.text[:300]}"
                )
                return

            try:
                data = response.json()
            except Exception:
                response.failure("Login response was not valid JSON.")
                return

            token = self.extract_access_token(data)

            if not token:
                response.failure(
                    f"Login succeeded but access token was not found. Response keys: {list(data.keys())}"
                )
                return

            self.auth_headers = {
                "Authorization": f"Bearer {token}"
            }

            response.success()

    def extract_access_token(self, data):#trying different token names cuz honestly no idea how backend works
        possible_tokens = [
            data.get("accessToken"),
            data.get("token"),
            data.get("access_token"),
            data.get("jwt"),
        ]

        if isinstance(data.get("data"), dict):
            possible_tokens.extend([
                data["data"].get("accessToken"),
                data["data"].get("token"),
                data["data"].get("access_token"),
                data["data"].get("jwt"),
            ])

        if isinstance(data.get("tokens"), dict):
            possible_tokens.extend([
                data["tokens"].get("accessToken"),
                data["tokens"].get("token"),
                data["tokens"].get("access_token"),
            ])

        for token in possible_tokens:
            if token:
                return token

        return None

    def search_request(self, endpoint, terms, request_name):
        term = random.choice(terms)

        params = {
            self.SEARCH_PARAM: term
        }

        with self.client.get(
            endpoint,
            params=params,
            headers=self.auth_headers,
            name=request_name,
            catch_response=True,
        ) as response:

            if response.status_code == 200:
                response.success()

            elif response.status_code in [401, 403]:
                response.failure(
                    f"Auth failed on {request_name}. Status code: {response.status_code}. "
                    f"Maybe token/header format is wrong."
                )

            elif response.status_code == 400:
                response.failure(
                    f"Bad request on {request_name}. Status code 400. "
                    f"Maybe query parameter should not be '{self.SEARCH_PARAM}'. "
                    f"Response: {response.text[:300]}"
                )

            else:
                response.failure(
                    f"{request_name} failed with status code {response.status_code}: {response.text[:300]}"
                )

    @task(4)
    def global_search(self):
        self.search_request(
            endpoint="/api/search",
            terms=self.GLOBAL_SEARCH_TERMS,
            request_name="Global Search",
        )

    @task(3)
    def search_tracks(self):
        self.search_request(
            endpoint="/api/search/tracks",
            terms=self.TRACK_SEARCH_TERMS,
            request_name="Search Tracks",
        )

    @task(2)
    def search_people(self):
        self.search_request(
            endpoint="/api/search/people",
            terms=self.PEOPLE_SEARCH_TERMS,
            request_name="Search People",
        )

    @task(2)
    def search_collections(self):
        self.search_request(
            endpoint="/api/search/collections",
            terms=self.COLLECTION_SEARCH_TERMS,
            request_name="Search Collections",
        )