import unittest
import os
from test.aiml_tests.client import TestClient
from programy.config import ConfigurationFactory
from programy.config import ClientConfiguration

class NowAskMeTrainTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self, debug=True)

    def load_configuration(self, arguments):
        self.configuration = ClientConfiguration()
        ConfigurationFactory.load_configuration_from_file(self.configuration, os.path.dirname(__file__)+"/testconfig.yaml")

class TrainAIMLTests(unittest.TestCase):

    def setUp(cls):
        TrainAIMLTests.test_client = NowAskMeTrainTestClient()

    def test_now_ask_me(self):
        TrainAIMLTests.test_client.bot.brain.dump_tree()
        response = TrainAIMLTests.test_client.bot.ask_question("test", "daddy is great")
        self.assertIsNotNone(response)
        #TODO Sort out space in questions
        self.assertEqual("Now you can ask me: \" Who IS GREAT \"? and \" What does my DADDY BE \"?", response)
