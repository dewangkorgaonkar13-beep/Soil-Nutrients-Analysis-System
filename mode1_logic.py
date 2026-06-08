import json

# Load ideal values
with open("crop_ideal_values.json") as f:
    ideal_data = json.load(f)

def optimize_crop(crop, soil):
    ideal = ideal_data[crop]

    # Calculate deficiency
    req_N = max(ideal["N"] - soil["N"], 0)
    req_P = max(ideal["P"] - soil["P"], 0)
    req_K = max(ideal["K"] - soil["K"], 0)

    # Fertilizer calculation
    urea = (req_N * 100) / 46
    dap  = (req_P * 100) / 46
    mop  = (req_K * 100) / 60

    return {
        "ideal": ideal,
        "deficiency": {
            "N": round(req_N, 2),
            "P": round(req_P, 2),
            "K": round(req_K, 2)
        },
        "fertilizer": {
            "Urea (kg/ha)": round(urea, 2),
            "DAP (kg/ha)": round(dap, 2),
            "MOP (kg/ha)": round(mop, 2)
        }
    }
