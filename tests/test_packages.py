"""Check that each guardian can be installed on its own."""

import re
import unittest
from pathlib import Path


SKILLS = Path(__file__).resolve().parents[1] / "skills"
WEB = SKILLS / "web-experience-guardian"
MINI = SKILLS / "miniprogram-experience-guardian"


class GuardianPackages(unittest.TestCase):
    def test_shared_protocol_is_identical(self):
        for filename in (
            "guardian-routing.md",
            "guardian-contract.md",
            "guardian-report.schema.json",
        ):
            with self.subTest(filename=filename):
                relative = Path("references") / filename
                self.assertEqual((WEB / relative).read_bytes(), (MINI / relative).read_bytes())

    def test_package_links_resolve_after_standalone_install(self):
        for package in (WEB, MINI):
            self.assertTrue((package / "SKILL.md").is_file())
            for document in package.rglob("*.md"):
                for link in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                    if link.startswith(("#", "https://", "http://", "mailto:")):
                        continue
                    with self.subTest(document=document.name, link=link):
                        destination = (document.parent / link.split("#", 1)[0]).resolve()
                        self.assertIn(package, destination.parents)
                        self.assertTrue(destination.exists(), destination)


if __name__ == "__main__":
    unittest.main()
