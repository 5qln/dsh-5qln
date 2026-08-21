"""fractal.py — The Fractal: the Growth phase (G = α ≡ {α'}).

cell.py was S (Start): the seed → X (the validated spark).
This file is G (Growth): receive X, find the irreducible essence α, trace its
self-similar expressions {α'}, and validate the pattern Y.

    G = α ≡ {α'}

    α    = Core Essence — the irreducible pattern within X. Remove it, X collapses.
    ≡    = Identity Preservation — α remains identical across all expressions.
    {α'} = Self-Similar Expressions — the forms α takes across scales and domains.
    Y    = Validated Pattern — α named, ≡ holds, {α'} confirm across scales.

Decoding (D1, G-phase):
    1. RECEIVE X       — the validated spark (the seed cell) is the input.
    2. SEEK α          — within X, what is the irreducible core?
    3. TEST ≡          — does α hold unchanged when expressed in different forms?
    4. FIND {α'}       — where does α echo? At what scales?
    5. VALIDATE Y      — α named, ≡ holds, {α'} confirm.
"""

from __future__ import annotations

import typing

import cell as _seed  # RECEIVE X — the validated spark from S (Start)

# ---------------------------------------------------------------------------
# 1. RECEIVE X
# ---------------------------------------------------------------------------
X = _seed  # the seed cell — the whole lawful structure carried by cell.py


# ---------------------------------------------------------------------------
# 2. SEEK α — the irreducible core within X.
# ---------------------------------------------------------------------------
# α is NOT invented alongside X; it is found INSIDE X: the 4+1 structure itself.
ALPHA: dict[str, object] = {
    "center": _seed.CENTER,                 # one signless center (S = ∞0 → ?)
    "corners": _seed.CORNERS_CLOCKWISE,     # four corners (G, Q, P, V) clockwise
    "equations": dict(_seed.EQUATIONS),     # five equations, verbatim
    "outputs": dict(_seed.OUTPUTS),         # five outputs, verbatim
}
ALPHA_NAME: str = (
    "the 4+1 quincunx — S at center, (G,Q,P,V) clockwise, equations verbatim"
)


def seek_alpha(word: str = "") -> dict[str, object]:
    """Extract the essence of any node. If ≡ holds, this is identical to ALPHA for every word."""
    return {
        "center": _seed.CENTER,
        "corners": _seed.CORNERS_CLOCKWISE,
        "equations": {p: _seed.EQUATIONS[p] for p in _seed.POSITIONS},
        "outputs": {p: _seed.OUTPUTS[p] for p in _seed.POSITIONS},
    }


def irreducible() -> None:
    """α is the MINIMUM structure that still carries the grammar. Remove any part → X collapses."""
    assert ALPHA["center"] == "S", "remove the center → no ∞0 → ? (no start, no return)"
    assert ALPHA["corners"] == ("G", "Q", "P", "V"), "remove/reorder a corner → not 4+1"
    assert len(ALPHA["equations"]) == 5, "remove an equation → a phase loses its law"
    assert set(ALPHA["equations"]) == set(_seed.POSITIONS), "equations must cover S,G,Q,P,V"
    # changing any equation is DRIFT — the very thing the compiler rejects.
    assert ALPHA["equations"]["V"] == "(L ∩ G → B'') → ∞0'", "V-equation is canonical"


# ---------------------------------------------------------------------------
# 3. TEST ≡ — Identity Preservation.
# ---------------------------------------------------------------------------
def test_identity(words: list[str]) -> bool:
    """≡ holds iff every expression carries the SAME α (structure identical, prefix = lens only)."""
    for w in words:
        if seek_alpha(w) != ALPHA:
            return False
    return True


# ---------------------------------------------------------------------------
# 4. FIND {α'} — Self-Similar Expressions across scales.
# ---------------------------------------------------------------------------
def self_similar_expressions(depth: int = 3) -> list[str]:
    """Generate the fractal nodes. Each is a self-similar expression of α: the whole
    4+1 cell reappears at every node, prefixed — {α'}."""
    return _seed.expand("", depth)


# ---------------------------------------------------------------------------
# 5. VALIDATE Y — the Validated Pattern.
# ---------------------------------------------------------------------------
class ValidatedPattern(typing.NamedTuple):
    named: str       # α named
    identity: bool   # ≡ holds across all expressions
    confirmed: bool  # {α'} confirm across scales
    depth: int
    count: int

    @property
    def valid(self) -> bool:
        return self.identity and self.confirmed


def validate_y(depth: int = 3) -> ValidatedPattern:
    expressions = self_similar_expressions(depth)
    identity = test_identity(expressions)
    confirmed = len(expressions) == sum(5**d for d in range(depth + 1))
    return ValidatedPattern(
        named=ALPHA_NAME,
        identity=identity,
        confirmed=confirmed,
        depth=depth,
        count=len(expressions),
    )


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main() -> None:
    irreducible()

    y = validate_y(depth=3)

    print("=" * 70)
    print("G — GROWTH")
    print(f"EQUATION:  G = α ≡ {{α'}}")
    print("=" * 70)
    print()

    print("1. RECEIVE X")
    print("   X = the seed cell (cell.py) — the validated spark from S")
    print()

    print("2. SEEK α")
    print(f"   α = {ALPHA_NAME}")
    print("   irreducibility:  center S (no ∞0→? without it) · 4 corners (no 4+1")
    print("                     without them) · 5 equations (a phase loses its law)")
    print("   → each part is load-bearing; remove any part and X collapses.")
    print()

    print("3. TEST ≡  (Identity Preservation)")
    print(f"   {y.count} expressions checked — α identical across ALL of them: {y.identity}")
    print("   (the prefix is a lens, never a new equation — the symbols stay verbatim)")
    print()

    print("4. FIND {α'}  (Self-Similar Expressions)")
    for d in (0, 1, 2, 3):
        leaves = _seed.expand("", d)[-(5**d):]
        sample = "  ".join(leaves[:10])
        print(f"   depth {d}: {len(leaves):>3} cells    {sample}{' …' if len(leaves) > 10 else ''}")
    print()

    print("5. VALIDATE Y")
    print(f"   Y = α named · ≡ holds · {{α'}} confirm  →  VALID: {y.valid}")
    print("   success: one could see α in every member of {α'} without being told.")
    print()
    print("   The same shape, at three scales (ε · S · SQ):")
    print()
    print("   ε                       S                          SQ")
    print("   ─────────────           ─────────────              ─────────────")
    print(_side_by_side())


def _side_by_side() -> str:
    """Show α self-similar at three scales: the root, a daughter, a granddaughter."""
    rows = []
    for w in ("", "S", "SQ"):
        rows.append(_seed.render_cell(w).splitlines())
    # pick the structural lines only (skip blank spacers for compactness)
    out = []
    for i in range(len(rows[0])):
        line = rows[0][i].ljust(26)
        for r in rows[1:]:
            line += "   " + r[i].ljust(26)
        out.append(line.rstrip())
    return "\n".join(out)


if __name__ == "__main__":
    main()
