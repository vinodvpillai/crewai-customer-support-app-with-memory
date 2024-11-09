#!/usr/bin/env python
import sys
from customer_support_automation.crew import CustomerSupportAutomationCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "customer": "Vinod Pillai",
        "person": "Vinod",
        "inquiry": "I need help with setting up a Crew "
                "and kicking it off, specifically "
                "how can I add memory to my crew? "
                "Can you provide guidance?"
    }
    CustomerSupportAutomationCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew "
                "and kicking it off, specifically "
                "how can I add memory to my crew? "
                "Can you provide guidance?"
    }
    try:
        CustomerSupportAutomationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CustomerSupportAutomationCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew "
                "and kicking it off, specifically "
                "how can I add memory to my crew? "
                "Can you provide guidance?"
    }
    try:
        CustomerSupportAutomationCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
