# DOC-2-091 F0: plant-stress grammar source-feasibility audit

Status: preregistration for metadata-only feasibility, not a scientific outcome study. No expression values, stress-response scores or author DEG tables have been opened by this executor. No success credit is claimed from F0. The parent must release lock-1 before the registered metadata audit; all numerical expression acquisition/scoring remains prohibited until a separately released outcome protocol.

## Original question and source

Source topic DOC-2-091, source position 191: "Plants Have a Stress Grammar". Can unrelated stresses share a conserved regulatory grammar even when individual genes differ? Required eventual validation: leave-one-stress-out. This registration addresses whether a source can support that question without forcing mismatched cohorts into a predictive model.

Metadata leads, already viewed before this registration: GEO GSE5620 (control), GSE5621 (cold), GSE5622 (osmotic), GSE5624 (drought), and catalog descriptions for GSE5623 (salt), GSE5625 (genotoxic). No numerical source values were opened. AtGenExpress is Arabidopsis ATH1 microarray data, not the source prompt's RNA-seq example. Any eventual study using it must explicitly be an array-based replication/transfer study, not a new RNA-seq or cross-species result. Author publications describe stress overlap already, so novelty is unestablished. GEO pages contain published summaries; those are prior knowledge, not blind findings.

## Registered bounded candidate set

GSE5620 through GSE5628 inclusive, accession ascending. Fetch brief series HTML metadata only. Do not fetch GEO sample pages, series matrices, MINiML/SOFT family archives, author supplementary numerical tables, or raw CEL/FASTQ data during F0. Do not expand or swap this candidate set after viewing metadata. Record URL, fetch time, bytes, SHA256, HTTP failure, and extracted series title, platform, organism and GSM title list. URLs follow GEO's documented accession-view endpoint; no invented scientific claim links.

## Gates (all required for GO)

F1: One verified common platform and one organism across control and at least four biologically distinct non-control stress series in the candidate set. Each must explicitly label the perturbation in metadata. Similar words do not create separate biological stresses.
F2: For roots or shoots separately, at least three common positive post-treatment time points shared by controls and each of at least four stresses. At least two biological replicate labels per stress/tissue/time cell and two matching control replicate labels must be present. Do not call technical replicas biological. An ambiguous replicate definition makes F2 unresolved, not pass.
F3: A processed series matrix or explicitly described normalized shared feature table must have an actual link on each admitted GEO page, with common platform probe identifiers. Metadata alone cannot prove its numerical scale or normalization comparability: those remain outcome-protocol checks.
F4: Original experiment description must support comparability of growth batch, tissue, sampling schedule and matched controls. Shared controls are dependence, not extra independent samples. If stress is perfectly confounded with separate experimental batch or matched controls cannot be established, STOP.
F5: Record source-use terms/public-access constraints from source documentation. No private data or paid source may be used. An unknown reuse license stays UNKNOWN and prevents raw redistribution; it is not silently treated as public domain. Source attribution remains mandatory.

F0 labels: METADATA-GO only if all five gates are verified; METADATA-STOP if a required floor fails; METADATA-UNRESOLVED if documentation is insufficient. GO does not establish a biological discovery, model effectiveness, success, or untouched-test status.

## Procedure and independence

Run the locked metadata collector once, retaining network failures verbatim. A transient failed metadata request may be retried once with its failure logged; no accession substitution. Hash each saved page and the locked code/protocol. Gate interpretation is documented against exact quoted metadata, not inferred from a title. The program-wide exposure ledger and other builders' state must be checked through parent before any future frozen expression test. A source not mentioned in the exposure ledger is not automatically untouched.

## Next-stage boundary

Only after METADATA-GO or a reviewed resolution, draft a separate executable outcome protocol specifying sample unit, transformations, leave-one-stress-out folds, baselines, uncertainty, dependence handling and failure policy. No threshold can be selected using expression values. All source changes require a new numbered registration. F0 is preparation and carries zero project-success credit even when GO.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5620
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5621
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5622
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5624
- https://www.omicsdi.org/dataset/geo/GSE5623
- https://www.omicsdi.org/dataset/geo/GSE5625
