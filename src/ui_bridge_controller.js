// -*- coding: utf-8 -*-
class NWOLaunchDashboardController {
    constructor() {
        this.modeSelector = document.getElementById("match-mode-selector");
        this.seatsInput = document.getElementById("total-seats-count");
        this.simSelector = document.getElementById("simulation-mode-selector");
        this.archetypeSelector = document.getElementById("bot-template-selector");
        this.behaviorSliders = {
            "aggression": { slider: document.getElementById("slider-aggro"), checkbox: document.getElementById("random-aggro") },
            "subversion": { slider: document.getElementById("slider-subvert"), checkbox: document.getElementById("random-subvert") },
            "trust": { slider: document.getElementById("slider-trust"), checkbox: document.getElementById("random-trust") }
        };
    }

    compileMasterInitializationPayload() {
        const seatsValue = parseInt(this.seatsInput.value, 10);
        if (isNaN(seatsValue) || seatsValue < 3 || seatsValue > 13) {
            return null;
        }
        const resolvedBehaviorMatrix = {};
        for (const trait in this.behaviorSliders) {
            const target = this.behaviorSliders[trait];
            resolvedBehaviorMatrix[trait] = target.checkbox ? "Random" : parseInt(target.slider.value, 10);
        }
        return {
            "global_game_mode": this.modeSelector ? this.modeSelector.value : "CLOSED_GENESIS",
            "allocated_seats_count": seatsValue,
            "bot_factory_settings": resolvedBehaviorMatrix
        };
    }
}
