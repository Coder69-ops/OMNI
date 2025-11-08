
import torch
import torch.optim as optim
import torch.nn as nn
import voice_handler
import command_router
import session_manager
import ml_model
import context_builder
from config import ACTIONS

class Orchestrator:
    def __init__(self):
        # Initialize Model
        sample_context = context_builder.create_context_tensor(None)
        input_size = sample_context.shape[1]
        hidden_size = 32
        self.output_size = len(ACTIONS)
        self.model = ml_model.OMNIModel(input_size, hidden_size, self.output_size)

        # Initialize optimizer and loss function for training
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01)
        self.criterion = nn.CrossEntropyLoss()
        self.actions = ACTIONS

    def run(self):
        session_manager.start_session()
        print("OMNI is listening...")

        while True:
            command = voice_handler.listen()

            if command:
                last_interaction = session_manager.get_session_context()
                context = context_builder.create_context_tensor(last_interaction)
                predicted_action_index = ml_model.predict_next_action(self.model, context)
                predicted_action = self.actions[predicted_action_index]

                was_correct = voice_handler.get_feedback(predicted_action)

                if was_correct:
                    target_action_index = predicted_action_index
                    if ml_model.confirm_action(predicted_action):
                        session_manager.log_interaction(command, predicted_action)
                        command_router.route_command(command, predicted_action)
                else:
                    voice_handler.speak("My apologies. What should I have done?")
                    correct_action_command = voice_handler.listen()
                    if correct_action_command:
                        try:
                            target_action = correct_action_command.lower().replace(" ", "_")
                            target_action_index = self.actions.index(target_action)
                            session_manager.log_interaction(command, self.actions[target_action_index])
                            command_router.route_command(command, self.actions[target_action_index])
                        except ValueError:
                            print(f"Could not map the correction '{correct_action_command}' to a known action.")
                            target_action_index = self.actions.index("default")

                target_tensor = torch.tensor([target_action_index], dtype=torch.long)
                ml_model.train_on_interaction(self.model, (context, target_tensor), self.optimizer, self.criterion)
                print("Model has been updated based on your feedback.")
