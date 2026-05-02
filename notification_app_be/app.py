from flask import Flask, request, jsonify
app = Flask(__name__)
notifications = [
    {
        "id": 1,
        "title": "Service Reminder",
        "message": "Vehicle service is due tomorrow",
        "status": "pending"
    }
]
@app.route("/")
def home():
    return "Backend server is running"
@app.route("/notifications", methods=["GET"])
def get_notifications():
    return jsonify(notifications)
@app.route("/notifications", methods=["POST"])
def add_notification():
    data = request.json
    new_notification = {
        "id": len(notifications) + 1,
        "title": data["title"],
        "message": data["message"],
        "status": "pending"
    }
    notifications.append(new_notification)
    return jsonify(new_notification)
if __name__ == "__main__":
    app.run(port=5000, debug=True)