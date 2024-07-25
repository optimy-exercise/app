FROM php:7.4-cli

# Copy the PHP script into the container
COPY router.php /var/www/html/

# Set working directory
WORKDIR /var/www/html

# Start PHP built-in server
CMD ["php", "-S", "0.0.0.0:80", "-t", "/var/www/html"]
