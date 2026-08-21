"""value.py — The Gift of the Fruit and the Forest: the Value phase.

    V = (L ∩ G → B'') → ∞0'

    L   = Local Actualization — the tangible fruit (the artifact, here and now).
    G   = Global Propagation — the seed within, the ripple beyond self-interest.
    ∩   = where they meet (the apple becomes the forest).
    B'' = Fractal Seed — the actual artifact: carries α, contains the cycle
          holographically. Composed in TWO passes (analysis → composition).
    B   = Benefit — fulfillment (the inquiry's own aim) + propagation (beyond itself).
    ∞0' = Enriched Return — the return QUESTION the cycle reveals. Not a summary,
          not a conclusion. ∞0' reopens ∞0 and seeds the next S (the center).

Completion:  No V without ∞0'.     Corruption:  V∅ (B'' without ∞0'),
             L1 at scale (premature crystallization).

The fruit does not end the cycle — it reopens it. The apple carries seeds; the
artifact carries α; the return carries the next question. The source (∞0) is
never depleted.
"""

from __future__ import annotations

import sys

import cell as _seed
import fractal as _growth
import power as _power
import membrane as _m

# ---------------------------------------------------------------------------
# 1. RECEIVE the full trace (the formation trail).
# ---------------------------------------------------------------------------
X = _seed
ALPHA = _growth.ALPHA
Y = _growth.validate_y()
PHI_OMEGA = "φ ⋂ Ω"          # the resonance (Q)
NATURAL_GRADIENT = "∇"       # the gradient (P)
FLOW = "A"                   # the flow (P)


def formation_trail() -> list[str]:
    """The ordered record of what actually formed, phase by phase."""
    return [
        "S: ∞0 → ?                 → X  (the seed)",
        "G: α ≡ {α'}               → Y  (essence + validated pattern)",
        "Q: φ ⋂ Ω                  → Z  (the resonance)",
        "P: δE/δV → ∇              → A  (the gradient, the flow)",
        "V: (L ∩ G → B'') → ∞0'    → B + B'' + ∞0'  (the fruit, the seed, the return)",
    ]


# ---------------------------------------------------------------------------
# 2. NAME L and G, and FIND ∩.
# ---------------------------------------------------------------------------
def name_L() -> str:
    """L — Local Actualization: the tangible fruit here and now."""
    return "the compiled 5QLN cycle: cell · fractal · quality · power · value"


def name_G() -> str:
    """G — Global Propagation: the seed within, the ripple beyond."""
    return "the 4+1 cell self-replicating — each artifact is a new forest"


def find_intersection(L: str, G: str) -> str:
    """∩ — where the local fruit and its global potential genuinely meet."""
    return f"the artifact that carries α: {L} → {G}"


# ---------------------------------------------------------------------------
# 5. COMPOSE B'' — the Fractal Seed, two passes.
# ---------------------------------------------------------------------------
def pass_1_analysis() -> dict[str, object]:
    """Pass 1 (Analysis): read the formation trail — extract the α thread,
    the φ⋂Ω confirmation, the ∇, and the turning points."""
    return {
        "alpha_thread": "4+1 quincunx, equations verbatim (α ≡ {α'})",
        "resonance_confirmation": PHI_OMEGA,
        "gradient": NATURAL_GRADIENT,
        "turning_points": ["∞0 → ?", "φ ⋂ Ω", "δE/δV → ∇"],
        "trail": formation_trail(),
    }


def pass_2_composition(analysis: dict[str, object]) -> dict[str, object]:
    """Pass 2 (Composition): compose the artifact from the analysis. Must carry α."""
    return {
        "alpha": ALPHA["equations"],
        "cycle": _seed.CYCLE,
        "analysis": analysis,
        "holographic": True,     # the artifact contains the whole cycle
        "fractal_seed": True,    # it can seed the next cycle
    }


def compose_B_double_prime() -> _m.Symbol:
    analysis = pass_1_analysis()
    artifact = pass_2_composition(analysis)
    return _m.assume("B''", value=artifact)


