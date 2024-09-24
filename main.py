from flask import Flask, render_template
from flask_socketio import SocketIO
import controls
import socket

app = Flask(__name__, template_folder='front', static_folder='front', static_url_path='')
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html', ip_host=ip_host, port=port)


@socketio.on('cev')
def handle_connect_event(msg):
    print(f'Client {msg} connected')


@socketio.on('sev')
def handle_message_event(msg):
    # print(f'Accelerometer Y: {msg}')
    controls.control_steering(float(msg))


@socketio.on('gas_hold')
def handle_gashold_event(msg):
    print('Gas HOLD')
    controls.gas_hold()


@socketio.on('gas_release')
def handle_gasrelease_event(msg):
    print('Gas RELEASE')
    controls.gas_release()


@socketio.on('brake_hold')
def handle_brakehold_event(msg):
    print('Brake HOLD')
    controls.brake_hold()


@socketio.on('brake_release')
def handle_brakerelease_event(msg):
    print('Brake RELEASE')
    controls.brake_release()

def get_local_ip():
    # Создаем временное подключение для получения локального IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Пытаемся подключиться к любому внешнему серверу (Google DNS)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# required
ip_host = get_local_ip()
port = input('Enter port: ' )

if __name__ == '__main__':
    print('Running on http://' + ip_host + ':' + port)
    socketio.run(app, host=ip_host, port=port)
