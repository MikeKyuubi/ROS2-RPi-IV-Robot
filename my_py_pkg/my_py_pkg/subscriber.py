#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.subscriber_ = self.create_subscription(
            Int16, "pub_topic", self.listener_callback, 10)
        self.subscriber_    
        self.get_logger().info("Subscriber has been started")

    def listener_callback(self, msg):
        self.get_logger().info('Subscribing "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()