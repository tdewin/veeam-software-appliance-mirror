build
```
podman build -t web .
```


make cert (or inject propper ones)
```
mkdir certs
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -sha256 -days 3650 -nodes -subj "/C=eu/ST=state/L=city/O=mirror/OU=mirror/CN=mirror"
```


run
```
podman run -it --rm -v ./certs:/certs:z -v ../capture/mirror:/mirror:z -p 9999:80 -p 9943:443 web 
```
