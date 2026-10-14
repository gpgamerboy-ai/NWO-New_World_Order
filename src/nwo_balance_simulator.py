# -*- coding: utf-8 -*-
import random
import json
from nwo_core_engine import NWOLoopOrchestrator

class NWOThreePlayerSimulator:
    def __init__(self, total_iterations=1000):
        self.total_iterations = total_iterations
        self.metrics_ledger = {
            "THE_CUTTHROAT_HEGEMON": 0, "THE_CONTESTED_TYCOON": 0,
            "THE_GENERATIONAL_PATRIARCH": 0, "TOTAL_GAMES_SIMULATED": 0,
            "AVERAGE_ROUND_DURATION": 0.0
        }
        self.total_rounds_played = 0

    def execute_3_player_simulation_batch(self):
        for sim_idx in range(self.total_iterations):
            orchestrator = NWOLoopOrchestrator(human_players=[], ai_players=["Bot_A", "Bot_B", "Bot_C"])
            orchestrator.bot_nodes["Bot_A"].profile_type = "CUTTHROAT_HEGEMON"
            orchestrator.bot_nodes["Bot_B"].profile_type = "CONTESTED_TYCOON"
            orchestrator.bot_nodes["Bot_C"].profile_type = "GENERATIONAL_PATRIARCH"
            
            match_complete = False
            round_counter = 0
            while not match_complete and round_counter < 50:
                round_counter += 1
                victory_audit = orchestrator.execute_single_global_round_cycle()
                if victory_audit["match_complete"]:
                    path_key = victory_audit.get("winning_path", "THE_CUTTHROAT_HEGEMON")
                    self.metrics_ledger[path_key] += 1
                    match_complete = True
            if not match_complete:
                self.metrics_ledger["THE_CUTTHROAT_HEGEMON"] += 1
            self.total_rounds_played += round_counter
            self.metrics_ledger["TOTAL_GAMES_SIMULATED"] += 1
        self.metrics_ledger["AVERAGE_ROUND_DURATION"] = round(self.total_rounds_played / self.total_iterations, 2)
        return self.metrics_ledger

if __name__ == "__main__":
    balance_tester = NWOThreePlayerSimulator(total_iterations=100)
    final_analytics = balance_tester.execute_3_player_simulation_batch()
    print("\n=================================================================================")
    print(" 📊 NWO PRODUCTION LEVEL METRICS & DATA BALANCE ANALYSIS ")
    print("=================================================================================")
    print(json.dumps(final_analytics, indent=4))
    print("=================================================================================\n")
