# Login Feature Module

users = {
    "admin": "admin123",
    "student": "stud123"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful")
        return True
    else:
        print("Invalid username or password")
        return False

# Sample usage
login("admin", "admin123")
login("student", "wrongpass")
