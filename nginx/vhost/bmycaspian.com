location /static/ {
    alias /construction/static/;
}
location /media/ {
    alias /construction/media/;
}