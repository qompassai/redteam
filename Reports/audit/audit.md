# Security Audit Review

<style>
:root {
  --bg: #f7f6f2;
  --surface: #fbfbf9;
  --surface-2: #f1eee8;
  --text: #28251d;
  --muted: #6d6a63;
  --border: rgba(40,37,29,0.12);
  --primary: #01696f;
  --primary-soft: rgba(1,105,111,0.09);
  --warning: #964219;
  --warning-soft: rgba(150,66,25,0.10);
  --success: #437a22;
  --success-soft: rgba(67,122,34,0.10);
  --radius: 16px;
  --radius-sm: 12px;
  --shadow: 0 10px 30px rgba(28, 23, 16, 0.07);
}
.review-wrap {
  background: var(--bg);
  color: var(--text);
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  padding: 24px;
  border-radius: 24px;
}
.hero-card, .panel-card, .score-row, .review-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
.hero-card {
  padding: 28px;
  margin-bottom: 20px;
  background: linear-gradient(180deg, var(--primary-soft), rgba(255,255,255,0)) , var(--surface);
}
.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 12px;
  color: var(--muted);
  margin-bottom: 10px;
  font-weight: 700;
}
.hero-title {
  font-size: 2rem;
  line-height: 1.1;
  margin: 0 0 14px 0;
}
.hero-text {
  color: var(--muted);
  max-width: 70ch;
  margin: 0 0 18px 0;
}
.badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}
.badge {
  display: inline-block;
  padding: 8px 12px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  border: 1px solid var(--border);
  background: var(--surface-2);
}
.badge.primary { background: var(--primary-soft); color: var(--primary); }
.badge.warn { background: var(--warning-soft); color: var(--warning); }
.badge.ok { background: var(--success-soft); color: var(--success); }
.panel-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin: 20px 0;
}
.panel-card {
  padding: 20px;
}
.panel-card h3 {
  margin-top: 0;
  margin-bottom: 10px;
}
.panel-card p {
  margin: 0;
  color: var(--muted);
}
.section-title {
  margin-top: 30px;
  margin-bottom: 12px;
  font-size: 1.5rem;
}
.scorecard {
  display: grid;
  gap: 12px;
  margin: 16px 0 28px 0;
}
.score-row {
  padding: 14px 16px;
}
.score-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 10px;
  font-weight: 700;
}
.score-pill {
  font-size: 12px;
  font-weight: 700;
  padding: 6px 10px;
  border-radius: 999px;
  background: var(--primary-soft);
  color: var(--primary);
}
.meter {
  height: 10px;
  background: var(--surface-2);
  border-radius: 999px;
  overflow: hidden;
}
.meter > span {
  display: block;
  height: 100%;
  background: var(--primary);
  border-radius: inherit;
}
.review-list {
  display: grid;
  gap: 14px;
}
.review-card {
  padding: 18px;
}
.review-card p { color: var(--muted); }
.ref-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 12px;
}
.ref-links a {
  text-decoration: none;
  color: var(--primary);
  background: var(--primary-soft);
  border: 1px solid rgba(1,105,111,0.16);
  padding: 7px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}
.review-card details {
  margin-top: 12px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}
.review-card summary {
  cursor: pointer;
  font-weight: 700;
}
.review-card textarea {
  width: 100%;
  min-height: 92px;
  margin-top: 12px;
  border-radius: var(--radius-sm);
  border: 1px dashed var(--border);
  background: var(--bg);
  color: var(--text);
  padding: 12px;
  font: inherit;
}
.footer-note {
  margin-top: 26px;
  padding: 18px;
  border-radius: var(--radius);
  background: var(--surface-2);
  color: var(--muted);
  border: 1px solid var(--border);
}
</style>

