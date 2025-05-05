import rclpy
from rclpy.node import Node
from custom_interfaces.msg import FieldData

# Any additional imports here

# Decide your node class name
class GoalPub(Node):
    def __init__(self):

        # Change to have your node name
        super().__init__('goal_pub')

        self.map_subscriber = self.create_subscription(OccupancyGrid, '/robot2/map', self.callback_map, 10)
        self.maze_pub = self.create_publisher(FieldData, 'maze_data', 10)


    
    def callback_map(self,msg):
        data = FieldData()
        data.goal_x = 1, data.goal_y = 1
        data.field_data = msg
        self.maze_pub.publish(field_data)

        self.resolution = round(msg.info.resolution,3)
        self.origin_x = msg.info.origin.position.x
        self.origin_y = msg.info.origin.position.y
        self.origin_ang = msg.info.origin.orientation.z
        
        self.width = msg.info.width
        self.height = msg.info.height

        robot_x = round((self.x-self.origin_x)/self.resolution)
        robot_y = round((self.y-self.origin_y)/self.resolution)
        
        occupancy_grid = msg.data

        row = 0
        while row < self.height:
            col = 0
            while col < self.width:
                real_x,real_y = self.index_to_real(col,row)
                point = occupancy_grid[col + (row*self.width)]

                if point > 25:
                    self.obstacle_space.append([real_x, real_y])

                col += 1
            row += 1

def main(args=None):
    rclpy.init(args=args)

    # Change to be your node class name
    node = GoalPub()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()