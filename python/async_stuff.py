from shiny import App, render, ui
import asyncio

# Define the app UI
app_ui = ui.page_fluid(
    ui.h2("Asynchronous Shiny Example"),
    ui.input_action_button("button", "Click me!"),
    ui.output_text_verbatim("output"),
)


# Define the server logic
async def server(input, output, session):
    @output
    @render.text
    async def output_txt():
        # Simulate an asynchronous operation
        await asyncio.sleep(2)  # Simulate a delay
        return "This is an async response after 2 seconds!"

    @session.on_input_change
    async def on_button_click():
        if input.button:
            print("Button clicked!")


# Create the app
app = App(app_ui, server)
