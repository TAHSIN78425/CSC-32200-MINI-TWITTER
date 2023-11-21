#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Step 1: System Architecture and User Management

class User:
    def __init__(self, user_id, user_type):
        self.user_id = user_id
        self.user_type = user_type
        self.warnings = 0

class SuperUser(User):
    def process_application(self, applicant, decision):
        if decision == 'accept':
            # Send temporary password
            print(f"Temporary password sent to {applicant.user_id}")
            # Deposit money to the system
            # ...

# Message Structure
class Message:
    def __init__(self, author, timestamp, keywords, content):
        self.author = author
        self.timestamp = timestamp
        self.keywords = keywords
        self.content = content
        self.read_count = 0
        self.likes = 0
        self.dislikes = 0
        self.complaints = 0

# Step 2: Messaging and Interaction Features

class TrendyUser(User):
    def suggest_accounts_to_follow(self):
        # Implement logic to suggest accounts based on user's history
        # ...

# Step 3: Additional Features and GUI

# GUI Development - Simplified Console Interface
class GUI:
    
    def display_top_page(self, top_messages, top_trendy_users):
        # Display top messages and trendy users on the top page
        print("Top Messages:")
        for message in top_messages:
            print(message)
        print("\nTop Trendy Users:")
        for user in top_trendy_users:
            print(user)

# Instantiate Users
super_user = SuperUser("su001", "SU")
ordinary_user = User("ou001", "OU")
trendy_user = TrendyUser("tu001", "TU")

# Instantiate GUI
gui = GUI()

# Display Top Page
gui.display_top_page(["Message 1", "Message 2", "Message 3"], ["User 1", "User 2", "User 3"])

# Process User Application
super_user.process_application(ordinary_user, 'accept')


# In[ ]:




