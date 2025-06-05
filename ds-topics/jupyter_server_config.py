# jupyter_server_config.py

# Configuration file for Jupyter Server.

# Set the message rate limit (messages/sec)
# Increase this value if you encounter "IOPub message rate exceeded" errors.
c.ServerApp.iopub_msg_rate_limit = 10000000000 # A very large number

# You can also set the rate limit window (in seconds)
# c.ServerApp.rate_limit_window = 3.0 # Default is 3 seconds

# Other common configurations you might add:
# Set the default directory where Jupyter will open
# c.ServerApp.root_dir = '/Users/yourusername/MyJupyterProjects'

# Disable opening the browser automatically
# c.ServerApp.open_browser = False

# Set a specific port (default is 8888, will try next available if busy)
# c.ServerApp.port = 9999