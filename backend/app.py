from flask import Flask, request, jsonify
import os
import openai
import config
from openai import OpenAI

openai_api_key = config.OPENAI_API_KEY

app = Flask(__name__)

client = OpenAI()

# In-memory database for simplicity
items = []


@app.route('/get_fit', methods=['GET'])
def get_fit():
    # assume location is passed as a string
    # call openai api with location
    return

@app.route('/translate', methods=['POST'])
def get_fit():
    return

if __name__ == '__main__':
    app.run(debug=True)   