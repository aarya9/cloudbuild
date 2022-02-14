COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
import random

def GenerateConfig(context):
    resources = [{
        'name': context.env['name'],
        'type': 'compute.v1.instance',
        'properties': {
            'zone': context.properties['zone'],
            'machineType': ''.join([COMPUTE_URL_BASE, 'projects/', context.env["project"],
                                    '/zones/',context.properties['zone'],'/',
                                    'machineTypes/',context.properties["machineType"]]) ,
            'disks': [{
                'type': 'PERSISTENT',
                'boot': True,
		        'diskSizeGb': 10.0,
                'diskName':context.env['name']+str(random.randint(100,999)),
                'autoDelete': True,
                'diskType': ''.join([COMPUTE_URL_BASE,'projects/',context.env["project"],
                                 '/zones/',context.properties['zone'],'/',
                                 'diskTypes/',context.properties["diskTypes"]]),
                'initializeParams': {
                        'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                            'debian-cloud/global',
                                            '/images/family/debian-9']),
                        }
                    }],
			
            'tags': context.properties['tags'],
			
            'metadata': {
            "items": [
                {
                    "key": "startup-script",
                    "value": context.properties['startup-script']
                }
                ]
            },
            
            'networkInterfaces': [{
                'network': 'https://www.googleapis.com/compute/v1/projects/gcp-dc-sandbox-01/global/networks/gcp-vpc-sndbx-dmz-01',
                'subnetwork': 'https://www.googleapis.com/compute/v1/projects/gcp-dc-sandbox-01/regions/us-east4/subnetworks/ge4-snet-sndbx-dmz-pub-01',
                'accessConfigs': [{
                    #   'name': 'External NAT',	
                    #   'type': 'ONE_TO_ONE_NAT'
                }]
            }],
            'serviceAccounts': [{
                "email": "gcp-svc-sandbox-defaultce-01@gcp-dc-sandbox-01.iam.gserviceaccount.com",
                "scopes": [
                    ]
                }],
			
            'labels': {
                "name": context.properties['servername'],
                "environment": context.properties['environment']
            }
            }

    }]
    return {'resources': resources}
