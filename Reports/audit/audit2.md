# Security Audit Review — Current Homelab Plan

<div class="audit-wrap">
  <div class="audit-card audit-hero">
    <div class="audit-eyebrow">Objective review artifact</div>
    <h1 class="audit-title">Review of Current Homelab Security Plan</h1>
    <p class="audit-text">This review evaluates the current plan described by <code>Trevor Lougy </code> against recognized security frameworks and standards, with emphasis on segmentation, access control, monitoring, protocol handling, and documented assurance. The review is intentionally evidence-oriented and separates architectural strengths from unsupported claims, missing controls, and areas where reviewer-specific comments should be added. </p>
    <div class="audit-badges">
      <span class="audit-badge primary">Disposition: Revise and strengthen</span>
      <span class="audit-badge ok">Strongest area: Network segmentation</span>
      <span class="audit-badge warn">Weakest area: Validation evidence</span>
      <span class="audit-badge">Framework lens: NIST CSF 2.0</span>
      <span class="audit-badge">Control lens: CIS Controls v8</span>
      <span class="audit-badge">Protocol refs: RFC 1918 / RFC 4193</span>
    </div>
  </div>

<details class="audit-details">
  <summary><strong>Rating methodology reference</strong></summary>

  | Rating area | Scale used | Meaning | Source |
  |---|---|---|---|
  | NIST CSF 2.0 implementation tier | Tier 1–4 | Tier 1 = Partial, Tier 2 = Risk-Informed, Tier 3 = Repeatable, Tier 4 = Adaptive | [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) |
  | CIS Controls v8 maturity | Level 1–5 (internal mapping) | Internal scoring shorthand used to describe how completely the documented controls appear to be implemented and evidenced; this is an audit-layer maturity summary, not an official CIS numeric scale | [CIS Controls v8 Overview](https://www.cisecurity.org/controls/v8) |
  | CIS Controls v8 implementation groups | IG1–IG3 | IG1 = basic cyber hygiene, IG2 = additional protections for more complexity, IG3 = mature protections for higher-risk environments | [CIS Implementation Groups](https://www.cisecurity.org/controls/implementation-groups) |
  | NIST CSF function status language | Weak / Partial / Moderate / Strong | Plain-language reviewer shorthand used to summarize how well the current plan addresses a CSF function based on the evidence present in the document | [NIST CSF 2.0 Core](https://www.nist.gov/cyberframework) |
  | Objective evidence strength | Low / Emerging / Established | Reviewer shorthand for how much validation evidence is actually included, such as diagrams, rule matrices, logs, captures, test records, and recovery proof | [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) |

  <p><strong>Scoring note:</strong> This review now uses NIST CSF 2.0 implementation tiers as the primary maturity language and CIS Controls v8 as the control-family and implementation-group lens.</p>
</details>

  <div class="audit-grid">
    <div class="audit-panel">
      <h3>What the current plan does well</h3>
      <p>The plan is strongest in segmentation, internal boundary control, and reduction of easy lateral movement. It also shows mature awareness that IPv6 must be controlled separately from IPv4, which is often missed in homelab writeups.</p>
    </div>
    <div class="audit-panel">
      <h3>What the current plan does not yet prove</h3>
      <p>The writeup does not yet provide objective validation artifacts such as rule exports, packet captures, log excerpts, access tests, exception inventories, or incident-handling evidence. As written, it reads more like an architecture narrative than a defensible audit package. </p>
    </div>
    <div class="audit-panel">
      <h3>Overall assessment</h3>
      <p>The design intent is better than the documentation quality. The network policy model appears thoughtful, but the report currently overstates assurance relative to the evidence presented. </p>
# Linux privilege layers

```text
+--------------------------------------------+
| "Ring -3" : Firmware / Management Engine   |
|  - UEFI / BIOS                             |
|  - Intel ME / AMD PSP, BMC, etc.           |
+--------------------------+-----------------+
                           |
                           v
+--------------------------------------------+
| "Ring -2" : SMM / Secure Monitor           |
|  - System Management Mode (SMM)            |
|  - Low-level monitors / EL3-equivalent     |
+--------------------------+-----------------+
                           |
                           v
+--------------------------------------------+
| "Ring -1" : Hypervisor                     |
|  - KVM, Xen, other VMMs                    |
|  - Runs guest kernels in non-root mode     |
+--------------------------+-----------------+
                           |
                           v
+--------------------------------------------+
| Ring 0 : Kernel (guest OS)                 |
|  - Linux kernel                            |
|  - Drivers, memory mgmt, I/O, syscalls     |
+--------------------------+-----------------+
                           |
                           v
+--------------------------------------------+
| Rings 1–2 : Unused by Linux                |
|  - Architecturally defined on x86          |
|  - Typically not used by Linux             |
+--------------------------+-----------------+
                           |
                           v
+--------------------------------------------+
| Ring 3 : User space                        |
|  - Processes, shells, services, containers |
|  - Apps running as users                   |
+--------------------------------------------+
```
    
</div>
  </div>

  <h2 class="audit-section-title">Framework-based scorecard</h2>
  <div class="audit-scorecard">
    <div class="audit-score">
      <div class="audit-score-head"><span>Identify (NIST CSF) & Network (CIS)</span><span class="audit-pill">Tier 2–3 / CIS Level ~2–3</span></div>
      <div class="audit-meter"><span style="width:80%"></span></div>
      <p>VLAN segmentation, admin-device exceptions, and DMZ separation are meaningful controls aligned with network boundary protection objectives. </p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Access control (NIST/CIS)</span><span class="audit-pill">Tier 2 / CIS Level ~2</span></div>
      <div class="audit-meter"><span style="width:60%"></span></div>
      <p>The plan shows partial least-privilege thinking through aliases and narrow exceptions, but it does not yet document MFA, admin workflow assurance, credential protection, or session controls. </p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Detect (NIST CSF)</span><span class="audit-pill">Tier 2 / CIS Level ~2</span></div>
      <div class="audit-meter"><span style="width:60%"></span></div>
      <p>Suricata and Zenarmor add meaningful detection capability, but the report does not yet show alert tuning, retention, triage process, false-positive handling, or downstream logging and response procedures. </p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Recover (NIST CSF)</span><span class="audit-pill">Tier 1</span></div>
      <div class="audit-meter"><span style="width:20%"></span></div>
      <p>The current plan does not document backups, restore testing, incident recovery workflow, or failure-mode handling for the controls it depends on. </p>
    </div>
    <div class="audit-score">
      <div class="audit-score-head"><span>Auditability (CIS / NIST)</span><span class="audit-pill">Level ~1</span></div>
      <div class="audit-meter"><span style="width:20%"></span></div>
      <p>The report contains many claims of effect, but almost no direct evidence, measurements, screenshots, or test results. This is the biggest gap in the current package. </p>
    </div>
  </div>

  <h2 class="audit-section-title">Objective control mapping</h2>

| Plan element | Observed strength | Objective weakness | Recommendation |
|---|---|---|---|
| Dual 10G physical separation for trusted vs. DMZ traffic | Strong boundary separation concept that reduces accidental mixing of trust zones. | The report does not show interface diagrams, switchport assignments, or verification that traffic cannot bypass intended separation. | Add deployment-specific notes here. |
| VLAN segmentation into management, trusted, private servers, DMZ, and IoT/guest | Good segmentation pattern consistent with reducing lateral movement and scoping exposure. | No rule matrix, inter-VLAN flow table, or validation test results are shown. There is also no asset inventory tied to each VLAN. | Add VLAN-specific findings here. |
| RFC1918-based internal block rules | Good default-deny intent for IPv4 internal traffic between zones. | RFC 1918 applies to IPv4 private space only, so the report must clearly separate IPv4 logic from IPv6 logic and show rule parity. | Add IPv4 rule review notes here. |
| Admin device alias for management access | Better than broad subnet trust because it narrows privileged access to named systems. | IP-based trust is not the same as identity assurance; no MFA, device health, certificate trust, or admin session controls are documented. | Add admin-plane concerns here. |
| Native LAN lock to network hardware alias | Strong anti-misuse idea for untagged infrastructure ports. | The report does not prove port-security behavior, switch configuration, or what happens during switch replacement, emergency maintenance, or mispatching. | Add switch and port validation notes here. |
| DMZ to private-server micro-allowlisting | Strongest control in the writeup because it scopes cross-zone exposure to named application paths. | No service dependency map, allowed-port inventory, or validation test is included, and no host-layer hardening is documented for the allowlisted targets. | Add service-path review notes here. |
| Forced DNS via NAT redirect on port 53 | Useful for traditional DNS control and policy enforcement. | The report does not discuss DNS over HTTPS, DNS over TLS, QUIC-based bypass paths, or how exceptions are detected and blocked. | Add DNS bypass observations here. |
| IPv6 ULA with NAT66 | Shows awareness that IPv6 must be governed explicitly and separately. | The report should justify NAT66 operationally, define policy parity with IPv4, and explain residual risks and tradeoffs. | Add IPv6 architecture notes here. |
| Zenarmor NGFW on internal interfaces | Adds application visibility and policy depth beyond port-level filtering. | No evidence is shown for policy sets, exception handling, update cadence, or how detection output feeds response. | Add DPI policy notes here. |
| Suricata IPS on WAN/DMZ edge | Appropriate perimeter detection and block control for exposed services. | No description of ruleset source, tuning, alert fatigue handling, or packet-drop validation is provided. | Add IPS tuning notes here. |
| GeoIP restrictions on WAN forwards | Can reduce opportunistic scan exposure. | GeoIP is only a coarse filter; it is not identity, and it is bypassable through VPNs, proxies, and cloud egress regions. The report overstates its effect with “99%” language without measurement evidence. | Add exposure-reduction notes here. |

  <h2 class="audit-section-title">Strengths</h2>
  <div class="audit-list">
    <div class="audit-card">
      <strong>1. Segmentation is intentional rather than cosmetic.</strong>
      <p>The current plan separates management, user, server, public, and untrusted device roles into distinct zones instead of relying on a single flat network. That is a concrete architectural strength because it supports narrower trust boundaries and better scoping of access rules.</p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="This segmentation model is a strong foundation for homelab security. For this environment, keep the current zone layout (management, user, server, DMZ, IoT/guest), but make sure each zone has: (1) a clearly documented IP range, (2) explicit inter-zone rules in a matrix, and (3) one or two validation tests **showing** that traffic cannot bypass the intended boundaries. This will turn a good design idea into a verifiable control."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>2. The plan uses default-deny thinking for east-west traffic.</strong>
      <p>The described RFC1918 block model and app-specific exceptions reflect a genuine least-privilege mindset for lateral movement reduction. This is one of the strongest parts of the current plan. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="The default‑deny approach for east–west traffic is one of the most valuable controls in this design. To preserve that strength over time, keep a small, reviewed list of explicit “allow” rules per VLAN pair, and add a short justification for each. Consider scheduling a quarterly review where you remove stale exceptions and re‑test that blocked paths are still blocked."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>3. The plan recognizes IPv6 as a separate policy domain.</strong>
      <p>Many otherwise competent network writeups ignore IPv6 entirely; this one does not. The explicit treatment of ULA and IPv6 rule intent is a meaningful strength even though the documentation still needs refinement. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="Treating IPv6 as a first‑class policy domain is a major differentiator from typical homelabs. To build on this, maintain side‑by‑side IPv4 and IPv6 rule intent for each zone (e.g., a simple table showing what is allowed over v4 and v6). Make sure every new rule is evaluated for both families so you do not accidentally create an IPv6 “back door” for flows that are blocked over IPv4."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>4. Public-service exposure is narrowed through multiple layers.</strong>
      <p>The DMZ design, micro-allowlisting, IPS, and GeoIP filtering show that exposure control is layered rather than dependent on a single port-forward decision. That layered approach is directionally strong. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="Add public-service exposure notes here..."></textarea></details>
    </div>
  </div>

  <h2 class="audit-section-title">Weaknesses</h2>
  <div class="audit-list">
    <div class="audit-card">
      <strong>1. The report overstates assurance relative to evidence.</strong>
      <p>The document frequently claims outcomes such as trapping attackers, eliminating exposure, or stopping compromise, but it does not include proof artifacts to support those outcomes. Audit-quality language must tie claims to tests, logs, diagrams, or measured results. </p>
      <details><summary>Reviewer comment area</summary><textare>Please replace broad outcome claims (“stops attackers,” “physically traps,” “eliminates exposure”) with statements that reference specific evidence. For each major control, attach or reference at least one concrete artifact: a diagram, rule export, test result, log snippet, or packet capture. The goal is for a third party to be able to see not just what you intend, but what you have actually verified in this environment."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>2. Identity and privileged access controls are under-documented.</strong>
      <p>The current plan treats admin devices as privileged based on IP assignment, but it does not show stronger management controls such as MFA, certificate-bound access, PAM policy, separate admin workflows, or management-plane session assurance. </p>
      <details><summary>Reviewer comment area</summary><textarea> The current writeup focuses on which IPs can reach management interfaces, but does not yet show how administrator identity is verified or how privileged sessions are governed. Please add detail on: (1) which accounts can administer the firewall, hypervisor, and key servers; (2) where MFA is enforced; (3) whether SSH keys / certificates are used instead of passwords and if so what non-deprecated protocols are used (rsa2048 replaced with sntrup761/x25519- https://datatracker.ietf.org/doc/rfc9941/ | https://www.rfc-editor.org/info/rfc9941/); and (4) how admin actions are logged and reviewed. This will bring the access model closer to least‑privilege rather than “trusted by IP. show, AND tell."</textarea></details>
    </div>
    <div class="audit-card">
      <strong>3. Host and workload hardening are mostly absent from the writeup.</strong>
      <p>The report is strong on network policy but thin on endpoint, container, VM, and host-layer hardening. There is no visible discussion of patching cadence, EDR, file integrity monitoring, secure boot, kernel hardening, or workload isolation assumptions. </p>
      <details><summary>Reviewer comment area</summary><textarea> "Network policy is well developed, but the host and workload layer is under‑documented. For the next revision, please describe: (1) the patching approach and frequency for hosts, containers, and appliances; (2) which hardening baselines or controls you apply (e.g., AppArmor/SELinux(SELinux as long as you're ok with poss NSA backdoor), minimal packages, SSH hardening); and (3) how you separate high‑risk services (e.g., lab workloads, internet‑facing apps) from more sensitive data‑bearing systems. This ensures the inside of each segment is as defensible as the boundaries."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>4. Detection controls are described, but response workflow is not.</strong>
      <p>The writeup names Suricata and Zenarmor, but it does not explain where alerts go, who reviews them, how often they are triaged, what constitutes a false positive, or how incidents are handled after detection. </p>
      <details><summary>Reviewer comment area</summary><textarea> "The plan schematic needs to show how detections move from “alert exists” to “action taken.” Please add a short description/diagram of: (1) where alerts and logs from these tools go; (2) who reviews them and how often; (3) how you distinguish real issues from noise; and (4) what you do when you confirm a suspicious event (e.g., block rule, isolate host, collect evidence). Even a simple, homelab‑sized response workflow will strengthen this section"</textarea></details>
    </div>
    <div class="audit-card">
      <strong>5. Several claims need narrower and more accurate wording.</strong>
      <p>Phrases like “physically trapped,” “violently drops,” “God Mode,” and “99%” read as persuasive language rather than audit language. The report should describe control function, scope, and limitations in neutral terms. </p>
      <details><summary>Reviewer comment area</summary><textarea> "Some phrases read more like marketing than audit language (for example, “physically trapped,” “violently drops,” “God Mode,” “99%”). Please revise these into neutral, scoped descriptions such as “contained within the VLAN,” “denies and logs traffic that does not match allow rules,” “administrative access,” or “reduces unsolicited traffic from disallowed regions.” Where you include numbers (percentages, coverage), tie them to an actual measurement rather than an estimate. This will make the report more credible to reviewers and future you."</textarea></details>
    </div>
  </div>

  <h2 class="audit-section-title">Recommended objective metrics</h2>

| Control area | Metric to add | Why it matters |
|---|---|---|
| VLAN segmentation | Number of authorized inter-VLAN flows vs. denied flows per review period | Demonstrates that segmentation is defined and measured rather than assumed. |
| Admin access | Count of management interfaces exposed; count of systems allowed to reach them | Shows whether privileged access scope is minimized. |
| DNS enforcement | Percentage of DNS requests observed through approved resolver path; count of blocked direct DNS attempts | Validates whether “forced DNS” is actually working. |
| Suricata | Alerts per day, true-positive rate after tuning, drop count for relevant signatures | Converts IPS claims into measurable operational effectiveness. |
| Zenarmor | Blocked application categories, exceptions granted, update cadence | Shows whether L7 policy is governed and maintained. |
| Public exposure | Number of WAN-exposed services, allowed source countries, authentication controls per service | Makes internet exposure concrete and reviewable. |
| Recovery | Backup frequency, restore test frequency, last successful restore date | Addresses resilience, not just prevention. |
| Change control | Firewall rule review interval, number of stale rules removed, documented exceptions | Prevents segmentation drift over time. |

  <h2 class="audit-section-title">Standards and reference corrections</h2>
  <div class="audit-list">
    <div class="audit-card">
      <strong>RFC 1918 usage</strong>
      <p>Use RFC 1918 only when referring to the IPv4 private ranges 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Do not use it as shorthand for all internal addressing or as an IPv6 concept. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="Add IPv4 standards comments here..."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>IPv6 ULA usage</strong>
      <p>Use RFC 4193 when discussing Unique Local IPv6 Unicast Addresses. If NAT66 remains part of the design, explain the operational reason for it, the tradeoffs, and how policy consistency is maintained across IPv4 and IPv6. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="Add IPv6 standards comments here..."></textarea></details>
    </div>
    <div class="audit-card">
      <strong>Compliance wording</strong>
      <p>Do not imply FIPS, NIST, or similar compliance from architecture quality alone. If a compliance-adjacent term is used, it should be tied to a defined control, a documented requirement, and supporting evidence. </p>
      <details><summary>Reviewer comment area</summary><textarea placeholder="Add compliance-language corrections here..."></textarea></details>
    </div>
  </div>

  <h2 class="audit-section-title">Framework alignment summary</h2>

| Framework area | Current status | Notes |
|---|---|---|
| NIST CSF — Identify | Partial | Zones and asset roles are implied, but formal asset inventory and dependency mapping are not shown.  |
| NIST CSF — Protect | Moderate | Segmentation and filtering are the strongest
documented areas. |
| NIST CSF — Detect | Partial | IPS and NGFW are present, but alert operations
are undocumented. |
| NIST CSF — Respond | Weak | No incident workflow, ownership, or escalation path is described.  |
| NIST CSF — Recover | Weak | No backup, restore, or resilience testing evidence is described.  |
| CIS Controls v8 — Network infrastructure management | Moderate | Good control intent, weak evidence and maintenance documentation.  |
| CIS Controls v8 — Access control management | Partial | Alias-based narrowing exists, but identity assurance and admin governance are thin.  |
| CIS Controls v8 — Audit log management | Weak | Logging and review workflow are not documented.  |
| CIS Controls v8 — Secure configuration | Partial | Configuration intent is strong, but baselines and change control are not shown.  |

  <div class="audit-note">
    <strong>Reviewer guidance:</strong>
    The current plan should be graded as a promising technical design that needs a more rigorous audit package. The next revision should add a network diagram, rule matrix, validation tests, exception inventory, logging flow, and recovery evidence before stronger assurance claims are made. Skeleton example below:

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
                                   │  L3 Switch│
                                   └─┬────┬────┘
      ┌──────────────────────────────┘    └──────────────────────────────┐
      │                                                                   │

  VLAN 10 - Management                           VLAN 20 - Trusted / Users
  192.168.10.0/24                                192.168.20.0/24
  ────────────────────────────                   ────────────────────────────
  -  Hypervisor mgmt (Proxmox/ESXi)               -  Workstations / laptops
  -  Switch / AP management IPs                   -  Admin workstation
  -  Out-of-band IPMI / BMC                       -  Developer boxes
  -  Jump host / bastion                          -  Internal print/file

      │ upstream only from admin alias               │ egress to core services
      └─────────────▲───────────────────────────────┘
                    │
                    │ tightly controlled ACLs / FW rules


  VLAN 30 - Server / Private Services          VLAN 40 - DMZ / Public Services
  192.168.30.0/24                              192.168.40.0/24
  ────────────────────────────                 ────────────────────────────
  -  Internal DNS / DHCP                        -  Public-facing web apps
  -  Internal Git / CI                          -  Reverse proxy
  -  Monitoring (Prometheus, Grafana)           -  VPN termination
  -  Internal DBs                               -  Any test “Internet-facing” labs

      ▲    ▲                                         ▲
      │    └──── micro‑allowlist from DMZ ───────────┘
      │           (only specific ports/hosts)
      │
      │ east‑west default‑deny between VLANs


  VLAN 50 - IoT / Guest
  192.168.50.0/24
  ────────────────────────────
  -  Smart TVs, cameras
  -  Guest Wi‑Fi clients
  -  Other untrusted devices

  -  Only allowed out to:
    – Internet (via FW rules)
    – Very specific internal services (if needed)
  -  No direct reachability to Management or Server VLANs
```
```
```

</div>
</div>
