server {
    listen                     ${LISTEN_PORT};
    server_name                134.122.10.67; 
    
    location /static {
        alias /vol/static;
        client_max_body_size    1000M;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    1000M;
    }    
}



