#!/usr/bin/env python3
"""
Test runner script
"""
import subprocess
import sys
import os

# Change to test-project directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Add src to Python path
sys.path.insert(0, 'src')

# Run pytest
try:
    result = subprocess.run([
        sys.executable, '-m', 'pytest', 'tests/', '-v', '--tb=short'
    ], capture_output=True, text=True, cwd='.')
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print(f"\nReturn code: {result.returncode}")
    
except Exception as e:
    print(f"Error running tests: {e}")