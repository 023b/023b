<!--
  Retro Terminal README for @023b (Arun Prakash S)
  - No GIFs
  - Green-monochrome / CRT vibe
  - Contribution graph + animated SVG "snake"
  - 6 showcased projects (links below)
-->

<!-- ===== Animated CRT Header (SVG) ===== -->
<div align="center">
  <!-- Inline SVG — CRT screen title with slight flicker (SMIL animation) -->
  <svg width="860" height="140" viewBox="0 0 860 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Arun Prakash - Retro Terminal">
    <defs>
      <linearGradient id="g1" x1="0" x2="0" y1="0" y2="1">
        <stop offset="0" stop-color="#9efc9e" stop-opacity="0.95"/>
        <stop offset="1" stop-color="#2b6b2b" stop-opacity="0.45"/>
      </linearGradient>
      <filter id="crt" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="0.9" result="blur"/>
        <feColorMatrix in="blur" type="matrix" values="0 0 0 0 0
                                                      0 0 0 0 0
                                                      0 0 0 0 0
                                                      0 0 0 0.7" />
        <feBlend in="SourceGraphic" mode="screen"/>
      </filter>
    </defs>

    <!-- black rounded rect -->
    <rect x="6" y="6" width="848" height="128" rx="8" ry="8" fill="#041204" stroke="#0f2a0f" stroke-width="3"/>

    <!-- CRT glow band -->
    <rect x="10" y="10" width="840" height="40" rx="6" fill="url(#g1)" opacity="0.12" />

    <!-- Large username text (retro monospace) -->
    <g filter="url(#crt)">
      <text x="36" y="62" font-family="Courier New, Courier, monospace" font-size="30" fill="#aaffaa" letter-spacing="1.5">
        Arun Prakash S — <tspan font-size="20" fill="#8cff8c">Independent AI Dev & Researcher</tspan>
      </text>

      <!-- subtitle lines -->
      <text x="36" y="90" font-family="Courier New, monospace" font-size="14" fill="#92ff92">
        Home Lab Networker • Local AI • Privacy-first LLMs • BCI & CV experiments
      </text>
    </g>

    <!-- flicker overlay -->
    <rect x="0" y="0" width="860" height="140" fill="#000" opacity="0">
      <animate attributeName="opacity" values="0;0.03;0;0.015;0" dur="3s" repeatCount="indefinite"/>
    </rect>
  </svg>
</div>

---

<div align="center">

<!-- Contribution graph (SVG) - loads from ghchart.rshah.org (SVG) -->
<!-- If you prefer the GitHub contributions calendar, replace URL with your preferred service -->
<img src="https://ghchart.rshah.org/023b" alt="Contributions chart for 023b" style="max-width:700px; border: 2px solid #063006; border-radius:6px; padding:8px; background:#041204"/>

</div>

---

# ✦ About me
Arun Prakash S (He/Him)
Independent AI Developer & Researcher | Home Lab Networker
Coimbatore, Tamil Nadu, India

Recent BCA (AI & DS) grad — I build privacy-first AI tools, self-hosted LLMs, BCI frameworks and home-lab systems.


- 709 followers · 500+ connections
- Open to roles: AI Developer, ML Researcher, Generative AI Engineer
- Strong on: Local LLMs, semantic search, signal processing (BCI), computer vision, self-hosting & networking

---

# ⚙️ Quick stats
| 🔭 Currently | ⚡ Tools | 💾 Home lab |
|---|---:|---|
| Building **Shendu.ai** (local assistant with Mistral-7B + Obsidian sync) | Python · PyTorch · Hugging Face · Qiskit · MediaPipe | TrueNAS SCALE, Tailscale, networked NAS & monitoring |

---

# 🧩 Featured projects
> Six highlighted repos — short, terminal-style summaries. Click titles to open.

