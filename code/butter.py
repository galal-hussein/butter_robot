from time import sleep
from gpiozero import AngularServo, Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from stream import StreamingHandler, StreamingServer, output
import picamera
from http import server

motor_1_a_pin = 19
motor_1_b_pin = 26
motor_2_a_pin = 16
motor_2_b_pin = 20

neck_servo_pin = 17
left_arm_servo_pin = 27
right_arm_servo_pin = 22

factory = PiGPIOFactory()
neck_servo = AngularServo(neck_servo_pin, min_angle=-90, max_angle=90, pin_factory=factory)
left_arm_servo = AngularServo(left_arm_servo_pin, min_angle=-90, max_angle=90, pin_factory=factory)
right_arm_servo = AngularServo(right_arm_servo_pin, min_angle=-90, max_angle=90, pin_factory=factory)
robot = Robot(left=(motor_1_a_pin, motor_1_b_pin), right=(motor_2_a_pin, motor_2_b_pin), pin_factory=factory)
camera = picamera.PiCamera(resolution='640x480', framerate=24)

def main():
    
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()

