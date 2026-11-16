# Percussion Labs

Thirty-two self-contained, browser-native percussion laboratories, plus two
specialty pendulum pieces. Each one builds an instrument out of a different
piece of physics or mathematics, and generates its sound from the model rather
than playing samples over it.

**Live suite:** https://agenticocho.github.io/percussion-labs/

No build step, no backend, no account. Open `index.html` or any module directly.

Listed in the order the modules were built, which tracks the order of ambition
as well — technique first, then visible physics, then abstractions.

## The thirty-two

| # | Module | Built on |
|---|---|---|
| 01 | **PAS-40 STUDIO** | The forty PAS rudiments as an interactive simulator and sample lab |
| 02 | **EIGENPULSE** | Spatial drumline drill, Bessel-mode cymatics, polyrhythmic hocket |
| 03 | **CHRONOCRYSTAL** | 3D spectral graph percussion, pendulum wave, polyrhythmic automaton |
| 04 | **KAC-SPECTRA** | Isospectral drum solver, Poincaré hyperbolic tree, Kuramoto chimera synth |
| 05 | **QUASICRYSTAL-PU** | Penrose aperiodic percussion, delta-rule state machine, reversible automaton |
| 06 | **PADIC-BRAID** | p-adic ultrametric tree, non-holomorphic fractal series, braid group B₄ loom |
| 07 | **CYMA-FORGE** | Percussive cymatics: Faraday hydro-tank, biharmonic Chladni plate, acoustic levitation |
| 08 | **HYPER-SOLITON** | 4D polychoron percussion via Hopf fibration, nonlinear Toda soliton lattice |
| 09 | **CAVITRON** | Rayleigh–Plesset sonoluminescence, Rijke thermoacoustic flame, shear-thickening impact |
| 10 | **CHIMERA-SWARM** | 3D Kuramoto–Sakaguchi chimera manifold, swarmalator dynamics |
| 11 | **DIAPASON-3D** | Full-screen 3D Euler–Bernoulli tuning fork, von Mises stress, six eigenmodes |
| 12 | **KÁRMÁN-GONG 3D** | Föppl–von Kármán nonlinear shell, wave turbulence, pitch glissando |
| 13 | **KEISU-3D** | Standing bell and singing bowl, Rayleigh–Love rim modes, Faraday spouting |
| 14 | **CAMPANA-3D** | Free-free hanging bell, hum/prime/tierce/quint/nominal partials, bell swarm |
| 15 | **TIMPANI-3D** | Coupled kettle-cavity air spring, live pedal portamento, Bessel inharmonicity |
| 16 | **TAIKO-3D** | Coupled dual-membrane wadaiko, nonlinear pitch glide, kuchi-shōga WAV loop |
| 17 | **CYMBAL-3D** | Föppl–von Kármán nonlinear plate, Weyl modal density, wave-turbulence chaos |
| 18 | **SNARE-3D** | Coupled membrane and snare-wire physics, PAS-40 rudiment lab |
| 19 | **PAN-3D** | Steelpan and handpan, 1:2:3 orthogonal mode coupling, tuned harmonic note fields |
| 20 | **RAINSTICK-3D** | Granular avalanche through a pin lattice, jamming phase transition, inter-arrival timing |
| 21 | **MARIMBA-3D** | Arch-carved bar, 1:4:10 harmonic tuning, quarter-wave resonator, four mallets |
| 22 | **BEAT-FORGE 3D** | Euclidean necklaces, microtiming, groove and polyrhythm architecture |
| 23 | **COCHLEA-MASK 3D** | Auditory masking thresholds and pitch perception |
| 24 | **TALKING-DRUM 3D** | Hourglass tension-cord pitch modulation, speech-surrogate physics |
| 25 | **CROTALES-3D** | Chladni disk modes, chromatic antique cymbals, bowed edge |
| 26 | **WATERPHONE-3D** | Hydro-acoustic friction idiophone, fluid slosh, modal portamento |
| 27 | **METRONOME-SYNC 3D** | Huygens coupled pendulums, anti-phase locking, order-parameter phase transition |
| 28 | **BEAT-FIELD 3D** | Interference and polyrhythm from integer ratios, rhythm-to-pitch crossover |
| 29 | **SAND-PILE 3D** | Bak–Tang–Wiesenfeld self-organised criticality, avalanche rhythm, Poisson null |
| 30 | **DRIP-CLOCK 3D** | Dripping faucet relaxation oscillator, Tate law tempo, period-doubling to chaos |
| 31 | **STRANGE-DRUM 3D** | Thresholded chaotic oscillator, Lyapunov exponent, seed replay, shuffle test |
| 32 | **TIMBRE-CLOCK 3D** | Spectrum-rhythm unifier, 20-50 Hz fusion crossover, single partial array |

## Specialty

| Module | Built on |
|---|---|
| **PENDULUM-LOOM** | 3D harmonic phase loom, Blackburn Lissajous figures, coupled Huygens clocks |
| **NEWTON-PULSE 3D** | Precision percussive Newton's cradle, oddball mass chain, zero-G BPM collider |

Two ways a pendulum makes a rhythm: harmonically, where coupled clocks drift in
and out of phase, and impulsively, where momentum passes through a chain of
balls. Both are more physical than musical — every hit traces back to a swing
you can watch.

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
*.html          thirty-two laboratory modules + two specialty pendulum pieces
```

## Licence

MIT — see [LICENSE](LICENSE). Each module is a standalone artifact; take what's
useful.
