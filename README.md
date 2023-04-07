## PyATS Parse Examples

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
