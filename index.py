from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

with open("recipe.json") as f:
    json_data = json.load(f)

prev = []

def generate_random_index (array_list):
    while True:
        new_index = random.randint(0, (len(array_list) - 1))
        if new_index not in prev:
            break
    prev.append(new_index)
    if len(prev) > 3:
        prev.pop(0)
    return new_index


@app.route("/", methods=["GET"])
def get_recipes():
    return jsonify(json_data), 200

@app.route("/get-recipe", methods=["GET"])
def get_random_recipe ():
    random_index = generate_random_index(json_data)
    random_recipe = json_data[random_index]
    return jsonify(random_recipe), 200

if __name__ == "__main__":
    app.run(debug=True, port=2000)