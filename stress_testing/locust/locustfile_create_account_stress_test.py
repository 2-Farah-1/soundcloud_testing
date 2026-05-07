import random
import time

from locust import HttpUser, task, between


# simulate many users creating accounts without verifying emails
class TunifyRegistrationStressUser(HttpUser):
    host = "https://tunify.duckdns.org"

    wait_time = between(0.5, 2)

    PASSWORD = "Farah@123"
    GENDER = "FEMALE"
    DATE_OF_BIRTH = "2000-01-01"

    def generate_random_user(self):
        random_number = f"{int(time.time() * 1000)}{random.randint(1000, 9999)}"

        return {
            "email": f"stresstestingaccount{random_number}@gmail.com",
            "username": f"stressuser{random_number}",
            "password": self.PASSWORD,
            "gender": self.GENDER,
            "date_of_birth": self.DATE_OF_BIRTH,
            "avatarUrl": ""
        }

    @task
    def register_user(self):
        payload = self.generate_random_user()

        with self.client.post(
            "/api/auth/register",
            json=payload,
            name="Register User - Unverified",
            catch_response=True,
        ) as response:

            if response.status_code == 201:
                response.success()

            elif response.status_code == 400:
                response.failure(
                    f"Bad request. Maybe payload field names/values are wrong. Response: {response.text[:300]}"
                )

            elif response.status_code == 409:
                response.failure(
                    f"Conflict. Email or username already exists. Response: {response.text[:300]}"
                )

            else:
                response.failure(
                    f"Register failed with status code {response.status_code}: {response.text[:300]}"
                )