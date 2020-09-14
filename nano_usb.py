from serial import Serial

def setup(port = '/dev/ttyUSB0'):
  global ard
  ard = Serial(port, 9600,timeout=5)

def send(msg):
  global ard
  if type(msg) is int:
    ard.write(bytes([msg]))
  elif type(msg) is list:
    two_bytes = msg[0:2]
    if len(msg) == 3:
      two_bytes += [int(msg[2] / 256), msg[2] % 256]
    else:
      two_bytes += [0,0]
    ard.write(bytes(two_bytes))
  elif type(msg) is bytes:
    ard.write(msg)
  elif type(msg) is str:
    ard.write(str.encode(msg))

def listen():
  global ard
  sensors = []
  ard.write([255])
  for i in range(14):
    sensors.append(ard.read())
  return(sensors)

def close():
  global ard
  ard.close()

print("Imported NANO_USB!")
print("Use the .setup() function to set the port -- default is /dev/ttyUSB0")
