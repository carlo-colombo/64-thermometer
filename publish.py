from umqtt.robust import MQTTClient
import network

def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def read_credentials_and_connect():
    try:
        with open('wifi-creds.txt') as creds:
            print('WiFi credentials found')

            ssid = creds.readline().strip()
            password = creds.readline().strip()
            
            do_connect(ssid, password)

    except OSError:
        print("WiFi credentials not found, create a file with 'username\npassword'")
        
import machine, ubinascii

hwid = ubinascii.hexlify(machine.unique_id()).decode('utf-8')

print("hardware id", hwid)

def mqttClient(server):
    name = f"64-thermometer-{hwid}"
    mqttClient = MQTTClient(name, server)
    print(f"Instantiating {name} ({server})", mqttClient.connect())

    def publish(key, value):
        mqttClient.publish(f"/64-thermometer/{hwid}/{key}", str(value))
        
    return publish

