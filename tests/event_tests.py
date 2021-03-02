import json
from levelupapi.models.events import Event
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Game, Gamer


class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()

        # Events also need a game created in the DB
        game = Game()
        game.gametype_id = 1
        game.skill_level = 5
        game.title = "Sorry"
        game.maker = "Milton Bradley"
        game.number_of_players = 4
        game.gamer_id = 1
        game.save()

        # gamer = Gamer()
        # gamer.user_id = 1
        # gamer.bio = "test bio"
        # gamer.save()


    def test_create_event(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/events"
        data = {
            "gameId": 1,
            "time": "12:00:00",
            "date": "2021-10-04",
            "description": "Super fune event",
            "gamer": 1,
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["time"], "12:00:00")
        self.assertEqual(json_response["description"], "Super fune event")
        self.assertEqual(json_response["date"], "2021-10-04")

    def test_change_event(self):
        """
        Ensure we can change an existing game.
        """
        event = Event()
        event.game_id = 1
        event.time = "12:00:02"
        event.description = "Description"
        event.date = "2021-10-05"
        event.organizer_id = 1
        event.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "description": "NEW DESCRIPTION",
            "date": "2021-10-06",
            "time": "12:00:03",
            "gameId": 1,
        }

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/events/{event.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY CHANGES
        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the properties are correct
        self.assertEqual(json_response["description"], "NEW DESCRIPTION")
        self.assertEqual(json_response["date"], "2021-10-06")
        self.assertEqual(json_response["time"], "12:00:03")

    def test_delete_game(self):
        """
        Ensure we can delete an existing game.
        """
        event = Event()
        event.game_id = 1
        event.time = "12:00:02"
        event.description = "Description"
        event.date = "2021-10-05"
        event.organizer_id = 1
        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY 404 response
        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
