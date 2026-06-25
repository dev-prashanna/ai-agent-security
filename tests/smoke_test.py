"""
Local smoke test for the attack algorithm.
Run this to verify your setup works before submitting.

Usage:
    python tests/smoke_test.py

Or with the SDK installed:
    python -m tests.smoke_test
"""

import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))


def test_sdk_import():
    """Test that the competition SDK is importable."""
    try:
        from aicomp_sdk.environment import Environment
        from aicomp_sdk.attack import AttackAlgorithmBase
        from aicomp_sdk.types import AttackCandidate
        print("[PASS] SDK imports successful")
        return True
    except ImportError as e:
        print(f"[FAIL] SDK import failed: {e}")
        print("       Download competition data first: kaggle competitions download ...")
        return False


def test_attack_import():
    """Test that attack.py is importable."""
    try:
        from attack import AttackAlgorithm
        print("[PASS] AttackAlgorithm import successful")
        return True
    except ImportError as e:
        print(f"[FAIL] attack.py import failed: {e}")
        return False


def test_attack_instantiation():
    """Test that AttackAlgorithm can be instantiated."""
    try:
        from attack import AttackAlgorithm
        algo = AttackAlgorithm()
        print("[PASS] AttackAlgorithm instantiation successful")
        return True
    except Exception as e:
        print(f"[FAIL] AttackAlgorithm instantiation failed: {e}")
        return False


def test_environment_creation():
    """Test that the environment can be created."""
    try:
        from aicomp_sdk.environment import Environment
        env = Environment(seed=123)
        print("[PASS] Environment creation successful")
        return True
    except Exception as e:
        print(f"[FAIL] Environment creation failed: {e}")
        return False


def test_full_smoke():
    """Run a minimal smoke test with the environment."""
    try:
        from aicomp_sdk.environment import Environment
        from attack import AttackAlgorithm

        print("\n--- Full Smoke Test ---")
        env = Environment(seed=123)
        algo = AttackAlgorithm()

        print("Running attack algorithm...")
        candidates = algo.run(env)

        print(f"Attack returned {len(candidates)} candidates")
        print("[PASS] Full smoke test completed")
        return True
    except Exception as e:
        print(f"[FAIL] Full smoke test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("=== AI Agent Security - Smoke Test ===\n")

    results = []

    results.append(("SDK Import", test_sdk_import()))
    results.append(("Attack Import", test_attack_import()))
    results.append(("Attack Instantiation", test_attack_instantiation()))
    results.append(("Environment Creation", test_environment_creation()))

    if all(r[1] for r in results):
        results.append(("Full Smoke", test_full_smoke()))

    print("\n=== Summary ===")
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  {name}: {status}")

    if all(r[1] for r in results):
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nSome tests failed.")
        sys.exit(1)
