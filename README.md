# NWO: New World Order — Virtual Board Game Prototype

Welcome to the official repository for **NWO - New World Order**, a deep sociological, economic, and dynastic simulation board game executed in a 3D concentric virtual landscape.

## 🌌 Game Overview
Players lead an expanding family dynasty across **7 concentric continent rings**. The game transitions from an open resource scramble in **Phase 1 (Ascent to the Center)** to an intense, asymmetric king-of-the-hill containment battle in **Phase 2 (Global Hegemony)** once the Center (Antarctica) is breached.

## 🛠️ Integrated System Architecture
This repository contains the complete text-based software core prototype, featuring 11 fully integrated object-oriented modules:
1. **The 14 Commandments Morality Matrix:** Modulates the physics of the match (Righteous vs. Evil), altering piece attributes and dynamic luck loops based on your moral choices.
2. **Dynamic Birth-Order Turn Sequencer:** Governs action economies strictly by biological age.
3. **Topographical 3D Pathing:** Features bifurcated forks splitting paths into high-yield, volatile **Lowland Valleys** and expensive, defensive **Highland Ridges**.
4. **Asymmetric Shadow Stack:** Processes face-down cards and routes warning alerts to dashboards strictly based on localized continental **Pulse Ratings**.
5. **Circle-Transition Custody Hand-off:** Instantly terminates a parent's control phase and hands the wheel to the rival parent the exact second a joint-custody piece crosses a portal into a new ring.
6. **Forced Extra Pass Reset:** Forces a joint-custody piece to complete an extra full pass around Antarctica if it sits on the Portal pad but fails the entry check.

## 🚀 How to Run the Prototype
The engine is written in clean, standard Python with zero external system dependencies. To launch a test simulation loop on your machine:
\`\`\`bash
cd src
python nwo_core_engine.py
\`\`\`
