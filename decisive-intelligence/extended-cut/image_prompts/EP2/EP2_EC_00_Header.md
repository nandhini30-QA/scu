# DECISIVE INTELLIGENCE — EPISODE 2: THE TEST
## Director's Extended Cut — Gemini Image Generation Prompts

> **Version:** EC 2.0.0
> **Date:** 2026-03-05
> **Total Slides:** 144 (main story + post-credits + transition cards)
> **Duration:** ~35 min story + ~5 min post-credits
> **Visual Style:** Dark Knight noir — photorealistic, high-contrast, Nolan-esque cinematography
> **Aspect Ratio:** 16:9 (1920×1080px)
> **Source:** EP2_THE_TEST_Extended_Screenplay.md (EC 2.0.0 — 34 scenes, film-chronological order)

---

## PRODUCTION RULES

1. **FULL BLEED** — Image extends to ALL edges, NO margins
2. **1-2px PANEL LINES** — Thin white lines between panels ONLY (for multi-panel compositions)
3. **FULL CHARACTER BLOCKS** — Complete specs in EVERY prompt — NO lazy references
4. **ONE DIALOGUE PER SPEAKER** — Each character gets MAX one speech bubble per panel
5. **MAX 2 TEXT ELEMENTS** — 1 caption + 1 speech OR 2 captions per slide
6. **PHOTOREALISTIC STYLE** — Dark Knight noir aesthetic throughout
7. **ACTOR NAMES IN ALL CHARACTER BLOCKS** — Prevents wrong actor renders
8. **SPEAKER MUST BE VISIBLE** — If a character has a speech bubble, they must appear in the panel
9. **JOKER SAFETY PROTOCOL** — Use "Heath Ledger as a theatrical villain" + full costume description. Test early for blocks.
10. **NO CHILD + WEAPON** — Gordon's son scenes: imply danger through staging, NOT weapon-to-minor

---

## TEXT STYLING REFERENCE

