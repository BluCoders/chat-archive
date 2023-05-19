from sqlalchemy import create_engine
from logger import root_log

engine = create_engine("sqlite+pysqlite:///content.db", echo=True)

if __name__ == "__main__":
    log = root_log.getChild("Main")
    log.info("Log test")


