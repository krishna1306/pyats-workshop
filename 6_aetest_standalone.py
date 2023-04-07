from pyats import aetest

# Read inventory and do pre-checks
class CommonSetup(aetest.CommonSetup):
    
    @aetest.subsection
    def establish_connections(self, testbed):
        for device in testbed:
            device.connect(log_stdout=False)

class SimpleTestcase(aetest.Testcase):

    @aetest.test
    def simple_test(self, testbed):
        for device in testbed:
            interfaces = device.parse("show ip interface brief")
            interfaces_count = len(interfaces["interface"].keys())
            # Uncomment for debugging
            # print(interfaces["interface"].keys())
            # print(interfaces_count)
            if device == "PE1":
                assert interfaces_count == 4
            elif device == "PE2":
                assert interfaces_count == 5

class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        for device in testbed:
            device.disconnect()

if __name__ == "__main__":
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
