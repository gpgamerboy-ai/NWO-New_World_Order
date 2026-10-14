# -*- coding: utf-8 -*-
"""
=================================================================================
             NWO: NEW WORLD ORDER — UNIFIED PROTOTYPE CORE ENGINE
=================================================================================
Core Software Architecture for NWO.
Manages Birth-Order Turn TIMELINEs, 14-Commandment Physics Sliders,
3D Topographical Fork Navigation, Shared-Custody Transitions,
Asymmetric Shadow Stack Espionage, and Network Interception firewalls.
"""

import random
import json

class NWOMatchManager:
    def __init__(self, target_players):
        self.players = target_players
        self.family_estates = {pid: {"cash": 5000, "masses": 100000} for pid in self.players}
        self.birth_order_timeline = []
        self.initialize_first_generation_lineage()

    def initialize_first_generation_lineage(self):
        for pid in self.players:
            pioneer_piece = {
                "piece_id": f"{pid}1",
                "owner_id": pid,
                "active_controller": pid,
                "current_circle": 1,
                "tile_index": 0,
                "generation": 1,
                "Metric_Concealment": False,
                "attributes": {"age_vitality": 100, "health": 100, "mind": 100, "spirit": 50}
            }
            self.birth_order_timeline.append(pioneer_piece)

    def register_new_procreation(self, parent_id, generation_layer):
        estate = self.family_estates[parent_id]
        birth_fee = 1000 * generation_layer
        if estate["cash"] < birth_fee:
            return {"status": "FAILED", "reason": "Insufficient capital."}
        estate["cash"] -= birth_fee
        new_child_id = f"{parent_id}{generation_layer}"
        new_piece = {
            "piece_id": new_child_id,
            "owner_id": parent_id,
            "active_controller": parent_id,
            "current_circle": 1,
            "tile_index": 0,
            "generation": generation_layer,
            "Metric_Concealment": False,
            "attributes": {"age_vitality": 100, "health": 100, "mind": 100, "spirit": 50}
        }
        self.birth_order_timeline.append(new_piece)
        return {"status": "SUCCESS", "piece_id": new_child_id}

class NWOCommandmentsEngine:
    def __init__(self):
        self.universe_sliders = {
            "C1_Faith_Mandate": None, "C2_Veracity_Mandate": None, 
            "C3_Harm_Mandate": None, "C4_Altruism_Mandate": None,
            "C5_Lineage_Mandate": 0, "C6_Execution_Mandate": 0,
            "C7_Alliance_Mandate": 0, "C8_Asset_Mandate": 0,
            "C9_Faction_Mandate": 0, "C10_Territorial_Mandate": 0,
            "C11_Blood_Martyrdom": 3, "C12_Eschata_Politics": 2,
            "C13_War_Profiteer": 4, "C14_Transhuman_Eugenics": 1
        }
        self.resolved_universe_physics = {}

    def execute_pregame_calibration(self, explicit_user_overrides=None):
        for rule, val in self.universe_sliders.items():
            if explicit_user_overrides and explicit_user_overrides.get(rule) == "Random":
                self.resolved_universe_physics[rule] = random.randint(-5, 5)
            elif val is None:
                self.resolved_universe_physics[rule] = random.randint(-5, 5)
            else:
                self.resolved_universe_physics[rule] = val
        return self.resolved_universe_physics

