## Check PyATS Version

```
pyats version check
```

In this tutorial, we are using `23.3`.

Make sure you refer to the documentation for this version
AEtest documentation is also present in the same link
https://pubhub.devnetcloud.com/media/pyats/docs/overview/index.html

A more beginner-friendly documentation is here
https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/index.html

## PyATS Parse Examples

`parse` uses Genie. Parsers are typically written using `genie.metaparser` module

https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/parseoutput.html

```
pyats parse "show version" --testbed-file testbed.yaml --device PE1 --output initial_output

pyats parse "show version" --testbed-file testbed.yaml --device PE2 --output initial_output
```

> Omit the `--device PE1` to run the `parse` command for all testbed devices

## PyATS Learn Example

```
pyats learn interface --testbed-file testbed.yaml --devices PE1 --output interfaces
```

Learn all

```
pyats learn all --testbed-file testbed.yaml --devices PE1 --output output_folder
```

## aeTest

### Running Standalone

Inside `6_aetest_standalone.py` we are using `argparse` to parse `--testbed` argument and pass testbed to the testing classes.

```
python3 6_aetest_standalone.py --testbed=testbed.yaml
```

### Running as a job

```
pyats run job 7_aetest_easypy.py --testbed-file testbed.yaml
```