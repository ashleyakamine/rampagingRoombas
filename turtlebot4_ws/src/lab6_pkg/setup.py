from setuptools import find_packages, setup

package_name = 'lab6_pkg'

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
    maintainer='ashley.akamine@plu.edu',
    maintainer_email='ashley.akamine@plu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "go_to_goal = lab6_pkg.go_to_goal_server:main",
            "go_to_goal_client = lab6_pkg.go_to_goal_client:main"
        ],
    },
)
