class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def request_support(self, support_type):
        return {
            "status": "created",
            "type": support_type,
            "user": self.name
        }
