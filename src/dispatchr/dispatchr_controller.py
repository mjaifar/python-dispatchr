from core.algorithms import RoundRobinAlgorithm
from data.models import ServerService
from data.models import Tenant


class DispatchrController:
    def __init__(self):
        t1_server_1 = ServerService('http', '127.0.0.1', '8081')
        t1_server_2 = ServerService('http', '127.0.0.1', '8082')
        t1_servers = [t1_server_1, t1_server_2]
        t1_algorithm = RoundRobinAlgorithm(t1_servers)
        tenant_1 = Tenant('1', t1_servers, t1_algorithm)
        self.tenants_dict = {tenant_1.identifier: tenant_1}

    def dispatch(self, tenant_id):
        tenant = self.tenants_dict.get(tenant_id)
        server = tenant.algorithm.apply()
        return server
