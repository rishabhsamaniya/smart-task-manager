class User:
    def __init__(self, user_id, username, email):
        self.__user_id = user_id
        self.__username = username
        self.__email = email

    # Getter for user_id

    def get_user_id(self):
        return self.__user_id

    # Getter for user_id

    def get_username(self):
        return self.__username    
    
     # Setter for username

    def set_username(self, username):
        if len(username) < 3:
            print("Username must be at least 3 characters long")
        else:
            self.__username = username

    # Getter for email

    def get_email(self):
        return self.__email
    
    # Setter for email

    def set_email(self, email):
        if "@" not in email:
            print("Invalid email address")
        else:
            self.__email = email
    
    def __str__(self):
        return f"""
User Id = {self.__user_id}
Username = {self.__username}
Email = {self.__email}
"""


