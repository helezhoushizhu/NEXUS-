#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class ParameterNode : public rclcpp::Node
{
public:
    ParameterNode() : Node("parameter_cpp")
    {
        this->declare_parameter<std::string>("frames/odom", "default_odom");
        this->declare_parameter<std::string>("frames/baselink", "default_base");
        this->declare_parameter<std::string>("frames/lidar", "default_lidar");
        this->declare_parameter<std::string>("frames/imu", "default_imu");

        timer_ = this->create_wall_timer(
            2s, [this]() { print_parameters(); });
    }

private:
    void print_parameters()
    {
        auto odom = this->get_parameter("frames/odom").as_string();
        auto base = this->get_parameter("frames/baselink").as_string();
        auto lidar = this->get_parameter("frames/lidar").as_string();
        auto imu = this->get_parameter("frames/imu").as_string();

        RCLCPP_INFO(
            this->get_logger(),
            "odom=%s, base=%s, lidar=%s, imu=%s",
            odom.c_str(), base.c_str(), lidar.c_str(), imu.c_str()
        );
    }

    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<ParameterNode>();
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}