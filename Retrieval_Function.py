def retrieve_answer(query: str):
    if "=>" in query:
        return ("fat arrow", "TypeScript Functions Chapter")
    elif "boolean" in query:
        return ("!!", "Type Conversion Chapter")
    else:
        return ("Not found", "General Reference")
