# Telegram Phishing Demonstration Tool

**IMPORTANT: This tool is for EDUCATIONAL PURPOSES ONLY**

This application demonstrates how phishing attacks work to educate users about security risks. It simulates a Telegram login page to show how credentials can be captured through deceptive websites.

## Educational Purpose

This tool is designed exclusively for:
- Cybersecurity education and awareness training
- Classroom demonstrations on phishing techniques
- Understanding social engineering attack vectors

## Ethical Usage Guidelines

- **NEVER** use this tool for actual phishing or any malicious activity
- **ONLY** use in controlled educational environments
- **ALWAYS** obtain explicit consent from all participants
- **DELETE** all captured data after educational demonstrations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-phishing-demo.git
cd telegram-phishing-demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Access the demonstration at: http://localhost:5000

## Features

- Simulated Telegram login page
- Two-factor authentication simulation
- Admin dashboard to view captured data
- Educational disclaimers throughout the application
- Mobile-responsive design

## Project Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, and image files
- `captured_data.json` - Stores demonstration data

## Legal Disclaimer

This tool is provided for educational purposes only. The developers assume no liability and are not responsible for any misuse or damage caused by this program. Users are responsible for ensuring they comply with all applicable laws and regulations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Deployment Instructions

To deploy this educational  tool:

```bash
git clone https://github.com/yourusername/telegram-phishing-demo.git
cd telegram-phishing-demo
```

```bash
python -m venv venv
```

On Linux/Mac:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
