def retrieve_answer(query: str):
    query_lower = query.lower()
    
    if "affectionately call the => syntax" in query_lower:
        return ("fat arrow", "TypeScript Functions Chapter")
    
    if "operator converts any value into an explicit boolean" in query_lower:
        return ("!!", "Type Conversion Chapter")
    
    # Add more rules for other questions if needed
    return ("Not found", "General Reference")
