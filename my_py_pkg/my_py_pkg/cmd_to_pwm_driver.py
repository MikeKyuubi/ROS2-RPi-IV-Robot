import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO

from geometry_msgs.msg import Twist

class VelocitySubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_to_pwm_callback, 10)
        self.left_motor_a = 16
        self.left_motor_b = 18
        left_motor_en = 11

        self.right_motor_a = 38
        self.right_motor_b = 40
        right_motor_en = 36

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.left_motor_a, GPIO.OUT)
        GPIO.setup(self.left_motor_b, GPIO.OUT)
        GPIO.setup(left_motor_en, GPIO.OUT)

        GPIO.setup(self.right_motor_a, GPIO.OUT)
        GPIO.setup(self.right_motor_b, GPIO.OUT)
        GPIO.setup(right_motor_en, GPIO.OUT)

        self.pwm_l = GPIO.PWM(left_motor_en, 1000)
        self.pwm_r = GPIO.PWM(right_motor_en, 1000)

        self.pwm_r.start(79)
        self.pwm_l.start(60)
    
    def cmd_to_pwm_callback(self, msg):
        right_wheel_velocity = (msg.linear.x + msg.angular.z) / 2
        left_wheel_velocity = (msg.linear.x +- msg.angular.z) / 2

        print(right_wheel_velocity, " / ", left_wheel_velocity)

        GPIO.output(self.right_motor_a, right_wheel_velocity > 0)
        GPIO.output(self.right_motor_b, right_wheel_velocity < 0)
        GPIO.output(self.left_motor_a, left_wheel_velocity > 0)
        GPIO.output(self.left_motor_b, left_wheel_velocity < 0)

def main(args=None):
    rclpy.init(args=args)
    node = VelocitySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
