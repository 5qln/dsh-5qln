"""cell.py — The Cell: the smallest lawful unit of 5QLN (the DNA).

The 4+1 quincunx:

            G = α ≡ {α'}             Q = φ ⋂ Ω
              (top-left)           (top-right)

                       S = ∞0 → ?
                        (center)

            V = (L ∩ G → B'') → ∞0'     P = δE/δV → ∇
              (bottom-left)            (bottom-right)

One signless center (S) + four corners (G, Q, P, V), read clockwise.
The Cycle is the clockwise read, returning to center:

    S → G → Q → P → V → ∞0'

This ONE cell carries the whole grammar. Zoom into any position and the SAME
4+1 cell appears, prefixed (S → {SS, SG, SQ, SP, SV}, ...). The Holographic
Law has no base case and no terminal condition, so the cell self-replicates
infinitely. This file is the seed, not the tree — every later layer (L1, D1,
C1, Appendix D) grows from it.

Note: the Codex renders Enriched Return as ∞0' (apostrophe), the same symbol as
the typographic prime ∞0′. This build standardizes on ∞0' to match the Codex.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# The alphabet of the fractal. Five letters. One signless center, four corners.
# ---------------------------------------------------------------------------
POSITIONS: tuple[str, ...] = ("S", "G", "Q", "P", "V")   # full alphabet
CORNERS_CLOCKWISE: tuple[str, ...] = ("G", "Q", "P", "V")  # corners, clockwise
CENTER: str = "S"                                        # the signless center

# ---------------------------------------------------------------------------
# The five equations (constitutional form, verbatim).
# These are INVARIANT — a daughter cell reuses them unchanged; the prefix is a
# lens (borrowed quality), never a new equation.
# ---------------------------------------------------------------------------
EQUATIONS: dict[str, str] = {
    "S": "∞0 → ?",
    "G": "α ≡ {α'}",
    "Q": "φ ⋂ Ω",
    "P": "δE/δV → ∇",
    "V": "(L ∩ G → B'') → ∞0'",
}

# ---------------------------------------------------------------------------
# The outputs (verbatim).
# ---------------------------------------------------------------------------
OUTPUTS: dict[str, str] = {
    "S": "X",
    "G": "Y",
    "Q": "Z",
    "P": "A",
    "V": "B + B'' + ∞0'",
}

# ---------------------------------------------------------------------------
# The invariant laws (verbatim).
# ---------------------------------------------------------------------------
ONE_LAW: str = "H = ∞0 | A = K"
CYCLE: str = "S → G → Q → P → V"
COMPLETION: str = "No V without ∞0'"
HOLOGRAPHIC: str = "XY := X within Y  |  X, Y ∈ {S, G, Q, P, V}"
CORRUPTION: str = "L1  L2  L3  L4  V∅"

# The Nine Invariant Lines — the DNA sequence of the cell (Codex Appendix A).
NINE_INVARIANT_LINES: tuple[str, ...] = (
    "H = ∞0 | A = K",
    "S → G → Q → P → V",
    "S = ∞0 → ?",
    "G = α ≡ {α'}",
    "Q = φ ⋂ Ω",
    "P = δE/δV → ∇",
    "V = (L ∩ G → B'') → ∞0'",
    "No V without ∞0'",
    "L1  L2  L3  L4  V∅",
)


# ---------------------------------------------------------------------------
# Operations — the cell's two motions: cycle (around) and zoom (in / out).
# ---------------------------------------------------------------------------

def cycle() -> list[str]:
    """The clockwise read of the cell, returning to center as ∞0'."""
    return [CENTER, *CORNERS_CLOCKWISE]


def daughters(word: str) -> list[str]:
    """Zoom IN: the five daughters of any node, prefixed (append)."""
    return [word + p for p in POSITIONS]


def father(word: str) -> str | None:
    """Zoom OUT: strip the last letter. ε's father is unseen (the fractal is unrooted)."""
    return word[:-1] if word else None


