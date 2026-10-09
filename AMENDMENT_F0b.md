# DOC-2-091 F0b: transport/admission amendment only

F0 lock-1 commit: 9fd13fd27c05ed38bd2d6fbbfb3caa60f811c1a3. Its registered run returned nine pages titled "Checking your browser - reCAPTCHA", not GEO metadata. Result: METADATA-UNRESOLVED. HTTP 200 and script exit 0 did not prove admission. That result is preserved verbatim in RESULTS.md and is not replaced by this audit.

This amendment changes transport and content admission only. Candidate set GSE5620-GSE5628, accession ascending, F1-F5 gates, METADATA-GO/STOP/UNRESOLVED labels, array-vs-RNA-seq disclosure, zero success credit and all no-value boundaries stay unchanged. No gene-expression values, sample pages, matrices, raw data, numerical supplements or accession swaps.

## Transport

Primary: NCBI E-utilities gds database. For each exact accession, esearch with term GSE accession in the accession field; esummary on returned IDs. Record raw JSON, exact final URL, UTC times, hashes, errors and parsed fields. A valid esearch result must contain esearchresult.idlist; valid esummary must contain result.uids. Semantic admission additionally requires a returned summary accession equal to the requested GSE accession; zero hits or a different accession is not a successful metadata match. No efetch family payload is used here to avoid accidental numerical-table retrieval.

Each request has one logged retry after transport or content-admission failure. A JSON error, malformed JSON, interstitial, absent expected envelope, or no exact accession summary is recorded ADMISSION-FAILURE. Retry once with the same endpoint/parameters, never substitute accessions. Respect NCBI rate guidance using at most one request per second, no API key or paid access. Hash/retain responses even when admission fails.

Fallback: only if E-utilities is blocked or lacks a necessary F1-F5 field, render the same GEO accession series page in a browser. Only brief series metadata; never navigate sample links or download data. Valid fallback content must contain the requested Series GSE marker, series title and GPL/GSM markers. A challenge page is ADMISSION-FAILURE and cannot be read as zero samples. One bounded logged retry per failed accession; stop on an unresolved challenge. Record which fields come from which route; a missing field stays UNRESOLVED.

Run collect_metadata_f0b.py once after lock-2 release. Interpret F1-F5 against exact metadata quotations, preserving route-level failures. No scoring of expression data. F0b remains preparation with zero success credit. Any later outcome study needs a separate released registration and program-wide exposure check.
