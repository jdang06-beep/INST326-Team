"""
INTEGRATION TEST 4
Demo ↔ Core Modules

Strategy:
Ensures demo can execute and interact with underlying classes.

Coverage Rationale:
Prevents integration regressions between demo and business logic.
"""

import unittest
import demo


class TestDemoIntegration(unittest.TestCase):

    def test_demo_executes_successfully(self):
        try:
            demo.demonstrate_polymorphism()
            success = True
        except Exception:
            success = False

        self.assertTrue(success)
