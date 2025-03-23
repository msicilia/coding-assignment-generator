import yaml
from argparse import ArgumentParser
from codegen import Model

def main(yaml_filename: str):
    config = yaml.safe_load(open(yaml_filename, "r"))
    model_names = [#"ollama/qwen2.5-coder",   "ollama/yi-coder",
                    "ollama/codellama", "ollama/codegemma", "ollama/codestral"]
    for model_name in model_names:
        model = Model(model_name, config) # TODO: Do not pass the problem statements here
        problem_statements = config["problem_statements"]
        for i, problem_statement in enumerate(problem_statements):
            print(problem_statement)
            # TODO: Pass the prompt template filename. 
            out = model.run(problem_statement)
            with open(f"outputs/{config['config_name']}_ex_{i}_{model_name.split('/')[1]}.md", "w") as f:
                f.write(str(out))


if __name__ == "__main__":
    parser = ArgumentParser(description="Generates Python coding exercises.")
    parser.add_argument("-yaml_filename", "--y", "-y", 
                        help="The filename of the yaml with the config.",
                        required=True)
    args = parser.parse_args()
    main(args.y)