<div class="review-wrap">
  <div class="hero-card">
    <div class="eyebrow">Manager-ready review artifact</div>
    <h1 class="hero-title">A stronger visual review format for the homelab security architecture writeup</h1>
    <p class="hero-text">This enhanced Markdown version keeps the portability of a `.md` file while using embedded HTML and CSS to create a more polished internal-review document. The underlying review still reflects the original report’s emphasis on VLAN segmentation, RFC1918-based internal controls, IPv6 ULA handling, forced DNS, and layered threat prevention.[cite:157][cite:171]</p>
    <div class="badges">
      <span class="badge primary">Status: Needs revision</span>
      <span class="badge ok">Framework: Zero Trust</span>
      <span class="badge">RFC 1918</span>
      <span class="badge">RFC 4193</span>
      <span class="badge warn">FIPS 140-3: Context only</span>
      <span class="badge">Audience: Manager review</span>
    </div>
  </div>

  <div class="panel-grid">
    <div class="panel-card">
      <h3>Recommendation</h3>
      <p>Revise and resubmit. The architectural intent is strong, but the document still needs stronger proof artifacts, cleaner standards language, and more neutral engineering phrasing.</p>
    </div>
    <div class="panel-card">
      <h3>Primary gap</h3>
      <p>The biggest weakness is evidence quality: the source report describes controls confidently, but does not yet show enough screenshots, rule outputs, validation tests, or control-boundary documentation to support every major claim.</p>
    </div>
    <div class="panel-card">
      <h3>Mentoring value</h3>
      <p>This draft is a good coaching opportunity because the security instincts are mostly solid; the improvement needed is in documentation rigor, terminology precision, and review-grade communication.</p>
    </div>
  </div>

  <h2 class="section-title">Scorecard</h2>
  <div class="scorecard">
    <div class="score-row">
      <div class="score-head"><span>Architecture &amp; segmentation</span><span class="score-pill">4 / 5</span></div>
      <div class="meter"><span style="width:80%"></span></div>
    </div>
    <div class="score-row">
      <div class="score-head"><span>Standards accuracy</span><span class="score-pill">3 / 5</span></div>
      <div class="meter"><span style="width:60%"></span></div>
    </div>
    <div class="score-row">
      <div class="score-head"><span>Evidence &amp; validation</span><span class="score-pill">2 / 5</span></div>
      <div class="meter"><span style="width:40%"></span></div>
    </div>
    <div class="score-row">
      <div class="score-head"><span>Professional tone</span><span class="score-pill">2 / 5</span></div>
      <div class="meter"><span style="width:40%"></span></div>
    </div>
  </div>

  <h2 class="section-title">Strengths already present</h2>
  <div class="review-list">
    <div class="review-card">
      <strong>Defense-in-depth is real, not decorative.</strong>
      <p>The original report combines physical separation, VLAN segmentation, alias-driven access control, DNS enforcement, and inline threat inspection rather than relying on one protection point.</p>
    </div>
    <div class="review-card">
      <strong>The writeup correctly recognizes IPv6 as a separate design problem.</strong>
      <p>That is an important strength because RFC 1918 is limited to IPv4 private address space, while IPv6 local addressing is handled differently under RFC 4193.</p>
    </div>
    <div class="review-card">
      <strong>Management access is treated as privileged.</strong>
      <p>The report’s emphasis on limiting administrative access to a narrower device set shows the right instinct toward least privilege and management-plane protection.</p>
    </div>
  </div>

  <h2 class="section-title">Required revisions</h2>
  <div class="review-list">
    <div class="review-card">
      <strong>1. Add evidence for each major security claim.</strong>
      <p>Every important control should have a validation artifact: firewall screenshots, alias exports, test results, packet captures, or rule references. Without that, the report reads as a design assertion rather than a reviewable engineering document.[cite:157]</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
    <div class="review-card">
      <strong>2. Tighten standards language.</strong>
      <p>Use RFC 1918 specifically for IPv4 private ranges, use RFC 4193 for IPv6 ULA, and avoid implying FIPS 140-3 alignment unless validated cryptographic modules and supporting evidence are actually documented.[cite:157][cite:171][cite:169]</p>
      <div class="ref-links">
        <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a>
        <a href="https://datatracker.ietf.org/doc/html/rfc4193">RFC 4193</a>
        <a href="https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-standards">NIST FIPS 140-3</a>
      </div>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
    <div class="review-card">
      <strong>3. Replace dramatic language with bounded engineering wording.</strong>
      <p>Terms like “God Mode,” “violently drops,” or “hijacks” should be rewritten as policy outcomes, such as “restricted administrative exception,” “blocks and logs denied traffic,” or “transparently redirects DNS queries.”</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
    <div class="review-card">
      <strong>4. Document control limitations.</strong>
      <p>The report should explicitly note what each control does not cover, such as DoH and DoT bypass paths for forced DNS, VPN evasion for GeoIP filtering, or operational tradeoffs around NAT66.</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
  </div>

  <h2 class="section-title">Reference-backed revision bullets</h2>
  <div class="review-list">
    <div class="review-card">
      <strong>RFC 1918 correction</strong>
      <p>Revise internal-block wording so it explicitly says RFC 1918 covers the IPv4 private ranges 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16, and note that these ranges are not an IPv6 standard.</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
    <div class="review-card">
      <strong>RFC 4193 clarification</strong>
      <p>Revise IPv6 language so it states that Unique Local IPv6 Unicast Addresses are defined in RFC 4193 for local communications, which is the right citation when explaining ULA choices.</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
    <div class="review-card">
      <strong>FIPS 140-3 caution</strong>
      <p>Revise any compliance-adjacent wording so it clearly states that FIPS 140-3 applies to cryptographic module validation and should not be used as shorthand for general firewalling, segmentation, or hardening work.</p>
      <details>
        <summary>Reviewer comment area</summary>
        <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
      </details>
    </div>
  </div>

  <h2 class="section-title">Coaching notes</h2>
  <div class="review-list">
    <div class="review-card">
      <strong>Lead with fact, then effect, then evidence.</strong>
      <p>That structure makes the report read like an engineering review instead of a persuasive narrative.</p>
    </div>
    <div class="review-card">
      <strong>Separate design quality from compliance language.</strong>
      <p>A strong architecture can still be described inaccurately if standards and validation terms are used too loosely.</p>
    </div>
    <div class="review-card">
      <strong>Show residual risk.</strong>
      <p>Mature writeups state what is blocked by default, what is specifically allowlisted, how that was tested, and what assumptions remain unresolved.</p>
    </div>
  </div>

  <div class="footer-note">
    This Markdown file is intentionally enhanced with embedded HTML and CSS so it remains a portable `.md` document while presenting more like a lightweight internal review page than a plain header-and-bullet memo.
  </div>
</div>

<h2 class="section-title">Protection rings and coverage gaps</h2>
<div class="review-list">
  <div class="review-card">
    <strong>Why this section matters</strong>
    <p>The current review focuses mostly on network segmentation, traffic filtering, and application visibility, but those controls operate far above the CPU privilege boundary. In x86-style protection models, Ring 0 is kernel mode with unrestricted hardware and memory access, while Ring 3 is user mode where normal applications run.</p>
  </div>

  <div class="review-card">
    <strong>Ring model mapping for the current stack</strong>
    <p>The tools described in the report mostly address network and application-layer enforcement rather than CPU privilege rings directly, so this section reframes them as “what part of the stack they help defend” versus “what privilege ring they actually control.”[cite:199][cite:200][cite:201]</p>

| Tool / Control | What it addresses | Closest ring or layer relevance | What it does **not** cover |
|---|---|---|---|
| VLAN segmentation and RFC1918 blocking | East-west isolation and internal reachability policy | Network boundary, above Ring 3 | Does not prevent local privilege escalation, kernel compromise, or malicious code already executing on a host. |
| OPNsense firewall rules and aliases | Layer 3/4 policy enforcement based on interface, IP, and port | Network control plane, outside host CPU rings | Does not harden host kernel attack surface or application runtime integrity on endpoints. |
| Forced DNS / Port 53 interception | Resolver-path control and DNS policy enforcement | Network / service control, above Ring 3 | Does not stop DoH/DoT unless separately controlled, and does not affect kernel-level malware behavior on a host. |
| Zenarmor NGFW | Layer-7 application awareness, filtering, and reporting | Application/network visibility, roughly adjacent to Ring 3 behavior | Does not operate as kernel exploit mitigation or endpoint EDR on the protected hosts themselves. |
| Suricata IPS | Inline detection and dropping of known-bad traffic at Layer 2 or Layer 3 | Network inspection, outside CPU privilege rings | Does not stop post-exploitation privilege escalation after malicious code is already running locally. |
| GeoIP whitelisting | Reduces unsolicited inbound exposure by geography | Perimeter access reduction, not ring-specific | Does not provide identity assurance, process isolation, kernel integrity, or resistance to VPN/proxy bypass. |
| Admin device allowlisting | Restricts who can reach management interfaces | Trust boundary near user/admin access, still above Ring 3 | Does not prove device health, protect against stolen sessions, or defend the management host kernel if compromised. |
| IPv6 ULA with NAT66 and matching policy | Keeps IPv6 policy aligned with IPv4 segmentation goals | Network architecture, not CPU ring control | Does not itself provide endpoint hardening, kernel self-protection, or runtime exploit mitigation. |

<details>
<summary>Reviewer comment area</summary>
<textarea placeholder="Add your comments for the junior engineer here..."></textarea>
</details>
  </div>

  <div class="review-card">
    <strong>What is currently missing at the lower rings</strong>
    <p>If Ring 0 is the kernel, then the present report is strongest at the network and application-visibility layers and weakest at the host and kernel assurance layers. That means the architecture says much more about how traffic is filtered than about how endpoints resist compromise after code execution begins.[cite:199][cite:205]</p>
    <ul>
      <li><strong>Ring 0 / kernel protections:</strong> no explicit mention of Secure Boot, kernel module control, kernel lockdown, driver minimization, kernel exploit mitigations, or host-based integrity controls.[cite:199]</li>
      <li><strong>Ring 3 / user-space protections:</strong> no explicit mention of application allowlisting, endpoint detection and response, sandboxing, process isolation, or memory-exploit mitigation on user workloads.[cite:199]</li>
      <li><strong>Identity and admin-plane assurance:</strong> no clear mention of MFA, PAM hardening, device posture, privileged access workstation patterns, or certificate-backed management access.[cite:157]</li>
      <li><strong>Host visibility:</strong> no host-based logging, auditd-style telemetry, file integrity monitoring, or incident-response collection path is described.[cite:157]</li>
      <li><strong>Container and VM isolation details:</strong> the report names services and public apps, but does not document namespace hardening, seccomp, AppArmor/SELinux, capability dropping, or hypervisor-boundary assumptions.[cite:157]</li>
    </ul>
    <details>
      <summary>Reviewer comment area</summary>
      <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
    </details>
  </div>

  <div class="review-card">
    <strong>Suggested language to add to the review</strong>
    <p>A concise way to explain the current posture is: “The documented controls primarily reduce attack surface and lateral movement at the network and application-policy layers, but the report does not yet document equivalent controls for host hardening, user-space containment, or kernel-level assurance.” That wording helps distinguish perimeter and segmentation strength from endpoint and kernel resilience.[cite:199][cite:200][cite:201]</p>
    <details>
      <summary>Reviewer comment area</summary>
      <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
    </details>
  </div>
</div>

<h2 class="section-title">Protection rings and coverage gaps</h2>
<div class="review-list">
  <div class="review-card">
    <strong>Why this section matters</strong>
    <p>The current review focuses mostly on network segmentation, traffic filtering, and application visibility, but those controls operate far above the CPU privilege boundary. In x86-style protection models, Ring 0 is kernel mode with unrestricted hardware and memory access, while Ring 3 is user mode where normal applications run.[cite:199][cite:205]</p>
  </div>

  <div class="review-card">
    <strong>Ring model mapping for the current stack</strong>
    <p>The tools described in the report mostly address network and application-layer enforcement rather than CPU privilege rings directly, so this section reframes them as what part of the stack they help defend versus what privilege ring they actually control.[cite:199][cite:200][cite:201]</p>

