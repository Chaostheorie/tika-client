import os
from pathlib import Path
from typing import Final

import pytest

from tika_client.client import TikaClient

TIKA_URL: Final[str] = os.getenv("TIKA_URL", "http://localhost:9998")

SAMPLE_DIR: Final[Path] = Path(__file__).parent.resolve() / "samples"


@pytest.fixture()
def tika_client() -> TikaClient:
    with TikaClient(tika_url=TIKA_URL) as client:
        yield client
