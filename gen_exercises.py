import yaml
from argparse import ArgumentParser
from codegen import Model
def main(yaml_filename: str):
    config = yaml.safe_load(open(yaml_filename, "r"))
    print(config)
    model = Model(config) # Do not pass the problem statements here
    problem_statements = config["problem_statements"]
    for i, problem_statement in enumerate(problem_statements):
        print(problem_statement)
        print(model.run(problem_statement))
        out = model.run(problem_statement)
        with open(f"exercise_{i}.md", "w") as f:
            f.write(out)


if __name__ == "__main__":
    parser = ArgumentParser(description="Generates Python coding exercises.")
    parser.add_argument("-yaml_filename", "--y", "-y", 
                        help="The filename of the yaml with the config.",
                        required=True)
    args = parser.parse_args()
    main(args.y)
