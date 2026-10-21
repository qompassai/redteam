# Wave-1 tail bundle — 2026-10-17

Decision 7 (Owner, 2026-10-16): vendored `BlackArch/scripts/baconflict`
patched minimally — one `;` added before the closing brace of the
`check_files` brace group (line ~77), which was unclosed as shipped
upstream and made the script unparseable. Divergence from upstream
BlackArch: exactly that one character; noted in
`tests/test_collection.py`, whose KNOWN_UNPARSEABLE_SCRIPTS exact set
is now empty. Gate re-run: pytest 8/8.
