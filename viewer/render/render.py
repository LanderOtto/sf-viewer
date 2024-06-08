from __future__ import annotations

import os
import statistics

import pandas as pd
import plotly.express as px
import plotly.io as pio

from datetime import datetime, timedelta
from typing import MutableSequence

from viewer.core.entity import Step
from viewer.render.utils import print_split_section


def plot_gantt(
    steps: MutableSequence[Step],
    workflow_start_date: datetime,
    outdir: str,
    filename: str,
    format: str,
) -> None:

    df = pd.DataFrame(
        [
            dict(
                Task=step.name,
                Start=workflow_start_date + step.get_start(),
                Finish=workflow_start_date + step.get_end(),
                Jobs=len(step.instances),
            )
            for step in steps
        ]
    )
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Task", text="Jobs", color="Task"
    )
    fig.update_yaxes(visible=False)
    _, ext = os.path.splitext(filename)
    pio.write_html(
        fig,
        os.path.join(
            outdir, filename if f".{format}" == ext else f"{filename}.{format}"
        ),
    )


def print_to_stdout(
    steps: MutableSequence[Step],
    workflow_start_date: datetime,
    workflow_end_date: datetime,
) -> None:
    for step in steps:
        print(f"Step name:      {step.name}")
        print(f"N.of instances: {len(step.instances)}")
        print(f"Start time:     {step.get_start()}")
        print(f"End time:       {step.get_end()}")
        step_exec = step.get_exec()
        print(f"Exec time:      {step_exec} = {step_exec.total_seconds():.4f} seconds")
        if len(step.instances) > 1:
            # tempo che intercorre tra il deploy della prima istanza e l'ultima
            first_instance_deploy = min(instance.start for instance in step.instances)
            last_instance_deploy = max(instance.start for instance in step.instances)
            instance_deploy_time = last_instance_deploy - first_instance_deploy
            print(
                f"Instance deploy time:   {instance_deploy_time} = {instance_deploy_time.total_seconds():.4f} seconds"
            )
            min_instance_exec = min(instance.get_exec() for instance in step.instances)
            print(
                f"Min instance exec:      {min_instance_exec} = {min_instance_exec.total_seconds():.4f} seconds"
            )
            max_instance_exec = max(instance.get_exec() for instance in step.instances)
            print(
                f"Max instance exec:      {max_instance_exec} = {max_instance_exec.total_seconds():.4f} seconds"
            )
            avg_instance_exec = timedelta(
                seconds=statistics.mean(
                    instance.get_exec().total_seconds() for instance in step.instances
                )
            )
            print(
                f"Avg instances exec:     {avg_instance_exec} = {avg_instance_exec.total_seconds():.4f} seconds"
            )
        print_split_section()
    print("workflow start date: ", workflow_start_date)
    print("workflow end date:   ", workflow_end_date)
    print("workflow exec time:  ", workflow_end_date - workflow_start_date)