1. **[gpt](https://github.com/023b/gpt)**  
   `→ local LLM experiments / fine-tuning · lightweight assistant prototypes · transfer learning`  
   *Personal experiments around language models and compact inference.*

2. **[hand_tracking-](https://github.com/023b/hand_tracking-)**  
   `→ real-time hand gesture recognition · OpenCV + MediaPipe · webcam demos`  
   *11-gesture recognizer for interactive CV experiments.*

3. **[Shendu.ai](https://github.com/023b/Shendu.ai)**  
   `→ Local AI Assistant for Obsidian · Mistral-7B integration · privacy-first`  
   *Conversational search over personal notes, real-time sync & vector indexing.*

4. **[quantum_learning](https://github.com/023b/quantum_learning)**  
   `→ Quantum-enhanced training · DistilBERT + hybrid optimization · Qiskit experiments`  
   *Research experiments merging quantum updates with classical fine-tuning.*

5. **[BCI](https://github.com/023b/BCI)**  
   `→ Brain-Computer Interface framework · EEG pipelines · motor imagery classification`  
   *Modular signal acquisition, preprocessing, inference & dashboards.*

6. **[live_classifier](https://github.com/023b/live_classifier)**  
   `→ Live webcam object classification · OpenCV training UI · real-time predictions`  
   *Capture → train → infer loop for rapid prototyping.*

---

# 🔭 Spotlight: Shendu (local LLM assistant)
- 100% local. No cloud. Self-hosted Mistral-7B with Obsidian sync.  
- Features: semantic search, background memory sync, graph visualization, retraining pipelines.  
- Why it matters: privacy-first & tailored to YOUR knowledge graph.

---

# 🐍 Snake — tiny SVG "repo snake" (no GIFs)
<!-- Simple animated SVG snake to evoke the snake game / repo graph -->
<div align="center">
<svg width="620" height="70" viewBox="0 0 620 70" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Retro snake animation">
  <rect width="620" height="70" rx="6" fill="#041204" stroke="#083008" stroke-width="2"/>
  <g transform="translate(20,35)" fill="#9efc9e">
    <!-- path -->
    <path id="s" d="M0 0 Q80 -20 160 0 T320 0 T480 0 T560 0" fill="none" stroke="none"/>
    <!-- moving dots (snake body) -->
    <!-- dot template -->
    <g id="dot">
      <circle cx="0" cy="0" r="5"/>
    </g>
    <!-- instantiate multiple dots and animate them along path with staggered begin times -->
    <use href="#dot">
      <animateMotion dur="6s" repeatCount="indefinite">
        <mpath href="#s"/>
      </animateMotion>
    </use>
    <use href="#dot" x="-12" >
      <animateMotion dur="6s" repeatCount="indefinite" begin="0.12s">
        <mpath href="#s"/>
      </animateMotion>
    </use>
    <use href="#dot" x="-24">
      <animateMotion dur="6s" repeatCount="indefinite" begin="0.24s">
        <mpath href="#s"/>
      </animateMotion>
    </use>
    <use href="#dot" x="-36">
      <animateMotion dur="6s" repeatCount="indefinite" begin="0.36s">
        <mpath href="#s"/>
      </animateMotion>
    </use>
    <use href="#dot" x="-48">
      <animateMotion dur="6s" repeatCount="indefinite" begin="0.48s">
        <mpath href="#s"/>
      </animateMotion>
    </use>
  </g>
</svg>
</div>

---

# 📫 Contact & links
- GitHub: [023b](https://github.com/023b)  
- Location: Coimbatore, Tamil Nadu, India  
- Open to: AI research & engineering roles, remote & relocation-friendly opportunities  
- Quick CV-summary: BCA (AI & DS), IBM & Pantech internships, multiple certs (Datamites, GreatLearning, Udemy)

---

# 🛠 How to personalize this README (quick)
- Change accent color: in the SVG tags, update `#aaffaa` / `#9efc9e` to amber `#ffd87a` for MS-DOS amber vibe.  
- Replace contribution graph: use another SVG provider or GitHub's contrib graph.  
- Add more repos: duplicate the project block and add link & one-liner.

---

# ✨ Final notes
- No GIFs — only SVG + SMIL animations (safe for GitHub).  
- Retro green terminal is the default here; if you'd like the **amber** MS-DOS treatment or **minimal pixel-art** instead, I’ll produce a variant immediately (I already built green for you — fastest for copy/paste).  
- Want the README split into sections (CV, Publications, Papers, Demos) or add badges (languages / top languages / top repo pins)? I can append them.

---

If you want, I’ll also:
- produce an **amber** and a **pixel-art** variant and paste them below, or
- generate a compact `profile README` + separate `projects.md` file for deeper docs.

Which do you want next — **amber** or **pixel-art** variant? (No extra info required — I’ll convert automatically.)