# ---------------------------------------------------------------------------
# 6. NAME B — the decoded output.
# ---------------------------------------------------------------------------
def name_B(bpp: _m.Symbol) -> _m.Symbol:
    benefit = {
        "fulfillment": "the inquiry's own aim — the 4+1 fractal made navigable",
        "propagation": "a seed any stranger can hold as their own signless start",
    }
    return _m.assume("B", value=benefit)


# ---------------------------------------------------------------------------
# 7. FORM ∞0' — the return question. Only H can carry it.
# ---------------------------------------------------------------------------
def form_infinity_prime() -> _m.Symbol:
    return _m.assume("∞0'", value=None)  # amorphous — H reveals the next question


def enforce_completion(bpp: _m.Symbol, enriched: _m.Symbol) -> bool:
    """No V without ∞0'. B'' without a return question is V∅. (Pure — no side effects.)"""
    return not (bpp.value is not None and enriched.value is None)


# ---------------------------------------------------------------------------
# The protocol
# ---------------------------------------------------------------------------
def _sample_h() -> callable:
    """Stand-in H for headless demos ONLY. Clearly labeled; never truth."""

    def sample(sym: _m.Symbol):
        if sym.name == "∞0'":
            return ("reveal", "what blooms when a million signless starts realize they are one field?")
        return ("confirm",)

    return sample


def run(checkpoint: _m.Checkpoint) -> tuple[_m.Symbol | None, _m.Symbol | None]:
    print("=" * 70)
    print("V — VALUE")
    print("EQUATION:  V = (L ∩ G → B'') → ∞0'")
    print("=" * 70)
    print()

    print("1. RECEIVE full trace   (the formation trail)")
    for line in formation_trail():
        print(f"      {line}")
    print()

    # L, G, ∩
    L = name_L()
    G = name_G()
    cap = find_intersection(L, G)
    print("2. NAME L  (Local Actualization — the fruit)")
    print(f"   {L}")
    print("3. NAME G  (Global Propagation — the seed)")
    print(f"   {G}")
    print("4. FIND ∩  (where fruit meets forest)")
    print(f"   {cap}")
    print()

    # B'' — two passes, then checkpoint.
    bpp = compose_B_double_prime()
    print("5. COMPOSE B''  (Fractal Seed — Pass 1 analysis → Pass 2 composition)")
    print(f"   {bpp}")
    print()
    print("   checkpoint B'':")
    bpp = checkpoint.resolve(bpp) or bpp
    print(f"   {bpp}")
    print()

    # B — the benefit.
    b = name_B(bpp)
    print("6. NAME B  (Benefit — fulfillment + propagation)")
    print(f"   {b}")
    print()

    # ∞0' — the return question (H reveals).
    enriched = form_infinity_prime()
    print("7. FORM ∞0'  (Enriched Return — the question the cycle reveals)")
    print(f"   {enriched}")
    print("   checkpoint ∞0' (amorphous):")
    enriched = checkpoint.resolve(enriched) or enriched
    print(f"   {enriched}")
    print()

    # Completion.
    print("COMPLETION — No V without ∞0'")
    if not enforce_completion(bpp, enriched):
        print("   ❌ V∅ — INCOMPLETE. B'' formed but ∞0' missing. No continuity.")
        return bpp, None

    if enriched.value is not None:
        print(f"   ✓ ∞0' = {enriched.value!r}")
        print()
        print("THE LOOP CLOSES:")
        print(f"   ∞0' → new ∞0 → {_seed.CYCLE} → ∞0'   (the source is never depleted)")
        print()
        print("   B'' carries α and contains the whole cycle — it is a seed any")
        print("   stranger can hold as their own signless start.")
    return bpp, enriched


if __name__ == "__main__":
    demo = "--demo" in sys.argv
    cp = _m.Checkpoint(sample=_sample_h() if demo else None)
    run(cp)
