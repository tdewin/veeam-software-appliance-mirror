# build
```
podman build -t web .
```

# remote build
alternative exporting it after build
```
podman run -d --name web web
podman stop web
podman export -o web.tar web
```

```
podman import -m "import" web.tar
```


# make cert

make cert (or inject propper ones) CN=mirror -> mirror should be your hostname or the ip that you use as a link
```
mkdir certs
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -sha256 -days 3650 -nodes -subj "/C=eu/ST=state/L=city/O=mirror/OU=mirror/CN=mirror"
```

# run
run
```
podman run -it --rm -v ./certs:/certs:z -v ../capture/mirror:/mirror:z -p 9999:80 -p 9943:443 web
```

paste in the ```https://mirror:9943/rocky``` and upload ```certs/cert.pem``` as the public key / certificate
