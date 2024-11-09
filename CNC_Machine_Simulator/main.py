from input_form import get_user_inputs
from path_generation import generate_tool_path
from visualization import display_simulation
from database import save_simulation_data

def main():
    user_inputs = get_user_inputs()
    tool_path = generate_tool_path(user_inputs)
    display_simulation(tool_path)
    save_simulation_data(user_inputs, tool_path)

if __name__ == "__main__":
    main()
