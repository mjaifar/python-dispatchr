import collections


class Algorithm:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name

    def apply(self, servers):
        pass


class RoundRobinAlgorithm(Algorithm):
    def __init__(self, servers):
        self.identifier = 1;
        self.name = "round_robin"
        self.servers = servers

    def apply(self):
        self.rotate()
        return self.servers[0]

    def rotate(self):
        self.servers = self.servers[-1:] + self.servers[:-1]
        return self.servers
