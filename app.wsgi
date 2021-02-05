import sys
sys.path.insert(0,'/var/www/clashGenN')

# fuck wsgi
import os
os.chdir('/var/www/clashGenN')

from app import app as application
