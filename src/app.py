from flask import Flask, jsonify, request
app = Flask(__name__)

# Global variable containing the list of todos
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

# Define the route for '/todos' (POST method)
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    # Add the new todo to the todos list
    new_todo = {
        "label": request_body.get("label"),
        "done": request_body.get("done", False)
    }
    todos.append(new_todo)
    
    # Return the updated list of todos
    return jsonify(todos)

# Define the route for '/todos/<int:position>' (DELETE method)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        deleted_todo = todos.pop(position)
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400

# Keep the lines below at the end of the app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
