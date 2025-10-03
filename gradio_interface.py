
import gradio as gr

def gradio_interface(ask_elevenmadison_assistant_partial):
    with gr.Blocks(theme=gr.themes.Soft(), title="Eleven Madison Park Q&A Assistant") as demo:
    # Title and description for the app
        gr.Markdown(
            """
            # Eleven Madison Park - AI Q&A Assistant 💬
            Ask questions about the restaurant based on its website data.
            The AI provides answers and cites the source document.
            *(Examples: What are the menu prices? Who is the chef? Is it plant-based?)*
            """
        )

        # Input component for the user's question
        question_input = gr.Textbox(
            label = "Your Question:",
            placeholder = "e.g., What are the opening hours on Saturday?",
            lines = 2,  # Allow a bit more space for longer questions
        )

        # Row layout for the output components
        with gr.Row():
            # Output component for the generated answer (read-only)
            answer_output = gr.Textbox(label="Answer:", interactive=False, lines=6)  # User cannot edit this
            # Output component for the sources (read-only)
            sources_output = gr.Textbox(label="Sources:", interactive=False, lines=2)

        # Row for buttons
        with gr.Row():
            # Button to submit the question
            submit_button = gr.Button("Ask Question", variant="primary")
            # Clear button to reset inputs and outputs
            clear_button = gr.ClearButton(components=[question_input, answer_output, sources_output], value="Clear All")

        # Add some example questions for users to try
        gr.Examples(
            examples=[
                "What are the different menu options and prices?",
                "Who is the head chef?",
                "What is Magic Farms?"],
            inputs=question_input,  # Clicking example loads it into this input
            # We could potentially add outputs=[answer_output, sources_output] and cache examples
            # but that requires running the chain for each example beforehand.
            cache_examples=False,  # Don't pre-compute results for examples for simplicity
        )

        # --- Connect the Submit Button to the Function ---
        # When submit_button is clicked, call 'ask_emp_assistant'
        # Pass the value from 'question_input' as input
        # Put the returned values into 'answer_output' and 'sources_output' respectively
        submit_button.click(fn = ask_elevenmadison_assistant_partial, inputs = question_input, outputs = [answer_output, sources_output])

    print("Gradio interface defined.")

    # --- Launch the Gradio App ---
    print("\nLaunching Gradio app... (Stop the kernel or press Ctrl+C in terminal to quit)")
    # demo.launch() # Launch locally in the notebook or browser
    demo.launch()  