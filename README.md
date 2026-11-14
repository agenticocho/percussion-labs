# Percussion Labs

Ten self-contained, browser-native percussion laboratories. Each one builds an
instrument out of a different piece of physics or mathematics, and generates its
sound from the model rather than playing samples over it.

**Live suite:** https://agenticocho.github.io/percussion-labs/

No build step, no backend, no account. Open `index.html` or any module directly.

## The modules

| # | Module | Built on |
|---|---|---|
| 01 | **PENDULUM-LOOM** | 3D harmonic phase loom, Blackburn Lissajous figures, coupled Huygens clocks |
| 02 | **CHRONOCRYSTAL** | 3D spectral graph percussion, pendulum wave, polyrhythmic automaton |
| 03 | **EIGENPULSE** | Spatial drumline drill, Bessel-mode cymatics, polyrhythmic hocket |
| 04 | **CYMA-FORGE** | Percussive cymatics: Faraday hydro-tank, biharmonic Chladni plate, acoustic levitation |
| 05 | **CAVITRON** | Rayleigh–Plesset sonoluminescence, Rijke thermoacoustic flame, shear-thickening impact |
| 06 | **HYPER-SOLITON** | 4D polychoron percussion via Hopf fibration, nonlinear Toda soliton lattice |
| 07 | **KAC-SPECTRA** | Isospectral drum solver, Poincaré hyperbolic tree, Kuramoto chimera synth |
| 08 | **PADIC-BRAID** | p-adic ultrametric tree, non-holomorphic fractal series, braid group B₄ loom |
| 09 | **QUASICRYSTAL-PU** | Penrose aperiodic percussion, delta-rule state machine, reversible automaton |
| 10 | **PAS-40 STUDIO** | The forty PAS rudiments as an interactive simulator and sample lab |

## Running locally

Any static server works — some browsers restrict `file://` for audio and WebGL:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

Audio requires a user gesture (click or key press) before a page may produce
sound. That's a browser policy, not a bug.

## Hosting

GitHub Pages serves this repository directly from the `main` branch root.

## Dependencies

Each module loads from public CDNs, with no local assets:

- [Tailwind CSS](https://tailwindcss.com) 3.4.17
- [three.js](https://threejs.org) r128
- [Google Fonts](https://fonts.google.com) — Inter, JetBrains Mono

Nothing else is fetched. If you want a fully offline copy, vendor those three
and rewrite the `<link>` / `<script>` tags.

## Contents

```
index.html      the suite landing page
*.html          ten standalone laboratory modules
```

## Licence

MIT — see [LICENSE](LICENSE). Each module is a standalone artifact; take what's
useful.
