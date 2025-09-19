build

```
podman build -t capture .
```

run on fedora
```
mkdir mirror
podman run -it --rm -v $(pwd)/mirror:/mirror:z  capture
```

run on windows (untested)
```
mkdir mirror
podman run -it --rm -v ./mirror:/mirror  capture
```


