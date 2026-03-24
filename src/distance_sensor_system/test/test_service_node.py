import pytest
import rclpy
from distance_sensor_system.service_node import ServiceNode

def test_service_node_initialization():
    
    rclpy.init()
    node = ServiceNode()
    
    assert node.get_name() == 'service_node', "Node name should be 'service_node'"
    
    node.destroy_node()
    rclpy.shutdown()