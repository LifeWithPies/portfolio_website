# Estimated Token Consumption: 2500
"""
Unit tests for subagent_manager.py
"""

import pytest
from core.subagent_manager import SubagentManager, SubagentReviewer, SubagentTester

def test_can_spawn_subagent_within_limit():
    sm = SubagentManager()
    assert sm.can_spawn_subagent('reviewer') == True

def test_cannot_spawn_subagent_beyond_limit():
    sm = SubagentManager()
    sm.active_subagents = ['existing']
    assert sm.can_spawn_subagent('tester') == False

def test_spawn_subagent_reviewer():
    sm = SubagentManager()
    sub = sm.spawn_subagent('reviewer', code='test code')
    assert isinstance(sub, SubagentReviewer)
    assert sm.active_subagents == ['reviewer']

def test_subagent_reviewer_review():
    reviewer = SubagentReviewer('TODO: fix this')
    result = reviewer.review()
    assert 'TODO' in str(result['issues'])

def test_subagent_tester_run_tests():
    tester = SubagentTester('tests/test_hook_manager.py')
    result = tester.run_tests()
    assert 'passed' in result