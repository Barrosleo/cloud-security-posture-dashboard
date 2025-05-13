# python-module/evaluate_policies.py

import json

def evaluate_config(config):
    """
    Check a given configuration against defined policies.
    E.g., ensure MFA is enabled, storage is not public, etc.
    """
    risk_score = 0
    recommendations = []
    
    # Example check: if public IP is present, add risk points.
    if config.get("PublicIpAddress"):
        risk_score += 5
        recommendations.append("Consider removing the public IP or using a VPN.")
    
    # Add additional checks based on policies...
    
    return risk_score, recommendations

def process_configs(configs):
    results = []
    for config in configs:
        risk, recs = evaluate_config(config)
        config.update({"risk_score": risk, "recommendations": recs})
        results.append(config)
    return results

if __name__ == "__main__":
    with open("sample_data/aws_sample.json", "r") as f:
        configs = json.load(f)
    evaluated = process_configs(configs)
    print(json.dumps(evaluated, indent=2))
