from time import sleep
from gpiozero import AngularServo, Robot
from gpiozero.pins.pigpio import PiGPIOFactory

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

while True:
    neck_servo.angle = 45
    sleep(5)
    exit(0)