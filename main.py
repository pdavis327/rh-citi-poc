"""
TODO: Edit this
[Example pipeline]
pipeline description
"""

import argparse
import os
import logging
from util.argparse import pretty_print_args, setup_logging
from pipeline import Pipeline

# This is an example file. Rewrite using this template
# to execute your own pipeline.
PIPELINE_VERSION = "0.0.1"
PIPELINE_NAME = "[Example pipeline]"
PIPELINE_DESCRIPTION = "Pipeline repo template used for..."

# Some optional git parameters for logging
# Used for logging.
COMMIT_SHA = os.getenv("COMMIT_SHA", "")
COMMIT_BRANCH = os.getenv("COMMIT_BRANCH", "")
COMMIT_REPO = os.getenv("COMMIT_REPO", "")

parser = argparse.ArgumentParser(
    description=f"{PIPELINE_NAME} {PIPELINE_VERSION} - {PIPELINE_DESCRIPTION}"
)

# Common command line arguments.
# These are examples. Update to run your pipeline.
parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    dest="verbosity",
    default=1,
    help="verbose output (repeat for increased verbosity)",
)

parser.add_argument(
    "-q",
    "--quiet",
    action="store_const",
    const=-1,
    default=0,
    dest="verbosity",
    help="quiet output (show errors only)",
)

# Add subcommand arguments if needed
subparsers = parser.add_subparsers(dest="operation", required=True)
train = subparsers.add_parser("training", help="rf model training parameters")

train.add_argument(
    "--source_training_data",
    type=str,
    help="Source table for model training",
)

# Parse arguments
args = parser.parse_args()

# Setup logging
setup_logging(args.verbosity)

# Logger instance
log = logging.getLogger(__name__)

# Log pipeline metadata
args.COMMIT_SHA = COMMIT_SHA
args.COMMIT_BRANCH = COMMIT_BRANCH
args.COMMIT_REPO = COMMIT_REPO

log.info(f"{PIPELINE_NAME} v{PIPELINE_VERSION}")
log.info(f"{PIPELINE_DESCRIPTION}")
log.info(pretty_print_args(args))

# Additional metadata
args.PIPELINE_VERSION = PIPELINE_VERSION
args.PIPELINE_NAME = PIPELINE_NAME
args.PIPELINE_DESCRIPTION = PIPELINE_DESCRIPTION

# Pipeline execution
pipeline = Pipeline(args)

if __name__ == "__main__":
    result = pipeline.run()

    # Exit code: 0 indicates success, 1 indicates failure
    exit_code = 0 if result else 1
    exit(exit_code)
