#!/usr/bin/python

from app import app
import os

port = int(os.environ.get("PORT", 6969))
app.run(host="0.0.0.0", port=port)