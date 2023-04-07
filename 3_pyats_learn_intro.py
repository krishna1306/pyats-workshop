from pyats.topology import  loader
from pprint import pprint

testbed = loader.load(f'./testbed.yaml')

learnt = {}

for name, dev in testbed.devices.items():
    dev.connect(log_stdout=False)
    learnt[name] = {}
    learnt[name]['interface'] = dev.learn('interface')

for name, interface in learnt.items():
    interfaces = interface["interface"].info
    print(name + " : ")
    # Uncomment below line to see the 'info' object structure
    # pprint(interface["interface"].info)
    for interface in interfaces:
        print(interface + " " + interfaces[interface]["oper_status"])
    print("\n")