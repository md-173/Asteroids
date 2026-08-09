import unittest

import pygame  # pyright: ignore[reportMissingImports]

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_countdown = 0
        self.lives = 3

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation = self.rotation % 360
        print(self.rotation)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.shoot_countdown -= dt

        if keys[pygame.K_a]:
            self.move_right(-dt)
            if keys[pygame.K_s]:
                self.rotation = 45
            if keys[pygame.K_w]:
                self.rotation = 135
            if self.rotation < 95 and self.rotation > 85:
                self.rotation = 90
            elif self.rotation >= 90 and self.rotation <= 270:
                self.rotate(-dt)
            elif self.rotation >= 270 or self.rotation <= 90:
                self.rotate(dt)
        if keys[pygame.K_d]:
            self.move_right(dt)
            if keys[pygame.K_s]:
                self.rotation = 315
            if keys[pygame.K_w]:
                self.rotation = 225
            if self.rotation < 275 and self.rotation > 265:
                self.rotation = 270
            elif self.rotation < 90 or self.rotation >= 270:
                self.rotate(-dt)
            else:
                self.rotate(dt)
        if keys[pygame.K_w]:
            self.move_up(dt)
            if keys[pygame.K_a]:
                self.rotation = 135
            if keys[pygame.K_d]:
                self.rotation = 225
            if self.rotation < 185 and self.rotation > 175:
                self.rotation = 180
            elif self.rotation >= 0 and self.rotation <= 180:
                self.rotate(dt)
            elif self.rotation > 180 and self.rotation <= 360:
                self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move_up(-dt)
            if keys[pygame.K_a]:
                self.rotation = 45
            if keys[pygame.K_d]:
                self.rotation = 315
            if self.rotation < 5 or self.rotation > 355:
                self.rotation = 0
            elif self.rotation >= 0 and self.rotation <= 180:
                self.rotate(-dt)
            elif self.rotation > 180 and self.rotation <= 360:
                self.rotate(dt)

        if keys[pygame.K_UP]:
            if keys[pygame.K_LEFT]:
                self.shoot(135)
            elif keys[pygame.K_RIGHT]:
                self.shoot(225)
            else:
                self.shoot(180)
        if keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                self.shoot(45)
            elif keys[pygame.K_RIGHT]:
                self.shoot(315)
            else:
                self.shoot(0)
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                self.shoot(135)
            elif keys[pygame.K_DOWN]:
                self.shoot(45)
            else:
                self.shoot(90)
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                self.shoot(225)
            elif keys[pygame.K_DOWN]:
                self.shoot(315)
            else:
                self.shoot(270)


    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation).normalize()
        rotate_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotate_with_speed_vector

    def move_up(self, dt):
        up_vector = pygame.Vector2(0,-1)
        self.position += up_vector * PLAYER_SPEED * dt

    def move_right(self, dt):
        right_vector = pygame.Vector2(1,0)
        self.position += right_vector * PLAYER_SPEED * dt

    def shoot(self, angle):
        if self.shoot_countdown > 0:
            return
        self.shoot_countdown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(angle).normalize()
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOT_SPEED
        shot.velocity = rotated_with_speed_vector
