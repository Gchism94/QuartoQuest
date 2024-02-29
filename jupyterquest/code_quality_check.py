from radon.complexity import cc_rank, cc_visit
import ast

def assess_code_complexity(code):
    """
    Assesses the complexity of code using Radon.
    Returns a list of complexity metrics for each function/method in the code.
    """
    if not isinstance(code, str):
        return "Invalid input: Code must be a string"
    try:
        complexities = cc_visit(code)
        return [(item.name, item.complexity, cc_rank(item.complexity)) for item in complexities]
    except Exception as e:
        return f"Error assessing complexity: {str(e)}"

def assess_code_structure(code):
    """
    Assess code structure using Python's ast module to parse code and analyze its structure.
    Returns an assessment result.
    """
    if not isinstance(code, str):
        return "Invalid input: Code must be a string"
    try:
        tree = ast.parse(code)
        functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        num_functions = len(functions)
        return f"Number of functions: {num_functions}"
    except SyntaxError as e:
        return f"Syntax error in code: {str(e)}"

def assess_code_quality(code_blocks):
    """
    Main function to assess the overall code quality.
    Returns a summary of code quality assessments.
    """
    quality_report = {}

    if not all(isinstance(code, str) for code in code_blocks):
        return {"Error": "All code blocks must be strings"}

    for i, code in enumerate(code_blocks, 1):
        complexity_report = assess_code_complexity(code)
        structure_report = assess_code_structure(code)

        quality_report[f"Code Block {i}"] = {
            "Complexity": complexity_report,
            "Structure": structure_report
        }

    return quality_report

# Example usage
if __name__ == "__main__":
    sample_code_blocks = [
        "def example_function(x):\n    return x * x\n",  # Sample code block
        # ... other code blocks
    ]
    code_quality_results = assess_code_quality(sample_code_blocks)
    for block, results in code_quality_results.items():
        print(f"{block} Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
        print()  # Newline for readability
