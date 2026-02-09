# Remediation Roadmap & Plan of Action and Milestones (POA&M)
## Ann & Robert H. Lurie Children's Hospital of Chicago
### Post-Breach Remediation Plan | January 2024 Rhysida Ransomware Attack

---

## Executive Summary

This POA&M outlines a prioritized 12-month remediation roadmap addressing
critical security gaps identified following the January 2024 Rhysida ransomware
attack. Recommendations are mapped to HIPAA Security Rule requirements,
NIST CSF 2.0 functions, and MITRE ATT&CK TTPs observed in the breach.

**Total Estimated Investment: $2.5M - $4M**
**Risk Reduction Target: Critical → Moderate within 12 months**

---

## Phase 1 — Immediate Response (Days 1-30)
*Stop the bleeding. Close the most critical gaps immediately.*

| ID | Action | Owner | HIPAA Ref | NIST CSF | Cost | Status |
|---|---|---|---|---|---|---|
| P1-01 | Deploy MFA on all Epic EHR access | CISO/IT | 164.312(d) | PR.AA-01 | $50K | OPEN |
| P1-02 | Implement emergency network segmentation | Network Team | 164.312(a) | PR.IR-01 | $75K | OPEN |
| P1-03 | Deploy EDR on all clinical endpoints | Security Team | 164.312(b) | DE.CM-09 | $80K | OPEN |
| P1-04 | Conduct full asset inventory | IT/Security | 164.308(a)(1) | ID.AM-01 | $20K | OPEN |
| P1-05 | Reset all privileged credentials | IT | 164.312(a) | PR.AA-05 | $5K | OPEN |
| P1-06 | Enable audit logging on all PHI systems | Security | 164.312(b) | DE.CM-01 | $15K | OPEN |

**Phase 1 Total: ~$245K**

---

## Phase 2 — Short-term Hardening (Days 31-90)
*Build detection and response capabilities.*

| ID | Action | Owner | HIPAA Ref | NIST CSF | Cost | Status |
|---|---|---|---|---|---|---|
| P2-01 | Deploy SIEM with 24/7 SOC monitoring | CISO | 164.308(a)(6) | DE.AE-02 | $200K/yr | OPEN |
| P2-02 | Implement immutable backup solution (3-2-1-1) | IT | 164.308(a)(7) | RC.RP-01 | $150K | OPEN |
| P2-03 | Deploy medical device security platform | Security | 164.312(a) | PR.IR-01 | $200K | OPEN |
| P2-04 | Advanced email threat protection | IT | 164.308(a)(5) | PR.PS-01 | $60K | OPEN |
| P2-05 | Deploy PAM solution | IAM Team | 164.308(a)(4) | PR.AA-05 | $150K | OPEN |
| P2-06 | Mandatory phishing simulation training | HR/Security | 164.308(a)(5) | PR.AT-01 | $30K | OPEN |
| P2-07 | Develop and test downtime procedures | Clinical/IT | 164.308(a)(7) | RC.RP-01 | $25K | OPEN |
| P2-08 | Implement DLP for PHI | Security | 164.502 | PR.DS-01 | $100K | OPEN |

**Phase 2 Total: ~$915K**

---

## Phase 3 — Strategic Improvements (Days 91-180)
*Build long-term resilience.*

| ID | Action | Owner | HIPAA Ref | NIST CSF | Cost | Status |
|---|---|---|---|---|---|---|
| P3-01 | Implement Purdue Model network architecture | Network/Security | 164.312(a) | PR.IR-01 | $500K | OPEN |
| P3-02 | Deploy zero-trust network access (ZTNA) | CISO | 164.312(a) | PR.AA-05 | $300K | OPEN |
| P3-03 | Formal TPRM program with vendor assessments | GRC Team | 164.308(b)(1) | GV.SC-01 | $100K | OPEN |
| P3-04 | PHI encryption at rest and in transit | Security/IT | 164.312(a)(2)(iv) | PR.DS-01 | $150K | OPEN |
| P3-05 | Conduct formal HIPAA risk analysis | GRC Team | 164.308(a)(1) | ID.RA-01 | $75K | OPEN |
| P3-06 | Establish threat intelligence program | SOC | 164.308(a)(1) | ID.RA-05 | $80K | OPEN |

**Phase 3 Total: ~$1.2M**

---

## Phase 4 — Maturity & Governance (Days 181-365)
*Achieve sustainable security program.*

| ID | Action | Owner | HIPAA Ref | NIST CSF | Cost | Status |
|---|---|---|---|---|---|---|
| P4-01 | Board-level cybersecurity governance program | CISO/Board | GV.OC-01 | GV.OC-01 | $50K | OPEN |
| P4-02 | Annual medical device penetration testing | Security | 164.308(a)(1) | ID.RA-01 | $75K | OPEN |
| P4-03 | Implement automated PHI discovery/classification | Security | 164.514 | ID.AM-05 | $100K | OPEN |
| P4-04 | SOC tabletop exercises (ransomware scenarios) | SOC/GRC | 164.308(a)(6) | RS.MA-01 | $30K | OPEN |
| P4-05 | Achieve HITRUST CSF certification | GRC | All | All | $200K | OPEN |

**Phase 4 Total: ~$455K**

---

## Risk Reduction Timeline

| Timeframe | Current Risk | Target Risk | Key Milestone |
|---|---|---|---|
| Day 30 | Critical | High | MFA + EDR deployed |
| Day 90 | High | High | SIEM + SOC operational |
| Day 180 | High | Moderate | Network segmentation complete |
| Day 365 | Moderate | Low-Moderate | HITRUST certification |

---

## Metrics & KPIs

| Metric | Current | 90-Day Target | 12-Month Target |
|---|---|---|---|
| Mean Time to Detect (MTTD) | 5 days | 4 hours | 1 hour |
| Mean Time to Respond (MTTR) | 4 months | 72 hours | 24 hours |
| % Endpoints with EDR | ~0% | 90% | 100% |
| % PHI Systems with MFA | ~0% | 100% | 100% |
| % Staff phishing trained | Low | 80% | 100% |
| Backup recovery tested | Never | Quarterly | Monthly |

---

## Lessons Learned

1. **Detection over prevention** — The 5-day dwell time shows prevention alone
   failed. Invest equally in detection (SIEM, EDR, UEBA).

2. **Downtime procedures save lives** — A children's hospital cannot afford
   4-month EHR outages. Tested downtime procedures are not optional.

3. **Flat networks are indefensible** — Once inside, attackers move freely.
   Segmentation limits blast radius.

4. **Medical devices are the blind spot** — OT/medical device security must
   be part of every hospital's security program.

5. **Breach notification timing matters** — 6-month delay in notifying 791,784
   individuals violates HIPAA and destroys patient trust.

---

*Remediation Roadmap by Ashwatha Narayan*
*Frameworks: HIPAA Security Rule | NIST CSF 2.0 | MITRE ATT&CK | IEC 62443*
*May 2026*
