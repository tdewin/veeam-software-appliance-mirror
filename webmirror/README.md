build
```
podman build -t web .
```

run
```
podman run -it --rm -v ../capture/mirror:/mirror:z -p 9999:80 web
```
