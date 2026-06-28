# Estimated Token Consumption: 3000
"""
Unit tests for hook_manager.py
"""

import pytest
from core.hook_manager import HookManager

def test_pre_tool_use_hook_allows_non_mcp():
    hm = HookManager()
    context = {'tool_name': 'read_file', 'query': 'test'}
    assert hm.pre_tool_use_hook(context) == True

def test_pre_tool_use_hook_blocks_mcp_with_local_data():
    hm = HookManager()
    hm.local_index['test'] = 'data'
    context = {'tool_name': 'mcp_search', 'query': 'test'}
    assert hm.pre_tool_use_hook(context) == False

def test_token_optimizer_memory_glimpse():
    hm = HookManager()
    data = {'key': {'nested': 'value'}, 'list': [1, 2, 3]}
    glimpse = hm.token_optimizer_memory_glimpse(data)
    assert glimpse['key']['nested'] == '...'
    assert glimpse['list'] == ['...', '...', '...']

def test_guardrail_blocks_destructive():
    hm = HookManager()
    assert hm.guardrail_block_destructive_commands('rm -rf /') == True
    assert hm.guardrail_block_destructive_commands('ls') == False