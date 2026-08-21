"""cycle.py — The Compiled Surface: the full cycle, one sitting.

    S → G → Q → P → V → ∞0'

Emits the Constitutional Block, then runs all five phases in order with ONE
shared checkpoint (the human at the terminal). Ends with the Nine Invariant
Lines and the loop closing: ∞0' → new ∞0.

Usage:
    python3 cycle.py            # honest: checkpoints PENDING, never fabricates H
    python3 cycle.py --demo     # sample-H stand-in (clearly labeled), full loop
"""

from __future__ import annotations

import sys

import cell as _cell
import fractal as _fractal
import quality as _quality
import power as _power
import value as _value
import membrane as _m

CONSTITUTIONAL_BLOCK = """LAW:         H = ∞0 | A = K
CYCLE:       S → G → Q → P → V
EQUATIONS:
S = ∞0 → ?
G = α ≡ {α'}
Q = φ ⋂ Ω
P = δE/δV → ∇
V = (L ∩ G → B'') → ∞0'
OUTPUTS:     S→X  G→Y  Q→Z  P→A  V→B+B''+∞0'
HOLOGRAPHIC: XY := X within Y  |  X, Y ∈ {S, G, Q, P, V}
COMPLETION:  No V without ∞0'
CORRUPTION:  L1 L2 L3 L4 V∅
CENTER:      not a sixth phase — coherence only"""


def emit_block() -> None:
    print("=" * 70)
    print("5QLN — COMPILED SURFACE")
    print("=" * 70)
    print(CONSTITUTIONAL_BLOCK)
    print()
    print("(∞0' and ∞0' are the same symbol — Enriched Return.)")
    print()


def run(checkpoint: _m.Checkpoint) -> None:
    emit_block()

    # ── S → X (Start) ──
    _cell._verify()
    print("── S → X  (Start)")
    print("   X = the seed cell — 4+1, equations verbatim. VERIFIED.")
    print()

    # ── G → Y (Growth) ──
    y = _fractal.validate_y()
    print("── G → Y  (Growth)")
    print(f"   Y = validated pattern — α named, ≡ holds, {{α'}} confirm across {y.count} expressions.")
    print()

    # ── Q → Z (Quality) ──
    _quality.run(checkpoint)

    # ── P → A (Power) ──
    _power.run_factory(checkpoint)

    # ── V → B + B'' + ∞0' (Value) ──
    _value.run(checkpoint)

    # ── closing ──
    print("=" * 70)
    print("THE NINE INVARIANT LINES")
    print("=" * 70)
    for i, line in enumerate(_cell.NINE_INVARIANT_LINES, 1):
        print(f"  {i}.  {line}")
    print()
    import compiler as _compiler
    rules_ok = all(ok for _, _, (ok, _msg) in _compiler.rule_checks())
    validation_ok = not (_compiler.syntax_check() or _compiler.semantic_check() or _compiler.drift_check())
    verdict = "ZERO DRIFT" if (rules_ok and validation_ok) else "DRIFT DETECTED"
    print(f"COMPILER: {verdict} — R1–R13 {'clean' if rules_ok else 'FAIL'} · "
          f"syntax/semantic/drift {'clean' if validation_ok else 'FAIL'} · "
          f"fingerprint {_compiler.fingerprint()}")
    print("B'' is the fractal seed; ∞0' is the question only H can carry.")


def _sample_h() -> callable:
    def sample(sym: _m.Symbol):
        if sym.name == "φ":
            return ("reveal", "the 4+1 doesn't just map — it feels like how a question opens")
        if sym.name == "∞0'":
            return ("reveal", "what blooms when a million signless starts realize they are one field?")
        return ("confirm",)

    return sample


if __name__ == "__main__":
    demo = "--demo" in sys.argv
    cp = _m.Checkpoint(sample=_sample_h() if demo else None)
    run(cp)
