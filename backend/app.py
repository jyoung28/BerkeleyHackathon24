from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for simplicity
items = []