build

```
podman build -t capture .
```

run on fedora
```
mkdir mirror
podman run -it --rm -v $(pwd)/mirror:/mirror:z  capture
```

or multiruns
```
podman run -it --name capture -v $(pwd)/mirror:/mirror:z capture
podman start -i -a capture
```



run on windows (untested)
```
mkdir mirror
podman run -it --rm -v ./mirror:/mirror  capture
```


