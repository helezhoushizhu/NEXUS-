#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class HelloPublisher : public rclcpp::Node
{
public:
    HelloPublisher() : Node("cpp_hello_publisher")
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>(
            "cpp_hello_topic", 10);

        timer_ = this->create_wall_timer(
            100ms, [this]() {
                auto message = std_msgs::msg::String();
                message.data = "HelloWorld";

                publisher_->publish(message);
                RCLCPP_INFO(this->get_logger(), "发布：%s", message.data.c_str());
            });
    }

private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<HelloPublisher>();
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}