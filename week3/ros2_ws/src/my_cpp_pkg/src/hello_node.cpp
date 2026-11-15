
#include <memory>
#include <chrono>
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class HelloNode : public rclcpp::Node
{
public:
    HelloNode() : Node("hello_cpp_node")
    {
        timer_ = this->create_wall_timer(
            1s,
            [this]() {
                RCLCPP_INFO(this->get_logger(), "HelloWorld");
            }
        );
    }

private:
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<HelloNode>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}
