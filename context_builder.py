
import torch
from config import ACTIONS

def create_context_tensor(last_interaction):
    """
    Creates a one-hot encoded context tensor from the last interaction's action.
    """
    num_actions = len(ACTIONS)

    # Create a zero tensor
    context_tensor = torch.zeros(1, num_actions)

    if last_interaction:
        last_action = last_interaction[1]  # last_interaction is (command, action)
        try:
            action_index = ACTIONS.index(last_action)
            # Create a one-hot encoded vector
            context_tensor[0][action_index] = 1
        except ValueError:
            # If the last action is not in our list, we don't set any hot bit.
            # This is a safe fallback.
            print(f"Warning: Last action '{last_action}' not found in known actions.")

    return context_tensor
