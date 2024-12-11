from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    print("Home route was accessed.")  # แจ้งเมื่อมีการเข้าถึงหน้าแรก
    return "Server is running!"

def run():
    print("Flask server is starting...")  # แจ้งเมื่อเซิร์ฟเวอร์เริ่มทำงาน
    app.run(host='0.0.0.0', port=8080)

def server_on():
    print("Initializing server thread...")  # แจ้งเมื่อเริ่มต้น thread
    t = Thread(target=run)
    t.start()
    print("Server thread started!")  # แจ้งเมื่อ thread เริ่มทำงาน
