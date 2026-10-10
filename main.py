import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="a",
                    format="We have next logging message: %(asctime)s:%(levelname)s - %(message)s")


logging.info("Програма  запустилася")
