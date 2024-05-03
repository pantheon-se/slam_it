from locust import HttpUser, between, task
from locust.runners import MasterRunner, WorkerRunner


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Configure wait time between tasks

    @task
    def my_task(self):
        self.client.get("/")


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2 and sys.argv[1] == "worker":
        runner = WorkerRunner([MyUser])
    else:
        runner = MasterRunner([MyUser])
    runner.main()
