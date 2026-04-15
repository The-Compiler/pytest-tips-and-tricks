import asyncio
import pytest


@pytest.mark.asyncio
async def test_asyncio():
    answer = 42
    val = await asyncio.sleep(1, result=answer)
    assert val == answer
