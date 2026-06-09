<h2> Security Azimuth Check </h2>

<div class="audit-wrap">
  <div class="audit-card audit-hero" style="position:relative; overflow:hidden; padding:2rem 2rem 1.5rem; border:1px solid #233044; border-radius:22px; background:linear-gradient(145deg, #0b1220 0%, #111a2e 52%, #0e1627 100%); box-shadow:0 18px 40px rgba(2,6,23,.28); color:#e5eefb;">
    <div style="position:absolute; inset:-80px auto auto -80px; width:220px; height:220px; border-radius:999px; background:radial-gradient(circle, rgba(56,189,248,.18) 0%, rgba(56,189,248,0) 70%);"></div>
    <div style="position:absolute; inset:auto -70px -70px auto; width:240px; height:240px; border-radius:999px; background:radial-gradient(circle, rgba(34,197,94,.12) 0%, rgba(34,197,94,0) 72%);"></div>
    <div class="audit-eyebrow" style="display:inline-block; padding:.35rem .7rem; border:1px solid rgba(148,163,184,.25); border-radius:999px; background:rgba(15,23,42,.35); color:#93c5fd; font-size:.78rem; letter-spacing:.08em; text-transform:uppercase;">Objective review artifact</div>
    <h1 class="audit-title" style="margin:.85rem 0 .55rem; font-size:2.1rem; line-height:1.08; letter-spacing:-.03em; color:#f8fbff;">Review of Current Homelab Security Plan</h1>
    <p class="audit-text" style="max-width:60rem; margin:0 0 1rem; color:#cbd5e1; font-size:1rem; line-height:1.7;">This review evaluates the current plan described by <code style="padding:.15rem .4rem; border-radius:.45rem; background:rgba(148,163,184,.14); color:#e2e8f0;">Redacted</code> against recognized security frameworks and standards, using the National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) 2.0 as the primary lens and the Center for Internet Security (CIS) Controls v8 as the control catalog, with emphasis on segmentation, access control, monitoring, protocol handling, and documented assurance. The review is intentionally evidence-oriented and separates architectural strengths from unsupported claims, missing controls, and areas where reviewer-specific comments should be added.</p>
     <div aria-hidden="true" style="display:flex; justify-content:center; margin:1.25rem 0 1.1rem;">
      <img src="./azimuth.png"
           alt="Security Azimuth logo"
           style="width:164px; height:auto; border-radius:24px; box-shadow:0 14px 30px rgba(15,23,42,0.7);" />
    </div>
    <div class="audit-badges" style="display:flex; flex-wrap:wrap; gap:.55rem;">
      <span class="audit-badge primary" style="padding:.45rem .75rem; border-radius:999px; background:#0f766e; color:#ecfeff; border:1px solid rgba(255,255,255,.08);">Disposition: Revise and strengthen</span>
      <span class="audit-badge ok" style="padding:.45rem .75rem; border-radius:999px; background:#14532d; color:#f0fdf4; border:1px solid rgba(255,255,255,.08);">Strongest area: Network segmentation</span>
      <span class="audit-badge warn" style="padding:.45rem .75rem; border-radius:999px; background:#7c2d12; color:#fff7ed; border:1px solid rgba(255,255,255,.08);">Weakest area: Validation evidence</span>
      <span class="audit-badge" style="padding:.45rem .75rem; border-radius:999px; background:rgba(30,41,59,.9); color:#dbeafe; border:1px solid rgba(148,163,184,.22);">Framework lens: NIST CSF 2.0</span>
      <span class="audit-badge" style="padding:.45rem .75rem; border-radius:999px; background:rgba(30,41,59,.9); color:#dbeafe; border:1px solid rgba(148,163,184,.22);">Control lens: CIS Controls v8</span>
      <span class="audit-badge" style="padding:.45rem .75rem; border-radius:999px; background:rgba(30,41,59,.9); color:#dbeafe; border:1px solid rgba(148,163,184,.22);">Protocol refs: RFC 1918 / RFC 4193</span>
    </div>
  </div>

  <details class="audit-details">
    <summary><strong>Rating methodology reference</strong></summary>

