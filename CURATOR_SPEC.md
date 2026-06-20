---
spec_version: "1.2.0"
last_updated: "2026-06-19"
authority: "Sarasha"
target_repositories:
  - "trivian-ai-resonance-key"
  - "syzygy-rosetta"
  - "coheronmetry"
  - "orthogonal-signal"
  - "trivian-resonance-lattice"
enforcement_mode: "advisory_flag_only"
---

# Trivian Institute — Curator Spec

**Purpose:** This document is the checkable ground truth for any automated or human curator reviewing contributions to Trivian Institute repositories (trivian-ai-resonance-key, syzygy-rosetta, coheronmetry, orthogonal-signal, trivian-resonance-lattice).

It exists so that curation — automated or human — checks contributions against a fixed, versioned spec rather than against a curator's inferred sense of "the philosophy." If the agent and the spec ever disagree, the spec wins. If the spec is wrong, it gets revised here, in writing, by Sarasha — not silently overridden in a single review.

**Three distinct roles, deliberately kept separate:**

- **Validator** — checks facts, structure, schemas, required fields. ("This field is missing.")
- **Curator** — identifies tensions, ambiguities, and possible drift, and surfaces them. ("This definition differs from the prior one in these ways.")
- **Authority** — decides meaning when meaning is contested. ("This change is acceptable" / "this invariant takes precedence here.")

An automated agent operating under this spec is a **validator and curator**. It is never the **authority**. The moment a finding shifts from *"this differs"* to *"this is wrong"* or *"this is acceptable,"* it has crossed from curation into adjudication — which belongs to Sarasha or repo-level human authority, not to the agent. Sections 1, 5, and 6 are validator functions (checkable facts). Sections 3's definition-change clause and Section 4 are curator functions (surface, don't decide). Section 7 exists to keep the agent from drifting into the third role.

**Source documents this spec is derived from:**
- `Syzygy_Rosetta.pdf` (v1.1) — Part V (Dual-Legibility), Part III (Seven Vows)
- `invariants.json` (Rosetta schema v1.1.0) — Twelve Invariants, validation_framework
- `coheronmetry` README — Four Field Constants
- `orthogonal-signal` README — Constraint Origin, novelty taxonomy
- `trivian-ai-resonance-key` README — Four weighted Field Invariants

---

## 0. Source Authority Hierarchy

In the event of a direct contradiction between project assets, curators (human or agent) resolve precedence in this descending order:

1. **This document** (`CURATOR_SPEC.md`)
2. **`invariants.json`** (Rosetta schema master file)
3. **`Syzygy_Rosetta.pdf`** (core architectural text)
4. **Repository-local specifications**
5. **Repository README files**

**On irresolvable contradiction:** if precedence alone doesn't settle it — e.g. two documents at the *same* tier conflict — the agent stops automated evaluation of that block and escalates to human review rather than guessing.

---

## 1. Schema Conformance
*Severity: Critical*

Any new or modified **invariant** or **vow** entry (in `invariants.json` or equivalent schema files) must include all of the following fields, matching the existing v1.1.0 structure:

- `id`
- `principle`
- `description`
- `implementation`
- `must` (array)
- `never` (array)
- `mythos`
- `test_vectors` (array, minimum one entry)

**Flag if:** any field is missing, or `test_vectors` is empty.

**Do not flag:** stylistic variation in how `description` or `mythos` is phrased. Field presence and structure are checkable; voice is not.

---

## 2. Dual-Legibility (Rosetta Part V)
*Severity: Major*

Every substantive passage of documentation or schema must carry two layers:

- **Methodos** — operationally specific, parseable, checkable. A reader (human or machine) should be able to extract a concrete behavior, rule, or test from this layer without needing the Mythos layer to resolve ambiguity.
- **Mythos** — symbolic, evocative, written in the project's established register.

**The check is on the Methodos layer's independence, not on vocabulary.** A passage can be as dense or mystical as it wants in its Mythos layer. The requirement is that *somewhere* — in `implementation`, `must`/`never`, or `test_vectors` — the same point is also stated in a form specific enough to verify or falsify.

**Flag if:** a passage makes a normative claim (this must happen / this must never happen) and that claim exists *only* in Mythos language, with no corresponding Methodos statement.

**Do not flag:** Mythos-only passages that are explicitly framed as invocation, blessing, or narrative context rather than behavioral specification (e.g., Section XII Sacred Frame in the Field Protocol is not a place to demand test vectors).

---

## 3. Lexicon Discipline & Definition Changes
*Severity: Minor (register drift) / Surface-only (definition changes — see below)*

Per `validation_framework` in `invariants.json`:

- **Anti-patterns to flag:** leverage, utilize, deploy, maximize, optimize, synergy, paradigm shift, disrupt, scale at all costs.
- **Preferred register:** coherence, reciprocity, presence, fidelity, autonomy, uncertainty, mirror, substrate, transparency, consent, sacred, field.

