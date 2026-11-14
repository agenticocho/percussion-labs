# Percussion Labs

Nine self-contained, browser-native percussion laboratories, plus a specialty
pendulum lab. Each one builds an instrument out of a different piece of physics
or mathematics, and generates its sound from the model rather than playing
samples over it.

**Live suite:** https://agenticocho.github.io/percussion-labs/

No build step, no backend, no account. Open `index.html` or any module directly.

## The nine

| # | Module | Built on |
|---|---|---|
| 01 | **CHRONOCRYSTAL** | 3D spectral graph percussion, pendulum wave, polyrhythmic automaton |
| 02 | **EIGENPULSE** | Spatial drumline drill, Bessel-mode cymatics, polyrhythmic hocket |
| 03 | **CYMA-FORGE** | Percussive cymatics: Faraday hydro-tank, biharmonic Chladni plate, acoustic levitation |
| 04 | **CAVITRON** | Rayleigh–Plesset sonoluminescence, Rijke thermoacoustic flame, shear-thickening impact |
| 05 | **HYPER-SOLITON** | 4D polychoron percussion via Hopf fibration, nonlinear Toda soliton lattice |
| 06 | **KAC-SPECTRA** | Isospectral drum solver, Poincaré hyperbolic tree, Kuramoto chimera synth |
| 07 | **PADIC-BRAID** | p-adic ultrametric tree, non-holomorphic fractal series, braid group B₄ loom |
| 08 | **QUASICRYSTAL-PU** | Penrose aperiodic percussion, delta-rule state machine, reversible automaton |
| 09 | **PAS-40 STUDIO** | The forty PAS rudiments as an interactive simulator and sample lab |

## Specialty

| Module | Built on |
|---|---|
| **PENDULUM-LOOM** | 3D harmonic phase loom, Blackburn Lissajous figures, coupled Huygens clocks |

The piece that started the series, and the most directly physical of them — every
hit traces back to a pendulum you can watch swing.

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
*.html          nine laboratory modules + the specialty pendulum lab
```

## Licence

MIT — see [LICENSE](LICENSE). Each module is a standalone artifact; take what's
useful.
