from fishfry import __version__, webapp
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.asyncio
class TestViews:
    async def test_index(self):
        assert "Welcome" in (await webapp.index())
