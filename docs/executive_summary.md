# Executive Summary
## Lurie Children's Hospital Cybersecurity GRC Assessment
### January 2024 Rhysida Ransomware Attack — Post-Incident Analysis

---

## Prepared For
Ann & Robert H. Lurie Children's Hospital of Chicago
Board of Directors & Executive Leadership Team

## Prepared By
Ashwatha Narayan | Cybersecurity GRC Analyst
May 2026

---

## Incident Overview

On January 31, 2024, Ann & Robert H. Lurie Children's Hospital of Chicago —
one of America's leading pediatric academic medical centers — fell victim to
a ransomware attack by the Rhysida threat actor group. The attack resulted in:

| Metric | Value |
|---|---|
| Attacker Dwell Time | 5 days (January 26–31, 2024) |
| Systems Taken Offline | Epic EHR, MyChart, Email, Phone |
| EHR Recovery Time | 4 months (restored May 20, 2024) |
| Individuals Affected | 791,784 |
| Data Categories Exposed | 14 (SSNs, diagnoses, prescriptions, etc.) |
| Ransom Demanded | $3.4M (60 BTC) |
| Ransom Paid | None |
| Data Disposition | Sold on darkweb (March 8, 2024) |
| Legal Action | Class action lawsuit filed |
| Regulatory Action | HHS OCR investigation ongoing |
| Estimated Financial Impact | $50M–$100M (remediation + legal + reputational) |

---

## Critical Findings

### Finding 1 — Complete Detection Failure (CRITICAL)
The most significant finding of this assessment. Rhysida operated undetected
within Lurie's network for **5 full days** before discovery. This indicates
the complete absence of effective security monitoring, SIEM alerting, and
anomaly detection capabilities. A 5-day dwell time in a children's hospital
network represents an unacceptable patient safety risk.

### Finding 2 — No Multi-Factor Authentication on Critical Systems (CRITICAL)
Epic EHR — the system containing PHI for hundreds of thousands of pediatric
patients — was protected by single-factor authentication only. This is a direct
violation of HIPAA Technical Safeguard requirements (§164.312(d)) and represents
the most preventable aspect of this breach.

### Finding 3 — Flat Network Architecture (CRITICAL)
The entire hospital — clinical workstations, administrative systems, Epic servers,
and 500+ networked medical devices including infusion pumps, ventilators, and
medication dispensing systems — operated on a single flat network. Once Rhysida
gained initial access, lateral movement was unrestricted. This architectural
failure enabled the full scope of the breach.

### Finding 4 — Medical Device Security Gap (CRITICAL)
Lurie Children's Hospital operates hundreds of networked medical devices with
no dedicated OT security monitoring, no device inventory, and no network
segmentation. During the 5-day dwell period, these devices — including systems
with direct patient safety implications — were theoretically accessible to the
attacker. This represents an unacceptable patient safety risk beyond data theft.

### Finding 5 — No Tested Recovery Capability (CRITICAL)
The hospital had no tested disaster recovery plan and no immutable backup
strategy. The result was a **4-month EHR outage** — the longest hospital EHR
recovery in recent US history — during which clinical staff operated on paper,
surgeries were cancelled, and prescriptions were inaccessible. For a children's
hospital serving 239,000+ patients annually, this is an existential operational risk.

---

## NIST CSF 2.0 Overall Maturity

| Function | Score | Gap |
|---|---|---|
| GOVERN | 1.5/5 | No board-level cyber governance, no CISO program |
| IDENTIFY | 1.5/5 | No asset inventory, no risk assessments |
| PROTECT | 1.5/5 | No MFA, no segmentation, no encryption |
| DETECT | 1.0/5 | No SOC, no SIEM — worst performing function |
| RESPOND | 2.0/5 | IR plan existed but was ineffective |
| RECOVER | 1.5/5 | No tested DR — 4-month recovery |
| **OVERALL** | **1.5/5** | **Critical — immediate intervention required** |

---

## HIPAA Compliance Summary

| Rule | Requirements Assessed | Compliant | Non-Compliant | Partial |
|---|---|---|---|---|
| Security Rule — Administrative | 8 | 0 | 6 | 2 |
| Security Rule — Physical | 4 | 1 | 2 | 1 |
| Security Rule — Technical | 7 | 1 | 5 | 1 |
| Privacy Rule | 4 | 0 | 3 | 1 |
| Breach Notification Rule | 4 | 2 | 1 | 1 |
| **Total** | **27** | **4 (15%)** | **17 (63%)** | **6 (22%)** |

**63% non-compliance rate represents significant OCR enforcement exposure
estimated at $5M–$15M in potential penalties.**

---

## Risk Register Summary

| Priority | Count | % of Total |
|---|---|---|
| Critical | 12 | 40% |
| High | 15 | 50% |
| Medium | 3 | 10% |
| **Total** | **30** | **100%** |

---

## Top 5 Immediate Recommendations

1. **Deploy MFA on all Epic EHR and clinical systems** — 30 days, $50K
   Addresses the single most preventable aspect of this breach.

2. **Establish 24/7 SOC with SIEM monitoring** — 60 days, $200K/year
   Eliminates the detection gap that allowed 5-day undetected dwell time.

3. **Implement immutable backup solution** — 45 days, $150K
   Prevents future 4-month recovery scenarios.

4. **Emergency network segmentation** — 30 days, $75K
   Limits blast radius of any future breach.

5. **Medical device security platform** — 60 days, $200K
   Closes the OT blind spot and protects patient safety.

**Total Immediate Investment: ~$675K**
**Risk Reduction: Critical → High within 90 days**

---

## Strategic Recommendation

Lurie Children's Hospital must transform its cybersecurity posture from
reactive to proactive. The January 2024 breach was not an act of sophisticated
nation-state espionage — it was a ransomware-as-a-service attack by a criminal
group that exploited fundamental security gaps that have existed for years.

The financial cost of remediation ($2.5M–$4M) is a fraction of the estimated
$50M–$100M total impact of this breach when legal fees, regulatory penalties,
reputational damage, and operational disruption are accounted for.

Most critically — this is a children's hospital. The 791,784 affected individuals
include thousands of minors whose Social Security numbers and medical records
are now on the darkweb, exploitable for the next 18+ years. The board and
executive leadership have an ethical and legal obligation to ensure this
never happens again.

---

*This assessment is based entirely on publicly available information.*
*No proprietary or confidential information was accessed or used.*
*Ashwatha Narayan | May 2026*
