import pytest
import rclpy
from distance_sensor_system.processing_node import ProcessingNode

def test_processing_node_initialization():

    rclpy.init()
    node = ProcessingNode()
    
    assert node.get_name() == 'processing_node', "Node name should be 'processing_node'"
    
    node.destroy_node()
    rclpy.shutdown()