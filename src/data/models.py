import json


class ServerService(object):
    def __init__(self, protocol, ip, port):
        self.protocol = protocol
        self.ip = ip
        self.port = port

    def show(self):
        print(self.protocol + "://" + self.ip + ":" + self.port)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Tenant(object):
    def __init__(self, identifier, servers):
        self.identifier = identifier
        self.servers = servers
