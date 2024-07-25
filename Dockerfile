FROM php:8.0-apache

# Install necessary extensions
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli

# Copy application files
COPY . /var/www/html/

# Set the working directory
WORKDIR /var/www/html

# Set the default index file
RUN echo "DirectoryIndex router.php" > /etc/apache2/conf-available/router.conf && a2enconf router

# Expose the port Apache is listening on
EXPOSE 80
