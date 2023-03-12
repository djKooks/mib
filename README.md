# laconic
Pack up your command


## Build project

### With source code
```
$ python3 -m pip install -e path/to/laconic
...
$ lcn <command>
...
```


## How to use
### Use case
Assume you're using following command frequently

```
$ kubectl get pods --sort-by=.metadata.name --field-selector=status.phase=Running
```
by changing value of `sort-by` and `field-selector`.

`laconic` offers packaged command, by wrapping up existing command.
```
$ lcn put k8s-sort-field "kubectl get pods --sort-by={1} --field-selector=status.phase={2}"
...
// this commands works same as 'kubectl get pods --sort-by=.metadata.name --field-selector=status.phase=Running'
$ lcn run k8s-sort-field .metadata.name Running
```

### Commands
- `create`: Create command storage
- `get`: Get value from storage with key
- `put`: Put command set to storage
- `run`: Trigger command in storage
- `list`: Display list of key-value sets in storage
- `delete`: Delete key-value set from storage
