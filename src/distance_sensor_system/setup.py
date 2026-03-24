import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'distance_sensor_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
     data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add these two lines to install launch and config files:
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='k4',
    maintainer_email='k4@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
     entry_points={
        'console_scripts': [
            'sensor_node = distance_sensor_system.sensor_node:main',
            'processing_node = distance_sensor_system.processing_node:main',
            'service_node = distance_sensor_system.service_node:main',
        ],
    },
)
