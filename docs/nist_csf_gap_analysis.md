# NIST CSF 2.0 Gap Analysis
## Ann & Robert H. Lurie Children's Hospital of Chicago
### Post-Incident Assessment | Rhysida Ransomware Attack | January 2024

---

## Executive Summary

This gap analysis evaluates Lurie Children's Hospital's cybersecurity posture against the NIST Cybersecurity Framework 2.0 (CSF 2.0) following the January 2024 Rhysida ransomware attack that resulted in:

- **5-day undetected attacker dwell time** (January 26–31, 2024)
- **4-month EHR outage** (restored May 20, 2024)
- **791,784 individuals** affected — PHI exfiltrated and sold on darkweb for $3.4M
- **Class action lawsuit** filed
- **FBI investigation** initiated

---

## NIST CSF 2.0 Function Assessment

### 1. GOVERN (GV) — NEW in CSF 2.0
*Establishes organizational cybersecurity strategy, expectations, and policy*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| GV.OC-01 | Cybersecurity integrated into enterprise risk | No evidence of board-level cyber risk oversight | CRITICAL |
| GV.RM-01 | Risk management policy established | No formal enterprise risk management program | HIGH |
| GV.SC-01 | Vendor/supply chain risk managed | No formal TPRM program, BAAs not regularly reviewed | HIGH |

**Overall Score: 1.5/5 — CRITICAL GAP**

---

### 2. IDENTIFY (ID)
*Understand organizational cybersecurity risk*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| ID.AM-01 | Asset inventory maintained | No comprehensive medical device inventory | HIGH |
| ID.AM-05 | Network mapped and documented | Flat network, no OT/IT segmentation documented | CRITICAL |
| ID.RA-01 | Risk assessments conducted | No evidence of pre-incident risk assessment | CRITICAL |
| ID.RA-05 | Threats and vulnerabilities identified | No threat intelligence program | HIGH |

**Overall Score: 1.5/5 — CRITICAL GAP**

---

### 3. PROTECT (PR)
*Implement safeguards to manage cybersecurity risk*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| PR.AA-01 | Identities and credentials managed | No MFA on EHR access, no PAM solution | CRITICAL |
| PR.AA-05 | Access permissions managed | Overprivileged accounts, no zero-trust | CRITICAL |
| PR.DS-01 | Data at rest protected | PHI not encrypted at field level | HIGH |
| PR.DS-02 | Data in transit protected | Partial TLS implementation | MEDIUM |
| PR.IR-01 | Network segmentation implemented | Flat network — clinical, admin, medical devices co-mingled | CRITICAL |
| PR.PS-01 | Config management maintained | No formal patch management program | HIGH |

**Overall Score: 1.5/5 — CRITICAL GAP**

---

### 4. DETECT (DE)
*Find and analyze cybersecurity attacks*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| DE.CM-01 | Networks monitored | No 24/7 SOC — 5-day dwell time undetected | CRITICAL |
| DE.CM-03 | User activity monitored | No UEBA or anomaly detection | CRITICAL |
| DE.CM-09 | Computing hardware monitored | No EDR on all endpoints | HIGH |
| DE.AE-02 | Anomalies analyzed | No SIEM correlation rules for ransomware TTPs | CRITICAL |

**Overall Score: 1/5 — CRITICAL GAP**
*The 5-day undetected dwell time is the most damning evidence of detection failure.*

---

### 5. RESPOND (RS)
*Take action regarding detected incidents*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| RS.MA-01 | Incident response plan activated | IRP existed but was not effective | HIGH |
| RS.CO-02 | Incidents reported to authorities | FBI notified — PARTIAL CREDIT | MET |
| RS.CO-03 | Information shared with stakeholders | Patient notification delayed months | HIGH |
| RS.AN-03 | Forensic analysis conducted | External forensics engaged — PARTIAL CREDIT | MET |

**Overall Score: 2/5 — HIGH GAP**

---

### 6. RECOVER (RC)
*Restore capabilities after a cybersecurity incident*

| Subcategory | Expected | Observed | Gap |
|---|---|---|---|
| RC.RP-01 | Recovery plan executed | No tested recovery plan — 4 months to restore EHR | CRITICAL |
| RC.RP-03 | Recovery activities communicated | Poor communication to patients and families | HIGH |
| RC.CO-04 | Recovery communicated to stakeholders | Updates delayed and unclear | HIGH |

**Overall Score: 1.5/5 — CRITICAL GAP**
*4-month EHR recovery time is unacceptable for a critical healthcare provider.*

---

## Overall CSF 2.0 Maturity Score

| Function | Score | Rating |
|---|---|---|
| GOVERN | 1.5/5 | Critical |
| IDENTIFY | 1.5/5 | Critical |
| PROTECT | 1.5/5 | Critical |
| DETECT | 1.0/5 | Critical |
| RESPOND | 2.0/5 | High |
| RECOVER | 1.5/5 | Critical |
| **OVERALL** | **1.5/5** | **Critical** |

---

## Top 5 Critical Findings

1. **No 24/7 SOC monitoring** — 5-day attacker dwell time went completely undetected
2. **No MFA on EHR access** — single factor authentication on Epic allowed unauthorized access
3. **Flat network architecture** — no segmentation between clinical, administrative, and medical device networks
4. **No immutable backups** — forced 4-month manual paper-based operations
5. **No formal downtime procedures** — clinical staff unprepared, patient safety compromised

---

## Recommendations Priority Matrix

| Priority | Control | Timeline | Estimated Cost |
|---|---|---|---|
| Immediate | Deploy MFA on all clinical systems | 30 days | $50K |
| Immediate | Implement 24/7 SOC with SIEM | 60 days | $200K/yr |
| Immediate | Immutable backup solution | 45 days | $150K |
| Short-term | Network segmentation (Purdue Model) | 90 days | $500K |
| Short-term | EDR on all endpoints | 60 days | $100K |
| Medium-term | Zero-trust architecture | 12 months | $1M+ |
| Medium-term | PAM solution | 6 months | $200K |
| Long-term | Formal TPRM program | 12 months | $100K/yr |

---

*Assessment conducted by Ashwatha Narayan | NIST CSF 2.0 | May 2026*
*Based on publicly available breach disclosures, HHS filings, and forensic investigation reports*
