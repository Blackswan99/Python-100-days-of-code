# PascalCase for class names
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    # pass
    # for keeping the class empty in the beginning


user1 = User("001", "Ted")
user2 = User("002", "Marc")

user1.follow(user2)
print(f"User 1 has {user1.followers} followers.")
print(f"User 2 has {user2.followers} followers.")

print(f"User 1 is following {user1.following} users.")
print(f"User 2 is following {user2.following} users.")
