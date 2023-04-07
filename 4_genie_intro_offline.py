from genie.testbed import load
from pprint import pprint

output = """
Fri Apr  7 11:13:25.051 UTC

Interface                      IP-Address      Status          Protocol Vrf-Name
MgmtEth0/RP0/CPU0/0            192.168.122.14  Up              Up       oam
GigabitEthernet0/0/0/0         unassigned      Shutdown        Down     default
GigabitEthernet0/0/0/1         unassigned      Shutdown        Down     default
GigabitEthernet0/0/0/2         unassigned      Shutdown        Down     default
GigabitEthernet0/0/0/3         unassigned      Shutdown        Down     default
"""

# Step 0: load the testbed
testbed = load(f'./testbed.yaml')

# Step 1: testbed is a dictionary. Extract the device iol-test
pe3 = testbed.devices["PE3"]

# Step 2: Get data and parse - in one step
show_interface = pe3.parse('show ip interface brief', output=output)

# Step 3: printing the `show ip interface brief` output
pprint(show_interface)