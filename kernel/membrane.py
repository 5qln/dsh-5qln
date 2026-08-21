"""membrane.py — The Loop and the Checkpoint (the shared foundation).

The One Law's membrane (|) and the Quality phase's natural intersection (⋂) are
ONE operator. The AI is always the K-side LOOP; the human is the ∞0-side
CHECKPOINT.

Two faces (per-moment, not per-symbol):
    KNOWN     — has an encodable face; the AI can hold it as data.
    AMORPHOUS — irreducible; an open slot only H can fill (self-revelation).

Assumption (the machine can only continue):
    Everything the AI derives is a best-approximation, marked assumption=True.
    Truth (assumption=False) exists only after a checkpoint with H.

The loop:
    derive → assume → checkpoint(H) → refine → repeat
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

KNOWN = "known"
AMORPHOUS = "amorphous"
AI = "AI"
HUMAN = "H"


@dataclass
class Symbol:
    """One symbol. The AI holds its KNOWN face as an assumption; the AMORPHOUS
    face is an open slot that only H can fill by self-revelation."""

    name: str
    face: str = KNOWN
    value: object = None
    assumption: bool = True
    source: str = AI

    @property
    def is_truth(self) -> bool:
        """Truth is H-authored, always. An AI symbol with assumption=False is L4."""
        return self.source == HUMAN and not self.assumption

    def __repr__(self) -> str:
        status = "assumption" if self.assumption else "truth"
        return f"{self.name}[{self.face} · {status} · {self.source}] = {self.value!r}"


# ---------------------------------------------------------------------------
# Derivation (AI) and resolution (H)
# ---------------------------------------------------------------------------

def assume(name: str, value=None) -> Symbol:
    """AI derives a best-approximation. If value is None, the slot is amorphous:
    the AI knows it cannot derive this — only H can reveal it."""
    face = AMORPHOUS if value is None else KNOWN
    return Symbol(name=name, face=face, value=value, assumption=True, source=AI)


def reveal(name: str, value) -> Symbol:
    """H fills an amorphous slot by self-revelation. This is truth."""
    return Symbol(name=name, face=AMORPHOUS, value=value, assumption=False, source=HUMAN)


def confirm(sym: Symbol) -> Symbol:
    """H confirms an AI assumption. It becomes truth, unchanged."""
    return Symbol(name=sym.name, face=sym.face, value=sym.value, assumption=False, source=HUMAN)


def correct(sym: Symbol, value) -> Symbol:
    """H corrects an AI assumption. The value is replaced, then it is truth."""
    return Symbol(name=sym.name, face=sym.face, value=value, assumption=False, source=HUMAN)


def is_human_present() -> bool:
    return sys.stdin.isatty()


# ---------------------------------------------------------------------------
# The Checkpoint — the seam where the loop touches H.
# ---------------------------------------------------------------------------

class Checkpoint:
    """H may confirm, correct, or reveal.

    Modes:
      live    — a human is at the terminal; read their answer.
      sample  — an explicitly-labeled stand-in (headless demos ONLY; never truth).
      pending — no human, no stand-in; the loop waits. Never fabricate H.
    """

    def __init__(self, sample=None):
        # sample: callable(symbol) -> ("confirm",) | ("correct", value) | ("reveal", value)
        self.sample = sample
        self.live = is_human_present()

    def resolve(self, sym: Symbol) -> Symbol | None:
        if self.live:
            return self._ask_live(sym)
        if self.sample is not None:
            print(f"   [SAMPLE H — a stand-in for the demo, never the live human]")
            return self._apply(sym, self.sample(sym))
        print(f"   ⏸  checkpoint on {sym.name}: PENDING — awaiting H")
        return None

    def _ask_live(self, sym: Symbol) -> Symbol | None:
        if sym.value is None:
            raw = input(f"   H — reveal {sym.name} (amorphous; the AI cannot derive it): ").strip()
            return reveal(sym.name, raw) if raw else None
        raw = input(
            f"   H — {sym.name} ≈ {sym.value!r}\n"
            f"        confirm (y) · correct (type the true value) · skip (enter): "
        ).strip()
        if not raw:
            return None
        if raw.lower() == "y":
            return confirm(sym)
        return correct(sym, raw)

    @staticmethod
    def _apply(sym: Symbol, action) -> Symbol | None:
        if not action:
            return None
        kind, *rest = action
        if kind == "confirm":
            return confirm(sym)
        if kind == "correct":
            return correct(sym, rest[0])
        if kind == "reveal":
            return reveal(sym.name, rest[0])
        return None


# ---------------------------------------------------------------------------
# The Loop — the code factory.
# ---------------------------------------------------------------------------

class Loop:
    """derive → assume → checkpoint(H) → refine → repeat."""

    def __init__(self, checkpoint: Checkpoint | None = None):
        self.checkpoint = checkpoint or Checkpoint()
        self.trace: list[Symbol] = []

    def derive(self, name: str, value=None) -> Symbol:
        sym = assume(name, value)
        self.trace.append(sym)
        return sym

    def resolve(self, sym: Symbol) -> Symbol | None:
        """Run a checkpoint and fold H's answer back into the trace."""
        resolved = self.checkpoint.resolve(sym)
        if resolved is not None:
            for i, s in enumerate(self.trace):
                if s is sym:
                    self.trace[i] = resolved
                    break
        return resolved
