from locust import HttpUser, task, between

class FlipkartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def search_product(self):
        self.client.get("/search?q=laptop")

    @task
    def view_cart(self):
        self.client.get("/viewcart")
