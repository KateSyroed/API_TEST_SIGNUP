import requests
from user_signup import UserSignUp
from user_login import UserLogin

class TestAuth:
    def sign_up(self):
        self.session = requests.session()
        user_sign_up = UserSignUp(name="Name", last_name="LastName", email="test1988@test.com", password="Qwerty12345", repeat_password="Qwerty12345")
        response = self.session.post(url="https://qauto2.forstudy.space/api/auth/signup", json=user_sign_up.__dict__)
        assert response.status_code == 200, f"Failed to log in user: {'Account is not created'}"

    def login(self):
        self.user_to_login = UserLogin("test1988@test.com", "Qwerty12345", False)
        response = self.session.post(url="https://qauto2.forstudy.space/api/auth/signin",
                          json=self.user_to_login.__dict__)
        assert response.status_code == 200, f"Failed to log in user: {'Wrong account'}"