class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # directions = ['N', 'E', 'S', 'W']
        # 0 - N, 1 - E, 2 - S, 3 - W
        position_offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                x_offset, y_offset = position_offset[direction]
                while command:
                    if (x + x_offset, y + y_offset) not in obstacles:
                        x += x_offset
                        y += y_offset
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        return max_distance