from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        subprocess.run(["bash", "update_site_auto.sh"], check=True)
        return {"status": "success", "message": "Script executed"}, 200
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)