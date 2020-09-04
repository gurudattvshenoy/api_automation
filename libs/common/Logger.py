import os
import logging
import pathlib

# The same can be done using environment variable having project absolute path
# Create a enviroment variable like export API_HOME=<abs path to project> and add it in .bashrc in linux
# import os
# print(os.environ['API_HOME'])
# Read the above created environment variable

path = pathlib.Path(__file__).parent.parent.parent.absolute()
logs_path = os.path.join(path,"logs","testcase.log")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler = logging.FileHandler(logs_path)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)