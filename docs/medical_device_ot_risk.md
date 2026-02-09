# Medical Device & OT Security Risk Assessment
## Ann & Robert H. Lurie Children's Hospital of Chicago
### OT/IT Convergence Risk | January 2024 Breach Context

---

## Overview

Modern hospitals operate a complex OT environment that is frequently overlooked
in traditional IT security assessments. Lurie Children's Hospital, as a major
pediatric academic medical center, operates hundreds of networked medical devices
that represent a critical — and largely unprotected — attack surface.

This section applies OT security principles (IEC 62443, NIST SP 800-82) to the
hospital's medical device ecosystem, drawing direct parallels to the January 2024
Rhysida ransomware attack.

---

## Medical Device Inventory (Estimated)

| Device Category | Estimated Count | Network Connected | Legacy OS Risk |
|---|---|---|---|
| Infusion Pumps | 200+ | Yes | HIGH |
| Patient Monitors | 150+ | Yes | MEDIUM |
| Imaging Systems (MRI/CT) | 20+ | Yes | CRITICAL |
| Ventilators | 50+ | Yes | HIGH |
| Laboratory Analyzers | 30+ | Yes | MEDIUM |
| Building Management Systems | Multiple | Yes | HIGH |
| Nurse Call Systems | Hospital-wide | Yes | MEDIUM |
| Medication Dispensing (Pyxis) | 50+ | Yes | HIGH |

**Critical Finding:** All of the above device categories were potentially exposed
during the January 2024 breach due to flat network architecture.

---

## Network Architecture Risk Analysis

### Current State (Pre-Breach)[Internet] → [Firewall] → [Flat Hospital Network]
↓
┌───────────────────────────────────────┐
│  Clinical Workstations                │
│  Epic EHR Servers                     │
│  Administrative Systems               │
│  Medical Devices (Infusion Pumps)     │
│  Imaging Systems (MRI/CT)             │
│  Building Management Systems          │
└───────────────────────────────────────┘
**All systems on the same flat network — lateral movement trivial for attacker.**

### Recommended State (Purdue Model)[Internet] → [DMZ] → [Enterprise Zone (Level 4-5)]
↓
[Clinical IT Zone (Level 3)]
↓
[Medical Device Zone (Level 2)]
↓
[Device Control Zone (Level 1)]
↓
[Physical Devices (Level 0)]---

## MITRE ATT&CK for ICS — Hospital Context

| Technique | ID | Hospital Scenario | Risk |
|---|---|---|---|
| Initial Access via Spearphishing | T0817 | Staff phishing email — confirmed initial vector | CRITICAL |
| Lateral Movement | T0812 | Flat network enabled spread to clinical systems | CRITICAL |
| Inhibit Response Function | T0816 | EHR taken offline — clinical response inhibited | CRITICAL |
| Denial of Control | T0814 | Infusion pumps potentially inaccessible | CRITICAL |
| Manipulation of Control | T0831 | Medication dispensing systems at risk | HIGH |
| Spoof Reporting | T0856 | Patient monitor readings potentially manipulated | HIGH |

---

## Patient Safety Risk Analysis

The January 2024 breach created direct patient safety risks:

### Confirmed Safety Impacts
- Surgeries cancelled or delayed due to EHR unavailability
- Prescription refills inaccessible via MyChart for weeks
- Ultrasound results inaccessible during patient appointments
- Staff forced to manual paper-based medication administration
- Blood transfusion scheduling disrupted

### Potential Safety Impacts (If OT Compromised)
- **Infusion pump manipulation** — incorrect drug dosing in pediatric patients
- **Ventilator interference** — life-critical device disruption
- **Medication dispensing errors** — Pyxis system compromise
- **Lab result manipulation** — incorrect diagnoses based on falsified results

**Note:** No evidence exists that medical devices were directly manipulated
in this attack. However, the flat network architecture made such attacks
theoretically possible during the 5-day dwell period.

---

## IEC 62443 Gap Analysis (Medical Device Context)

| Zone | IEC 62443 Requirement | Hospital Finding | Gap |
|---|---|---|---|
| Security Level 1 | Basic protection | Partial firewall only | HIGH |
| Security Level 2 | Protection against intentional violation | No network segmentation | CRITICAL |
| Security Level 3 | Protection against sophisticated attack | No OT monitoring | CRITICAL |
| Security Level 4 | Protection against state-level attack | Not applicable | N/A |

---

## Medical Device Security Recommendations

### Immediate (0-30 days)
1. **Device inventory audit** — catalog all networked medical devices
2. **Emergency VLAN segmentation** — isolate medical devices from clinical IT
3. **Disable unnecessary network services** on all medical devices

### Short-term (30-90 days)
4. **Deploy medical device security platform** (Claroty, Medigate, or Armis)
5. **Implement Purdue Model network architecture**
6. **Establish medical device patching program** with vendor coordination

### Long-term (90 days - 12 months)
7. **Zero-trust microsegmentation** for medical device zones
8. **OT-specific incident response playbook**
9. **Medical device security policy** aligned to FDA cybersecurity guidance
10. **Annual medical device penetration testing**

---

## FDA Cybersecurity Alignment

The FDA's 2023 cybersecurity guidance for medical devices (Section 524B of FD&C Act)
requires manufacturers to submit cybersecurity plans for new devices. However,
hospitals remain responsible for:

- Network segmentation of medical devices
- Monitoring medical device network traffic
- Coordinating with manufacturers on patches
- Maintaining device inventory and risk assessments

Lurie Children's Hospital showed significant gaps in all four areas.

---

*Assessment by Ashwatha Narayan | IEC 62443 | NIST SP 800-82 | FDA Medical Device Cybersecurity*
*May 2026*
