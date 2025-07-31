# scripts/sql_utils.py

import os
import sys
# Auto-Locate project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import config
from utils.logger import get_logger

logger = get_logger()

def get_trip_summary_query():
    """
    Return SQL to query the trip summary created by render_create_summary_sql().
    """
    return f"""
    SELECT
        pickup_hour,
        trip_count,
        avg_fare,
        avg_tip,
        total_passengers,
        avg_distance
    FROM `{config.PROJECT_ID}.{config.DATASET_ID}.{config.SUMMARY_TABLE_NAME}`
    ORDER BY pickup_hour
    """

if __name__ == "__main__":
    logger.info(get_trip_summary_query())