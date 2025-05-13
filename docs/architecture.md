# Architecture & Design Overview

## System Components

1. **Python Module:**
   - **fetch_configs.py:** Uses APIs (e.g., AWS Boto3) to pull configuration data.
   - **evaluate_policies.py:** Evaluates each configuration against defined cloud security policies and calculates a risk score.
     
2. **Node.js API:**
   - Exposes endpoints for both the evaluated configuration data and serves the interactive dashboard.
   - Can be extended to trigger remediation alerts using integrations (email, Slack).

3. **Dashboard:**
   - An HTML/JavaScript frontend that uses Plotly.js to visualize the risk scores and compliance status over time.
   - Provides an interactive way to monitor cloud security posture trends.

## Data Flow
- Raw configuration data is fetched by the Python module.
- Configurations are evaluated for compliance; each resource is scored, and remediation steps suggested.
- Evaluated results are served via the Node.js API.
- The dashboard fetches these results and renders an interactive risk timeline.

## Future Enhancements
- Integration with real-time cloud APIs in production (secure credentials management).
- Advanced risk scoring based on additional features.
- Automated remediation playbooks triggered directly from the dashboard.
