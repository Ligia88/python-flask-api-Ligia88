from flask import Flask, jsonify, request
app = Flask(__name__)

# Global variable containing the list of todos
todos = [
    { "label": "feed the cat", "done": False },
    { "label": "Make the bed", "done": False }
]

# Define the route for '/todos' (GET method)
@app.route('/todos', methods=['GET'])
def get_todos():
    # Return the JSON version of the todos list
    return jsonify(todos)

# Define the route for '/todos' (POST method)
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

# Keep the lines below at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
