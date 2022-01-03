# Traefik Template

[Traefik](https://github.com/traefik/traefik) setting template.

1. Serving traefik dashboard behind traefik itself
2. file based config provider hot reload example (file-based-app.yaml, conf/dynamic.toml)
3. label based config provider example (label-based-app.yaml)

The image nginxdemos/hello, used in file-based-app.yaml and label-based-app.yaml, is [nginx demo image](https://github.com/nginxinc/NGINX-Demos/tree/master/nginx-hello), which serves a simple page containing its hostname, IP address and port as wells as the request URI and the local time of the webserver.
