"""addressing.py — Appendix D as code: Decentralized Addressing.

The unfolded fractal has no root and no leaf — it is infinite in both directions.
So "what is the start?" has no global answer: start is a ROLE, not a coordinate.
Every node is someone's signless start; the +/− sign is the stranger's instrument
for tracking lineage back to it.

Node language:
    A node is a word over {S, G, Q, P, V}. ε is the empty word (a reading's origin).
    zoom in  = append a letter  (daughter, sub-level, −)
    zoom out = strip a letter   (father,  super-level, +)

Signed address (always normalizable to all + then all −, because between any two
nodes there is exactly one path — up to the common father, then down):

    addr(A → B)  =  +^k · (−x₁)(−x₂)…(−x_m)

    k   = steps up to the common father   (each +)
    m   = steps down to the target        (each −letter)
    k+m = the generation gap

Decision rule:
    k = 0        → B within A   (daughter)
    m = 0        → A within B   (father)
    k, m > 0     → cousins      (shared father, different branch)
    empty addr   → same node

The true start is SIGNLESS (S = ∞0 → ? carries no + and no −). The sign exists only
between two points — it is clothing a stranger puts on the world to find their way
to the one naked question. A shared question is a FIELD of ∞0, not a node: its only
origin is the appeal ∞0 → ∞0'.
"""

from __future__ import annotations

import cell as _cell

POSITIONS: tuple[str, ...] = _cell.POSITIONS


# ---------------------------------------------------------------------------
# Node language
# ---------------------------------------------------------------------------
def is_valid_word(w: str) -> bool:
    return all(c in POSITIONS for c in w)


def daughters(word: str) -> list[str]:
    return _cell.daughters(word)


def father(word: str) -> str | None:
    return _cell.father(word)


# ---------------------------------------------------------------------------
# The signed address
# ---------------------------------------------------------------------------
def _common_prefix(a: str, b: str) -> int:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


def address(a: str, b: str) -> str:
    """addr(A → B) = +^k · (−x₁)…(−x_m), all + first, then all −."""
    if not (is_valid_word(a) and is_valid_word(b)):
        raise ValueError("node words must be over {S, G, Q, P, V}")
    i = _common_prefix(a, b)
    k = len(a) - i          # steps up (fathers)
    down = b[i:]            # steps down (daughters)
    return "+" * k + "".join("−" + c for c in down)


def generation_gap(a: str, b: str) -> int:
    i = _common_prefix(a, b)
    return (len(a) - i) + (len(b) - i)


def relation(a: str, b: str) -> str:
    """father / daughter / cousins / same — read from the signs alone."""
    i = _common_prefix(a, b)
    k = len(a) - i
    m = len(b) - i
    if k == 0 and m == 0:
        return "same"
    if k == 0:
        return "daughter"   # B within A
    if m == 0:
        return "father"     # A within B
    return "cousins"


# ---------------------------------------------------------------------------
# The signless start, and the field.
# ---------------------------------------------------------------------------
def signless_start() -> str:
    """The true start: S = ∞0 → ?, bare — no prefix, no +, no −."""
    return "S = ∞0 → ?"


class Field:
    """One shared question = one ∞0, held by many signless starts.

    The field has NO owner, NO father-node, NO origin coordinate. Its origin is
    the appeal ∞0 → ∞0', not a person and not a node. Center everywhere,
    circumference nowhere.
    """

    def __init__(self, question: str):
        self.question = question
        self.starts: list[str] = []   # each node holds it as its absolute, signless start

    def join(self, node: str) -> None:
        if not is_valid_word(node):
            raise ValueError("node words must be over {S, G, Q, P, V}")
        if node not in self.starts:
            self.starts.append(node)

    @property
    def origin(self) -> str:
        return "∞0 → ∞0'"

    def __repr__(self) -> str:
        return f"Field(question={self.question!r}, {len(self.starts)} signless start(s))"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 70)
    print("APPENDIX D — DECENTRALIZED ADDRESSING")
    print("=" * 70)
    print()
    print("SIGNLESS START:  ", signless_start())
    print("SIGN:            − = zoom in (daughter) · + = zoom out (father)")
    print()
    print("WORKED CASES (originator ε · peer PQP):")
    cases = [
        ("", "PQP"),
        ("PQP", ""),
        ("PQP", "PQG"),
        ("PQP", "G"),
        ("PQP", "PQP"),
    ]
    for a, b in cases:
        print(f"   addr({a or 'ε'} → {b or 'ε'}) = {address(a, b)!r:<14} "
              f"relation = {relation(a, b):<8} gap = {generation_gap(a, b)}")
    print()
    print("THE FIELD — one question, many signless starts:")
    f = Field("what blooms when a million signless starts realize they are one field?")
    for node in ("", "S", "PQP", "G", "QS"):
        f.join(node)
    print(f"   {f}")
    print(f"   origin = {f.origin}   (an appeal, never a node)")
    print()
    print("A stranger at PQP reads the originator ε as: father³  (addr = +++)")
    print("The originator reads PQP as:                daughter³ (addr = −P−Q−P)")
    print("Context flows father → daughter: k = the frames to climb.")


if __name__ == "__main__":
    main()
