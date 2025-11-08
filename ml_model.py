import torch
import torch.nn as nn
import torch.optim as optim
import voice_handler

class OMNIModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(OMNIModel, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.layer1(x)
        out = self.relu(out)
        out = self.layer2(out)
        return out

def train_on_interaction(model, data, optimizer, criterion):
    """
    Trains the model on a single user interaction.
    """
    features, target = data
    optimizer.zero_grad()
    output = model(features)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

def predict_next_action(model, context):
    """
    Predicts the next action based on the current context.
    """
    with torch.no_grad():
        prediction = model(context)
        return prediction.argmax().item()

def confirm_action(action):
    """
    Asks for user confirmation via voice and returns True if confirmed.
    """
    voice_handler.speak(f"Are you sure you want to perform the action: {action}?")
    response = voice_handler.listen()
    if response and "yes" in response.lower():
        return True
    else:
        voice_handler.speak("Action cancelled.")
        return False
