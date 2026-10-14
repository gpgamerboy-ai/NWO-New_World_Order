// -*- coding: utf-8 -*-
class NWOHUDVisualEngine {
    constructor() {
        this.cashDisplay = document.querySelector(".panel div[style*='#479e63']");
        this.canvasBox = document.querySelector(".canvas-box");
        this.timelineScroller = document.querySelector(".scroll");
    }

    updateGlobalDashboardState(masterHUDDataPacket) {
        if (!masterHUDDataPacket) return;
        const assets = masterHUDDataPacket.HUD_Zone_A_Assets;
        if (assets && this.cashDisplay) {
            this.cashDisplay.textContent = `${assets.ui_cash_readout} Cash`;
        }
        const canvasMeta = masterHUDDataPacket.HUD_Zone_B_Canvas;
        if (canvasMeta && this.canvasBox) {
            this.canvasBox.innerHTML = `Concentric Map Viewport Mesh Render Active<br><span style="color:#6195c2; font-weight:bold;">🌊 Climate Status: ${canvasMeta.active_3d_viewport_mode}</span>`;
            this.canvasBox.style.backgroundColor = canvasMeta.global_flood_water_mesh_opacity > 0 ? "#05111d" : "#030509";
        }
        const lineageData = masterHUDDataPacket.HUD_Zone_D_Lineage;
        if (lineageData && this.timelineScroller) {
            this.timelineScroller.innerHTML = "";
            lineageData.forEach(piece => {
                const card = document.createElement("div");
                card.className = "card";
                if (piece.diagnostic_status === "HIDDEN_MASKED_BY_CLOAK") {
                    card.style.borderColor = "#d67a47";
                    card.innerHTML = `<div style="font-weight:bold; color:#d67a47;">${piece.piece_tag}</div><div style="font-size:10px; color:#965da8; text-align:center; margin-top:5px;">⚠️ DATA CLOAKED</div>`;
                } else {
                    card.innerHTML = `<div style="font-weight:bold;">${piece.piece_tag}</div><div class="bar-row"><span>Health</span><div class="track"><div class="fill" style="width:${piece.bars.health};"></div></div></div>`;
                }
                this.timelineScroller.appendChild(card);
            });
        }
    }
}
