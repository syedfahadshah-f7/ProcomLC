import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from rigorous_tests import RigorousTester

tester = RigorousTester()
print("Starting Scenario A Test...")
result = tester.run_pipeline("A", "The Poisoned Researcher", "Sarah Chen")
print(f"\nFinal Result: {'PASS' if result else 'FAIL'}")
