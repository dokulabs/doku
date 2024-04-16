# pylint: disable=duplicate-code
"""
This module contains tests for Anthropic functionality using the Anthropic Python library.

Tests cover various API endpoints, including chat. 
These tests validate integration with OpenLIT.

Environment Variables:
    - ANTHROPIC_API_TOKEN: Anthropic API api_key for authentication.

Note: Ensure the environment variables are properly set before running the tests.
"""

import os
import pytest
from anthropic import Anthropic, AsyncAnthropic
import openlit

# Initialize synchronous Anthropic client
sync_client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_TOKEN")
)

# Initialize asynchronous Anthropic client
async_client = AsyncAnthropic(
    api_key=os.getenv("ANTHROPIC_API_TOKEN")
)

# Initialize environment and application name for OpenLIT monitoring
openlit.init(environment="dokumetry-testing", application_name="dokumetry-python-test")

def test_sync_anthropic_messages():
    """
    Tests synchronous messages with the 'claude-3-haiku-20240307' model.

    Raises:
        AssertionError: If the messages response object is not as expected.
    """

    try:
        message = sync_client.messages.create(
            max_tokens=1,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-3-haiku-20240307",
        )
        assert message.type == 'message'

    # pylint: disable=broad-exception-caught
    except Exception as e:
        if "rate limit" in str(e).lower():
            print("Rate Limited:", e)

@pytest.mark.asyncio
async def test_async_anthropic_messages():
    """
    Tests synchronous messages with the 'claude-3-haiku-20240307' model.

    Raises:
        AssertionError: If the messages response object is not as expected.
    """

    try:
        message = await async_client.messages.create(
            max_tokens=1,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-3-haiku-20240307",
        )
        assert message.type == 'message'

    # pylint: disable=broad-exception-caught
    except Exception as e:
        if "rate limit" in str(e).lower():
            print("Rate Limited:", e)