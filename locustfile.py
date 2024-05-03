from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Configure wait time between tasks

    @task
    def my_task(self):
        self.client.get("/")
