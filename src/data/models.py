import json


class ServerService(object):
    def __init__(self, protocol, ip, port):
        self.protocol = protocol
        self.ip = ip
        self.port = port

    def to_string(self):
        to_str = self.protocol + "://" + self.ip + ":" + self.port
        print(to_str)
        return to_str

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Tenant(object):
    def __init__(self, identifier, servers, algorithm):
        self.identifier = identifier
        self.servers = servers
        self.algorithm = algorithm
