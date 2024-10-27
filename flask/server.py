from flask import Flask, render_template, request, jsonify
import serial
import time

app = Flask(__name__)

# Initialize connection to Arduino
try:
    ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
    time.sleep(2)  # Wait for the connection to establish
    print('Arduino initialized')
except serial.SerialException as e:
    print(f"Error initializing Arduino: {e}")

@app.route('/sensor')
def read_sensors():
    try:
        ser.write(b'R')  
        time.sleep(0.1)
        line = ser.readline().decode('utf-8').strip()
        data = line.split(' ')
        print(data)

        
        accel_data = data[0].split(':')[1].split(',')
        light_data = data[1].split(':')[1]
        sound_data = data[2].split(':')[1]

        data = {
            "accel_x": accel_data[0],
            "accel_y": accel_data[1],
            "accel_z": accel_data[2],
            "light": light_data,
            "sound": sound_data
        }

        return jsonify(data)
        
    except Exception as e:
        print(f"Error reading sensors: {e}")
        data = {
            "accel_x": "Error",
            "accel_y": "Error",
            "accel_z": "Error",
            "light": "Error",
            "sound": "Error"
        }

        return jsonify(data)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    author = "Suchita"
    
    if request.method == 'POST':
        if request.form['submit'] == 'Turn On':
            ser.write(b'H')  # Send 'H' to turn on the LED
        elif request.form['submit'] == 'Turn Off':
            ser.write(b'L')  # Send 'L' to turn off the LED
    
    return render_template('index.html', author=author) 




@app.route('/alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    message = data.get('message', 'Alert')

    try:
        ser.write(b'A')  # Send 'A' as the command to display alert
        time.sleep(0.1)
        ser.write(message.encode('utf-8'))  # Send the alert message text
        return jsonify({"status": "Alert sent to Arduino"}), 200
    except Exception as e:
        print(f"Error sending alert to Arduino: {e}")
        return jsonify({"status": "Failed to send alert"}), 500
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')