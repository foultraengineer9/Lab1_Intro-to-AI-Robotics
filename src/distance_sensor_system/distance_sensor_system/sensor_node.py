import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorNode(Node):
    def __init__(self):
        
        super().__init__('sensor_node')
        
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Sensor Node has been started.")

    def timer_callback(self):
    
        msg = Float32()
        msg.data = random.uniform(0.5, 10.0)
        
       
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance: {msg.data:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node) 
    rclpy.shutdown()

if __name__ == '__main__':
    main()