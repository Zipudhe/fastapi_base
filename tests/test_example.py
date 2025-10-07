# import pytest
import logging

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)
logger = logging.getLogger(__name__)


def original_method():
    return


def example_override():
    client = "orreridden method or value"
    return client


app.dependency_overrides[original_method] = example_override
