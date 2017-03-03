import unittest
from unittest import TestCase

from data.models import ServerService

from core.algorithms import RoundRobinAlgorithm


class TestRoundRobinAlgorithm(TestCase):
    server1 = ServerService('http', '127.0.0.1', '9901')
    server2 = ServerService('http', '127.0.0.1', '9902')
    server3 = ServerService('http', '127.0.0.1', '9903')
    servers = [server1, server2, server3]

    def test_apply(self):
        algorithm = RoundRobinAlgorithm(TestRoundRobinAlgorithm.servers)
        selectedServer = algorithm.apply()
        assert selectedServer.port == '9903'

    def test_rotate(self):
        algorithm = RoundRobinAlgorithm(TestRoundRobinAlgorithm.servers)
        lastElemBefore = TestRoundRobinAlgorithm.servers[2]
        rotatedList = algorithm.rotate()
        firstElemAfter = rotatedList[0]
        assert lastElemBefore.port == firstElemAfter.port


if __name__ == '__main__':
    unittest.main()
