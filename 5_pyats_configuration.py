from pyats.topology import  loader
from pprint import pprint

testbed = loader.load(f'./testbed.yaml')

pe1 = testbed.devices["PE1"]

pe1.connect(log_stdout=False)

pe1.configure("""
    interface GigabitEthernet2
        ip address 10.1.10.1 255.255.255.0
        no shut
""")

pe1.disconnect()