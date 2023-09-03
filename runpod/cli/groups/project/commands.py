
import re
import click

@click.group('project')
def project_cli():
    ''' Launch new project on RunPod '''

def validate_project_name(name):
    '''
    Validate the project name
    '''
    if re.search(r"[<>:\"/\\|?*]", name):
        raise click.BadParameter("Project name contains invalid characters.")
    return name

@project_cli.command('new')
def new_project_wizard():
    '''
    Create a new project
    '''
    # Prompt for project name
    project_name = click.prompt("Enter the project name", type=str)
    validate_project_name(project_name)

    # Prompt for runpod network storage volume ID
    runpod_volume_id = click.prompt("Enter the ID of your runpod network storage volume", type=str)

    # Prompt for Python version
    python_version = click.prompt(
        "Select a Python version",
        type=click.Choice(['3.10', '3.11'], case_sensitive=False)
    )

    click.echo(f"Project Name: {project_name}")
    click.echo(f"RunPod Volume ID: {runpod_volume_id}")
    click.echo(f"Python Version: {python_version}")
