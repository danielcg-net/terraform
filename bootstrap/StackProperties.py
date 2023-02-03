from dataclasses import dataclass


@dataclass
class StackBackendProperties:
    hostname: str
    organization: str
    workspace: str

    def __init__(self, hostname: str = 'app.terraform.io',
                 organization: str = 'danielcg',
                 workspace: str = 'bootstrap'):
        self.hostname = hostname
        self.organization = organization
        self.workspace = workspace


@dataclass
class StackVpcProperties:
    region: str
    cidr: str
    private_subnets: list
    public_subnets: list
    az_suffix: list

    def __defaults(self, az_suffix, private_subnets, public_subnets):
        if az_suffix is None:
            self.az_suffix = ['a', 'b', 'c']

        if private_subnets is None:
            self.private_subnets = ['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']

    def __init__(self, region: str = 'us-east-2', az_suffix=None, cidr: str = '10.0.0.0/16', private_subnets=None,
                 public_subnets=None):
        self.__defaults(self, az_suffix, private_subnets)
        self.region = region
        self.cidr = cidr
