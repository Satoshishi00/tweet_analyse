#!/usr/bin/python
import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/tweet_analyse/')

from tweet_analyse import app as application

application.secret_key = 'kdjkjlejkqleqlkslekldskkdh'
