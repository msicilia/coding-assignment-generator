from smolagents import CodeAgent, LiteLLMModel

def build_prompt(prompt_template: str, problem_stmt: str, config: dict):
    """Build a prompt from a template file, a problem statement and a configuration dictionary."""
    with open(prompt_template, "r") as f:
        prompt = f.read()
    params = {k: ", ".join(v) for k, v in config.items() if k in ["banned_elements", 
                                                                  "required_elements",
                                                                  "test_case_hints",
                                                                  "additional_requirements"]}
    return prompt.format(problem_statement=problem_stmt, **params)

class Model:
    """Simple class to wrap the LiteLLMModel and CodeAgent classes."""
    def __init__(self, model_name, config: dict, temp: float):
        self.model = LiteLLMModel(model_name, temp=temp)
        self.temp = temp
        self.config = config
        self.system_prompt = "You are a Python instructor in an introduction to programming course at graduate level.\n"
        self.agent = CodeAgent(tools=[], model=self.model, max_steps=3)
      
    def run(self, problem_stmt: str):
        """Buld the prompt for the given problem statement and run the model."""
        self.prompt = build_prompt(self.config["prompt_template"], problem_stmt, self.config)
        return self.agent.run(self.system_prompt + " \n" + self.prompt + " " + problem_stmt)