class NWOMovementEngine:
    def __init__(self, rings_metadata):
        self.rings_metadata = rings_metadata
        self.global_path_signatures = {}

    def get_tile_topography_data(self, circle_num, tile_index):
        max_tiles = self.rings_metadata[circle_num]["total_tiles"]
        normalized_index = tile_index % max_tiles
        if normalized_index % 3 == 0:
            return {"topology": "LOWLAND_VALLEY", "yield_mod": 2.5, "defense_mod": 0.4, "is_portal": (normalized_index == max_tiles // 2)}
        return {"topology": "HIGHLAND_RIDGE", "yield_mod": 0.8, "defense_mod": 1.0, "is_portal": False}

    def execute_piece_movement(self, piece_state, dice_roll, preferred_fork=None):
        circle_id = piece_state["current_circle"]
        max_tiles = self.rings_metadata[circle_id]["total_tiles"]
        piece_id = piece_state["piece_id"]
        target_tile = (piece_state["tile_index"] + dice_roll) % max_tiles
        
        tile_meta = self.get_tile_topography_data(circle_id, target_tile)
        if preferred_fork and tile_meta["topology"] != preferred_fork:
            if preferred_fork == "LOWLAND_VALLEY":
                target_tile = (target_tile - (target_tile % 3)) % max_tiles
            else:
                target_tile = (target_tile + 1) % max_tiles
                
        final_meta = self.get_tile_topography_data(circle_id, target_tile)
        piece_state["tile_index"] = target_tile
        
        coord = (circle_id, target_tile)
        if coord not in self.global_path_signatures: self.global_path_signatures[coord] = set()
        self.global_path_signatures[coord].add(piece_id)
        return {"piece_id": piece_id, "landed_coordinate": f"C{circle_id}_T{target_tile}", "topography_profile": final_meta}

class NWOAllianceEngine:
    def __init__(self, match_manager_ref):
        self.match_manager = match_manager_ref
        self.custody_ledger = {}
        self.lap_trackers = {}

    def formalize_dynastic_marriage(self, player_a, player_b, generation_layer):
        shared_id = f"J_{player_a}{player_b}_{generation_layer}"
        self.custody_ledger[shared_id] = {"parent_1": player_a, "parent_2": player_b, "current_lap_owner": player_a, "total_hijack_turns_remaining": 0}
        self.lap_trackers[shared_id] = {"start_tile": 0, "has_completed_lap": False}
        new_joint = {
            "piece_id": shared_id, "owner_id": f"{player_a}+{player_b}", "active_controller": player_a,
            "current_circle": 1, "tile_index": 0, "generation": generation_layer, "Metric_Concealment": False,
            "attributes": {"age_vitality": 100, "health": 100, "mind": 100, "spirit": 50}
        }
        self.match_manager.birth_order_timeline.append(new_joint)
        return shared_id

    def evaluate_lap_completion_and_handoff(self, piece_id, piece_ref):
        if piece_id not in self.custody_ledger: return
        tracker = self.lap_trackers[piece_id]
        custody = self.custody_ledger[piece_id]
        if piece_ref["tile_index"] == tracker["start_tile"] and not tracker["has_completed_lap"]:
            tracker["has_completed_lap"] = True
        if tracker["has_completed_lap"]:
            old = custody["current_lap_owner"]
            nxt = custody["parent_2"] if old == custody["parent_1"] else custody["parent_1"]
            custody["current_lap_owner"] = nxt
            piece_ref["active_controller"] = nxt
            tracker["start_tile"] = piece_ref["tile_index"]
            tracker["has_completed_lap"] = False
            print(f"[CUSTODY ROTATION] Token {piece_id} rotated to {nxt}.")

class NWOShadowStackEngine:
    def __init__(self):
        self.shadow_stack_queue = []
        self.player_pulse_ledger = {}

    def register_covert_shadow_plot(self, caster_id, card_name, target_piece_id, target_circle):
        plot_packet = {"plot_id": random.randint(1000, 9999), "caster_id": caster_id, "card_name": card_name, "target_id": target_piece_id, "circle_num": target_circle}
        self.shadow_stack_queue.append(plot_packet)
        return plot_packet

class NWOVictoryConditionMatrix:
    def __init__(self, match_manager_ref):
        self.match_manager = match_manager_ref

    def execute_global_victory_audit(self):
        for piece in self.match_manager.birth_order_timeline:
            if piece["current_circle"] == 7 and piece["tile_index"] == 3:
                return {"match_complete": True, "victor_id": piece["active_controller"], "summary": "Vortex Central Capture achieved!"}
        return {"match_complete": False, "summary": "The struggle for power continues."}

if __name__ == "__main__":
    match = NWOMatchManager(target_players=["Player_A", "Bot_B"])
    physics = NWOCommandmentsEngine()
    physics.execute_pregame_calibration()
    movement = NWOMovementEngine(rings_metadata={1: {"total_tiles": 12}, 7: {"total_tiles": 6}})
    alliance = NWOAllianceEngine(match_manager_ref=match)
    victory = NWOVictoryConditionMatrix(match_manager_ref=match)
    
    print("--- NWO PROTOTYPE ENGINE INITIALIZED AND RUNNING CLEANLY ---")
    active_heir = match.birth_order_timeline[0]
    move_receipt = movement.execute_piece_movement(active_heir, dice_roll=4, preferred_fork="HIGHLAND_RIDGE")
    print(f"Test Run Success: Piece {move_receipt['piece_id']} advanced to {move_receipt['landed_coordinate']}.")

# =================================================================================
# MODULE 10: THE BLESSING DECK GENERATOR
# =================================================================================
class NWOBlesingDeckMatrix:
    def __init__(self, commandments_engine_ref):
        self.physics = commandments_engine_ref
        self.blessing_pool = ["Divine_Intervention", "Papal_Absolution", "Regulatory_Safeguard"]

    def evaluate_blessing_draw_chance(self, piece_spirit_attribute):
        """Calculates draw modifiers based on individual piece Spirit integrity."""
        if piece_spirit_attribute > 85:
            # High spiritual health unlocks supreme baseline blessing probabilities
            return {"draw_success": True, "drawn_card": random.choice(self.blessing_pool), "luck_modifier": 1.5}
        elif piece_spirit_attribute < 30:
            # Corrupted lineage lines are algorithmically locked out of the Blessing deck
            return {"draw_success": False, "drawn_card": None, "luck_modifier": 0.5}
        
        # Standard baseline roll threshold calculation
        return {"draw_success": random.choice([True, False]), "drawn_card": "Regulatory_Safeguard", "luck_modifier": 1.0}

# =================================================================================
# MODULE 11: THE TRAGEDY DECK GENERATOR
# =================================================================================
class NWOTragedyDeckMatrix:
    def __init__(self, match_manager_ref):
        self.match_manager = match_manager_ref
        self.tragedy_pool = ["Hyperinflation_Collapse", "Inherited_Curse", "Bank_Audit_Freeze"]

    def evaluate_tragedy_trigger(self, piece_ref, global_commandments):
        """Programmatically scans active parameters to force-inject a Tragedy event."""
        attrs = piece_ref["attributes"]
        harm_slider = global_commandments.get("C3_Harm_Mandate", 0)
        
        # If a family's Spirit collapses or the universe is highly predatory, risk spikes
        if attrs["spirit"] < 25 or harm_slider > 3:
            triggered_event = random.choice(self.tragedy_pool)
            
            if triggered_event == "Inherited_Curse":
                # Inject the severe physical defect directly into the token metadata
                piece_ref["traits"].append("Fragile Heir / -2 Move Modifier")
                attrs["health"] = 70
                attrs["mind"] = 70
                
            return {"tragedy_active": True, "event_launched": triggered_event, "severity_index": "CRITICAL"}
            
        return {"tragedy_active": False, "event_launched": None, "severity_index": "STABLE"}

# =================================================================================
# MODULE 12: THE TECHNOLOGICAL ERA CLOCK ENGINE
# =================================================================================
class NWOEraClockEngine:
    def __init__(self, match_manager_ref):
        self.match_manager = match_manager_ref
        self.current_cycle = 1
        self.active_era = "AGRARIAN_EPOCH"

    def advance_global_era_clock(self, global_commandments):
        """Advances the round cycle counter and processes macro paradigm shifts under the hood."""
        self.current_cycle += 1
        
        # Determine the macro civilization tier based on the clock cycle counter
        if self.current_cycle <= 5:
            self.active_era = "AGRARIAN_EPOCH"
        elif 5 < self.current_cycle <= 12:
            self.active_era = "INDUSTRIAL_FORGE"
        else:
            self.active_era = "INFORMATION_TECHNOCRACY"
            
        print(f"\n⏳ [ERA CLOCK] Ticking into Cycle {self.current_cycle}. Current World State: {self.active_era}")
        
        # If the Information Technocracy hits and Eschata-Politics is Evil, spark labor revolts
        eschata_slider = global_commandments.get("C12_Eschata_Politics", 0)
        if self.active_era == "INFORMATION_TECHNOCRACY" and eschata_slider > 2:
            print("🚨 [LABOR STRIKE] Automation has triggered massive working-class unrest on the outer rings!")
            # Systemic fallout forces a 50% revenue deduction on Circle 1 raw material extraction nodes
            for pid in self.match_manager.players:
                self.match_manager.family_estates[pid]["masses"] = max(1000, int(self.match_manager.family_estates[pid]["masses"] * 0.90))
                
        return {"current_cycle": self.current_cycle, "active_era": self.active_era}

# =================================================================================
# MODULE 13: MACRO ECONOMIC TRADE & ASSET LEDGER
# =================================================================================
class NWOEconomicLedgerSystem:
    def __init__(self, match_manager_ref):
        self.match = match_manager_ref

    def execute_private_wire_transfer(self, sender_id, recipient_id, transfer_amount, global_commandments):
        """Processes peer-to-peer asset transfers, calculating structural compliance taxes."""
        sender_vault = self.match.family_estates[sender_id]
        recipient_vault = self.match.family_estates[recipient_id]
        
        if sender_vault["cash"] < transfer_amount:
            return {"status": "REJECTED", "reason": "Insufficient capital inside sender vault."}
            
        # Deduct starting base payload
        sender_vault["cash"] -= transfer_amount
        
        # Evaluate compliance tax based on Commandment 8 (Asset Mandate)
        asset_slider = global_commandments.get("C8_Asset_Mandate", 0)
        final_delivery_amount = transfer_amount
        
        if asset_slider < 0:
            # Universe enforces Sacred Stewardship: apply strict financial regulation tax
            tax_deduction = int(transfer_amount * 0.15)
            final_delivery_amount -= tax_deduction
            print(f"[BANK REGULATION] A 15% compliance tax (${tax_deduction}) was siphoned into global reserves.")
            
        recipient_vault["cash"] += final_delivery_amount
        return {
            "status": "TRANSFER_COMPLETE",
            "debited": sender_id,
            "credited": recipient_id,
            "net_received": final_delivery_amount
        }

# =================================================================================
# MODULE 14: GLOBAL CATASTROPHE RESOLUTION & ENGINE RESETS
# =================================================================================
class NWOCatastropheResolutionSystem:
    def __init__(self, match_manager_ref, movement_engine_ref):
        self.match = match_manager_ref
        self.movement = movement_engine_ref
        self.sea_level = 0

    def execute_instant_shockwave(self, target_circle):
        """Processes immediate topographical wreckage calculations across a continent ring."""
        print(f"\n💥 [CRITICAL SHOCKWAVE] Processing Asteroid impact calculations for Circle {target_circle}...")
        
        for piece in self.match.birth_order_timeline:
            if piece["current_circle"] == target_circle:
                # Retrieve tile elevation metadata to factor cover bonuses
                tile_meta = self.movement.get_tile_topography_data(target_circle, piece["tile_index"])
                attrs = piece["attributes"]
                
                if tile_meta["topology"] == "LOWLAND_VALLEY":
                    print(f"💀 Piece {piece['piece_id']} caught in valley basin. Maximum damage applied.")
                    attrs["health"] = max(0, attrs["health"] - 80)
                    attrs["mind"] = max(10, attrs["mind"] - 50)
                else:
                    print(f"⛰️ Piece {piece['piece_id']} protected by highland topography cover. Damage mitigated.")
                    attrs["health"] = max(0, attrs["health"] - 30)
                    attrs["mind"] = max(10, attrs["mind"] - 50)
                    
        return {"status": "SHOCKWAVE_RESOLVED", "circle_targeted": target_circle}

    def process_exponential_flood_tick(self, target_circle, active_wave_cycle):
        """Simulates real-time multi-cycle sea level rises, force-displacing pieces uphill."""
        self.sea_level += (20 * active_wave_cycle)
        print(f"\n🌊 [CLIMATE INFRASTRUCTURE RESET] Flood Wave {active_wave_cycle} rising. Sea level: {self.sea_level}%")
        
        for piece in self.match.birth_order_timeline:
            if piece["current_circle"] == target_circle:
                tile_meta = self.movement.get_tile_topography_data(target_circle, piece["tile_index"])
                
                # Check for valley submergence threshold limits
                if tile_meta["topology"] == "LOWLAND_VALLEY" and self.sea_level > 35:
                    print(f"⚠️ [EVACUATION REQUIRED] Piece {piece['piece_id']} valley tracks drowned. Moving piece uphill.")
                    piece["tile_index"] = (piece["tile_index"] + 1) # Force spatial displacement
                    piece["attributes"]["health"] = max(10, piece["attributes"]["health"] - 15)
                    
        if self.sea_level >= 100:
            self.sea_level = 0 # Ocean parameters settle post total geographical reset
            print("🌊 The Great Flood has completed its absolute environmental reset cycle.")
            
        return {"current_sea_level": self.sea_level}

# =================================================================================
# MODULE 15: VISUAL HUD INTERFACE CONTROLLER
# =================================================================================
class NWOHUDVisualController:
    def __init__(self, match_manager_ref):
        self.match = match_manager_ref
        self.interface_theme = "TACTICAL_DARK_CYBER"

    def compile_screen_render_frame(self, target_player_id, localized_pulse_rating, current_sea_level):
        estate_profile = self.match.family_estates.get(target_player_id, {"cash": 0, "masses": 0})
        asset_panel = {"ui_cash_readout": f"${estate_profile['cash']}", "ui_masses_readout": f"{estate_profile['masses']} Citizens"}
        
        map_canvas_layer = {
            "global_flood_water_mesh_opacity": 0.0 if current_sea_level == 0 else 0.65,
            "render_lowlands_as_active": True if current_sea_level <= 35 else False,
            "active_3d_viewport_mode": "STANDARD_MAP" if current_sea_level < 80 else "CRISIS_MIGRATION_GLOW"
        }
        
        lineage_panel_items = []
        for piece in self.match.birth_order_timeline:
            piece_id = piece["piece_id"]
            owner = piece["owner_id"]
            attrs = piece["attributes"]
            is_cloaked = piece.get("Metric_Concealment", False)
            
            if owner != target_player_id and is_cloaked:
                lineage_panel_items.append({"piece_tag": piece_id, "coordinate": f"C{piece['current_circle']}_T{piece['tile_index']}", "owner_crest": f"Team_{owner}", "diagnostic_status": "HIDDEN_MASKED_BY_CLOAK"})
            else:
                lineage_panel_items.append({
                    "piece_tag": piece_id, "coordinate": f"C{piece['current_circle']}_T{piece['tile_index']}", "owner_crest": f"Team_{owner}", "diagnostic_status": "RENDER_FULL_CLARITY",
                    "bars": {"vitality": f"{attrs['age_vitality']}%", "health": f"{attrs['health']}%", "mind": f"{attrs['mind']}%", "spirit": f"{attrs['spirit']}%"}
                })

        return {"theme_configuration": self.interface_theme, "HUD_Zone_A_Assets": asset_panel, "HUD_Zone_B_Canvas": map_canvas_layer, "HUD_Zone_D_Lineage": lineage_panel_items}

# =================================================================================
# MODULE 16: THE BLESSING DECK CARD DATA LEDGER
# =================================================================================
class NWOBlessingDeckRegistry:
    def __init__(self, match_manager_ref):
        self.match = match_manager_ref
        self.blessings = {
            "Divine_Intervention": {"cash_cost": 0, "mass_cost": 0, "class": "RESPONSE_AURA"},
            "Papal_Absolution": {"cash_cost": 0, "mass_cost": 2000, "class": "MACRO_ACTION"},
            "Regulatory_Safeguard": {"cash_cost": 1500, "mass_cost": 0, "class": "PASIVE_SHIELD"}
        }

    def process_blessing_deployment(self, player_id, blessing_key, target_ref):
        """Validates card constraints and applies positive trait overrides to character sheets."""
        card = self.blessings.get(blessing_key)
        if not card:
            return {"status": "ERROR", "msg": "Card missing from master blessing database."}
            
        estate = self.match.family_estates[player_id]
        if estate["cash"] < card["cash_cost"] or estate["masses"] < card["mass_cost"]:
            return {"status": "REJECTED", "reason": "Insufficient religious or corporate capital."}
            
        # Deduct transaction resource costs
        estate["cash"] -= card["cash_cost"]
        estate["masses"] -= card["mass_cost"]
        
        # --- EXECUTE CARD REWARD MATRIX ROUTINES ---
        if blessing_key == "Papal_Absolution":
            print(f"🕊️ [PAPAL ABSOLUTION]: Cleansing spiritual metrics for Player {player_id}...")
            for piece in self.match.birth_order_timeline:
                if piece["owner_id"] == player_id or player_id in piece["owner_id"]:
                    piece["attributes"]["spirit"] = 100 # Reset karma vector to absolute maximum
                    
        elif blessing_key == "Regulatory_Safeguard" and target_ref:
            # Append a permanent sovereign protection modifier tag to the asset
            target_ref["is_shielded_by_safeguard"] = True
            print(f"🛡️ [SAFEGUARD LOCKED]: Asset coordinate is now immune to corporate piracy loops.")
            
        return {"status": "SUCCESSFUL_BLESSING_DEPLOYMENT", "remaining_vault": estate}

# =================================================================================
# MODULE 17: COMBAT DAMAGE ALLOCATION & TOPOGRAPHICAL ARMOR
# =================================================================================
class NWOCombatDamageEngine:
    def __init__(self, movement_engine_ref):
        self.movement = movement_engine_ref

    def calculate_mitigated_combat_damage(self, attacker_type, target_piece_ref):
        """Processes kinetic hits, scaling damage against tile elevation profiles."""
        attrs = target_piece_ref["attributes"]
        circle = target_piece_ref["current_circle"]
        tile = target_piece_ref["tile_index"]
        
        # Pull layout metadata for target coordinates
        tile_meta = self.movement.get_tile_topography_data(circle, tile)
        topology_type = tile_meta["topology"]
        
        base_health_hit = 0
        base_mind_hit = 0
        
        # --- EXECUTE DAMAGE SCALING CALCULATION LOOPS ---
        if attacker_type == "DRONE_STRIKE":
            if topology_type == "LOWLAND_VALLEY":
                base_health_hit = 50 * 1.0
                base_mind_hit = 20
            else: # HIGHLAND_RIDGE
                base_health_hit = 50 * 0.4
                base_mind_hit = 10
                
        elif attacker_type == "KAMIKAZE_ZEALOT":
            if topology_type == "LOWLAND_VALLEY":
                base_health_hit = 100 # Immediate liquidation
                base_mind_hit = 100
            else: # HIGHLAND_RIDGE
                base_health_hit = 40
                base_mind_hit = 60
                
        # Deduct damage values from character sheet attribute arrays
        attrs["health"] = max(0, attrs["health"] - int(base_health_hit))
        attrs["mind"] = max(10, attrs["mind"] - int(base_mind_hit))
        
        return {
            "piece_id": target_piece_ref["piece_id"],
            "net_health_damage": int(base_health_hit),
            "net_mind_damage": int(base_mind_hit),
            "survived": attrs["health"] > 0
        }

# =================================================================================
# MODULE 18: PSYCHOLOGICAL WARFARE & IDEOLOGICAL INDOCTRINATION
# =================================================================================
class NWOPsychologicalSubversionEngine:
    def __init__(self, match_manager_ref):
        self.match = match_manager_ref

    def evaluate_mental_paralysis_state(self, piece_ref):
        """Checks target Mind threshold constraints to enforce psychological paralysis blocks."""
        attrs = piece_ref["attributes"]
        
        if attrs["mind"] <= 40:
            print(f"🧠 [PARALYSIS ACTIVE] Piece {piece_ref['piece_id']} is suffering from acute paranoia. Movement frozen.")
            return {"can_act": False, "status_flag": "PSYCHOLOGICAL_PARALYSIS"}
            
        return {"can_act": True, "status_flag": "MENTAL_STABILITY_INTACT"}

    def execute_mass_indoctrination_sweep(self, caster_id, target_player_id, target_circle):
        """Programmatically siphons ideological mass nodes from a compromised rival dynasty."""
        caster_estate = self.match.family_estates[caster_id]
        target_estate = self.match.family_estates[target_player_id]
        
        # Siphon exactly 25% of the local population pool away from the rival estate
        siphoned_masses = int(target_estate["masses"] * 0.25)
        target_estate["masses"] -= siphoned_masses
        caster_estate["masses"] += siphoned_masses
        
        print(f"☀️ [INDOCTRINATION SUCCESS] Player {caster_id} hijacked {siphoned_masses} masses from Player {target_player_id} on Circle {target_circle}.")
        return {"net_masses_shifted": siphoned_masses}

# =================================================================================
# MODULE 19: COUNTER-ESPIONAGE RADAR & INTELLIGENCE AUDITS
# =================================================================================
class NWOCounterEspionageRadar:
    def __init__(self, shadow_stack_ref, match_manager_ref):
        self.shadow_stack = shadow_stack_ref
        self.match = match_manager_ref

    def execute_ring_threat_audit(self, auditor_id, target_circle):
        """Scans the hidden Shadow Stack backend queue, uncloaking plots targeting this ring."""
        auditor_estate = self.match.family_estates[auditor_id]
        if auditor_estate["cash"] < 1000:
            return {"status": "REJECTED", "reason": "Insufficient corporate capital for radar probe."}
            
        auditor_estate["cash"] -= 1000
        uncovered_plots_count = 0
        exposed_data_briefs = []
        
        # Programmatically loop through the background stack array
        for plot in self.shadow_stack.shadow_stack_queue:
            if plot["circle_num"] == target_circle and not plot.get("is_exposed", False):
                plot["is_exposed"] = True  # Tear away information masking filters
                uncovered_plots_count += 1
                exposed_data_briefs.append(plot)
                print(f"📡 [RADAR EXPOSE] Secret trap ID {plot['plot_id']} successfully uncloaked on Circle {target_circle}!")
                
        return {
            "status": "AUDIT_RESOLVED",
            "plots_uncovered": uncovered_plots_count,
            "briefs": exposed_data_briefs,
            "remaining_cash": auditor_estate["cash"]
        }

    def pierce_metric_concealment(self, target_piece_ref):
        """Breaks biological data cloaking meshes to force-render true core metrics."""
        if target_piece_ref.get("Metric_Concealment", False):
            # De-cloak the encryption flags on the target character sheet data array
            target_piece_ref["Metric_Concealment"] = False
            print(f"👁️ [DE-CLOAKED] Biometric signature for piece {target_piece_ref['piece_id']} broken. Metrics exposed.")
            return {"decryption_status": "SUCCESSFUL_PENETRATION", "true_attributes": target_piece_ref["attributes"]}
            
        return {"decryption_status": "TARGET_WAS_ALREADY_VISIBLE", "true_attributes": target_piece_ref["attributes"]}
