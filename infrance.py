
def ask_elevenmadison_assistant(user_query, qa_chain, DATA_FILE_PATH):
    """
    Processes the user query using the RAG chain and returns formatted results.
    """
    print(f"\nProcessing Gradio query: '{user_query}'")
    if not user_query or user_query.strip() == "":
        print("--> Empty query received.")
        return "Please enter a question.", ""  # Handle empty input gracefully

    try:
        # Run the query through our RAG chain
        result = qa_chain.invoke({"question": user_query})

        # Extract answer and sources
        answer = result.get("answer", "Sorry, I couldn't find an answer in the provided documents.")
        sources = result.get("sources", "No specific sources identified.")

        # Basic formatting for sources (especially if it just returns the filename)
        if sources == DATA_FILE_PATH:
            sources = f"Retrieved from: {DATA_FILE_PATH}"
        elif isinstance(sources, list):  # Handle potential list of sources
            sources = ", ".join(list(set(sources)))  # Unique, comma-separated

        print(f"--> Answer generated: {answer[:100].strip()}...")
        print(f"--> Sources identified: {sources}")

        # Return the answer and sources to be displayed in Gradio output components
        return answer.strip(), sources

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(f"--> Error during chain execution: {error_message}")
        # Return error message to the user interface
        return error_message, "Error occurred"