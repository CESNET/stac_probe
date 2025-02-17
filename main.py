import argparse
from stac_probe import STACProbe

thresholds = {
    'ok': 24,
    'warn': 168
}
default_stac_server = "https://stac.cesnet.cz"


def prepare_parser():
    parser = argparse.ArgumentParser(description="Check status for a given STAC collection.")

    parser.add_argument(
        "--server", "-s",
        type=str,
        default=default_stac_server,
        help=f"STAC server to probe. Default: {default_stac_server}"
    )

    parser.add_argument(
        "--collection", "-c",
        type=str,
        required=True,
        help="The collection name to probe."
    )

    parser.add_argument(
        "--ok", "-o",
        type=int,
        default=thresholds['ok'],
        help=f"How old file (in hours) is considered OK? Anything older will be considered WARN (see --warn) or CRIT. Default: {thresholds['ok']} hours"
    )

    parser.add_argument(
        "--warn", "-w",
        type=int,
        default=thresholds['warn'],
        help=f"How old file (in hours) is considered CRIT? Anything older will be considered CRIT. Default: {thresholds['warn']} hours"
    )

    return parser


def main():
    parser = prepare_parser()
    args = parser.parse_args()

    stac_server = args.server
    collection_name = args.collection
    threshold_ok = args.ok
    threshold_warn = args.warn

    probe = STACProbe(
        root_url=stac_server, collection=collection_name,
        threshold_ok=threshold_ok, threshold_warn=threshold_warn
    )
    result = probe.check_last_entry_date()

    print(result[1])
    return result[0]


if __name__ == "__main__":
    result = main()
    exit(result)
