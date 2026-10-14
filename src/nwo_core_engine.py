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
