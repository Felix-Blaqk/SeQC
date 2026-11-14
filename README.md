SeQC: Sesame Quality Control Analytics Tool
SeQC turns raw sesame seed lab results into instant pass/fail decisions, so quality teams catch failing batches faster and spend less time on manual checks.

Built for sesame seed processing and export, where every batch must meet strict quality limits before it ships.

What it does
Checks each batch against grade-specific limits for NWSS, PSS and HSS sesame
Analyses 10 QC parameters: FFA, purity, moisture, Staphylococcus aureus, Salmonella, E. coli, total plate count, yeast and moulds, Enterobacteriaceae and Bacillus
Validates all input so bad data never enters the system
Reports pass/fail per parameter and overall for each batch, and tracks which parameters fail across a period
Features
Menu option	Description
1. Add New Batch	Enter a batch with full input validation (grade, date, numeric values, Salmonella status)
2 → 1. Batch Report	Search a batch by ID (case-insensitive) and see pass/fail for every parameter plus an overall result
2 → 2. Summary Report	Choose a date range and get total batches, pass/fail counts, pass rate, grade breakdown, failures by parameter (with batch IDs) and the most common failed parameter
QC limits
Parameter	NWSS	PSS	HSS	Rule
FFA (%)	2	2	1	at most
Purity (%)	99	99.95	99.98	at least
Moisture (%)	6	6	5.5	at most
S. aureus	10	10	10	at most
Salmonella	absent	absent	absent	must be absent
E. coli	10	10	10	at most
Total plate count	1000	1000	500	at most
Yeast and moulds	100	100	100	at most
Enterobacteriaceae	10	10	10	at most
Bacillus	100	100	100	at most
A batch passes only if every parameter passes.

Excel dashboard
A companion workbook for teams that prefer spreadsheets:

Limits sheet: the acceptable limits for each grade and parameter
Batch Data sheet: your batch results, with limits pulled in using INDEX/MATCH
OVERALL column: a pass/fail result per batch using COUNTIF
Requirements
Python 3.6 or newer. No packages to install: SeQC uses only the standard library (datetime, collections).

Getting started
git clone https://github.com/Felix-Blaqk/SeQC.git
cd SeQC
python seqc.py
Dates use the format DD-MM-YYYY. Grades must be entered in capitals (NWSS, PSS, HSS) and Salmonella as present or absent.

Example
Sample output from synthetic test data.

Batch report

========================================
BATCH REPORT
========================================
Batch ID  : SEQC-002
Grade     : PSS
Date      : 08 November 2026
----------------------------------------
 PARAMETER            RESULT
----------------------------------------
 FFA                  FAIL
 PURITY               PASS
 MOISTURE             PASS
 S_AUREUS             PASS
 SALMONELLA           PASS
 E_COLI               PASS
 TPC                  PASS
 YEAST_AND_MOULDS     PASS
 ETB                  PASS
 BACILLUS             PASS
----------------------------------------
OVERALL: FAIL
========================================
Summary report

========================================
SUMMARY REPORT
Reporting Period: 01 November 2026 to 14 November 2026
========================================
Total Batches       : 3
Total Pass          : 1
Total Fail          : 2
Pass Rate           : 33.33%
----------------------------------------
GRADE BREAKDOWN
----------------------------------------
HSS                 : 1 batches
PSS                 : 1 batches
NWSS                : 1 batches

----------------------------------------
FAILURE BREAKDOWN
----------------------------------------
FFA                 : 1 batches (IDs: SEQC-002)
MOISTURE            : 1 batches (IDs: SEQC-003)

Most Common Failed Parameter: ffa
========================================
Testing
Tested with synthetic batch data.

Current limitations and roadmap
Batch data is held in memory and cleared when the program exits. Saving to a file or database is the next step.
Planned: charts and trend tracking over time, and support for more grades and parameters.
License and ownership
© 2026 Felix Chigoziem Oba. All rights reserved. Proprietary software: no copying, distribution or commercial use without written permission.

Author
Felix Chigoziem Oba, QA/QC Officer and microbiologist, Lagos, Nigeria LinkedIn · chigoziemoba@gmail.com
