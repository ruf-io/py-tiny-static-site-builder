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
   git clone
   ```
4. Edit the nginx config to reflect your domain and the correct path to local directory
   ```
   nano nginx.config
   ```
   Edit: `server_name yourdomain.com;`
   Edit: `root /path/to/tinysite/static;`

5. Place link to nginx config in required directory
   ```
   sudo ln -s /path/to/tinysite/nginx.conf /etc/nginx/sites-enabled/tinysite.conf
   ```
6. (optionally) Add an incrontab task to trigger a rebuild every time you change a file
   ```
   incrontab -e
   ```
   _...then in the editor add..._
   ```
   /path/to/tinysite/posts IN_MODIFY cd /path/to/tinysite && python build.py
   ```
