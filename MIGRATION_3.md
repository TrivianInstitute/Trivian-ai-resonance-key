# Schema 3.0 migration

Authorized correction of the 2026-09-05 audit findings; submitted for human
merge review. Normative definitions and the Twelve Invariants are unchanged.
Active weights are replaced by computational roles and Rosetta 2.0 equations.
Old weights remain explicitly historical in the JSON; git preserves the full
prior schema. Consumers must not use legacy weights for current aggregation.

Symbolic frequencies and legacy coherence-window thresholds are retained as
orientation material, not validated measures or RCD thresholds.
License labels now match LICENSE and LICENSE-TEXT. This metadata cleanup
does not purport to revoke rights granted in earlier versions.

Verify: `python -m unittest discover -s tests -v`.
