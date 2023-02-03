#!/usr/bin/env python
from cdktf import App, CloudBackend, NamedCloudWorkspace
from VpcStack import VpcStack
from StackProperties import StackBackendProperties, StackVpcProperties

backend = StackBackendProperties()
vpc_properties = StackVpcProperties()

app = App()
vpc = VpcStack(app, backend.organization, vpc_properties)

CloudBackend(vpc,
             hostname=backend.hostname,
             organization=backend.organization,
             workspaces=NamedCloudWorkspace(backend.workspace)
             )

app.synth()
