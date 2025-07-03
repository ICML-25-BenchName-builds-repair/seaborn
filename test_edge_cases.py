#!/usr/bin/env python3
"""
Test edge cases for the get_layout_engine fix.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.objects import Plot
import numpy as np

def test_with_data():
    """Test layout extent with actual data"""
    print("Testing layout extent with data...")
    
    try:
        # Create some sample data
        data = {"x": [1, 2, 3, 4], "y": [1, 4, 2, 3]}
        
        p = (Plot(data, x="x", y="y")
             .add(sns.objects.Dot())
             .layout(extent=(.1, .1, .9, .9))
             .plot())
        
        print("✓ SUCCESS: Layout extent with data worked!")
        plt.close(p._figure)
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

def test_different_extents():
    """Test various extent values"""
    print("Testing different extent values...")
    
    extents = [
        (.0, .0, 1.0, 1.0),  # Full figure
        (.2, .2, .8, .8),    # Centered
        (.1, .3, .7, .9),    # Asymmetric
    ]
    
    for i, extent in enumerate(extents):
        try:
            p = Plot().layout(extent=extent).plot()
            print(f"  ✓ Extent {i+1}: {extent} worked!")
            plt.close(p._figure)
        except Exception as e:
            print(f"  ✗ Extent {i+1}: {extent} failed: {e}")
            return False
    
    return True

def test_different_engines():
    """Test layout extent with different engines"""
    print("Testing layout extent with different engines...")
    
    engines = ["tight", "constrained", None]
    
    for engine in engines:
        try:
            p = Plot().layout(engine=engine, extent=(.1, .2, .8, .9)).plot()
            print(f"  ✓ Engine '{engine}' worked!")
            plt.close(p._figure)
        except Exception as e:
            print(f"  ✗ Engine '{engine}' failed: {e}")
            return False
    
    return True

def test_import_directly():
    """Test that we can import get_layout_engine directly"""
    print("Testing direct import of get_layout_engine...")
    
    try:
        from seaborn._compat import get_layout_engine
        fig = plt.figure()
        engine = get_layout_engine(fig)
        print(f"  ✓ Direct import worked! Engine: {engine}")
        plt.close(fig)
        return True
    except Exception as e:
        print(f"  ✗ Direct import failed: {e}")
        return False

def main():
    print("=" * 60)
    print("TESTING EDGE CASES FOR get_layout_engine FIX")
    print("=" * 60)
    
    tests = [
        test_with_data,
        test_different_extents,
        test_different_engines,
        test_import_directly,
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    print("=" * 60)
    print("EDGE CASE TEST SUMMARY")
    print("=" * 60)
    
    if all(results):
        print("✓ ALL EDGE CASE TESTS PASSED!")
        return 0
    else:
        print("✗ SOME EDGE CASE TESTS FAILED!")
        return 1

if __name__ == "__main__":
    exit(main())