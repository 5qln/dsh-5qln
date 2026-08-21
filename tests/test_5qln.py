"""tests/test_5qln.py — the spec as its own test suite.

Locks every invariant of the 5QLN build: the nine invariant lines, the five
equations verbatim, the corruption taxonomy, the 4+1 cell and its self-replication,
the compiler's R1–R13 + validation, the signed addressing, and the membrane's
corruption guards.

Run:
    python3 tests/test_5qln.py
    python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "kernel"))

import addressing
import cell
import compiler
import fractal
import membrane as m
import power
import quality
import value


class TestNineInvariantLines(unittest.TestCase):
    def test_nine_lines_exactly(self):
        self.assertEqual(len(cell.NINE_INVARIANT_LINES), 9)
        self.assertEqual(cell.NINE_INVARIANT_LINES, compiler.NINE_INVARIANT_LINES)

    def test_one_law(self):
        self.assertEqual(cell.ONE_LAW, "H = ∞0 | A = K")

    def test_cycle(self):
        self.assertEqual(cell.CYCLE, "S → G → Q → P → V")

    def test_five_equations_verbatim(self):
        for p, eq in compiler.EQUATIONS.items():
            self.assertEqual(cell.EQUATIONS[p], eq, f"drift in {p}")

    def test_corruption_exactly_five(self):
        self.assertEqual(cell.CORRUPTION.split(), ["L1", "L2", "L3", "L4", "V∅"])

    def test_fingerprint_stable(self):
        self.assertEqual(compiler.fingerprint(), compiler.fingerprint())
        self.assertEqual(len(compiler.fingerprint()), 16)


class TestCell(unittest.TestCase):
    def test_four_plus_one(self):
        self.assertEqual(len(cell.POSITIONS), 5)
        self.assertEqual(cell.CENTER, "S")
        self.assertEqual(cell.CORNERS_CLOCKWISE, ("G", "Q", "P", "V"))

    def test_first_zoom(self):
        self.assertEqual(cell.daughters(""), ["S", "G", "Q", "P", "V"])

    def test_self_replication(self):
        self.assertEqual(len(cell.expand("", 1)), 1 + 5)
        self.assertEqual(len(cell.expand("", 2)), 1 + 5 + 25)
        self.assertEqual(len(cell.expand("", 3)), 1 + 5 + 25 + 125)

    def test_father_strips(self):
        self.assertEqual(cell.father("PQP"), "PQ")
        self.assertEqual(cell.father("P"), "")
        self.assertIsNone(cell.father(""))


class TestFractal(unittest.TestCase):
    def test_essence_identity(self):
        # α is identical under every lens prefix (≡ holds).
        for w in ("", "S", "SQ", "PQP", "GSS"):
            self.assertEqual(fractal.seek_alpha(w), fractal.ALPHA, f"≡ broken at {w!r}")

    def test_validated_pattern(self):
        y = fractal.validate_y(depth=3)
        self.assertTrue(y.valid)
        self.assertEqual(y.count, 1 + 5 + 25 + 125)

    def test_irreducible(self):
        fractal.irreducible()  # raises AssertionError if α is not load-bearing


class TestCompiler(unittest.TestCase):
    def test_all_rules_pass(self):
        for code, desc, (ok, msg) in compiler.rule_checks():
            self.assertTrue(ok, f"{code} failed: {msg}")

    def test_validation_clean(self):
        self.assertEqual(compiler.syntax_check(), [])
        self.assertEqual(compiler.semantic_check(), [])
        self.assertEqual(compiler.drift_check(), [])

    def test_compile_surface_zero_drift(self):
        self.assertTrue(compiler.compile_surface(emit=False))


class TestAddressing(unittest.TestCase):
    def test_worked_cases(self):
        self.assertEqual(addressing.address("", "PQP"), "−P−Q−P")
        self.assertEqual(addressing.address("PQP", ""), "+++")
        self.assertEqual(addressing.address("PQP", "PQG"), "+−G")
        self.assertEqual(addressing.address("PQP", "G"), "+++−G")
        self.assertEqual(addressing.address("PQP", "PQP"), "")

    def test_relations(self):
        self.assertEqual(addressing.relation("", "PQP"), "daughter")
        self.assertEqual(addressing.relation("PQP", ""), "father")
        self.assertEqual(addressing.relation("PQP", "PQG"), "cousins")
        self.assertEqual(addressing.relation("PQP", "PQP"), "same")

    def test_generation_gap(self):
        self.assertEqual(addressing.generation_gap("", "PQP"), 3)
        self.assertEqual(addressing.generation_gap("PQP", "PQG"), 2)

    def test_field_no_owner(self):
        f = addressing.Field("one question")
        for node in ("", "S", "PQP"):
            f.join(node)
        self.assertEqual(f.origin, "∞0 → ∞0'")
        self.assertNotEqual(f.origin, "")  # origin is an appeal, never a node


class TestMembraneGuards(unittest.TestCase):
    def test_l3_claiming_empty_phi(self):
        # Z cannot be argued into place with no φ.
        self.assertIsNone(quality.validate_z(quality.derive_z(quality.hold_phi(), quality.hold_omega()),
                                             quality.hold_phi(), True))

    def test_l4_engine_authored_phi(self):
        om = quality.hold_omega()
        engine_phi = m.Symbol("φ", face=m.AMORPHOUS, value="profound alignment",
                              assumption=False, source=m.AI)  # AI-authored → L4
        z = quality.derive_z(engine_phi, om)
        self.assertIsNone(quality.validate_z(z, engine_phi, True))

    def test_v_empty_incomplete(self):
        bpp = value.compose_B_double_prime()
        enriched = value.form_infinity_prime()
        self.assertFalse(value.enforce_completion(bpp, enriched))  # V∅

    def test_completion_when_return_present(self):
        bpp = value.compose_B_double_prime()
        enriched = m.reveal("∞0'", "the next question")
        self.assertTrue(value.enforce_completion(bpp, enriched))


if __name__ == "__main__":
    unittest.main(verbosity=2)