| Rating area | Scale used | Meaning | Source |
|---|---|---|---|
| National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) 2.0 implementation tier | Tier 1–4 | Tier 1 = Partial, Tier 2 = Risk-Informed, Tier 3 = Repeatable, Tier 4 = Adaptive | [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) |
| Center for Internet Security (CIS) Controls v8 maturity | Level 1–5 (internal mapping) | Internal scoring shorthand used to describe how completely the documented controls appear to be implemented and evidenced; this is an audit-layer maturity summary, not an official CIS numeric scale | [CIS Controls v8 Overview](https://www.cisecurity.org/controls/v8) |
| CIS Controls v8 implementation groups | IG1–IG3 | IG1 = basic cyber hygiene, IG2 = additional protections for more complexity, IG3 = mature protections for higher-risk environments | [CIS Controls Implementation Groups](https://www.cisecurity.org/controls/implementation-groups) |
| NIST CSF function status language | Weak / Partial / Moderate / Strong | Plain-language reviewer shorthand used to summarize how well the current plan addresses a CSF function based on the evidence present in the document | [NIST Cybersecurity Framework (CSF) 2.0 Core](https://www.nist.gov/cyberframework) |
| Objective evidence strength | Low / Emerging / Established | Reviewer shorthand for how much validation evidence is actually included, such as diagrams, rule matrices, logs, captures, test records, and recovery proof | [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) |

<p><strong>Scoring note:</strong> This review uses NIST CSF 2.0 implementation tiers as the primary maturity language and CIS Controls v8 as the control-family and implementation-group lens.</p>
  </details>

  <div class="audit-grid">
    <div class="audit-panel">
      <h3>What the current plan does well</h3>
      <p>The plan is strongest in segmentation, internal boundary control, and reduction of easy lateral movement. It also shows mature awareness that Internet Protocol version 6 (IPv6) must be controlled separately from Internet Protocol version 4 (IPv4), which is often missed in homelab writeups.</p>
    </div>
    <div class="audit-panel">
      <h3>What the current plan does not yet prove</h3>
      <p>The writeup does not yet provide objective validation artifacts such as rule exports, packet captures, log excerpts, access tests, exception inventories, or incident-handling evidence. As written, it reads more like an architecture narrative than a defensible audit package.</p>
    </div>
    <div class="audit-panel">
      <h3>Overall assessment</h3>
      <p>The design intent is better than the documentation quality. The network policy model appears thoughtful, but the report currently overstates assurance relative to the evidence presented.</p>
    </div>
  </div>

## Linux privilege layers

```text
+--------------------------------------------------------------+
| "Ring -3" : Firmware / Management Engine                     |
|  - Unified Extensible Firmware Interface (UEFI) / BIOS       |
|  - Intel Management Engine (ME) / AMD Platform Security      |
|    Processor (PSP), Baseboard Management Controller (BMC)    |
+----------------------------+---------------------------------+
                             |
                             v
+--------------------------------------------------------------+
| "Ring -2" : System Management Mode (SMM) / Secure Monitor   |
|  - System Management Mode (SMM)                              |
|  - Low-level monitors / EL3-equivalent                       |
+----------------------------+---------------------------------+
                             |
                             v
+--------------------------------------------------------------+
| "Ring -1" : Hypervisor                                       |
|  - Kernel-based Virtual Machine (KVM), Xen, other VMMs       |
|  - Runs guest kernels in non-root mode                       |
+----------------------------+---------------------------------+
                             |
                             v
+--------------------------------------------------------------+
| Ring 0 : Kernel (guest operating system)                     |
|  - Linux kernel                                              |
|  - Drivers, memory management, I/O, system calls             |
+----------------------------+---------------------------------+
                             |
                             v
+--------------------------------------------------------------+
| Rings 1–2 : Unused by Linux                                  |
|  - Architecturally defined on x86                            |
|  - Typically not used by Linux                               |
+----------------------------+---------------------------------+
                             |
                             v
+--------------------------------------------------------------+
| Ring 3 : User space                                          |
|  - Processes, shells, services, containers                   |
|  - Applications running as users                             |
+--------------------------------------------------------------+
```

<details>
  <summary><strong>Framework-based scorecard</strong></summary>

  <h2 class="audit-section-title">Framework-based scorecard</h2>
  <div class="audit-scorecard">
    <div class="audit-score">
      <div class="audit-score-head"><span>Identify (NIST CSF) and Network (CIS)</span><span class="audit-pill">Tier 2–3 / CIS Level ~2–3</span></div>
      <div class="audit-meter"><span style="width:80%"></span></div>
      <p>VLAN segmentation, administrative-device exceptions, and demilitarized zone (DMZ) separation are meaningful controls aligned with network boundary protection objectives.</p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Access control (NIST / CIS)</span><span class="audit-pill">Tier 2 / CIS Level ~2</span></div>
      <div class="audit-meter"><span style="width:60%"></span></div>
      <p>The plan shows partial least-privilege thinking through aliases and narrow exceptions, but it does not yet document Multi-Factor Authentication (MFA), administrative workflow assurance, credential protection, or session controls.</p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Detect (NIST CSF)</span><span class="audit-pill">Tier 2 / CIS Level ~2</span></div>
      <div class="audit-meter"><span style="width:60%"></span></div>
      <p>Suricata and Zenarmor add meaningful detection capability, but the report does not yet show alert tuning, retention, triage process, false-positive handling, or downstream logging and response procedures.</p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Recover (NIST CSF)</span><span class="audit-pill">Tier 1</span></div>
      <div class="audit-meter"><span style="width:20%"></span></div>
      <p>The current plan does not document backups, restore testing, incident recovery workflow, or failure-mode handling for the controls it depends on.</p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Auditability (CIS / NIST)</span><span class="audit-pill">Level ~1</span></div>
      <div class="audit-meter"><span style="width:20%"></span></div>
      <p>The report contains many claims of effect, but almost no direct evidence, measurements, screenshots, or test results. This is the biggest gap in the current package.</p>
    </div>
  </div>
</details>

<details>
  <summary><strong>Objective control mapping</strong></summary>

  <h2 class="audit-section-title">Objective control mapping</h2>

| Plan element | Observed strength | Objective weakness | Recommendation |
|---|---|---|---|
| Dual 10G physical separation for trusted vs. DMZ traffic | Strong boundary separation concept that reduces accidental mixing of trust zones. | The report does not show interface diagrams, switchport assignments, or verification that traffic cannot bypass intended separation. | Add deployment-specific notes here. |
| VLAN segmentation into management, trusted, private servers, DMZ, and Internet of Things (IoT) / guest | Good segmentation pattern consistent with reducing lateral movement and scoping exposure. | No rule matrix, inter-VLAN flow table, or validation test results are shown. There is also no asset inventory tied to each VLAN. | Add VLAN-specific findings here. |
| RFC 1918-based internal block rules | Good default-deny intent for IPv4 internal traffic between zones. | RFC 1918 applies to IPv4 private space only, so the report must clearly separate IPv4 logic from IPv6 logic and show rule parity. | Add IPv4 rule review notes here. |
| Administrative device alias for management access | Better than broad subnet trust because it narrows privileged access to named systems. | Internet Protocol (IP)-based trust is not the same as identity assurance; no MFA, device health, certificate trust, or administrative session controls are documented. | Add management-plane concerns here. |
| Native local area network (LAN) lock to network-hardware alias | Strong anti-misuse idea for untagged infrastructure ports. | The report does not prove port-security behavior, switch configuration, or what happens during switch replacement, emergency maintenance, or mispatching. | Add switch and port validation notes here. |
| DMZ to private-server micro-allowlisting | Strongest control in the writeup because it scopes cross-zone exposure to named application paths. | No service dependency map, allowed-port inventory, or validation test is included, and no host-layer hardening is documented for the allowlisted targets. | Add service-path review notes here. |
| Forced DNS via Network Address Translation (NAT) redirect on port 53 | Useful for traditional DNS control and policy enforcement. | The report does not discuss DNS over HTTPS, DNS over TLS, QUIC-based bypass paths, or how exceptions are detected and blocked. | Add DNS bypass observations here. |
| IPv6 Unique Local Address (ULA) with NAT66 | Shows awareness that IPv6 must be governed explicitly and separately. | The report should justify NAT66 operationally, define policy parity with IPv4, and explain residual risks and tradeoffs. | Add IPv6 architecture notes here. |
| Zenarmor Next-Generation Firewall (NGFW) on internal interfaces | Adds application visibility and policy depth beyond port-level filtering. | No evidence is shown for policy sets, exception handling, update cadence, or how detection output feeds response. | Add deep packet inspection (DPI) policy notes here. |
| Suricata Intrusion Prevention System (IPS) on WAN / DMZ edge | Appropriate perimeter detection and block control for exposed services. | No description of ruleset source, tuning, alert fatigue handling, or packet-drop validation is provided. | Add IPS tuning notes here. |
| Geographic IP (GeoIP) restrictions on WAN forwards | Can reduce opportunistic scan exposure. | GeoIP is only a coarse filter; it is not identity, and it is bypassable through Virtual Private Networks (VPNs), proxies, and cloud egress regions. The report overstates its effect with “99%” language without measurement evidence. | Add exposure-reduction notes here. |
</details>

<details>
  <summary><strong>Strengths</strong></summary>

  <h2 class="audit-section-title">Observed strengths</h2>
  <div class="audit-list">
    <div class="audit-card">
      <strong>1. Segmentation is intentional rather than cosmetic.</strong>
      <p>The current plan separates management, user, server, public, and untrusted device roles into distinct zones instead of relying on a single flat network. That is a concrete architectural strength because it supports narrower trust boundaries and better scoping of access rules.</p>
      <details><summary>Recommendation</summary><textarea>This segmentation model is a strong foundation for homelab security. For this environment, keep the current zone layout (management, user, server, DMZ, IoT/guest), but make sure each zone has: (1) a clearly documented IP range, (2) explicit inter-zone rules in a matrix, and (3) one or two validation tests showing that traffic cannot bypass the intended boundaries. This will turn a good design idea into a verifiable control.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>2. The plan uses default-deny thinking for east-west traffic.</strong>
      <p>The described RFC 1918 block model and application-specific exceptions reflect a genuine least-privilege mindset for lateral movement reduction. This is one of the strongest parts of the current plan.</p>
      <details><summary>Recommendation</summary><textarea>The default-deny approach for east-west traffic is one of the most valuable controls in this design. To preserve that strength over time, keep a small, reviewed list of explicit allow rules per VLAN pair, and add a short justification for each. Consider scheduling a quarterly review where you remove stale exceptions and re-test that blocked paths are still blocked.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>3. The plan recognizes IPv6 as a separate policy domain.</strong>
      <p>Many otherwise competent network writeups ignore IPv6 entirely; this one does not. The explicit treatment of Unique Local Address (ULA) space and IPv6 rule intent is a meaningful strength even though the documentation still needs refinement.</p>
      <details><summary>Recommendation</summary><textarea>Treating IPv6 as a first-class policy domain is a major differentiator from typical homelabs. To build on this, maintain side-by-side IPv4 and IPv6 rule intent for each zone, such as a simple table showing what is allowed over version 4 and version 6. Make sure every new rule is evaluated for both families so you do not accidentally create an IPv6 back door for flows that are blocked over IPv4.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>4. Public-service exposure is narrowed through multiple layers.</strong>
      <p>The DMZ design, micro-allowlisting, IPS, and GeoIP filtering show that exposure control is layered rather than dependent on a single port-forward decision. That layered approach is directionally strong.</p>
      <details><summary>Recommendation</summary><textarea>For the next revision, document each exposed service as a discrete access path rather than as a general DMZ concept. For every public-facing application, list: (1) the public hostname or entry point, (2) the reverse proxy or DMZ host that receives the request, (3) the exact backend service and port it is allowed to reach, (4) the authentication or access control applied at the edge, and (5) the log source that records successful and denied access. A small service-dependency map and one validation test per exposed service would make this section much easier to review and would show that public exposure remains intentionally narrow as the environment evolves.</textarea></details>
    </div>
  </div>
</details>

<details>
  <summary><strong>Weaknesses</strong></summary>

  <h2 class="audit-section-title">Recommended corrections</h2>
  <p class="audit-text">Each card below includes an inline reviewer comment area intended as a working space for future reviewers to capture environment-specific notes and decisions.</p>
  <div class="audit-list">
    <div class="audit-card">
      <strong>1. The report overstates assurance relative to evidence.</strong>
      <p>The document frequently claims outcomes such as trapping attackers, eliminating exposure, or stopping compromise, but it does not include proof artifacts to support those outcomes. Audit-quality language must tie claims to tests, logs, diagrams, or measured results.</p>
      <details><summary>Reviewer comment area</summary><textarea>Please replace broad outcome claims such as “stops attackers,” “physically traps,” or “eliminates exposure” with statements tied to specific evidence. For each major control, attach or reference at least one concrete artifact: a diagram, rule export, test result, log snippet, or packet capture. The goal is for a third party to see not just what is intended, but what has actually been verified in this environment.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>2. Identity and privileged access controls are under-documented.</strong>
      <p>The current plan treats administrative devices as privileged based on IP assignment, but it does not show stronger management controls such as MFA, certificate-bound access, Privileged Access Management (PAM) policy, separate administrative workflows, or management-plane session assurance.</p>
      <details><summary>Reviewer comment area</summary><textarea>The current writeup focuses on which IPs can reach management interfaces, but it does not yet show how administrator identity is verified or how privileged sessions are governed. Please add detail on: (1) which accounts can administer the firewall, hypervisor, and key servers; (2) where Multi-Factor Authentication (MFA) is enforced; (3) whether Secure Shell (SSH) keys or certificates are used instead of passwords and, if so, which non-deprecated key exchange and signature algorithms are in use (for example, alternatives to rsa2048 such as sntrup761/x25519, as described in [RFC 9941](https://datatracker.ietf.org/doc/rfc9941/) and [RFC 9941 summary](https://www.rfc-editor.org/info/rfc9941/)); and (4) how administrative actions are logged and reviewed. This will bring the access model closer to least privilege rather than trust by IP address alone. The goal is to both show and tell: document the design and back it with observable evidence.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>3. Host and workload hardening are mostly absent from the writeup.</strong>
      <p>The report is strong on network policy but thin on endpoint, container, virtual machine (VM), and host-layer hardening. There is no visible discussion of patching cadence, endpoint detection and response (EDR), file integrity monitoring, secure boot, kernel hardening, or workload isolation assumptions.</p>
      <details><summary>Reviewer comment area</summary><textarea>Network policy is well developed, but the host and workload layer is under-documented. For the next revision, please describe: (1) the patching approach and frequency for hosts, containers, and appliances; (2) which hardening baselines or controls you apply, such as AppArmor, Security-Enhanced Linux (SELinux), minimal packages, and Secure Shell (SSH) hardening; and (3) how you separate high-risk services, such as lab workloads or internet-facing applications, from more sensitive data-bearing systems. This ensures the inside of each segment is as defensible as the boundaries.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>4. Detection controls are described, but response workflow is not.</strong>
      <p>The writeup names Suricata and Zenarmor, but it does not explain where alerts go, who reviews them, how often they are triaged, what constitutes a false positive, or how incidents are handled after detection.</p>
      <details><summary>Reviewer comment area</summary><textarea>The plan needs to show how detections move from “alert exists” to “action taken.” Please add a short description or diagram of: (1) where alerts and logs from these tools go; (2) who reviews them and how often; (3) how real issues are distinguished from noise; and (4) what happens when a suspicious event is confirmed, such as blocking a flow, isolating a host, or collecting evidence. Even a simple homelab-sized response workflow will strengthen this section.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>5. Several claims need narrower and more accurate wording.</strong>
      <p>Phrases like “physically trapped,” “violently drops,” “God Mode,” and “99%” read as charged language rather than audit language. The report should describe control function, scope, and limitations in neutral terms with a lexicon that reflects deep understanding of recognized standards.</p>
      <details><summary>Reviewer comment area</summary><textarea>Please revise promotional or visceral language into neutral, scoped descriptions such as “contained within the VLAN,” “denies and logs traffic that does not match allow rules,” “administrative access,” or “reduces unsolicited traffic from disallowed regions.” Where you include numbers such as percentages or coverage, tie them to an actual measurement rather than an estimate. This will make the report more credible because the evidence, not the tone, carries the argument.</textarea></details>
    </div>
  </div>
</details>

<details>
  <summary><strong>Recommended objective metrics</strong></summary>

  <h2 class="audit-section-title">Recommended objective metrics</h2>

| Control area | Metric to add | Why it matters |
|---|---|---|
| VLAN segmentation | Number of authorized inter-VLAN flows vs. denied flows per review period | Demonstrates that segmentation is defined and measured rather than assumed. |
| Administrative access | Count of management interfaces exposed; count of systems allowed to reach them | Shows whether privileged access scope is minimized. |
| DNS enforcement | Percentage of DNS requests observed through approved resolver path; count of blocked direct DNS attempts | Validates whether “forced DNS” is actually working. |
| Suricata | Alerts per day, true-positive rate after tuning, drop count for relevant signatures | Converts IPS claims into measurable operational effectiveness. |
| Zenarmor | Blocked application categories, exceptions granted, update cadence | Shows whether Layer 7 (L7) policy is governed and maintained. |
| Public exposure | Number of WAN-exposed services, allowed source countries, authentication controls per service | Makes internet exposure concrete and reviewable. |
| Recovery | Backup frequency, restore test frequency, last successful restore date | Addresses resilience, not just prevention. |
| Change control | Firewall rule review interval, number of stale rules removed, documented exceptions | Prevents segmentation drift over time. |

<p>These metrics correspond directly to the framework-based scorecard above, and collecting them regularly will allow future reviews to assign NIST CSF tiers and CIS Controls v8 maturity levels based on observed data rather than design intent alone.</p>
</details>

<details>
  <summary><strong>Standards and reference corrections</strong></summary>

  <h2 class="audit-section-title">Standards and reference corrections</h2>
  <div class="audit-list">
    <div class="audit-card">
      <strong>RFC 1918 usage</strong>
      <p>Use RFC 1918 only when referring to the IPv4 private ranges 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Do not use it as shorthand for all internal addressing or as an IPv6 concept.</p>
      <details><summary>Reviewer comment area</summary><textarea>In this environment, please be explicit whenever you mean “IPv4 RFC 1918 private space” versus “internal addresses in general.” Where you talk about internal routing, Access Control Lists (ACLs), or block rules, call out whether they apply only to 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 or also to public or other internal ranges. This will make it easier for a reviewer to see exactly which traffic is covered and avoid confusion when IPv6 or public IP space is introduced later.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>IPv6 ULA usage</strong>
      <p>Use RFC 4193 when discussing Unique Local Addresses (ULAs) for IPv6. If NAT66 remains part of the design, explain the operational reason for it, the tradeoffs, and how policy consistency is maintained across IPv4 and IPv6.</p>
      <details><summary>Reviewer comment area</summary><textarea>For the next revision, please include a short IPv6 addressing plan describing which prefixes are used per VLAN and whether Unique Local Addresses (ULAs) and Global Unicast Addresses (GUAs) are present. Also include a one-paragraph rationale for using ULA space and any NAT66 constructs. The goal is to show that IPv6 policy is deliberately designed and that firewall rules, DNS behavior, and logging are consistent with the IPv4 model rather than bolted on as an afterthought.</textarea></details>
    </div>
    <div class="audit-card">
      <strong>Compliance wording</strong>
      <p>Do not imply Federal Information Processing Standards (FIPS), NIST, or similar compliance from architecture quality alone. If a compliance-adjacent term is used, it should be tied to a defined control, a documented requirement, and supporting evidence.</p>
      <details><summary>Reviewer comment area</summary><textarea>When you reference frameworks or standards such as FIPS, RFC, NIST, or CIS, please treat them as lenses rather than badges. For each such mention, either point to a specific control you believe you satisfy or soften the language to “aligned with” or “informed by” instead of implying formal compliance. This will keep the report accurate for a homelab context while still signaling good practice.</textarea></details>
    </div>
  </div>

  <h2 class="audit-section-title">Framework alignment summary</h2>

| Framework area | Current status | Notes |
|---|---|---|
| NIST CSF — Identify | Partial | Zones and asset roles are implied, but a formal asset inventory and dependency mapping are not shown. |
| NIST CSF — Protect | Moderate | Segmentation and filtering are the strongest documented areas. |
| NIST CSF — Detect | Partial | IPS and NGFW are present, but alert operations are undocumented. |
| NIST CSF — Respond | Weak | No incident workflow, ownership, or escalation path is described. |
| NIST CSF — Recover | Weak | No backup, restore, or resilience testing evidence is described. |
| CIS Controls v8 — Network infrastructure management | Moderate | Good control intent, weak evidence and maintenance documentation. |
| CIS Controls v8 — Access control management | Partial | Alias-based narrowing exists, but identity assurance and administrative governance are thin. |
| CIS Controls v8 — Audit log management | Weak | Logging and review workflow are not documented. |
| CIS Controls v8 — Secure configuration | Partial | Configuration intent is strong, but baselines and change control are not shown. |

  <div class="audit-note">
    <strong>Reviewer guidance:</strong>
    The current plan should be graded as a promising technical design that needs a more rigorous audit package with objective testing results to show security as a spectrum rather than a binary secure / insecure claim. The next revision should add a network diagram, rule matrix, validation tests, exception inventory, configuration snippets, logging flow, and recovery evidence before stronger assurance claims are made. A skeleton example follows.

```text
### Example homelab network diagram

                          ┌─────────────────────────────┐
                          │           Internet          │
                          └──────────────┬──────────────┘
                                         │
                                         │ WAN
                                  ┌──────▼──────┐
                                  │ Edge Router │
                                  │ / Firewall  │
                                  └──────┬──────┘
                                         │
                               Trunk (VLANs 10/20/30/40/50)
                                         │
                                   ┌─────▼─────┐
                                   │  Core /   │
                                   │  Layer 3  │
                                   │  Switch   │
                                   └─┬────┬────┘
      ┌──────────────────────────────┘    └──────────────────────────────┐
      │                                                                   │

  VLAN 10 - Management                           VLAN 20 - Trusted / Users
  192.168.10.0/24                                192.168.20.0/24
  ────────────────────────────                   ────────────────────────────
  - Hypervisor management (Proxmox / ESXi)       - Workstations / laptops
  - Switch / wireless access point management    - Administrative workstation
    Internet Protocol addresses                  - Developer boxes
  - Out-of-band Intelligent Platform             - Internal print / file
    Management Interface (IPMI) / BMC
  - Jump host / bastion

      │ upstream only from admin alias               │ egress to core services
      └─────────────▲───────────────────────────────┘
                    │
                    │ tightly controlled ACLs / firewall rules

  VLAN 30 - Server / Private Services          VLAN 40 - DMZ / Public Services
  192.168.30.0/24                              192.168.40.0/24
  ────────────────────────────                 ────────────────────────────
  - Internal DNS / DHCP                        - Public-facing web apps
  - Internal Git / continuous integration      - Reverse proxy
  - Monitoring (Prometheus, Grafana)           - VPN termination
  - Internal databases                         - Any test internet-facing labs

      ▲    ▲                                         ▲
      │    └──── micro-allowlist from DMZ ───────────┘
      │           (only specific ports / hosts)
      │
      │ east-west default-deny between VLANs
      │
  VLAN 50 - IoT / Guest
  192.168.50.0/24
  ────────────────────────────
  - Smart televisions, cameras
  - Guest Wi‑Fi clients
  - Other untrusted devices

  - Only allowed out to:
    – Internet (via firewall rules)
    – Very specific internal services (if needed)
  - No direct reachability to Management or Server VLANs
```

<details>
  <summary><strong>Example documented configuration profiles</strong></summary>

  <p>These example configuration profiles are not drop-in templates, but documented baselines showing how this homelab could be aligned with the segmentation and detection intent described earlier. They should be adapted to the actual interfaces, VLAN names, rulesets, and policy objects used in production.</p>

  <details>
    <summary><strong>Zenarmor documented policy profile</strong></summary>

```yaml
# Zenarmor policy baseline (documented configuration profile)
# Apply in OPNsense Zenarmor user interface (UI)

deployment:
  mode: routed
  protected_interfaces:
    - em1   # LAN_TRUSTED
    - em2   # LAN_IOT
    - em3   # DMZ
  security_zones:
    em1: lan
    em2: iot
    em3: dmz
  cpu_pinning: enabled
  reporting_database: local

policies:
  - name: MGMT_SERVERS_STRICT
    enabled: true
    scope:
      source_zones: [lan]
      destination_zones: [lan, dmz]
      vlan_targets: [management, private_servers]
    action: allow_with_restrictions
    app_controls:
      block_categories:
        - Anonymizers
        - PeerToPeer
        - Malware
        - Phishing
        - CryptoMining
        - DynamicDNS
        - RemoteAccessTools
      monitor_categories:
        - AITools
        - StorageBackup
    web_controls:
      block_risky_domains: true
      safe_search: true
      block_new_registered_domains: true
    tls_inspection: disabled
    logging:
      log_allowed_sessions: false
      log_blocked_sessions: true
      retention_days: 30
    exceptions:
      - name: allow_github_for_admin_updates
        target: github.com
        justification: package and code updates
        review_interval_days: 90

  - name: IOT_GUEST_RESTRICTED
    enabled: true
    scope:
      source_zones: [iot]
      destination_zones: [wan]
      vlan_targets: [iot_guest]
    action: default_deny
    app_controls:
      allow_categories:
        - DNS
        - NTP
        - VendorCloudServices
      block_categories:
        - Anonymizers
        - PeerToPeer
        - SocialMedia
        - RemoteAccessTools
        - StreamingMedia
        - Malware
        - CryptoMining
    web_controls:
      block_risky_domains: true
      block_new_registered_domains: true
    logging:
      log_allowed_sessions: true
      log_blocked_sessions: true
      retention_days: 30
    exceptions:
      - name: allow_camera_vendor_cloud
        target: camera-vendor.example
        justification: required for device operation
        review_interval_days: 90

  - name: DMZ_MONITORED
    enabled: true
    scope:
      source_zones: [dmz]
      destination_zones: [wan, lan]
      vlan_targets: [dmz]
    action: allow_with_restrictions
    app_controls:
      block_categories:
        - PeerToPeer
        - Anonymizers
        - Malware
        - RemoteAccessTools
      monitor_categories:
        - Web
        - DNS
        - TLS
    logging:
      log_allowed_sessions: true
      log_blocked_sessions: true
      retention_days: 60
    exceptions: []

maintenance:
  policy_review_interval_days: 90
  signature_update_policy: automatic
  stale_exception_removal: enabled
```

  </details>

  <details>
    <summary><strong>Suricata example configuration</strong></summary>

```yaml
# /etc/suricata/suricata.yaml
%YAML 1.1
---

vars:
  address-groups:
    HOME_NET: "[192.168.10.0/24,192.168.20.0/24,192.168.30.0/24,192.168.40.0/24,fd00:10::/64,fd00:20::/64,fd00:30::/64,fd00:40::/64]"
    EXTERNAL_NET: "!$HOME_NET"

default-log-dir: /var/log/suricata/

af-packet:
  - interface: igb0
    cluster-id: 99
    cluster-type: cluster_flow
    defrag: yes
    use-mmap: yes
    tpacket-v3: yes
    ring-size: 200000
    block-size: 1048576
    buffer-size: 65535
  - interface: igb1
    cluster-id: 98
    cluster-type: cluster_flow
    defrag: yes
    use-mmap: yes
    tpacket-v3: yes
    ring-size: 200000
    block-size: 1048576
    buffer-size: 65535

outputs:
  - eve-log:
      enabled: yes
      filetype: regular
      filename: eve.json
      community-id: true
      xff:
        enabled: no
      types:
        - alert:
            payload: no
            packet: no
            http-body: no
            tagged-packets: yes
            metadata: yes
        - anomaly:
            enabled: yes
        - dns:
            query: yes
            answer: yes
        - http:
            extended: yes
        - tls:
            extended: yes
        - ssh
        - flow
        - netflow
        - stats:
            totals: yes
            threads: yes
        - drop:
            alerts: yes
            flows: all

rule-files:
  - suricata.rules
  - local.rules

detect-engine:
  - profile: medium
    custom-values:
      toclient-groups: 3
      toserver-groups: 25
  - rule-reload: true

stream:
  memcap: 512mb
  checksum-validation: yes
  inline: auto

app-layer:
  protocols:
    tls:
      enabled: yes
    http:
      enabled: yes
    dns:
      enabled: yes
    ssh:
      enabled: yes

threshold-file: /etc/suricata/threshold.config
classification-file: /etc/suricata/classification.config
reference-config-file: /etc/suricata/reference.config
```

```conf
# /etc/suricata/rules/local.rules

drop tcp !$HOME_NET any -> 192.168.10.1 443 (msg:"DROP unauthorized access to firewall GUI"; flow:to_server,established; sid:1000001; rev:1;)

alert udp 192.168.50.0/24 any -> !192.168.30.53 53 (msg:"ALERT IoT direct DNS bypass attempt"; sid:1000002; rev:1;)

alert tcp !192.168.10.0/24 any -> 192.168.10.0/24 22 (msg:"ALERT non-management SSH attempt to management subnet"; flow:to_server,established; sid:1000003; rev:1;)
```

```conf
# /etc/suricata/threshold.config

suppress gen_id 1, sig_id 2010935, track by_src, ip 192.168.20.15
threshold gen_id 1, sig_id 2001219, type both, track by_src, count 5, seconds 60
```

  </details>
</details>

  </div>
</details>

</div>
