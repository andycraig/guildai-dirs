## With Guild AI

```
$ guild run train
You are about to run dir-check:train
  x: 0
Continue? (Y/n) y
Resolving file:data/file.txt dependency
Traceback (most recent call last):
  File "[PATH]/src/train.py", line 5, in <module>
    with open("data/file.txt", 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/file.txt'
```

## Without Guild AI

```
$ python src/train.py 
loss: 1
```
