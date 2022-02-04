FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/* /usr/nginx/
RUN ls /etc/nginx
RUN tail -n 50 /etc/nginx/nginx.conf
EXPOSE 80:443
CMD ["nginx", "-g", "daemon off;"]
