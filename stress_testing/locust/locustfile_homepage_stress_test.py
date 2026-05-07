from locust import HttpUser, task, between

#simulate many users visitng our website at the same time (only uses GET so the tests have to be aggressive-ish)
class TunifyHomepageUser(HttpUser):
    host = "https://tunify.duckdns.org"

    # Each virtual user waits randomly between 0.1 and 0.5 seconds (i feel like doing no wait is overkill)
    # before opening the homepage again.
    wait_time = between(0.1, 0.5)

    @task
    def open_homepage(self):
        with self.client.get("/", name="Open Tunify homepage", catch_response=True) as response:
            # 200 means OK.
            # 301/302/304 are also acceptable because websites sometimes redirect/cache.
            if response.status_code in [200, 301, 302, 304]:
                response.success()
            else:
                response.failure(
                    f"Homepage failed with status code {response.status_code}"
                )