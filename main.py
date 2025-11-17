# lis -> parse le yaml -> execute la pipeline
# python3 main.py --pipeline pipeline.yaml

import yaml
import argparse
from operations import overlay

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-p",
    "--pipeline",
    type=str,
    required=True,
    help="Emplacement du fichier yaml décrivant les traitements à effectuer",
)
args = arg_parser.parse_args()

yaml_file = open(args.pipeline, "r")
parsed_yaml = yaml.safe_load(yaml_file)

operations = {
    "overlay": overlay.sar_overlay,
}

for pipeline_name in parsed_yaml:
    pipeline = parsed_yaml[pipeline_name]

    # Premier loop pour s'assurer que toutes les operations sont valides
    for step in pipeline:
        try:
            _ = operations[pipeline[step]["operation"]]
        except KeyError:
            print(
                f"L'opération '{pipeline[step]["operation"]}' dans l'etape '{step}' n'existe pas'"
            )
            exit(1)

    for step in pipeline:
        print(pipeline)
        operation_args = pipeline[step]["args"]
        operations[pipeline[step]["operation"]](**operation_args)

    # Seulement Une pipeline par fichier
    break
