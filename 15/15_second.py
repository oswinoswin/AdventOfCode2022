import math
import re
import numpy as np

SEARCH_SIZE = 4000000


class Sensor:
    def __init__(self, nums):
        self.position = Point(int(nums[0]), int(nums[1]))
        self.beacon = Point(int(nums[2]), int(nums[3]))
        self.distance = self.position.manhattan_dist(self.beacon)

    def is_detected(self, point):
        return point.manhattan_dist(self.position) <= self.distance

    def corners(self):
        R = self.distance + 1
        top_x, top_y = self.position.x, self.position.y - R
        right_x, right_y = self.position.x + R, self.position.y
        down_x, down_y = self.position.x, self.position.y + R
        left_x, left_y = self.position.x - R, self.position.y
        return [(left_x, left_y), (down_x, down_y), (right_x, right_y), (top_x, top_y)]

    def point_border(self):
        # this could be iterator, but whatever now
        R = self.distance + 1
        top_x, top_y = self.position.x, self.position.y - R
        right_x, right_y = self.position.x + R, self.position.y
        down_x, down_y = self.position.x, self.position.y + R
        left_x, left_y = self.position.x - R, self.position.y
        border_points = []
        for i in range(R):
            border_points.append(Point(top_x + i, top_y + i))
            border_points.append(Point(right_x - i, right_y + i))
            border_points.append(Point(down_x - i, down_y - i))
            border_points.append(Point(left_x + i, left_y - i))
        return border_points

    def __str__(self):
        return f"Sensor: 'position': {self.position}, 'beacon': {self.beacon}, 'distance': {self.distance}"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        return f"{self.__dict__}"

    def get_hash(self):
        return SEARCH_SIZE * self.x + self.y

    def __hash__(self):
        return self.get_hash()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def is_in_area(self, area_size):
        if self.x < 0 or self.y < 0:
            return False
        if self.x > area_size or self.y > area_size:
            return False
        return True


def second(filename, search_size):
    beacons = set()
    sensors = []

    with open(filename, "r") as f:
        for line in f:
            nums = re.findall(r'-?[0-9]+', line)
            sensor = Sensor(nums)
            sensors.append(sensor)
            beacon = Point(int(nums[2]), int(nums[3]))
            beacons.add(beacon)
            print(sensor)

        counter = 1
        for sensor in sensors:

            points = sensor.point_border()
            print(f"{counter} | {sensor} boarder_points: {len(points)}")

            for point in points:
                point_is_detected = False
                # check if point is inside search area
                if point.x < 0 or point.y < 0 or point.x > search_size or point.y > search_size:
                    continue

                for drugi_sensor in sensors:
                    if drugi_sensor.is_detected(point):
                        point_is_detected = True
                        break

                if not point_is_detected:
                    print(point)
                    return point.get_hash()
            counter += 1


# 4692643 is too low
# negative nums in input XD -? solved this
if __name__ == "__main__":
    # top = Point(8, -2)
    # right = Point(17, 7)

    print(second("example.txt", 20))
    print(second("input.txt", 4000000))
