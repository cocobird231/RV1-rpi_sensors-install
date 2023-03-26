import os
from glob import glob
from setuptools import setup

package_name = 'py_singlerf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'launch'), glob('launch/common.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='coco',
    maintainer_email='cocobird231@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sender = py_singlerf.rfsend:main', 
            'receiver = py_singlerf.rfrecv:main', 
            'pub = py_singlerf.rfAll:main'
        ],
    },
)
