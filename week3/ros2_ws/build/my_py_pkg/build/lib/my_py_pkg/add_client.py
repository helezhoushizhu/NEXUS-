import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main():
    rclpy.init()

    node = Node('add_client')
    client = node.create_client(AddTwoInts, 'add_two_ints')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('等待加法服务启动……')

    request = AddTwoInts.Request()

    request.a = int(input('请输入第一个整数：'))
    request.b = int(input('请输入第二个整数：'))

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        print('计算结果：', future.result().sum)
    else:
        print('服务调用失败：', future.exception())

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()