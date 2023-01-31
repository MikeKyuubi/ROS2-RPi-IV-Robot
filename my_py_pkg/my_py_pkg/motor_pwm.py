import RPi.GPIO as GPIO
import time

left_motor_a = 16
left_motor_b = 18
left_motor_en = 11

right_motor_a = 38
right_motor_b = 40
right_motor_en = 36

GPIO.setmode(GPIO.BOARD)

GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)

pwm_l = GPIO.PWM(left_motor_en, 1000)
pwm_r = GPIO.PWM(right_motor_en, 1000)

pwm_r.start(49)
pwm_l.start(40)

def forward(second):
    print("Moving Forward")
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("Moving Reverse")
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)

def left(second):
    print("Moving Left")
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)

def left(second):
    print("Moving Left")
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(second)

def right(second):
    print("Moving Right")
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(second)

def stop():
    print("Stopping")
    pwm_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)

def exit():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(2)
    right(2)
    stop()
    exit()

if __name__ == '__main__':
    main()