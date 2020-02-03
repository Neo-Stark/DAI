import os.path, time
from datetime import datetime
file = "app.py"
print("created: %d" % os.path.getctime(file) + "actual time: %d" % datetime.now())