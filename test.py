import unittest
from unittest.mock import Mock
import pygame

from cargame import mixer

class TestCarGame(unittest.TestCase):

    def setUp(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Sonamcargame")

        # Load the car images
        self.car = pygame.image.load("photo.jpg")
        self.car2 = pygame.image.load("photo.jpg")

    def test_car_movement(self):
        # Initialize car positions
        car_loc = self.car.get_rect()
        car_loc.center = 400, 600
        car2_loc = self.car2.get_rect()
        car2_loc.center = 200, 200

        # Simulate keyboard presses for left and right movement
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_a}))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_d}))

        # Update car positions
        car_loc = car_loc.move([-int(road_w/2), 0])
        car2_loc = car2_loc.move([int(road_w/2), 0])

        # Assert that car positions have changed
        self.assertEqual(car_loc.center, (200, 600))
        self.assertEqual(car2_loc.center, (600, 200))

    def test_car_collision(self):
        # Initialize car positions and adjust car2_loc to simulate collision
        car_loc = self.car.get_rect()
        car_loc.center = 400, 600
        car2_loc = self.car2.get_rect()
        car2_loc.center = 400, 350

        # Simulate car movement
        car2_loc[1] += speed

        # Check for collision
        if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
            # Assert that game over message is printed
            print("Game Over! You Lost!")
            self.assertEqual(True, True)
        else:
            # Assert that no game over message is printed
            self.assertEqual(True, False)

if _name_ == '_main_':
    unittest.main()




