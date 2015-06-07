#!/usr/bin/env python
# exec commands within the flask environment

import os
import readline
from pprint import pprint

from flask import *
from app import *

# interactive mode
os.environ['PYTHONINSPECT'] = 'True'
