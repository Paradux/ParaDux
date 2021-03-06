#!/usr/bin/python
#
# Copyright (C) 2019 and later, Paradux project.
# All rights reserved. License: see package.
#

import argparse
import paradux


def run(args, settings) :
    """
    Run this command.

    args: parsed command-line arguments
    settings: settings for this paradux instance
    """
    return paradux.run_not_implemented(args, settings)


def addSubParser(parentParser, cmdName) :
    """
    Enable this command to add its own command-line options
    parentParser: the parent argparse parser
    cmdName: name of this command
    """
    parser = parentParser.add_parser( cmdName, help='Change the secret(s) for this paradux configuration.' )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--everyday', action='store_const', const=True, help='Change the everyday passphrase')
    group.add_argument('--recovery', action='store_const', const=True, help='Change the recovery secret (requires updating the info with all stewards)')
