# -*- coding: utf-8 -*-
"""
NWO Advanced AI Personality Factory & Match Controller.
Supports up to 13 players, handles Closed vs Open entry game modes,
and resolves customized behavioral slider personality matrices for computer bots.
"""

import random
import json

class NWOAIFactoryEngine:
    def __init__(self):
        # The 8 Default AI Historical Personas
        self.default_archetypes = {
            "Rogue_Spy": {"aggression": -2, "subversion": 5, "trust": -3, "expansion": 1, "sacrifice": 2},
            "Tech_Monopolist": {"aggression": -1, "subversion": 2, "trust": 2, "expansion": -4, "sacrifice": -3},
            "Cutthroat_Hegemon": {"aggression": 5, "subversion": 1, "trust": -5, "expansion": 5, "sacrifice": 4},
            "Holy_Indoctrinator": {"aggression": 1, "subversion": 4, "trust": -1, "expansion": 2, "sacrifice": 3},
            "War_Profiteer": {"aggression": 4, "subversion": 3, "trust": -4, "expansion": -5, "sacrifice": 1},
            "Insular_Patriarch": {"aggression": -4, "subversion": -3, "trust": 4, "expansion": -3, "sacrifice": -5},
            "Transhuman_Eugenicist": {"aggression": 0, "subversion": 1, "trust": 1, "expansion": 3, "sacrifice": -2},
            "Chaos_Agent": {"aggression": "Random", "subversion": "Random", "trust": "Random", "expansion": "Random", "sacrifice": "Random"}
        }

    def generate_custom_bot_profile(self, bot_id, archetype_name=None, custom_sliders=None):
        """Resolves personality sliders, mapping explicit values or hidden random arrays."""
        resolved_personality = {}
        base_traits = self.default_archetypes.get(archetype_name, {"aggression": 0, "subversion": 0, "trust": 0, "expansion": 0, "sacrifice": 0})
        
        target_source = custom_sliders if custom_sliders else base_traits
        
        for trait, val in target_source.items():
            if val == "Random" or val is None:
                # Random setting active: Roll personality traits blindly under the hood
                resolved_personality[trait] = random.randint(-5, 5)
            else:
                resolved_personality[trait] = val
                
        return {
            "bot_id": bot_id,
            "archetype_label": archetype_name if archetype_name else "CUSTOM_ESTATE",
            "behavior_matrix": resolved_personality
        }

class NWOAdvancedMatchController:
    def __init__(self, mode="CLOSED_GENESIS", max_slots=13):
        self.game_mode = mode # CLOSED_GENESIS or INFILTRATION_ALLOW
        self.max_slots = max_slots
        self.active_factions = {}
        self.current_round_cycle = 1

    def initialize_session_slots(self, human_list, initial_bot_profiles):
        """Initializes the multi-player matrix, enforcing 3-13 scaling boundaries."""
        total_starting = len(human_list) + len(initial_bot_profiles)
        if not (3 <= total_starting <= self.max_slots):
            raise ValueError("Match initialization failed. Player count bounds must sit between 3 and 13.")
            
        for player_id in human_list:
            self.active_factions[player_id] = {"type": "HUMAN", "meta": None}
            
        for bot_packet in initial_bot_profiles:
            self.active_factions[bot_packet["bot_id"]] = {"type": "AI_BOT", "meta": bot_packet}
            
        print(f"🎮 [MATCH INITIALIZED] Mode: {self.game_mode} | Active Seats: {len(self.active_factions)}/13")

    def process_midgame_infiltration_entry(self, incoming_bot_packet):
        """Handles mid-game infiltration entry constraints for late-joining players."""
        if self.game_mode == "CLOSED_GENESIS":
            return {"status": "REJECTED", "reason": "Structural mode constraint: Match is locked. No entry permitted."}
            
        if len(self.active_factions) >= self.max_slots:
            return {"status": "REJECTED", "reason": "Match room slots are entirely maxed out at 13."}
            
        self.active_factions[incoming_bot_packet["bot_id"]] = {"type": "AI_BOT", "meta": incoming_bot_packet}
        print(f"🚪 [INFILTRATION ENTRY] Bot {incoming_bot_packet['bot_id']} has parochuted into Circle 1 live!")
        return {"status": "SUCCESSFUL_ENTRY", "faction_id": incoming_bot_packet["bot_id"]}

# --- VERIFY SYSTEM MATRIX INTEGRATION ---
if __name__ == "__main__":
    factory = NWOAIFactoryEngine()
    controller = NWOAdvancedMatchController(mode="INFILTRATION_ALLOW")
    
    # 1. Generate autonomous rival bot profiles using presets and custom overrides
    bot_b = factory.generate_custom_bot_profile(bot_id="Bot_B", archetype_name="Cutthroat_Hegemon")
    bot_c = factory.generate_custom_bot_profile(bot_id="Bot_C", archetype_name="Chaos_Agent")
    
    custom_setup = {"aggression": 5, "subversion": -4, "trust": "Random", "expansion": 2, "sacrifice": 0}
    bot_d = factory.generate_custom_bot_profile(bot_id="Bot_D", custom_sliders=custom_setup)
    
    # 2. Fire up the 13-player capacity session manager
    controller.initialize_session_slots(human_list=["Player_A"], initial_bot_profiles=[bot_b, bot_c])
    
    # 3. Simulate a late-joining Infiltration entry during cycle loops
    infiltration_receipt = controller.process_midgame_infiltration_entry(incoming_bot_packet=bot_d)
    
    print("\n--- NWO MASTER FACTORY DIAGNOSTICS ---")
    print(f"Bot C (Chaos Agent Roll) Behavior Matrix: {json.dumps(bot_c['behavior_matrix'])}")
    print(f"Bot D (Custom Sliders Roll) Behavior Matrix: {json.dumps(bot_d['behavior_matrix'])}")
    print(f"Infiltration Access Status: {infiltration_receipt['status']}")
    print(f"Total Live Seats on the Board: {len(controller.active_factions)}/13 Factions Locked.")
    print("---------------------------------------")
