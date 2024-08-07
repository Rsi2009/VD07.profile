class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

# Пример пользователя
current_user = User(username="JohnDoe", email="john@example.com", password="password123")