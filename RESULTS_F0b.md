# DOC-2-091 F0b metadata result: METADATA-UNRESOLVED

Builder assessment, pending independent review. Preparation only: **zero project-success credit**. No expression values, sample pages, matrices, raw files or numerical supplements were opened. F0 lock-1's nine reCAPTCHA responses remain separately recorded in RESULTS.md.

## Locked execution

F0b lock-2 commit: 34e33715afe84144308fa504fe4f8a7e63ffed4d. Primary collector ran once, 2026-10-09T18:58:05Z to 18:58:28Z, exit 0. E-utilities gds esearch/esummary: 18 requests, nine exact accession admissions, zero primary failures/retries. Same-series browser fallback supplied matrix links, access status and design wording. Initial GSE5620 interstitial was preserved, then cleared on that loaded page; a selector wait reported navigation and the first read was sparse, before the admitted series read. No new request/retry of the collector occurred. All nine fallback pages contain their exact Series marker, title, GPL198 and GSM markers.

## Gate assessment

| Gate | Assessment | Evidence and limit |
|---|---|---|
| F1 | PASS | All nine series identify Arabidopsis thaliana, GPL198, expression profiling by array. Eight explicitly named stresses: cold, osmotic, salt, drought, genotoxic, UV-B, wounding, heat. |
| F2 | UNRESOLVED | Both tissues have common positive times 0.5, 1, 3, 6, 12, 24 h for all eight stresses and control. Every such cell has exactly Rep1 and Rep2 labels. The admitted series descriptions do not explicitly establish that these are independent biological replicates. |
| F3 | PARTIAL / UNRESOLVED | Actual Series Matrix File(s) links occur on all nine series pages and all use GPL198. Common platform feature identity is supported, but actual probe-ID matching is not proven without inspecting prohibited value-table payloads. Numerical scale and normalization are expressly reserved for an outcome protocol. |
| F4 | PASS, dependence retained | Same-batch growth, roots/shoots separation and schedule are explicitly described. GSE5620 is the single control series; reused controls are shared observations, not independent per-stress samples. This does not prove Rep1 and Rep2 biological independence. |
| F5 | Public access verified; license UNKNOWN | All nine admitted pages report Public status. No dataset reuse license was stated on these series pages. This is not public-domain evidence; no expression/raw-data redistribution is authorized by this audit. Source attribution is required. |

## Exact metadata quotations

GSE5620 summary: "At day 16 stress treatment started at 3 hrs of light period; samples taken at 0.5, 1, 3, 6, 12, 24 h after treatment (in selected indicated cases 0.25h and 4.0h too), control samples include 0h; roots and shoots were prepared separately; all treatments and preparations were done on the same batch of seedlings in one place (Lab J.Kudla/Ulm, Germany) by coworkers from the indicated groups."

The series summary also says "we have generated expression data from 80 biologicaly different samples in triplicate." This is a general project description, not an explicit definition of this candidate set's two Rep labels. It cannot silently satisfy F2. For example the control page lists "GSM131223 AtGen_6-0011_Control-Shoots-0h_Rep1" and "GSM131224 AtGen_6-0012_Control-Shoots-0h_Rep2". The complete primary GSM/title lists and derived cells are retained in the evidence pack.

Platform quotation: "GPL198 [ATH1-121501] Affymetrix Arabidopsis ATH1 Genome Array". Link label: "Series Matrix File(s) TXT". These are links, not downloaded or verified normalized numerical tables. Source's supplementary CEL label denotes raw data, not a processed-matrix proof.

## Candidate accounting and observed matrix links

| Accession | Title | GSM count | Positive times (h) | Observed matrix link |
|---|---|---:|---|---|
| GSE5620 | AtGenExpress: Stress Treatments (Control plants) | 36 | 0.25,0.5,1.0,3.0,4.0,6.0,12.0,24.0 | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5620/matrix/ |
| GSE5621 | AtGenExpress: Stress Treatments (Cold stress) | 24 | 0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5621/matrix/ |
| GSE5622 | AtGenExpress: Stress Treatments (Osmotic stress) | 24 | 0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5622/matrix/ |
| GSE5623 | AtGenExpress: Stress Treatments (Salt stress) | 24 | 0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5623/matrix/ |
| GSE5624 | AtGenExpress: Stress Treatments (Drought stress) | 28 | 0.25,0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5624/matrix/ |
| GSE5625 | AtGenExpress: Stress Treatments (Genotoxic stress) | 24 | 0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5625/matrix/ |
| GSE5626 | AtGenExpress: Stress Treatments (UV-B stress) | 28 | 0.25,0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5626/matrix/ |
| GSE5627 | AtGenExpress: Stress Treatments (Wounding stress) | 28 | 0.25,0.5,1.0,3.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5627/matrix/ |
| GSE5628 | AtGenExpress: Stress Treatments (Heat stress) | 32 | 0.25,0.5,1.0,3.0,4.0,6.0,12.0,24.0 | ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5628/matrix/ |

## Decision boundary

METADATA-UNRESOLVED because F2 biological replication and F3 direct common-probe verification remain unverified. Not METADATA-STOP: no documented required numerical floor failed. Not METADATA-GO: the gates are not all verified. This audit does not establish conserved stress grammar, prediction quality, RNA-seq applicability, cross-species transfer or novelty. No scoring or next-stage acquisition has been started.

Any resolution beyond brief series metadata needs a reviewed new amendment. Any outcome study needs a separately locked/released protocol and the program-wide exposure check. An unresolved result is preserved, not converted into success credit.

## Sources

- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5620
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5621
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5622
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5623
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5624
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5625
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5626
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5627
- https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5628
