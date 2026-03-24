import pytest
import rclpy
from distance_sensor_system.sensor_node import SensorNode

def test_sensor_node_initialization():

    rclpy.init()
    node = SensorNode()
    
    assert node.get_name() == 'sensor_node', "Node name should be 'sensor_node'"
    

    node.destroy_node()
    rclpy.shutdown()