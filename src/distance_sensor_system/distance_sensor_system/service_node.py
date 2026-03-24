import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from distance_sensor_interfaces.srv import SetThreshold

class ServiceNode(Node):
    def __init__(self):
        super().__init__('service_node')
        self.threshold = 1.0 
        
       
        self.srv = self.create_service(
            SetThreshold, 
            'set_threshold', 
            self.set_threshold_callback
        )
        
        
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.distance_callback,
            10
        )
        self.get_logger().info("Service Node started. Default safety threshold: 1.0m")

    def set_threshold_callback(self, request, response):
       
        self.threshold = request.threshold
        response.success = True
        response.message = f"Safety threshold successfully updated to {self.threshold:.2f}m"
        self.get_logger().info(response.message)
        return response

    def distance_callback(self, msg):
       
        if msg.data < self.threshold:
            self.get_logger().warn(f"ALERT: Distance {msg.data:.2f}m is below the safe threshold of {self.threshold:.2f}m!")

def main(args=None):
    rclpy.init(args=args)
    node = ServiceNode()
    rclpy.spin(node) 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()