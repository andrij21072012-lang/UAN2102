from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

current_date = datetime.now().strftime("%Y-%m-%d")

logging.info(f"Поточна дата: {current_date}")
