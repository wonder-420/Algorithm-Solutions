#!/usr/bin/env python3
import os
import argparse

def create_problem_structure(problem_name, category):
    """Create standardized problem directory structure"""
    
    base_path = f"categories/{category}/{problem_name}"
    os.makedirs(base_path, exist_ok=True)
    
    # Create README template
    readme_content = f"""# {problem_name.title().replace('-', ' ')}

## Problem Statement


## Approaches

### 1. Brute Force
- Time: 
- Space: 

### 2. Optimized
- Time: 
- Space: 

## Solutions

- [Python](solution.py)
- [Java](solution.java)
- [C++](solution.cpp)
- [JavaScript](solution.js)
"""
    
    with open(f"{base_path}/README.md", "w") as f:
        f.write(readme_content)
    
    # Create solution templates
    templates = {
        "solution.py": """def solution():
    \"\"\"
    Solution description
    \"\"\"
    pass

if __name__ == "__main__":
    # Test cases
    pass
""",
        "solution.java": """import java.util.*;

class Solution {
    public void solution() {
        // Implementation
    }
}
""",
        "solution.cpp": """#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void solution() {
        // Implementation
    }
};
""",
        "solution.js": """/**
 * @param {} input
 * @return {}
 */
function solution(input) {
    // Implementation
}

// Test cases
"""
    }
    
    for filename, content in templates.items():
        with open(f"{base_path}/{filename}", "w") as f:
            f.write(content)
    
    print(f"Created problem structure: {base_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_name", help="Name of the problem")
    parser.add_argument("category", help="Problem category")
    args = parser.parse_args()
    
    create_problem_structure(args.problem_name, args.category)
