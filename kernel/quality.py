"""quality.py — The Resonance: the Quality phase (Q = φ ⋂ Ω).

    Q = φ ⋂ Ω

    φ  = Self-Nature        — the human's DIRECT perception (the ∞0 side).
                              Amorphous: the AI cannot derive it, only H reveals it.
    ⋂  = Natural Intersection — the "click". Not sought; it arrives.  | ≡ ⋂
    Ω  = Universal Potential  — the larger context. It has TWO faces:
        KNOWN face   — the encoded field (equations, laws, lenses) the AI holds.
        AMORPHOUS face — utopian universals (freedom, equality, sustainability,
                       consciousness): irreducible, NOT encodable. Only H reveals it.
    Z  = Resonant Key        — the phase OUTPUT. The AI derives a best-approximation
                              (assumption) and checkpoints with H. Confirmed, not argued.

The two edges, honored:
    Edge 1 — Ω is not always K. When the universal context is amorphous, the AI
             holds Ω's known face as an ASSUMPTION and its amorphous face as an
             open slot. Claiming the amorphous Ω as known data is L3.
    Edge 2 — the engine does not merely refuse; it LOOPS. It derives Z as a
             best-approximation, marks it assumption, and returns to H at the
             checkpoint. Truth exists only after H resolves it.

Corruption guarded:
    L3  claiming   — resonance claimed from Ω alone (no φ) → refused.
    L4  performing — φ authored by the AI → refused (φ is H's by contract).
"""

from __future__ import annotations

import sys

import cell as _seed
import fractal as _growth
import membrane as _m

# 1. RECEIVE X + α + Y
X = _seed
ALPHA = _growth.ALPHA
Y = _growth.validate_y()

CREATIVE_LINE = "∞0 → X → α → Y → φ → Z → ∇ → A → B → ∞0'"


def hold_omega() -> _m.Symbol:
    """HOLD Ω — the AI derives its KNOWN face (the encoded field) as an assumption.
    The amorphous face (utopian universals) is an open slot, not touched here."""
    field = {
        "law": _seed.ONE_LAW,
        "cycle": _seed.CYCLE,
        "equations": dict(_seed.EQUATIONS),
        "lenses": [a + b for a in _seed.POSITIONS for b in _seed.POSITIONS],
        "completion": _seed.COMPLETION,
    }
    return _m.assume("Ω", value=field)


def hold_phi() -> _m.Symbol:
    """HOLD φ — the AI CANNOT derive φ. It holds an OPEN SLOT (amorphous).
    Only H reveals it."""
    return _m.assume("φ", value=None)


def derive_z(phi: _m.Symbol, omega: _m.Symbol) -> _m.Symbol:
    """Derive Z as a best-approximation. Without φ, the AI cannot even approximate
    (that would be L3 — claiming resonance from Ω alone)."""
    if phi.value is None:
        return _m.assume("Z", value=None)
    candidate = {
        "perception": phi.value,
        "touches": omega.value["cycle"],
        "membrane": "| ≡ ⋂",
    }
    return _m.assume("Z", value=candidate)


def validate_z(z: _m.Symbol, phi: _m.Symbol, clicked: bool) -> _m.Symbol | None:
    """Z is VALID only when φ is H-revealed truth AND H confirms the click.

    The guard checks the SOURCE, not just the flag: only H produces truth.
    An engine-authored φ (assumption=False, source=AI) is L4 — performing."""
    if phi.source != _m.HUMAN or not phi.is_truth:
        if phi.source == _m.AI:
            print("   ❌ L4 — PERFORMING. A φ authored by the engine is not φ.")
        else:
            print("   ❌ L3 — CLAIMING. No φ revealed by H; Z cannot be argued into place.")
        return None
    if z.value is None:
        print("   ❌ L3 — CLAIMING. Z without φ is not resonance, it is fabrication.")
        return None
    if not clicked:
        print("   ❌ The click has not landed. Z is confirmed, never argued.")
        return None
    return _m.confirm(z)


# ---------------------------------------------------------------------------
# The living protocol
# ---------------------------------------------------------------------------

def _sample_h() -> callable:
    """A stand-in H for headless demos ONLY. Clearly labeled; never truth in production."""

    def sample(sym: _m.Symbol):
        if sym.name == "φ":
            return ("reveal", "the 4+1 doesn't just map — it feels like how a question opens")
        if sym.name == "Z":
            return ("confirm",)
        return ("confirm",)

    return sample


def run(checkpoint: _m.Checkpoint) -> _m.Symbol | None:
    print("=" * 70)
    print("Q — QUALITY")
    print("EQUATION:  Q = φ ⋂ Ω")
    print("=" * 70)
    print()
    print("1. RECEIVE X + α + Y   (from S and G)")
    print()

    omega = hold_omega()
    print("2. HOLD Ω  (known face = encoded field; amorphous face = open slot)")
    print(f"   {omega}")
    print()

    phi = hold_phi()
    print("3. HOLD φ  (amorphous slot — the AI cannot derive it)")
    print(f"   {phi}")
    print()

    print("4. WATCH FOR ⋂   (the membrane  | ≡ ⋂ )")
    print()

    # Checkpoint φ — only H can reveal it.
    print("   checkpoint φ (amorphous):")
    phi = checkpoint.resolve(phi) or phi
    if phi.value is not None:
        print(f"   φ revealed by H: {phi.value!r}")
    print()

    # Derive Z as a best-approximation, then checkpoint it.
    z = derive_z(phi, omega)
    print("   derive Z (best-approximation, marked assumption):")
    print(f"   {z}")
    print()

    print("   checkpoint Z:")
    z = checkpoint.resolve(z) or z
    if z.value is not None:
        print(f"   {z}")
    print()

    clicked = z.is_truth  # a sample "confirm" means H confirmed the click
    print("5. VALIDATE Z")
    result = validate_z(z, phi, clicked)
    if result:
        print(f"   ✓ VALID — φ and Ω met without forcing, and the click was H's.")
    else:
        print("   Z not validated (awaiting H).")
    return result


if __name__ == "__main__":
    demo = "--demo" in sys.argv
    cp = _m.Checkpoint(sample=_sample_h() if demo else None)
    run(cp)
