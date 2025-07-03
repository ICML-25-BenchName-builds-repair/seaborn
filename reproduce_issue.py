#!/usr/bin/env python3
"""
Script to reproduce the get_layout_engine issue.
This script should fail before the fix and pass after the fix.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.objects import Plot

def test_layout_extent():
    """Test that reproduces the NameError: name 'get_layout_engine' is not defined"""
    print("Testing Plot().layout(extent=...).plot()...")
    
    try:
        # This should trigger the error
        p = Plot().layout(extent=(.1, .2, .6, 1)).plot()
        print("✓ SUCCESS: Plot with layout extent worked!")
        return True
    except NameError as e:
        if "get_layout_engine" in str(e):
            print(f"✗ FAILED: {e}")
            return False
        else:
            print(f"✗ UNEXPECTED ERROR: {e}")
            return False
    except Exception as e:
        print(f"✗ UNEXPECTED ERROR: {e}")
        return False

def test_constrained_layout_extent():
    """Test constrained layout with extent"""
    print("Testing Plot().layout(engine='constrained', extent=...).plot()...")
    
    try:
        p = Plot().layout(engine="constrained", extent=(.1, .2, .6, 1)).plot()
        print("✓ SUCCESS: Plot with constrained layout and extent worked!")
        return True
    except NameError as e:
        if "get_layout_engine" in str(e):
            print(f"✗ FAILED: {e}")
            return False
        else:
            print(f"✗ UNEXPECTED ERROR: {e}")
            return False
    except Exception as e:
        print(f"✗ UNEXPECTED ERROR: {e}")
        return False

def test_base_layout_extent():
    """Test base layout (engine=None) with extent"""
    print("Testing Plot().layout(engine=None, extent=...).plot()...")
    
    try:
        p = Plot().layout(engine=None, extent=(.1, .2, .6, 1)).plot()
        print("✓ SUCCESS: Plot with base layout and extent worked!")
        return True
    except NameError as e:
        if "get_layout_engine" in str(e):
            print(f"✗ FAILED: {e}")
            return False
        else:
            print(f"✗ UNEXPECTED ERROR: {e}")
            return False
    except Exception as e:
        print(f"✗ UNEXPECTED ERROR: {e}")
        return False

def main():
    print("=" * 60)
    print("REPRODUCING get_layout_engine ISSUE")
    print("=" * 60)
    
    # Test all three scenarios that fail in the CI
    results = []
    results.append(test_layout_extent())
    results.append(test_constrained_layout_extent()) 
    results.append(test_base_layout_extent())
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if all(results):
        print("✓ ALL TESTS PASSED - Issue is fixed!")
        return 0
    else:
        print("✗ SOME TESTS FAILED - Issue still exists!")
        return 1

if __name__ == "__main__":
    exit(main())