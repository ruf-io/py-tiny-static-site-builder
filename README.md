# Installation

On Ubuntu systems...

1. Install nginx, python, pip, git and incron

   ```
   sudo apt-get update
   sudo apt-get install nginx python python-pip git incron
   ```

2. Install necessary python modules

   ```
   sudo pip install pyyaml pystache jsonschema markdown
   ```

3. Clone this repo to the desired location

   ```
   git clone https://github.com/ruf-io/py-tiny-static-site-builder.git
   ```

4. Copy and edit the  example nginx config to reflect your domain and the correct path to webroot

   ```
   cp nginx.conf.example nginx.conf
   nano nginx.conf
   ```

   Edit: `server_name yourdomain.com;` to reflect your domain.

   Edit: `root /path/to/tinysite/static;` to reflect the absolute path to the webroot.

   Save and close the nginx config file

5. Place link to nginx config in required directory and restart nginx

   ```
   sudo ln -s /path/to/tinysite/nginx.conf /etc/nginx/sites-enabled/tinysite.conf
   sudo service nginx reload
   ```

6. (optionally) Add an incrontab task to trigger a rebuild every time you change a file

   ```
   incrontab -e
   ```

   _...then in the editor add..._

   ```
   /path/to/tinysite/posts IN_MODIFY cd /path/to/tinysite && python build.py
   ```
