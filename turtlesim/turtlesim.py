import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from turtlesim.msg import Pose
import math

positions = [
    [1,8],
    [1,1],
    [8,1],
    [8,8]
]


class GazeboRoda(Node):
    def __init__(self):
        super().__init__("node_gazebo")
        self.cmd_vel_publish = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.odom2 = self.create_subscription(Pose, "/turtle1/pose", self.odometria, 10)
        self.get_logger().info("rodano")

    def odometria(self, pose:Pose): 
        # acertando as posições e ângulos
        pos_atual = 0
        x = pose.x
        y = pose.y
        ang = pose.theta
        
        dif_ang_x = positions[pos_atual][0] - x
        dif_ang_y = positions[pos_atual][1] - y

        angulo = math.atan2(dif_ang_y, dif_ang_x)

        dif_ang_total = ang - angulo
        vel_msg = Twist()

        if abs(dif_ang_total) > 0.1:
            vel_msg.angular.z = 0.5
            vel_msg.linear.x = 0.0
        if (abs(positions[pos_atual][0] - x) > 0.25) and (abs(positions[pos_atual][1] - y) > 0.25):
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.0
        else:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0
            if abs(dif_ang_total) < 0.1:
                pos_atual += 1
                positions.pop(0)
                if pos_atual >= 3:
                    self.get_logger().info(f"pos_atual = {pos_atual}")
                    self.get_logger().info(positions)


        
        self.cmd_vel_publish.publish(vel_msg)
        self.get_logger().info(f"x={round(x, 2)},y={round(y, 2)}, dif_ang_total={abs(round(dif_ang_total, 2))}")

def main(args=None):
    rclpy.init(args=args)
    node = GazeboRoda()
    rclpy.spin(node)
    rclpy.shutdown