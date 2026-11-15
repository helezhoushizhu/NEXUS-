import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddServer(Node):

    def __init__(self):
        super().__init__('add_server')

        self.service = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_callback
        )

        self.get_logger().info('加法服务已启动')

    def add_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f'收到：{request.a} + {request.b} = {response.sum}'
        )

        return response


def main():
    rclpy.init()

    node = AddServer()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()