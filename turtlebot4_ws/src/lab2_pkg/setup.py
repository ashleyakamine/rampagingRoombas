from setuptools import find_packages, setup

package_name = 'lab2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vincent.c.le',
    maintainer_email='vincent.c.le@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'speed_cap_obstacle_detect_node = lab2_pkg.speed_cap_obstacle_detect:main',
        ],
    },
)
