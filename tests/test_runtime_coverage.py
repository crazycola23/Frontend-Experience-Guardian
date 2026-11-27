import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILLS = Path(__file__).resolve().parents[1] / "skills"
CHECKERS = [SKILLS / package / "scripts" / "check_runtime_coverage.py" for package in
            ("web-experience-guardian", "miniprogram-experience-guardian")]
MOUSE = "W-D3.mouse-close"
KEYBOARD = "W-D3.keyboard-restore"


def evidence(probe, detail, kind="RUNTIME", status="PASS", required=True):
    return {"probeId": probe, "kind": kind, "required": required, "status": status, "detail": detail}


def report(entries, verdict="PASS", scope="RUNTIME"):
    return {"schemaVersion": 1, "package": "apps/web", "target": "WEB", "adapter": "BROWSER",
            "scope": scope, "verdict": verdict, "findings": [], "evidence": entries, "blindspots": []}


class RuntimeCoverage(unittest.TestCase):
    def setUp(self):
        self.mouse = evidence(MOUSE, "Clicked Close and observed the dialog disappear.")
        self.keyboard = evidence(KEYBOARD, "Pressed Escape and observed focus return to the opener.")
        self.source = evidence(KEYBOARD, "Dialog.ts:42 calls focus() on the opener.", kind="STATIC")
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "report.json"

    def check(self, data, expected_code, message):
        self.path.write_text(json.dumps(data), encoding="utf-8")
        for checker in CHECKERS:
            with self.subTest(checker=checker):
                result = subprocess.run([sys.executable, str(checker), str(self.path),
                                         "--require", MOUSE, "--require", KEYBOARD],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, expected_code, result.stderr)
                self.assertIn(message, result.stdout + result.stderr)

    def test_standalone_checkers_are_identical(self):
        self.assertEqual(CHECKERS[0].read_bytes(), CHECKERS[1].read_bytes())

    def test_both_runtime_steps_pass_with_extra_static_evidence(self):
        self.check(report([self.mouse, self.keyboard, self.source]), 0, "PASS")

    def test_missing_or_static_only_second_step_blocks_pass(self):
        for extra in ([], [self.source]):
            with self.subTest(extra=extra):
                self.check(report([self.mouse] + extra), 1, KEYBOARD + ": expected one RUNTIME")

    def test_valid_incomplete_report_is_deliverable_but_cannot_pass(self):
        pending = evidence(KEYBOARD, "Keyboard session unavailable.", status="NOT_RUN")
        data = report([self.mouse, self.source, pending], "INCOMPLETE")
        data["blindspots"].append("Keyboard focus restoration unobserved.")
        self.check(data, 1, "INCOMPLETE")
        data["verdict"] = "PASS"
        self.check(data, 1, "NOT_RUN")

    def test_optional_or_conflicting_runtime_records_do_not_satisfy_requirement(self):
        self.check(report([self.mouse, dict(self.keyboard, required=False)]), 1, "required=true")
        conflicting = dict(self.keyboard, status="FAIL", detail="Focus landed on the body.")
        self.check(report([self.mouse, self.keyboard, conflicting]), 1, "found 2")

    def test_actual_failure_and_nonpassing_verdict_block_release(self):
        failure = dict(self.keyboard, status="FAIL", detail="Focus landed on the body.")
        self.check(report([self.mouse, failure]), 1, KEYBOARD + ": FAIL")
        self.check(report([self.mouse, self.keyboard], "BLOCKED (P0)"), 1, "BLOCKED (P0)")

    def test_static_or_malformed_input_cannot_pass(self):
        self.check(report([self.mouse, self.keyboard], scope="STATIC"), 1, "expected RUNTIME")
        self.check({"evidence": "bad input"}, 2, "expected a report object")


if __name__ == "__main__":
    unittest.main()
