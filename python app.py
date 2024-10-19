from flask import Flask, jsonify
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information using subprocess
    process_info = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    # Gather relevant system information
    system_info = {
        'name': 'Your Name',  # Replace with your name
        'username': os.getenv('USER') or os.getenv('USERNAME'),  # Get the system username
        'server_time': time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime()),  # Server time in IST
        'top_output': process_info.splitlines()[:10]  # Get first 10 lines of 'top' output for brevity
    }

    return jsonify(system_info)

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
