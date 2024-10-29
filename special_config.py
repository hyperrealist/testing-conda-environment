import argparse
import os
import json

action_map = {}
def register(f):
    action_map[f.__name__.lower()] = f
    return f

@register
def tla1():
    # action specific to beamline TLA1
    ...

@register
def tla2():
    # action specific to beamline TLA2
    ...


def main():
    curr_bdict = {}

    parser = argparse.ArgumentParser(description='Parses Json and passes arguments to download-artifacts-sh')
    parser.add_argument("-b", "--beamline_acronym", help="Example csx")
    args = parser.parse_args()

    beamline_actions = action_map.get(args.beamline_acronym.lower(), None)
    if beamline_actions is not None:
        beamline_actions()

if __name__ == "__main__":
    main()
