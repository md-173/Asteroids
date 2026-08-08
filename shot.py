from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init(x, y, SHOT_RADIUS)
