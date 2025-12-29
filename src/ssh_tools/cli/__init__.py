import click
from ssh_tools.__about__ import __version__

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="ssh-tools")
def main():
    """SSH Tools CLI."""
    pass

if __name__ == "__main__":
    main()