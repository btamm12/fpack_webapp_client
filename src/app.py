from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
from sanic import Sanic
from sanic.response import text
from sanic.request import Request

from src import constants
from src.logger import default_logger_path, logger, logger_setup
from src.model import Manager

# The application cannot run without the "subject_mapping.txt" file.
if not constants.SUBJECT_MAPPING_PATH.exists():
    msg = "The application cannot run without the 'subject_mapping.txt' file."
    msg += "\nPlease read the main README.md file to learn how to request it."
    print(msg)
    exit(0)

# The application cannot run without the "my_name.txt" file.
if not constants.MY_NAME_PATH.exists():
    msg = "The application cannot run without the 'collaboration/my_name.txt' file."
    msg += "\nPlease read the 'collaboration/README.md' file to learn how to create it."
    print(msg)
    exit(0)

# The application cannot run without the "my_sections.txt" file.
if not constants.MY_SECTIONS_PATH.exists():
    msg = "The application cannot run without the 'collaboration/my_sections.txt' file."
    msg += "\nPlease read the 'collaboration/README.md' file to learn how to create it."
    print(msg)
    exit(0)

# Load version file.
if not constants.VERSION_PATH.exists():
    msg = "The version.txt file could not be found! Exiting program..."
    print(msg)
    exit(1)
with open(constants.VERSION_PATH, "r") as f:
    version_str = f.readline().strip()
version_tuple = tuple(version_str.split("."))

# Load annotator name.
with open(constants.MY_NAME_PATH, "r") as f:
    annotator_name = f.readline().strip()
valid_names = ["bastiaan", "jade", "marthe"]
if annotator_name not in valid_names:
    msg = "The name provided in collaboration/my_name.txt '%s' is not valid."
    msg %= annotator_name
    msg += "\nValid names are: %s" % ", ".join(valid_names)
    msg += "\nPlease make sure that the file collaboration/my_name.txt is correct "
    msg += "and does not begin with a blank line."
    print(msg)
    exit(1)

# Create Sanic app.
app = Sanic(__name__)

# Tick interval, measured in seconds.
TICK_INTERVAL = 3

# Create manager.
mng = Manager(
    VERSION_TUPLE=version_tuple,
    ANNOTATOR_NAME=annotator_name,
    CONTEXT_SECS=4,
    TICK_INTERVAL=TICK_INTERVAL,
    DATA_DIR=str(constants.DIR_DATA),
    SUBJECT_MAPPING_PATH=constants.SUBJECT_MAPPING_PATH,
    MY_SECTIONS_PATH=constants.MY_SECTIONS_PATH,
    STATE_PATH=str(constants.STATE_PATH),
    SERVER_URL_BASE="https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v1/",
    DOWNLOAD_FAIL_TIMEOUT_SECS=60,
)

# Register logging middleware.
@app.middleware("request")
async def extract_user(request: Request):
    msg = "Received request at endpoint '%s'." % request.endpoint
    logger.info(msg)


# Test endpoint.
@app.get("/test")
async def test(request: Request):
    return text("test")


# Periodic task.
async def tick():
    await mng.tick()


# Handle IB connection/disconnection when server starts/stops.
@app.listener("before_server_start")
def before_start(app, loop):
    global TICK_INTERVAL

    # Start periodic task.
    scheduler = AsyncIOScheduler({"event_loop": loop}, timezone="Europe/Brussels")
    scheduler.add_job(tick, "interval", seconds=TICK_INTERVAL)
    scheduler.start()


if __name__ == "__main__":
    logger.info(f"Running fpack_webapp_client v{version_str}.")
    __DEBUG__ = False

    # Set up logger.
    __LOGGING_FMT__ = "[%(levelname)s @ %(asctime)s] %(message)s"
    __LOGGING_LVL_CONSOLE__ = logging.INFO
    __LOGGING_LVL_FILE__ = logging.INFO
    __LOGGING_FILE_PATH__ = default_logger_path(constants.DIR_SRC)
    logger_setup(
        fmt=__LOGGING_FMT__,
        console_level=__LOGGING_LVL_CONSOLE__,
        file_level=__LOGGING_LVL_FILE__,
        file_path=__LOGGING_FILE_PATH__,
    )
    logger.info("Setting up logger.")

    # Run app.
    # 0.0.0.0 means listen to all channels (e.g. both local_host==127.0.0.1 and
    # local_machine_ip==192.168.0.200)
    # Source: https://stackoverflow.com/a/38175246
    app.run(host="0.0.0.0", port=8080, debug=__DEBUG__)