| Tool / Control | What it addresses | Closest ring or layer relevance | What it does **not** cover |
|---|---|---|---|
| VLAN segmentation and RFC1918 blocking | East-west isolation and internal reachability policy | Network boundary, above Ring 3 | Does not prevent local privilege escalation, kernel compromise, or malicious code already executing on a host.[cite:157][cite:199] |
| OPNsense firewall rules and aliases | Layer 3/4 policy enforcement based on interface, IP, and port | Network control plane, outside host CPU rings | Does not harden host kernel attack surface or application runtime integrity on endpoints.[cite:157][cite:207] |
| Forced DNS / Port 53 interception | Resolver-path control and DNS policy enforcement | Network and service control, above Ring 3 | Does not stop DoH or DoT unless separately controlled, and does not affect kernel-level malware behavior on a host.[cite:157][cite:199] |
| Zenarmor NGFW | Layer-7 application awareness, filtering, and reporting | Application and network visibility, roughly adjacent to Ring 3 behavior | Does not operate as kernel exploit mitigation or endpoint EDR on the protected hosts themselves.[cite:201][cite:207] |
| Suricata IPS | Inline detection and dropping of known-bad traffic at Layer 2 or Layer 3 | Network inspection, outside CPU privilege rings | Does not stop post-exploitation privilege escalation after malicious code is already running locally.[cite:200][cite:206] |
| GeoIP whitelisting | Reduces unsolicited inbound exposure by geography | Perimeter access reduction, not ring-specific | Does not provide identity assurance, process isolation, kernel integrity, or resistance to VPN or proxy bypass.[cite:157] |
| Admin device allowlisting | Restricts who can reach management interfaces | Trust boundary near user and admin access, still above Ring 3 | Does not prove device health, protect against stolen sessions, or defend the management host kernel if compromised.[cite:157][cite:199] |
| IPv6 ULA with NAT66 and matching policy | Keeps IPv6 policy aligned with IPv4 segmentation goals | Network architecture, not CPU ring control | Does not itself provide endpoint hardening, kernel self-protection, or runtime exploit mitigation.[cite:171][cite:199] |

    <details>
      <summary>Reviewer comment area</summary>
      <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
    </details>
  </div>

  <div class="review-card">
    <strong>What is currently missing at the lower rings</strong>
    <p>If Ring 0 is the kernel, then the present report is strongest at the network and application-visibility layers and weakest at the host and kernel assurance layers. That means the architecture says much more about how traffic is filtered than about how endpoints resist compromise after code execution begins.[cite:199][cite:205]</p>
    <ul>
      <li><strong>Ring 0 and kernel protections:</strong> no explicit mention of Secure Boot, kernel module control, kernel lockdown, driver minimization, kernel exploit mitigations, or host-based integrity controls.[cite:199]</li>
      <li><strong>Ring 3 and user-space protections:</strong> no explicit mention of application allowlisting, endpoint detection and response, sandboxing, process isolation, or memory-exploit mitigation on user workloads.[cite:199]</li>
      <li><strong>Identity and admin-plane assurance:</strong> no clear mention of MFA, PAM hardening, device posture, privileged access workstation patterns, or certificate-backed management access.[cite:157]</li>
      <li><strong>Host visibility:</strong> no host-based logging, auditd-style telemetry, file integrity monitoring, or incident-response collection path is described.[cite:157]</li>
      <li><strong>Container and VM isolation details:</strong> the report names services and public apps, but does not document namespace hardening, seccomp, AppArmor or SELinux, capability dropping, or hypervisor-boundary assumptions.[cite:157]</li>
    </ul>
    <details>
      <summary>Reviewer comment area</summary>
      <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
    </details>
  </div>

  <div class="review-card">
    <strong>Suggested language to add to the review</strong>
    <p>A concise way to explain the current posture is: The documented controls primarily reduce attack surface and lateral movement at the network and application-policy layers, but the report does not yet document equivalent controls for host hardening, user-space containment, or kernel-level assurance. That wording helps distinguish perimeter and segmentation strength from endpoint and kernel resilience.</p>
    <details>
      <summary>Reviewer comment area</summary>
      <textarea placeholder="Add your comments for the junior engineer here..."></textarea>
    </details>
  </div>
</div>
