#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")
        self.publisher_ = self.create_publisher(Int16, '/pub_topic', 10)
        timer_ = 0.1
        self.timer = self.create_timer(timer_, self.timer_callback)
        self.iterator = 0
        self.get_logger().info("Publisher has been started")

    def timer_callback(self, msg):
        msg = Int16()
        msg.data = self.iterator
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        self.iterator += 1


def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
