from constructs import Construct
from cdktf import TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
from imports.vpc import Vpc
from StackProperties import StackVpcProperties


class VpcStack(TerraformStack):
    properties: StackVpcProperties

    def __init__(self, scope: Construct, stack_id: str, stack_properties: StackVpcProperties, environment: str = 'dev'):
        super().__init__(scope, stack_id)

        self.properties = stack_properties

        AwsProvider(self, 'Aws', region=self.properties.region)

        stack = Vpc(self, stack_id,
                    name=stack_id + '-' + environment,
                    cidr=self.properties.cidr,
                    azs=[self.properties.region + suffix for suffix in self.properties.az_suffix],
                    private_subnets=self.properties.private_subnets,
                    public_subnets=self.properties.public_subnets,
                    enable_nat_gateway=False,
                    enable_dns_hostnames=False
                    )

        TerraformOutput(self, 'vpc', value={
            "arn": stack.vpc_arn_output,
            "private_subnets": stack.private_subnets_output,
            "private_subnets_cidr_blocks": stack.private_subnets_cidr_blocks_output,
            "public_subnets": stack.public_subnets_output,
            "public_subnets_cidr_blocks": stack.public_subnets_cidr_blocks_output,
        })
