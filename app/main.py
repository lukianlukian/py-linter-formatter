def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line"],
        "column": error["column"],
        "message": error["message"],
        "name": error["name"],
        "source": error["source"]
    }

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "success" if errors else "no errors"
    }

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file, errors) for file, errors in linter_report.items()]
