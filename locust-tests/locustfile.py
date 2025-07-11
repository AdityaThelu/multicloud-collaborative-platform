from locust import HttpUser, task, between

class MultiCloudUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def upload_file(self):
        with open("sample-files/example.txt", "rb") as f:
            files = {'file': f}
            self.client.post("/upload", files=files)
