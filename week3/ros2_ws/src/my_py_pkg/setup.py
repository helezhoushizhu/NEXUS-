from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer='lyp',
    maintainer_email='helezhoushizhu@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "hello_node=my_py_pkg.hello_node:main",
            'hello_publisher = my_py_pkg.publisher:main',
            'hello_subscriber = my_py_pkg.subscriber:main',
            'add_server = my_py_pkg.add_server:main',
            'add_client = my_py_pkg.add_client:main',
            'parameter_python = my_py_pkg.parameter_node:main',
        ],
    },
)
