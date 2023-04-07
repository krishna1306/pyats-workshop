from genie.testbed import load
from pprint import pprint

# Step 0: load the testbed
testbed = load(f'./testbed.yaml')

# Step 1: testbed is a dictionary. Extract the device iol-test
pe2 = testbed.devices["PE2"]

# Step 2: Connect to the device
pe2.connect(log_stdout=False)

# Step 3: Get data and parse - in one step
show_interface = pe2.parse('show ip interface brief')

# Uncomment below lines to see CLI output also
show_interface_text = pe2.execute('show ip interface brief')
print(show_interface_text)

# Step 4: printing the `show ip interface brief` output
pprint(show_interface)

# Step 5: disconnect from the device
pe2.disconnect()