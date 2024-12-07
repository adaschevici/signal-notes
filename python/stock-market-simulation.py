from shiny import App, render, ui
import asyncio

# Define the app UI
app_ui = ui.page_fluid(
    ui.h2("Simple Shiny Dropdown Example"),
    ui.input_select(
        id="dropdown",
        label="Choose an option:",
        choices={
            "Option 1": "Option 1",
            "Option 2": "Option 2",
            "Option 3": "Option 3",
        },
    ),
    ui.input_switch(
        id="dark_mode_toggle",
        label="Enable Dark Mode",
    ),
    ui.output_text_verbatim("selected_value"),
    ui.tags.head(
        ui.tags.style(
            """
            .dark-mode {
                background-color: #121212;
                color: #ffffff;
            }
            """
        )
    ),
    ui.tags.script(
        """
        $(document).on("shiny:inputchanged", function(event) {
            console.log(event);
            if (event.name === "dark_mode_toggle") {
                if (event.value) {
                    document.body.classList.add("dark-mode");
                } else {
                    document.body.classList.remove("dark-mode");
                }
            }
        });
        """
    ),
)


# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def selected_value():
        return f"You selected: {input.dropdown.get()}"


# Create the app
app = App(app_ui, server)

# To run this script, use: shiny run <script_name.py>
