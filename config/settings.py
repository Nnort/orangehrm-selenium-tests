import os

BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
VALID_USERNAME = os.getenv("VALID_USERNAME", "Admin")
VALID_PASSWORD = os.getenv("VALID_PASSWORD", "admin123")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))