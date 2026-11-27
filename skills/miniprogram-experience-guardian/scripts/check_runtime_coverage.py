"""Compare a v1 guardian report to independently requested runtime probes."""

import argparse
import json
import sys
from pathlib import Path


def coverage_errors(report, required_ids):
    if not isinstance(report, dict) or not isinstance(report.get("evidence"), list):
        raise ValueError("expected a report object containing an evidence array")
    if "scope" not in report or "verdict" not in report:
        raise ValueError("missing report scope or verdict")

    errors = []
    if report["scope"] != "RUNTIME":
        errors.append("expected RUNTIME scope")
    if report["verdict"] != "PASS":
        errors.append("report verdict: " + str(report["verdict"]))

    runtime = {probe_id: [] for probe_id in required_ids}
    for index, entry in enumerate(report["evidence"]):
        if not isinstance(entry, dict) or not isinstance(entry.get("probeId"), str):
            raise ValueError("invalid probeId at evidence[{}]".format(index))
        probe_id = entry["probeId"]
        if entry.get("status") == "FAIL":
            errors.append(probe_id + ": FAIL")
        if entry.get("kind") == "RUNTIME" and probe_id in runtime:
            runtime[probe_id].append(entry)

    for probe_id, entries in runtime.items():
        if len(entries) != 1:
            errors.append("{}: expected one RUNTIME record, found {}".format(probe_id, len(entries)))
            continue
        entry = entries[0]
        if entry.get("required") is not True:
            errors.append(probe_id + ": RUNTIME record must have required=true")
        if entry.get("status") not in ("PASS", "FAIL"):
            errors.append("{}: no runtime result ({})".format(probe_id, entry.get("status")))
        if not isinstance(entry.get("detail"), str) or not entry["detail"].strip():
            errors.append(probe_id + ": missing runtime evidence detail")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="v1 report JSON file")
    parser.add_argument("--require", action="append", required=True, metavar="ID",
                        help="runtime probe ID from the original acceptance criteria (repeatable)")
    args = parser.parse_args()
    if any(not probe_id.strip() for probe_id in args.require):
        parser.error("--require expects a nonblank probe ID")
    try:
        report = json.loads(args.report.read_text(encoding="utf-8-sig"))
        errors = coverage_errors(report, args.require)
    except (OSError, ValueError) as exc:
        parser.exit(2, "Invalid report: {}\n".format(exc))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: all requested runtime probes passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
