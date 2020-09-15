from serial import Serial

### Low Level Function
######################

def setup(port = '/dev/ttyUSB0'):
  global ard
  ard = Serial(port, 9600,timeout=5)

def close():
  global ard
  ard.close()

def send(msg):
  global ard
  if type(msg) is list:
    two_bytes = msg[0:2]
    if len(msg) == 3:
      two_bytes += [int(msg[2] / 256), msg[2] % 256]
    else:
      two_bytes += [0,0]
    ard.write(bytes(two_bytes))
  elif type(msg) is int:
    ard.write(bytes([msg]))
  elif type(msg) is bytes:
    ard.write(msg)
  elif type(msg) is str:
    ard.write(str.encode(msg))

def listen(): # I'm really beginning to doubt the utility of this...
  global ard
  sensors = []
  ard.write([255])
  for i in range(14):
    sensors.append(ard.read())
  return(sensors)

### High Level Functions
########################

def digitalRead(pin):
  send([1, pin, 1])
  return(ard.read() == bytes([0]))

def servoWrite(pin, val):
  send([3, pin, val])

print("Imported NANO_USB!")
print("Use the .setup() function to set the port -- default is /dev/ttyUSB0")
