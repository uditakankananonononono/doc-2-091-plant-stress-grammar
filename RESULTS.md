# DOC-2-091 F0 registered result: METADATA-UNRESOLVED

Zero success credit. No biological outcome study has been performed.

The frozen collect_metadata.py was executed once after release against GSE5620-GSE5628, accession ascending. All nine requests returned HTTP 200 with HTML titled "Checking your browser - reCAPTCHA" rather than a GEO accession record. No exceptions were thrown, so the locked one-transient-failure retry branch was not used. The collector lacked a response-content admission check and therefore saved the challenge pages without identifying them as errors. Its exit code 0 is script completion, not metadata success.

| Gate | Registered question | Result | Quote/evidence |
|---|---|---|---|
| F1 | Common organism/platform across >=4 stresses and control | UNRESOLVED | Every saved page title: "Checking your browser - reCAPTCHA". No GEO organism/platform content. |
| F2 | Matched tissue/time cells with biological replicas | UNRESOLVED | 0 GSM IDs extracted from each challenge page. This is not evidence of zero samples. |
| F3 | Actual processed-matrix/shared-table links | UNRESOLVED | No series metadata or matrix links in returned challenge pages. This is not evidence that processed data are unavailable. |
| F4 | Comparable batch, tissue, timing, matched controls | UNRESOLVED | Original experiment description not returned by the registered collector. |
| F5 | Source-use/public-access constraints | UNRESOLVED | ReCAPTCHA challenge content cannot establish source-use terms. |

Locked inputs match tag lock-1 commit 9fd13fd27c05ed38bd2d6fbbfb3caa60f811c1a3, tree 0c003313a7a745638ec2e69536cfde3847dabc18. The parent released this metadata-only run after tag readback. No script/protocol changes, accession swaps, expression values, sample pages, matrices, raw data, or author numerical supplements were used. Earlier scout metadata remains pre-registration prior knowledge, not a replacement run.

The problem is transport/admission, not biological absence or negative efficacy. A future registration should validate the returned page's actual accession and metadata before accepting HTTP success. No rerun or alternative-route substitution has been performed under this lock.

Raw challenge pages are preserved locally by accession with SHA256s; they are not reposted as biological data. records.json, stdout, timestamps, exit status and this result record describe the failure. A separately reviewed registration is required to continue the source audit. Numerical outcome analysis would still need its own protocol and release.
