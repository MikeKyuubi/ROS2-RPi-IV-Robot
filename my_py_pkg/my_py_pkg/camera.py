import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
import cv2

class video_publisher(Node):
    def __init__(self):
        super().__init__('robot_video_publisher')
        self.publisher_ = self.create_publisher(Image, '/robot_video_feed', 10)
        self.timer = self.create_timer(timer_period, self.camera_callback)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.bridge = CvBridge()
    
    def camera_callback(self):
        ret, frame = self.cap.read()
        frame = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
        self.publisher_.publish(frame)

def main(args=None):
    rclpy.init(args=args)
    node = video_publisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

