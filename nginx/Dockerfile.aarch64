FROM arm64v8/nginx:latest

# Remove default sites
RUN rm -rf /usr/share/nginx/html/*

# Add configuration file
COPY nginx.conf /etc/nginx/nginx.conf
COPY http.conf /etc/nginx/conf.d/default.conf

# Start the container
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
