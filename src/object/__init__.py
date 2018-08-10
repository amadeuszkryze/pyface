import random
import math

class object:
    data = {
        'id':None,
        'x':None,
        'y':None,
        'speed':None,
        'angle':None,
        'aliveTime':None,
        'color': None
    }

    def __init__(self,
            id,
            x=0,
            y=0,
            size=None,
            speed=None,
            angle=None,
            aliveTime=None,
            color=None):
        self.data = {
            'id': id,
            'x': x,
            'y': y,
            'size': size if size is not None else 1,
            'speed': speed if speed is not None else random.uniform(1, 2),
            'angle': angle if angle is not None else random.uniform(0, 359),
            'aliveTime': aliveTime if aliveTime is not None else random.uniform(100, 800),
            'color': color if color is not None else random.uniform(128, 254)}

    def calculateNewPos(self) -> 'object':
        # Gatger old data
        old_x, old_y = self.data['x'], self.data['y']
        angle = float(self.data['angle'])
        # Compute the change in position
        delta_y = self.data['speed'] * math.cos(math.radians(angle))
        delta_x = self.data['speed'] * math.sin(math.radians(angle))
        # Add that to the existing position
        self.data['x'] = round(old_x + delta_x)
        self.data['y'] = round(old_y + delta_y)

        return self
