#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class HelloSubscriber : public rclcpp::Node
{
public:
    HelloSubscriber() : Node("cpp_hello_subscriber")
    {
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "cpp_hello_topic",
            10,
            [this](std_msgs::msg::String::SharedPtr message) {
                RCLCPP_INFO(
                    this->get_logger(),
                    "收到：%s",
                    message->data.c_str()
                );
            }
        );
    }

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<HelloSubscriber>();
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}