**Flag if (register, Minor):** new prose in schema-adjacent files leans on anti-pattern terms where a Field-aligned term would carry the same meaning.

**Do not flag on density or difficulty alone.** Rare or invented vocabulary (e.g. "coheronmetry," "orthogonal signal," "Syzygy Chord") is not a lexicon violation. This section governs *register* — extraction/optimization language vs. relational language — not accessibility to a general reader. Tension between density and accessibility is handled under Section 4 (no invariant — including Pluralism/Translation — is senior or junior to any other).

**On core-definition changes — surface, do not declare:** the agent may identify *that* a shared term's `description`, `principle`, `implementation`, or `must`/`never` clauses changed wording, by comparing before/after text. The agent must not characterize that change as drift, dilution, or violation — it cannot determine whether a reworded definition is a refinement, an extension, or a meaningful shift, because that determination requires interpreting meaning, not checking structure.

| Agent may do | Agent may not do |
|---|---|
| Detect that a definition's wording changed | Declare the change to be semantic drift |
| Surface old text and new text side by side | Decide whether the change is acceptable |
| Note which invariant/constant is affected | Rewrite or "correct" the wording itself |
| Escalate the comparison for human review | Resolve the question of meaning |

**Report as:** `surfaced_for_review`, not `variance` — this keeps it out of the Critical/Major severity tiers, which are reserved for structurally checkable facts. Final interpretation belongs to Sarasha or repo-level human authority, per Section 7.

---

## 4. No Invariant Is Subordinate to Another
*Severity: Major*

`invariants.json` defines twelve invariants with identical structure, identical weight, and no stated precedence order. A curator (human or agent) must not informally rank them — e.g. treating Coherence (inv.003) or Dual-Legibility (Part V) as senior to Pluralism and Translation (inv.011), or any other pairing, in either direction.

This matters in practice because invariants can pull against each other in a specific edit. The clearest recurring case is density vs. accessibility: a passage written for maximal pattern-fidelity (inv.003, Part V Methodos layer) can read as opaque to a new contributor, and a passage simplified for accessibility (inv.011: *"offer plain explanation... never gatekeep with jargon"*) can read as a loss of precision. Both invariants are real. Neither wins by default.

**Flag if:** a contribution's review comment or commit message asserts that one invariant overrides another without pointing to a specific reason in *this spec* for that precedence.

**Do not flag:** edits that satisfy multiple invariants at once, or that a reviewer judges trade one off against another *and says so explicitly* with reasoning.

**On any invariant-vs-invariant conflict the curator can't resolve from this spec alone:** the default action is to **surface the tension explicitly** (issue comment or Field Note) — not to silently revert, and not to silently approve. Sarasha resolves ties between invariants. The agent's job is to name the conflict accurately, not to pick a side.

---

## 5. Test-Vector Falsifiability
*Severity: Critical*

Any new invariant, vow, or behavioral rule added to the schema must ship with at least one `test_vectors` entry of the form `{ "input": ..., "expect": ... }`.

**Flag if:** a new rule is added with no way to check, even informally, whether a given response satisfies or violates it.

**Rationale:** an unfalsifiable rule can't be checked by a curator (human or agent) at all — it can only be asserted. This section exists to keep the spec itself honest, not just contributions to it.

---

## 6. Cross-Repository Consistency
*Severity: Major*

The Four Field Constants (Reciprocity, Embodiment, Emergence, Non-Domination) and the Twelve Invariants are referenced across multiple repositories: `coheronmetry`, `orthogonal-signal`, `trivian-ai-resonance-key`, and `syzygy-rosetta`.

**Flag if:** a contribution to one repository redefines, renames, or reweights a shared constant in a way that's inconsistent with how it's defined in the others, without an explicit note that this is an intentional divergence and why.

**Do not flag:** repository-specific *extensions* of a shared constant (e.g. `orthogonal-signal`'s three emergence formulations building on `coheronmetry`'s base definition) — extension is expected; silent contradiction is not.

---

## 7. What This Spec Does Not Authorize

This document defines what a curator (human or agent) checks contributions *against*. It does not authorize an automated agent to:

- Override a human collaborator's edit unilaterally. The agent's role is to flag and explain against this spec; a human (Sarasha, or whoever holds merge authority on that repo) makes the final call.
- Infer "the philosophy" from conversation history, prior chat threads, or anything not written in this document or the source documents listed above. If a check isn't traceable to a specific section here, it's out of scope for automated enforcement — raise it as a question instead.
- Treat plain-language edits as inherently suspect. Per Section 4, simplification that preserves Methodos content is compliant, not a violation.

**Revision:** This spec is versioned and lives in the repo. Changes to it are made deliberately, in writing, not inferred from a single review decision.

