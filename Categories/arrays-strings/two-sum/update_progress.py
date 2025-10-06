#!/usr/bin/env python3
import os
import json

def count_solutions():
    """Count solutions by language and category"""
    progress = {
        "categories": {},
        "languages": {"python": 0, "java": 0, "cpp": 0, "javascript": 0},
        "total": 0
    }
    
    for category in os.listdir("categories"):
        category_path = f"categories/{category}"
        if os.path.isdir(category_path):
            progress["categories"][category] = 0
            
            for problem in os.listdir(category_path):
                problem_path = f"{category_path}/{problem}"
                if os.path.isdir(problem_path):
                    # Count solutions for this problem
                    problem_solutions = 0
                    for lang in ["python", "java", "cpp", "javascript"]:
                        solution_file = f"{problem_path}/solution.{'js' if lang == 'javascript' else lang}"
                        if os.path.exists(solution_file):
                            progress["languages"][lang] += 1
                            problem_solutions += 1
                    
                    if problem_solutions > 0:
                        progress["categories"][category] += 1
                        progress["total"] += 1
    
    return progress

def update_readme(progress):
    """Update README with current progress"""
    # Implementation to update progress table in README
    pass

if __name__ == "__main__":
    progress = count_solutions()
    print(json.dumps(progress, indent=2))