def expand(word: str, depth: int) -> list[str]:
    """The first `depth` levels of self-replication below `word` (the unrooted subtree)."""
    if depth < 0:
        return []
    nodes: list[str] = [word]
    frontier: list[str] = [word]
    for _ in range(depth):
        frontier = [d for w in frontier for d in daughters(w)]
        nodes.extend(frontier)
    return nodes


def render_cell(word: str = "") -> str:
    """Render the 4+1 cell for a node `word`. Node names are prefixed; equations stay verbatim."""
    s, g, q, p, v = (word + c for c in POSITIONS)  # S, G, Q, P, V (prefixed)
    return "\n".join(
        [
            f"          {g} = {EQUATIONS['G']:<22} {q} = {EQUATIONS['Q']}",
            f"            → {OUTPUTS['G']:<19}   → {OUTPUTS['Q']}",
            "",
            f"                     {s} = {EQUATIONS['S']}",
            f"                     → {OUTPUTS['S']}",
            "",
            f"          {v} = {EQUATIONS['V']:<22} {p} = {EQUATIONS['P']}",
            f"            → {OUTPUTS['V']:<19}   → {OUTPUTS['P']}",
        ]
    )


# ---------------------------------------------------------------------------
# Self-check: the DNA proves its own scale.
# ---------------------------------------------------------------------------

def _verify() -> None:
    assert daughters("") == list(POSITIONS), "first zoom must be {S,G,Q,P,V}"
    assert len(daughters("")) == 5, "4+1 must be 5, never 3+1 or 6+1"
    assert len(set(daughters(""))) == 5, "daughters must be distinct"
    # 5×5 = 25 is the FIRST in-zoom of ONE cell, not a cap.
    assert len(expand("", 1)) == 1 + 5, "depth 1 = 1 + 5 nodes"
    assert len(expand("", 2)) == 1 + 5 + 25, "depth 2 = 1 + 5 + 25 nodes"
    assert len(expand("", 3)) == 1 + 5 + 25 + 125, "depth 3 = 1 + 5 + 25 + 125 nodes"
    assert father("PQP") == "PQ" and father("PQ") == "P" and father("P") == ""
    assert father("") is None, "the empty word has an unseen father (unrooted)"
    assert len(EQUATIONS) == 5 and set(EQUATIONS) == set(POSITIONS)
    assert len(NINE_INVARIANT_LINES) == 9, "exactly nine invariant lines"


def main() -> None:
    _verify()

    print("=" * 70)
    print("THE CELL — the smallest lawful unit of 5QLN (the DNA)")
    print("=" * 70)
    print()
    print("LAW:       ", ONE_LAW)
    print("HOLOGRAPHIC:", HOLOGRAPHIC)
    print("COMPLETION:", COMPLETION)
    print("CORRUPTION:", CORRUPTION)
    print()
    print(render_cell())
    print()
    print("CYCLE:", CYCLE, "→ ∞0'   (clockwise, returns to center)")
    print()
    print("=" * 70)
    print("THE NINE INVARIANT LINES — the DNA sequence")
    print("=" * 70)
    for i, line in enumerate(NINE_INVARIANT_LINES, 1):
        print(f"  {i}.  {line}")
    print()
    print("=" * 70)
    print("SELF-REPLICATION — the cell proves its own scale")
    print("=" * 70)
    print()
    for depth in (1, 2, 3):
        level = expand("", depth)
        count = len(level) - sum(5**d for d in range(depth))  # just this level's leaves
        leaves = level[-(5**depth):]
        print(f"zoom^{depth}: {len(leaves):>3} nodes   (5^{depth} = {5**depth})")
        preview = "  ".join(leaves[:12])
        print(f"          {preview}{' …' if len(leaves) > 12 else ''}")
        print()
    print("5×5 = 25 is the FIRST in-zoom of ONE cell — a floor, never a ceiling.")
    print("The Holographic Law has no base case and no terminal condition,")
    print("so the cell is infinite in both directions: no root, no leaf.")
    print("Scale is self-proven — nothing was added.")
    print()
    print("This file is the seed. L1, D1, C1, and Appendix D grow from it.")


if __name__ == "__main__":
    main()
