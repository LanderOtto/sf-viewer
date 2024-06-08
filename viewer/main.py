#!/usr/bin/python3
import argparse
import json
import os

from viewer.core.utils import get_path
from viewer.render.render import plot_gantt, print_to_stdout
from viewer.translator.streamflow import check_and_analysis, get_steps


def main(args):
    # Get report from json file
    with open(get_path(args.input), "r") as fd:
        data = json.load(fd)
    # Get Workflow start and end times
    workflow_start_date, workflow_end_date = check_and_analysis(data)
    # Get step times
    steps = get_steps(data, workflow_start_date)

    print_to_stdout(steps, workflow_start_date, workflow_end_date)
    plot_gantt(
        steps, workflow_start_date, get_path(args.outdir), args.filename, args.format
    )


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-i",
            "--input",
            help="Insert path file streamflow report.json",
            type=str,
            required=True,
        )
        parser.add_argument(
            "-o",
            "--outdir",
            help="Output directory",
            type=str,
            default=os.getcwd(),
        )
        parser.add_argument(
            "-n",
            "--filename",
            help="filename",
            type=str,
            default="gantt",
        )
        parser.add_argument(
            "-f",
            "--format",
            help="filename",
            type=str,
            default="html",
            choices=["html"],
        )
        args = parser.parse_args()
        main(args)
    except KeyboardInterrupt:
        print()
