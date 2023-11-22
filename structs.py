
from flask import Flask, request, render_template


class User:
    def __init__(self, creds):
      
        self.username = request.form['username']
        self.password = request.form['password']


# Message Structure
class Message:
    def __init__(self, Message):
        message = request.form['message']
        author = ""
        likes = 0
        dislikes = 0
