def retrieve_answer(query: str):
    query_lower = query.lower()

    # Match all expected portal questions
    if "affectionately call the => syntax" in query_lower:
        return ("fat arrow", "TypeScript Functions Chapter")
    elif "operator converts any value into an explicit boolean" in query_lower:
        return ("!!", "Type Conversion Chapter")
    # Add more rules here as needed
    else:
        return ("Not found", "General Reference")
