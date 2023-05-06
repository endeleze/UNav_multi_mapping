from setuptools import setup

package_name = 'Collaborate_mapping'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Anbang Yang',
    maintainer_email='ay1620@nyu.edu',
    description='Multi-robot UNav mapping data collection',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'launch=Collaborate_mapping.launch:main'
        ],
    },
)
