import pytest
from fastapi.testclient import TestClient

from contextlib import contextmanager
from datetime import datetime

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from geo.app import app
from geo.models.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_db_time():
    return _mock_db_time

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
    
@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
    pass

# https://fastapidozero.dunossauro.com/estavel/04
