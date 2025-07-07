# Test file with security issues for CodeRabbit to detect

import os
import subprocess

# Security issue 1: Using eval() - dangerous
def unsafe_eval(user_input):
    return eval(user_input)

# Security issue 2: Shell injection vulnerability
def unsafe_command(filename):
    os.system(f"cat {filename}")  # Shell injection risk

# Security issue 3: Hardcoded secrets
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

# Security issue 4: Unsafe file operations
def read_file(filepath):
    with open(filepath, 'r') as f:  # No path validation
        return f.read()

# Performance issue: Inefficient loop
def inefficient_function():
    result = []
    for i in range(1000):
        result = result + [i]  # Inefficient list concatenation
    return result

# Code quality issue: Unused imports and variables
import json
import sys
unused_variable = "this is not used"

def function_with_issues():
    # Missing error handling
    data = json.loads('{"key": "value"}')
    return data['nonexistent_key']  # Will cause KeyError