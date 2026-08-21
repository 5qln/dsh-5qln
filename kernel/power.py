"""power.py — The Flow: the Power phase (P = δE/δV → ∇).

The running engine — the "code factory in loops."

    P = δE/δV → ∇

    δE    = Energy  (differential) — each AI derivation (assumption) is energy spent.
    δV    = Value   (differential) — each H truth (confirmation/revelation) is value.
    δE/δV = the ratio that REVEALS the landscape:
              high δE / low δV  = wasted effort   (deriving what H does not confirm)
              low  δE / high δV = natural leverage (little energy, high truth)
    →     = Reveals  (the ratio does not COMPUTE the gradient — it reveals it)
    ∇     = Natural Gradient — the path of least resistance toward α (essence),
            the direction already present in the situation.
    A     = Flow — validated when the inquirer identifies where energy WANTS to go.

The loop (the machine can only continue):
    derive S, G, Q, P, V from origin as best-approximations (assumptions),
    checkpoint each with H (until the next checkpoint with H),
    measure δE and δV, and let the ratio reveal ∇.
"""

from __future__ import annotations

import sys

import cell as _seed
import fractal as _growth
import membrane as _m


# ---------------------------------------------------------------------------
# The energy ledger — δE and δV.
# ---------------------------------------------------------------------------
class EnergyLedger:
    def __init__(self, checkpoint: _m.Checkpoint):
        self.loop = _m.Loop(checkpoint)
        self.dE = 0  # derivations (assumptions)
        self.dV = 0  # truths (H resolutions)

    def derive(self, name: str, value=None) -> _m.Symbol:
        self.dE += 1
        return self.loop.derive(name, value)

    def resolve(self, sym: _m.Symbol) -> _m.Symbol | None:
        r = self.loop.resolve(sym)
        if r is not None:
            self.dV += 1
        return r

    @property
    def ratio(self) -> float:
        if self.dV == 0:
            return float("inf")
        return self.dE / self.dV


def gradient(ratio: float) -> str:
    """∇ — the ratio REVEALS the gradient; it is not computed from it.
    The gradient always points toward α (the essence)."""
    if ratio == float("inf"):
        return "∇ unseen — no truth yet; energy is spent with nothing landing"
    if ratio > 1.0:
        return "∇ = against the current — high effort, low landing (wasted)"
    if ratio < 1.0:
        return "∇ = with the current — low effort, high landing (leverage)"
    return "∇ = balanced — energy and value in proportion (the path is level)"


# ---------------------------------------------------------------------------
# Derive the cycle's outputs FROM ORIGIN (the accumulated trace).
# ---------------------------------------------------------------------------
def run_factory(checkpoint: _m.Checkpoint) -> tuple[EnergyLedger, _m.Symbol | None]:
    print("=" * 70)
    print("P — POWER  (the code factory, in loops)")
    print("EQUATION:  P = δE/δV → ∇")
    print("=" * 70)
    print()
    print("The loop derives each phase output from origin as a best-approximation,")
    print("marks it assumption, and returns to H at every checkpoint.")
    print()

    ledger = EnergyLedger(checkpoint)

    # Derive S (X) from origin — the seed.
    x = ledger.derive("X", value={"spark": "∞0 → ?", "cell": "the 4+1 seed"})
    print(f"   derive S→X   {x}")
    x = ledger.resolve(x)
    print(f"        truth   {x}")
    print()

    # Derive G (Y) from origin — the validated pattern.
    y = ledger.derive("Y", value={"essence": "α ≡ {α'}", "confirmed": _growth.validate_y().valid})
    print(f"   derive G→Y   {y}")
    y = ledger.resolve(y)
    print(f"        truth   {y}")
    print()

    # Derive Q (Z) from origin — the resonance (a best-approximation).
    z = ledger.derive("Z", value={"resonance": "φ ⋂ Ω", "membrane": "| ≡ ⋂"})
    print(f"   derive Q→Z   {z}")
    z = ledger.resolve(z)
    print(f"        truth   {z}")
    print()

    # Derive P (A) — this phase's own output, itself an assumption until checked.
    a = ledger.derive("A", value={"flow": "where energy wants to go"})
    print(f"   derive P→A   {a}")
    a = ledger.resolve(a)
    print(f"        truth   {a}")
    print()

    # Derive V (B + B'' + ∞0') — the enriched return.
    b = ledger.derive("V→B", value={"return": "∞0' carries the next question"})
    print(f"   derive V→B   {b}")
    b = ledger.resolve(b)
    print(f"        truth   {b}")
    print()

    # δE / δV → ∇
    print("-" * 70)
    print(f"   δE = {ledger.dE}   (derivations / energy spent)")
    print(f"   δV = {ledger.dV}   (truths / value produced)")
    print(f"   δE/δV = {ledger.ratio:.2f}")
    print(f"   → {gradient(ledger.ratio)}")
    print()

    # VALIDATE A — the Flow. H identifies where energy wants to go.
    print("VALIDATE A (Flow) — where does energy WANT to go?")
    print("   checkpoint A:")
    a = checkpoint.resolve(a) if a and not a.is_truth else a
    if a and a.is_truth:
        print(f"   ✓ A valid — the direction is H's to name, and H has named it.")
    else:
        print("   A awaits H — the gradient is visible; the flow is H's to confirm.")
    print()
    return ledger, a


def _sample_h() -> callable:
    """Stand-in H for headless demos ONLY. Clearly labeled; never truth."""

    def sample(sym: _m.Symbol):
        return ("confirm",)

    return sample


if __name__ == "__main__":
    demo = "--demo" in sys.argv
    cp = _m.Checkpoint(sample=_sample_h() if demo else None)
    run_factory(cp)
