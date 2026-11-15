import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPublisher(Node):

    def __init__(self):
        super().__init__('hello_publisher')

        self.publisher = self.create_publisher(
            String,
            'hello_topic',
            10
        )

        self.timer = self.create_timer(0.1, self.publish_message)

    def publish_message(self):
        message = String()
        message.data = 'HelloWorld'

        self.publisher.publish(message)
        self.get_logger().info('发布：' + message.data)


def main():
    rclpy.init()

    node = HelloPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()