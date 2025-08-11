import os
import sys
from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv
load_dotenv()

# Ensure the 'scripts' module is on the path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from scripts.logger import get_logger
logger = get_logger()

def get_bigquery_client():
    # Define credential paths for both local and container environments
    cred_path_local = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_PATH", "creds/gcp_service_account.json")
    cred_path_container = "/opt/airflow/creds/gcp_service_account.json"

    # Determine whether running inside a Docker container
    is_container = os.path.exists("/.dockerenv") or os.getenv("DOCKER_CONTAINER") == "true"

    # Choose appropriate credential path
    cred_path = cred_path_container if is_container else cred_path_local
    logger.info(f"Using credential path: {cred_path}")


    # Raise error if the credential file does not exist
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"Credential file not found: {cred_path}")

    # Load credentials and initialize BigQuery client
    credentials = service_account.Credentials.from_service_account_file(cred_path)
    return bigquery.Client(credentials=credentials, location="US")