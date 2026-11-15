import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloSubscriber(Node):

    def __init__(self):
        super().__init__('hello_subscriber')

        self.subscription = self.create_subscription(
            String,
            'hello_topic',
            self.receive_message,
            10
        )

    def receive_message(self, message):
        self.get_logger().info('收到：' + message.data)


def main():
    rclpy.init()

    node = HelloSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()