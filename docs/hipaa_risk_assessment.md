# HIPAA Risk Assessment
## Ann & Robert H. Lurie Children's Hospital of Chicago
### Post-Incident Analysis | January 2024 Rhysida Ransomware Attack

---

## Overview

This HIPAA Security Rule risk assessment evaluates Lurie Children's Hospital's
compliance posture following the January 2024 ransomware attack. The assessment
covers all three HIPAA rules and is based on publicly available breach disclosures,
HHS Office for Civil Rights (OCR) breach portal filings, and forensic investigation
findings.

**Breach Statistics:**
- Individuals Affected: 791,784
- PHI Categories Exposed: 14 data types including SSNs, diagnoses, prescriptions
- Attacker Dwell Time: 5 days (Jan 26–31, 2024)
- EHR Downtime: 4 months
- Ransom Demanded: $3.4M (60 BTC) — not paid
- Data Disposition: Sold on darkweb by Rhysida group
- Legal Action: Class action lawsuit filed

---

## HIPAA Security Rule Assessment (45 CFR Part 164)

### Administrative Safeguards (§164.308)

| Standard | Requirement | Finding | Compliance |
|---|---|---|---|
| 164.308(a)(1) | Risk Analysis | No evidence of pre-incident formal risk analysis | NON-COMPLIANT |
| 164.308(a)(1) | Risk Management | No documented risk management program | NON-COMPLIANT |
| 164.308(a)(3) | Workforce Clearance | Insufficient access review procedures | PARTIAL |
| 164.308(a)(4) | Access Management | Overprivileged accounts, no formal IAM | NON-COMPLIANT |
| 164.308(a)(5) | Security Training | Inadequate phishing awareness training | NON-COMPLIANT |
| 164.308(a)(6) | Incident Response | IRP existed but response took 5 days to detect | PARTIAL |
| 164.308(a)(7) | Contingency Plan | No tested downtime procedures, 4-month recovery | NON-COMPLIANT |
| 164.308(b)(1) | Business Associates | BAAs in place but not regularly reviewed | PARTIAL |

**Administrative Safeguards Score: 2/8 COMPLIANT**

---

### Physical Safeguards (§164.310)

| Standard | Requirement | Finding | Compliance |
|---|---|---|---|
| 164.310(a)(1) | Facility Access Controls | Physical security adequate | COMPLIANT |
| 164.310(b) | Workstation Use | No formal workstation security policy | PARTIAL |
| 164.310(c) | Workstation Security | Unencrypted workstations in clinical areas | NON-COMPLIANT |
| 164.310(d)(1) | Device/Media Controls | No formal media disposal policy | PARTIAL |

**Physical Safeguards Score: 1/4 COMPLIANT**

---

### Technical Safeguards (§164.312)

| Standard | Requirement | Finding | Compliance |
|---|---|---|---|
| 164.312(a)(1) | Access Control | No MFA on Epic EHR, no PAM solution | NON-COMPLIANT |
| 164.312(a)(2)(i) | Unique User IDs | Implemented | COMPLIANT |
| 164.312(a)(2)(iv) | Encryption/Decryption | PHI not encrypted at field level | NON-COMPLIANT |
| 164.312(b) | Audit Controls | Insufficient audit logging — 5-day breach undetected | NON-COMPLIANT |
| 164.312(c)(1) | Integrity Controls | No file integrity monitoring | NON-COMPLIANT |
| 164.312(d) | Authentication | Single-factor authentication on critical systems | NON-COMPLIANT |
| 164.312(e)(1) | Transmission Security | Partial TLS implementation | PARTIAL |

**Technical Safeguards Score: 1/7 COMPLIANT**

---

## HIPAA Privacy Rule Assessment (45 CFR Part 164)

| Standard | Requirement | Finding | Compliance |
|---|---|---|---|
| 164.502 | Uses and Disclosures | PHI exfiltrated without authorization | VIOLATED |
| 164.514 | De-identification | No PHI de-identification program | NON-COMPLIANT |
| 164.524 | Access of Individuals | MyChart offline for months — patient access denied | PARTIAL |
| 164.530 | Administrative Requirements | Security training inadequate | NON-COMPLIANT |

---

## HIPAA Breach Notification Rule Assessment (45 CFR Part 164)

| Requirement | Finding | Compliance |
|---|---|---|
| 60-day notification to individuals | Notifications sent July 2024 — 6 months post-breach | NON-COMPLIANT |
| HHS notification | Filed with HHS OCR | COMPLIANT |
| Media notification (500+ affected) | Public statements issued | COMPLIANT |
| Law enforcement notification | FBI notified | COMPLIANT |

**Note:** The 6-month delay in individual notification is a significant Breach
Notification Rule violation. OCR typically requires notification within 60 days
of discovery.

---

## PHI Exposure Analysis

| Data Category | Individuals Affected | HIPAA Classification | Risk Level |
|---|---|---|---|
| Social Security Numbers | ~791,784 | PHI + PII | CRITICAL |
| Medical Diagnoses | ~791,784 | PHI | CRITICAL |
| Prescription Information | ~791,784 | PHI | CRITICAL |
| Health Plan Information | ~791,784 | PHI | HIGH |
| Medical Record Numbers | ~791,784 | PHI | HIGH |
| Driver's License Numbers | ~791,784 | PII | HIGH |
| Dates of Service | ~791,784 | PHI | MEDIUM |
| Email Addresses | ~791,784 | PII | MEDIUM |

**Critical Note:** This is a children's hospital. Many affected individuals are
minors. PHI of minors carries additional legal protections under HIPAA and
state laws, including Illinois' PIPA (Personal Information Protection Act).

---

## Pediatric-Specific Risk Factors

1. **Minor PHI longevity** — Children's data remains exploitable for decades
2. **Parental consent complexity** — Breach notification must reach parents/guardians
3. **COPPA implications** — Children under 13 have additional federal protections
4. **Illinois PIPA** — State law imposes stricter breach notification requirements
5. **Long-term identity theft risk** — SSNs of minors can be exploited for 18+ years

---

## Estimated HIPAA Penalty Exposure

| Violation Category | Violations Found | Penalty Range |
|---|---|---|
| Unknowing violations | 2 | $100–$50,000 per violation |
| Reasonable cause | 4 | $1,000–$50,000 per violation |
| Willful neglect (corrected) | 3 | $10,000–$50,000 per violation |
| Willful neglect (uncorrected) | 1 | $50,000 per violation |
| **Estimated Total Exposure** | | **$5M–$15M** |

*Note: HHS OCR has not yet announced enforcement action as of May 2026.*

---

## Top HIPAA Remediation Priorities

1. **Immediate:** Conduct formal HIPAA Security Rule risk analysis per §164.308(a)(1)
2. **Immediate:** Implement MFA on all systems accessing ePHI
3. **30 days:** Deploy audit logging and SIEM alerting on all PHI access
4. **60 days:** Implement PHI encryption at rest and in transit
5. **90 days:** Develop and test incident response and downtime procedures
6. **6 months:** Establish formal security awareness training program
7. **12 months:** Implement zero-trust architecture for ePHI access

---

*Assessment by Ashwatha Narayan | HIPAA Security, Privacy & Breach Notification Rules*
*Based on HHS OCR breach portal, Maine AG breach filing, and public forensic reports*
*May 2026*