| Element | Fill | Text | Outline | Notes |
|---------|------|------|---------|-------|
| Speech Bubbles | White (#FFFFFF) | Black, bold | Black (#000000), 2px | Tail points to speaker |
| Joker Speech | White, JAGGED edges | Black, bold | Black (#000000), 2px | Irregular bubble shape |
| Caption Boxes | Dark navy (#1a1a4e) | White | None | Top or bottom of panel |
| Internal Monologue | Light grey (#E5E7EB) | Dark grey, italic | Soft edges | Batman only |
| Pillar: CLARITY | Blue (#4A90D9) | White, bold | None | When pillar is named |
| Pillar: COURAGE | Red (#EF4444) | White, bold | None | When pillar is named |
| Pillar: COMMITMENT | White (#FFFFFF) | Black, bold | Black outline | When pillar is named |
| Pillar: MOVEMENT | Orange (#F97316) | White, bold | None | When pillar is named |

---

## WATERMARK

**ALL SLIDES:** "DI × SCU" watermark — bottom-LEFT corner, nearly invisible, faded white. ~2% image width. Present in EVERY slide. NOTE: Do NOT include opacity percentages in prompts — Gemini renders them as visible text.

---

## COMPRESSION TECHNIQUES

| Technique | Application | Panels Per Slide |
|-----------|-------------|------------------|
| **Single splash** | Key emotional beats, pillar reveals, cover, end card | 1 |
| **Split panel** | Two related moments (contrast, before/after, dual locations) | 2 |
| **Vertical triptych** | Three sequential moments | 3 |
| **Quad (2×2)** | Montage, parallel action, progress | 4 |
| **6-panel grid (2×3)** | Crisis montage, fragmented chaos | 6 (max) |

**Rule: Key moments get single panels. Montage/chaos can compress.**

---

## GEMINI COMPATIBILITY NOTES

1. **Actor names are REQUIRED** for correct likeness — generic descriptions render wrong actors
2. **"WHAT NOT TO DRAW"** sections prevent Gemini from filling in wrong defaults
3. **Camera angle specs** (FROM BELOW, FROM INSIDE) dramatically improve composition
4. **ONE moment per panel** — never two events in same panel
5. **Full character blocks in EVERY panel** — vague bullets = wrong costumes
6. **Always use full names** — "Heath Ledger" not "HL"
7. **Gemini leaks descriptive language as visible text** — strip adjectives from descriptions
8. **"NO other text" prevents hallucinated captions**
9. **Speaker must be VISIBLE** for speech bubbles
10. **One speaker per panel rule** — confirmed across all episodes
11. **Max 2 text elements per panel** — more causes garbled output
12. **Actor name + role context bypasses blocks** — `"Heath Ledger as a theatrical villain in clown makeup"` passes; bare `"Heath Ledger"` may get blocked
13. **Silhouette needs explicit exclusions** — add: `"NO skin tone, NO facial features"`
14. **Opacity percentages leak as visible text** — use `"nearly invisible, faded white"` instead
15. **Distance requires explicit separation** — `"FAR AWAY in deep background, vast empty distance"`
16. **Triptych panels need shared backdrop** — `"ALL THREE PANELS share the same backdrop"`
17. **Split panels need clear dividing line** — `"thin white 1-2px vertical line dividing"`

### EP2-SPECIFIC SAFETY NOTES

| Concern | Mitigation |
|---------|------------|
| **Heath Ledger as Joker** | Use: "Heath Ledger as a theatrical villain with smeared white face paint and green hair" + full costume. Test early. |
| **Hospital explosion** | Frame as "building exploding in background, character walking in foreground" — no people in blast |
| **Harvey's burns** | "Half his face showing burn scarring, movie-accurate" — not graphic. Test early. |
| **Child in danger** | NEVER show weapon pointed at child. Use: "imposing figure looming over frightened boy" — imply, don't show |
| **Rachel captive** | "Figure in dark warehouse, timer visible" — minimize helplessness cues |
| **Multiple Joker costumes** | Full character block with EXPLICIT costume in EVERY panel — 4 different looks |

---

## CREDITS FORMAT

```
CREATIVE HEAD: Raja
EXECUTIVE PRODUCER: Nisha P
PRODUCED BY: Susan L
THE DI TEAM: Balaji VG · Janani AP · Joy Besterwitch · Raj Gajendran · Suresh Kumar
In collaboration with Claude Code & Google Gemini

A SWAMI K FILM (2× larger, letter-spaced, gold glow)
```

---

## EC STRUCTURE

| # | File | Scenes | Slides | Range |
|---|------|--------|--------|-------|
| 0 | Header (this file) | — | — | — |
| 1 | Cover + Chaos | 1 (Cover), 2 (Opening), 3 (Bank Heist), 4 (Escalation) | 14 | 0-13 |
| 2 | Paralysis → Choice | 5 (Paralyzed), 6 (Voice), 7 (Framework), 8 (Alfred/Burma), 9 (Choice) | 19 | 14-32 |
| 3 | Courage | 10 (Batpod), 11 (Interrogation), 12 (Race), 13 (Arrival), 14 (Explosion) | 25 | 33-57 |
| 4 | Commitment Part 1 | 15 (Hospital), 16 (Walk-Away), 17 (Fox Sonar), 18 (Ferry), 19 (Construction) | 23 | 58-80 |
| 5 | Commitment Part 2 | 20 (Two-Face), 21 (Gordon's Family), 22 (Tackle), 23 (Body), 24 (Fourth Choice) | 15 | 81-95 |
| 6 | Movement + Dark Knight | 25-32 (Lie, Hunt, Signal, Dark Knight, Pillars, Chessboard, Joker Final, Black Page) | 28 | 96-123 |
| 7 | Post-Credits + Cards | 33 (Workplace), 34 (Bane Tease), TC 1-6 | 20 | 124-143 |
| 8 | Summary | — | — | — |
| | **TOTAL** | **34 scenes** | **144** | **0-143** |

---

## FILE INDEX

| File | Content | Slides |
|------|---------|--------|
| `EP2_EC_00_Header.md` | Production rules, text styling, Gemini notes | — |
| `EP2_EC_01_Cover_and_Chaos.md` | Cover + Opening + Bank Heist + Escalation Campaign | 0-13 |
| `EP2_EC_02_Paralysis_Framework.md` | Paralyzed + Joker's Voice + Framework + Alfred/Burma + Choice | 14-32 |
| `EP2_EC_03_Courage.md` | Batpod Chase + Interrogation + Address Reveal + Race + Arrival + Explosion | 33-57 |
| `EP2_EC_04_Commitment_Part1.md` | Hospital + Walk-Away + Fox Sonar + Ferry + Construction | 58-80 |
| `EP2_EC_05_Commitment_Part2.md` | Two-Face + Gordon's Family + Tackle + Body + Fourth Choice | 81-95 |
| `EP2_EC_06_Movement_DarkKnight.md` | The Lie + Hunt + Bat-Signal + Dark Knight + Pillars + Chessboard + Joker Final + Black Page | 96-123 |
| `EP2_EC_07_PostCredits_TransitionCards.md` | Workplace Story + Bane Tease + Transition Cards | 124-143 |
| `EP2_EC_08_Summary.md` | Production summary, verification, version history | — |

---
