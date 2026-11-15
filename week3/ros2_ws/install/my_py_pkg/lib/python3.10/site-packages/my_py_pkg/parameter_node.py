import rclpy
from rclpy.clock import Clock, ClockType
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_python')

        self.declare_parameter('frames/odom', 'default_odom')
        self.declare_parameter('frames/baselink', 'default_base')
        self.declare_parameter('frames/lidar', 'default_lidar')
        self.declare_parameter('frames/imu', 'default_imu')

        # 使用系统时钟定时，方便观察参数变化
        self.system_clock = Clock(clock_type=ClockType.SYSTEM_TIME)
        self.timer = self.create_timer(
            2.0, self.print_parameters, clock=self.system_clock
        )

    def print_parameters(self):
        odom = self.get_parameter('frames/odom').value
        base = self.get_parameter('frames/baselink').value
        lidar = self.get_parameter('frames/lidar').value
        imu = self.get_parameter('frames/imu').value

        self.get_logger().info(
            f'odom={odom}, base={base}, lidar={lidar}, imu={imu}'
        )


def main():
    rclpy.init()

    node = ParameterNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()