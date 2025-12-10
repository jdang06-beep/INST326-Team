"""
SYSTEM TEST 1
Full End-to-End Demo Execution

Strategy:
Validates entire application workflow via demo execution.

Coverage Rationale:
Confirms system-level interaction of all components.
"""

import unittest
import demo


class TestFullSystemDemo(unittest.TestCase):

    def test_demo_full_run(self):
        try:
            demo.demonstrate_polymorphism()
            success = True
        except Exception:
            success = False

        self.assertTrue(success)
