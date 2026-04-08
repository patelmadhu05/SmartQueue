from flask import Flask, request, jsonify
from priority_queue import add_patient, get_next_patient

app = Flask(__name__)

@app.route('/')
def home():
    return "SmartQueue Backend Running!"

@app.route('/next', methods=['GET'])
def next_patient():
    patient = get_next_patient()
    
    if patient is None:
        return jsonify({"message": "No patients in queue"})
    
    from priority_queue import queue

@app.route('/queue', methods=['GET'])
def view_queue():
    return jsonify(queue)
    
    priority, name = patient
    
    return jsonify({
        "name": name,
        "priority": priority
    })

if __name__ == '__main__':
    app.run(debug=True)