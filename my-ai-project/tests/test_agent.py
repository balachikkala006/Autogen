
import unittest
from src.agents.agent import create_openai_agent

class TestAgent(unittest.TestCase):
    def test_agent_response(self):
        agent = create_openai_agent()
        response = agent("Test message")
        self.assertTrue(response is not None)

if __name__ == "__main__":
    unittest.main()