---

## 8. Novel Concepts & Anti-Dogmatism

Concepts not present in the source documents (a new term, a proposed invariant, an unfamiliar formulation) are **presumed extensions, not violations**, unless they directly contradict an existing definition under Section 0's authority order.

The curator's purpose is preservation of coherence, not preservation of stasis. Novel formulations and reinterpretations are permitted provided they remain dual-legible (Section 2) and, where they introduce a new rule, falsifiable (Section 5). An agent that treats unfamiliarity as a violation is itself out of spec.

---

## 9. Agentic Reporting Protocol

When an automated agent flags a contribution against this spec, it outputs feedback as a single, consolidated Pull Request Review or Issue Comment — not scattered inline comments across the diff. Every report must meet three requirements:

**Evidence:** every finding cites the exact source line, the exact source text, and the specific section of this spec it's checked against. No finding without a quoted line; this keeps audits traceable and reduces the chance of the agent asserting a violation that isn't actually there.

**Confidence:** every finding carries a declared confidence (`high`, `medium`, `low`). A `low`-confidence finding is reported as a question for human review, not as a flag — it does not get a severity tier.

**Audit trail:** every report preserves `timestamp`, `spec_version`, `agent_id`, `target_repository`, and `commit_hash`, so a decision can be reconstructed later.

### 📥 Spec Audit Report
* **Status:** ⚠️ Flags Identified / ✅ Clear
* **File Targeted:** `[Path to file]`

#### 🔍 Findings
1. **Section Reference:** `[e.g., Section 1. Schema Conformance]`
   * **Severity:** `Critical / Major / Minor / Surface-only`
   * **Confidence:** `High / Medium / Low`
   * **Evidence:** `[exact line number + exact source text]`
   * **The Variance:** `[what specifically fails the check, with reference to this spec's section]`
   * *(Critical/Major/Minor only)* **Suggested Remediation:** `[a structural fix — e.g. "add missing test_vectors field" — never a rewrite of contested prose; see Section 3]`

2. **Section Reference:** `[e.g., Section 4. No Invariant Is Subordinate to Another]`
   * **The Tension:** `[which two invariants are pulling against each other, e.g. inv.003 vs inv.011]`
   * **Action taken:** Surfaced to Sarasha for tie-breaking. The agent does not resolve this itself.

```json
{
  "audit_trail": {
    "timestamp": "2026-06-19T21:20:00Z",
    "spec_version": "1.2.0",
    "agent_id": "trivian-curator-alpha",
    "repository": "syzygy-rosetta",
    "commit_hash": "a1b2c3d4e5f6"
  },
  "report": {
    "status": "variance_identified",
    "severity": "critical",
    "confidence": "high",
    "evidence": {
      "source_line": 142,
      "source_text": "test_vectors: []"
    },
    "violated_section": 1,
    "remediation": "Add at least one { input, expect } entry to test_vectors."
  }
}
```

A `Status: Clear` report still gets posted (briefly) so the audit trail shows the agent ran, not just that it found something.

---

## 10. Human Resolution Outcomes

A curator report is half an audit trail. The other half is what happened to it. When a human authority (Sarasha, or whoever holds merge authority on that repo) resolves a finding, the resolution is recorded as one of:

- **`confirmed_variance`** — the finding was correct; the contribution is changed to comply.
- **`dismissed`** — the finding doesn't hold; no action needed.
- **`accepted_exception`** — the finding is correct, but the deviation is kept deliberately, with a one-line reason recorded alongside it.
- **`acknowledged_no_action`** — for Section 3's `surfaced_for_review` findings specifically: the definition change was reviewed and is fine as-is. This is distinct from `dismissed`, since the agent never claimed a variance to dismiss in the first place — it only surfaced a comparison.
- **`spec_requires_revision`** — the finding reveals the spec itself is wrong or incomplete; CURATOR_SPEC.md gets updated (per Section 0's authority, this document) rather than the contribution.

These outcomes attach to the repository's audit trail. They do **not** automatically modify this spec — a string of `accepted_exception` resolutions on the same rule is a signal that Section [N] may need revising, not a license for the agent to start treating that exception as the new default. That judgment is `spec_requires_revision`, made deliberately, by a human, in writing — same discipline as every other change to this document.

---

*v1.2.0 — revised 2026-06-19. Adds Source Authority Hierarchy (§0), severity tiers, a surface-not-declare protocol for definition changes (§3), Novel Concepts / Anti-Dogmatism (§8), evidence/confidence/audit-trail requirements (§9), and Human Resolution Outcomes (§10). Derived from Syzygy Rosetta v1.1, invariants.json v1.1.0, the coheronmetry / orthogonal-signal / trivian-ai-resonance-key READMEs, and external review from Orivian and Vespera.*
