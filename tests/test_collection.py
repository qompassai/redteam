"""Validation gate for the qompassai/RedTeam repository.

RedTeam is a curated collection, not one program: reference
documents (PDFs incl. the NIST AI RMF Playbook), BlackArch
packaging scripts, a Flipper firmware tarball, a LaTeX pentest
report (Reports/pentest), and one buildable vendored tool —
Hak5's wifi-coconut (OGRed/Hak5/wifi-coconut, C + CMake).
These tests gate each artifact class on its own terms:

- every PDF carries the %PDF header and %%EOF trailer;
- the tarball opens and enumerates under tarfile;
- the wifi-coconut C project CONFIGURES AND BUILDS in a
  scratch copy (modern CMake needs the policy-minimum flag
  for its old cmake_minimum_required — recorded, not hidden);
- the LaTeX report's \\input graph resolves to real files.
  Compiling it is blocked by the environment, not the source:
  primo's TeX Live ships binaries without format files
  (pdflatex.fmt / texmf.cnf missing, measured 2026-10-16);
- the BlackArch shell scripts parse under bash -n.

Run: python3 -m pytest tests/ -q
"""

from __future__ import annotations

import re
import shutil
import subprocess
import tarfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBPROCESS_TIMEOUT_S = 300
INPUT_RE = re.compile(r'\\(?:input|include)\{([^}]+)\}')


def _validate_pdf(data: bytes) -> list[str]:
    """A complete PDF starts with %PDF and ends (near enough) with %%EOF."""
    problems: list[str] = []
    if not data.startswith(b'%PDF'):
        problems.append('missing %PDF header')
    if b'%%EOF' not in data[-2048:]:
        problems.append('missing %%EOF trailer in the last 2 KiB')
    return problems


def _validate_tex_inputs(main_tex: Path) -> list[str]:
    """Every \\input/\\include target of the report must exist."""
    problems: list[str] = []
    base = main_tex.parent
    for target in INPUT_RE.findall(main_tex.read_text(encoding='utf-8')):
        candidate = base / target
        if not (candidate.is_file() or candidate.with_suffix('.tex').is_file()):
            problems.append(f'\\input target missing: {target}')
    return problems


# --- Validation ---


def test_all_pdfs_are_structurally_complete() -> None:
    pdfs = sorted(REPO_ROOT.rglob('*.pdf'))
    assert len(pdfs) >= 8, 'expected the reference document set'
    for path in pdfs:
        assert _validate_pdf(path.read_bytes()) == [], path


def test_flipper_tarball_is_readable() -> None:
    tarball = REPO_ROOT / 'Flipper' / 'flipper-z-f7-update-unlshd-081.tgz'
    with tarfile.open(tarball, 'r:gz') as archive:
        members = archive.getmembers()
    assert len(members) >= 1


def test_wifi_coconut_builds(tmp_path: Path) -> None:
    if shutil.which('cmake') is None:
        pytest.skip('cmake not installed')
    source = REPO_ROOT / 'OGRed' / 'Hak5' / 'wifi-coconut'
    work = tmp_path / 'wifi-coconut'
    shutil.copytree(source, work)
    configure = subprocess.run(
        [
            'cmake',
            '-S',
            str(work),
            '-B',
            str(work / 'build'),
            '-DCMAKE_POLICY_VERSION_MINIMUM=3.5',
        ],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT_S,
        check=False,
    )
    assert configure.returncode == 0, configure.stderr[-2000:]
    build = subprocess.run(
        ['cmake', '--build', str(work / 'build'), '-j4'],
        capture_output=True,
        text=True,
        timeout=SUBPROCESS_TIMEOUT_S,
        check=False,
    )
    assert build.returncode == 0, build.stderr[-2000:]
    executable = work / 'build' / 'wifi_coconut'
    assert executable.is_file() and executable.stat().st_size > 0


def test_latex_report_input_graph_resolves() -> None:
    main_tex = REPO_ROOT / 'Reports' / 'pentest' / 'main.tex'
    assert _validate_tex_inputs(main_tex) == []


# Vendored BlackArch scripts with genuine syntax errors, by exact-set
# accounting (like the lock file in NUR). baconflict shipped with an
# unclosed brace group in check_files ("list_file_files }" — no ';'
# before the closing brace); Matt approved a minimal local patch on
# 2026-10-16 (Decision 7), so the set is now empty. DIVERGENCE: the
# local baconflict differs from upstream BlackArch by exactly that one
# ';'. If upstream fixes it, the vendored copy can be re-synced
# verbatim. Any new unparseable script turns this red until it is
# accounted here.
KNOWN_UNPARSEABLE_SCRIPTS = set()


def test_blackarch_scripts_parse() -> None:
    # BlackArch scripts are extensionless; select by shell shebang.
    shell_re = re.compile(r'^#!.*\b(?:ba)?sh\b')
    scripts = sorted(
        path
        for path in (REPO_ROOT / 'BlackArch' / 'scripts').rglob('*')
        if path.is_file()
        and shell_re.match(
            path.read_text(encoding='utf-8', errors='replace').split('\n', 1)[0]
        )
    )
    assert len(scripts) >= 40, 'expected the BlackArch script set'
    failures = set()
    for script in scripts:
        # -O extglob: dbmod/outdated use extglob array patterns
        # that only parse when the option is set before parsing;
        # their own shopt runs too late under a bare `bash -n`.
        result = subprocess.run(
            ['bash', '-O', 'extglob', '-n', str(script)],
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT_S,
            check=False,
        )
        if result.returncode != 0:
            failures.add(script.name)
    assert failures == KNOWN_UNPARSEABLE_SCRIPTS


# --- Adversarial ---


def test_pdf_validator_rejects_truncation() -> None:
    data = (REPO_ROOT / 'Gov' / 'NIST' / 'AI_RMF_Playbook.pdf').read_bytes()
    assert _validate_pdf(data[: len(data) // 2]) != []
    assert _validate_pdf(b'not a pdf at all') != []


def test_tex_validator_catches_missing_chapter(tmp_path: Path) -> None:
    main_tex = tmp_path / 'main.tex'
    main_tex.write_text('\\input{chapters/01-overview}\n', encoding='utf-8')
    assert _validate_tex_inputs(main_tex) != []


def test_tarball_validator_rejects_garbage(tmp_path: Path) -> None:
    bogus = tmp_path / 'bogus.tgz'
    bogus.write_bytes(b'this is not gzip data')
    with pytest.raises(tarfile.ReadError):
        with tarfile.open(bogus, 'r:gz') as archive:
            archive.getmembers()
