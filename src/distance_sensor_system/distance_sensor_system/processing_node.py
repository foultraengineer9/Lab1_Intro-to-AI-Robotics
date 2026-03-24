import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ProcessingNode(Node):
    def __init__(self):
        super().__init__('processing_node')
        
    
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.distance_callback,
            10)
            
        self.publisher_ = self.create_publisher(Float32, 'distance_cm', 10)
        self.get_logger().info("Processing Node has been started. Converting m to cm.")

    def distance_callback(self, msg):
    
        processed_msg = Float32()
        processed_msg.data = msg.data * 100.0
        
    
        self.publisher_.publish(processed_msg)
        self.get_logger().info(f'Processed distance: {processed_msg.data:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = ProcessingNode()
    rclpy.spin(node) 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()