# Risk Scoring Methodology
## Ann & Robert H. Lurie Children's Hospital GRC Assessment

---

## Overview

This assessment uses a **semi-quantitative risk scoring methodology** based on
NIST SP 800-30 Rev 1 (Guide for Conducting Risk Assessments) and adapted for
healthcare environments per HHS Office for Civil Rights guidance.

Risk Score = Likelihood × Impact

---

## Likelihood Scale

| Score | Rating | Definition | Example |
|---|---|---|---|
| 1 | Very Low | Unlikely to occur — strong controls in place | Nation-state physical attack |
| 2 | Low | Could occur — some controls present | Insider sabotage |
| 3 | Medium | Moderately likely — partial controls | Phishing with basic email filter |
| 4 | High | Likely to occur — weak or missing controls | Phishing with no advanced protection |
| 5 | Very High | Almost certain — no controls present | Unpatched internet-facing system |

---

## Impact Scale

| Score | Rating | Definition | Patient Safety Impact |
|---|---|---|---|
| 1 | Very Low | Minimal operational impact | None |
| 2 | Low | Minor disruption — contained quickly | None |
| 3 | Medium | Moderate disruption — hours of downtime | Delayed non-urgent care |
| 4 | High | Significant disruption — days of downtime | Cancelled surgeries/procedures |
| 5 | Critical | Catastrophic — weeks/months of downtime | Direct patient safety risk |

---

## Risk Score Matrix

| | **Very Low (1)** | **Low (2)** | **Medium (3)** | **High (4)** | **Critical (5)** |
|---|---|---|---|---|---|
| **Very High (5)** | 5 | 10 | 15 | 20 | 25 |
| **High (4)** | 4 | 8 | 12 | 16 | 20 |
| **Medium (3)** | 3 | 6 | 9 | 12 | 15 |
| **Low (2)** | 2 | 4 | 6 | 8 | 10 |
| **Very Low (1)** | 1 | 2 | 3 | 4 | 5 |

---

## Risk Priority Thresholds

| Score Range | Priority | Action Required |
|---|---|---|
| 20–25 | Critical | Immediate remediation within 30 days |
| 12–19 | High | Remediation within 90 days |
| 8–11 | Medium | Remediation within 180 days |
| 4–7 | Low | Remediation within 12 months |
| 1–3 | Very Low | Monitor and review annually |

---

## Healthcare-Specific Adjustments

Standard IT risk assessments are adjusted for healthcare context:

### Patient Safety Multiplier
Any risk with direct patient safety implications receives a +1 impact adjustment:
- Medical device compromise → direct harm potential
- EHR unavailability → care delivery disruption
- Medication system compromise → dosing errors

### Pediatric Data Multiplier
Risks involving minor PHI receive a +1 likelihood adjustment due to:
- 18+ year exploitation window for SSNs of minors
- Higher long-term identity theft risk
- Additional regulatory obligations (COPPA, Illinois PIPA)

### Regulatory Exposure Factor
HIPAA violations add a separate regulatory risk dimension:
- Tier 1 (unknowing): $100–$50,000 per violation
- Tier 2 (reasonable cause): $1,000–$50,000 per violation
- Tier 3 (willful neglect corrected): $10,000–$50,000 per violation
- Tier 4 (willful neglect uncorrected): $50,000 per violation

---

## Data Sources

All risk ratings are based on:
1. HHS OCR breach portal filing (791,784 individuals affected)
2. Maine Attorney General breach notification
3. Forensic investigation findings (5-day dwell time confirmed)
4. FBI investigation statements
5. Class action lawsuit filing details
6. Verified press reports (HIPAA Journal, Healthcare Dive, Bleeping Computer)
7. Rhysida ransomware group TTPs (CISA Advisory AA23-319A)

---

## Limitations

- This assessment is based on publicly available information only
- Actual internal control states may differ from observed external indicators
- Risk scores reflect point-in-time assessment (May 2026)
- No access to internal systems, policies, or procedures was obtained

---

*Methodology by Ashwatha Narayan | NIST SP 800-30 Rev 1 | HHS OCR Guidance*
*May 2026*
