# packman
Pack up your command


## Build project

### With source code
```
$ python3 -m pip install -e path/to/packman
...
$ pkman <command>
...
```


## How to use
### Use case
Assume you're using following command often

```
$ kubectl get pods --sort-by=.metadata.name --field-selector=status.phase=Running
```
by changing value of `sort-by` and `field-selector`.

This commandline offers packaged command, which wrap-up existing command.

```
$ pkman put k8s-sort-field "kubectl get pods --sort-by={1} --field-selector=status.phase={2}"
...
$ pkman k8s-sort-field .metadata.name Running

```

### Commands
- `create`: Create command storage
- `put`: Put command set to storage
- `list`: Display list of key-value sets in storage
- `delete`: Delete key-value set from storage


