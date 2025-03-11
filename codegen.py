from smolagents import CodeAgent, LiteLLMModel


def build_prompt(prompt_template: str, problem_stmt: str, config: dict):
    with open(prompt_template, "r") as f:
        prompt = f.read()
    params = {k: ", ".join(v) for k, v in config.items() if k in ["banned_elements", 
                                                                  "required_elements",
                                                                  "test_case_hints",
                                                                  "additional_requirements"]}
    return prompt.format(problem_statement=problem_stmt, **params)



class Model:
    def __init__(self, config: dict):
        self.model = LiteLLMModel("ollama/qwen2.5-coder")
        self.temp = 0.5
        self.config = config
        self.system_prompt = "You are a Python instructor in an introduction to programming course at graduate level.\n"
        self.agent = CodeAgent(tools=[], model=self.model, )
      
    def run(self, problem_stmt: str):
        self.prompt = build_prompt(self.config["prompt-template"], problem_stmt, self.config)
        print(self.prompt)
        return self.agent.run(self.system_prompt + " \n" + self.prompt + " " + problem_stmt)