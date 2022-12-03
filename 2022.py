from dataclasses import dataclass
import math
import turtle

@dataclass
class Position:
    coord: tuple[int,int]
    angle: int
    movement_record: list[tuple[int,int]]

    def getX(self):
        return self.coord[0]

    def getY(self):
        return self.coord[1]

    def get_movement_record(self):
        return self.movement_record

    def walk(self, steps):
        before = self.coord
        self.coord = (self.getX() + horizontal_direction(self.angle) * steps, self.getY() + vertical_direction(self.angle) * steps)
        self.movement_record.append((before,self.coord))

    def jump(self, steps):
        self.coord = (self.getX() + horizontal_direction(self.angle) * steps, self.getY() + vertical_direction(self.angle) * steps)

    def turn(self, deg):
        self.angle = self.angle - deg

    def move(self, moves):
        for m in moves:
            action = m[0]
            attr = int(m[1])

            if action == "loop": self.walk(attr)
            elif action == "draai": self.turn(attr)
            elif action == "spring": self.jump(attr)

def horizontal_direction(angle):
    rad_angle = math.radians(angle)
    return round(math.cos(rad_angle))

def vertical_direction(angle):
    rad_angle = math.radians(angle)
    return round(math.sin(rad_angle))

def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [line.strip().split() for line in lines]

def manhattan(start, end):
    return abs(start.getX() - end.getX()) + abs(start.getY() - end.getY())

def draw_tracks(lines):
    s = turtle.getscreen()
    t = turtle.Turtle()
    for line in lines:
        t.penup()
        t.goto(line[0])
        t.pendown()
        t.goto(line[1])
    turtle.exitonclick()

def main():
    pos = Position((0,0), 90, [])
    moves = parse_input("input/2022_input_02")
    pos.move(moves)
    result = manhattan(Position((0,0), 90, []), pos)
    print(f"Manhattan distance: {result}")
    draw_tracks(pos.get_movement_record())

if __name__ == "__main__":
    main()