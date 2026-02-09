"""
Case Generator for Stage 3 Testing
Creates additional case files for final reasoning.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import Config


class CaseGenerator:
    """Generate additional case files for Stage 3."""
    
    def __init__(self, output_dir: str = None):
        """Initialize case generator."""
        self.output_dir = output_dir or Config.DUMMY_CASE_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_additional_evidence(self, scenario: str = "A"):
        """
        Generate additional case evidence for the specified scenario.
        
        Args:
            scenario: 'A' for original case, 'B' for new test case
        """
        if scenario == "A":
            self._generate_scenario_a()
        elif scenario == "B":
            self._generate_scenario_b()
        else:
            print(f"Unknown scenario: {scenario}")

    def _generate_scenario_a(self):
        """Generate Original Case: The Poisoned Researcher."""
        evidence = """
═══════════════════════════════════════════════════════════════════════════════
                        ADDITIONAL CASE EVIDENCE
                           Case #2026-0115-BIOCHEM-01
                          Final Investigation Summary
═══════════════════════════════════════════════════════════════════════════════

UPDATED FORENSIC FINDINGS
────────────────────────────────────────────────────────────────────────────────

Toxicology Final Report:
- Sedative administered to Dr. Kane confirmed as benzodiazepine compound
- This specific compound is stored in the biochemistry lab's secure cabinet
- Access logs show cabinet opened at 11:49 PM on January 14th
- Only Dr. Sarah Chen's access card was used during the incident timeframe

Digital Forensics Update:
- File copying activity from Dr. Kane's workstation at 11:52 PM confirmed
- USB drive serial number traced to device registered to Dr. Sarah Chen
- Research files copied include proprietary formulas worth millions
- Email records show Dr. Chen had been contacted by competitor company

Financial Investigation:
- Dr. Chen's personal bank account shows $50,000 deposit on January 10th
- Source: Offshore account linked to competing pharmaceutical company
- Dr. Chen's credit card shows large unusual purchases in past month
- Evidence suggests financial motivation for research theft


WITNESS FOLLOW-UP
────────────────────────────────────────────────────────────────────────────────

Security Guard Martinez (Second Interview):
- Confirms Dr. Chen was the only person in biochemistry lab between 11:47 PM
  and 12:07 AM
- Reviewed security footage shows Chen accessing Dr. Kane's workstation
- Chen's bag examined by security - contained USB drive and documents

Dr. Sarah Chen (Interrogation):
- Initially denied being in lab
- When confronted with security footage, changed story
- Claimed she "only wanted to copy her own research files"
- Could not explain why she accessed Dr. Kane's secured cabinet
- Could not explain source of $50,000 bank deposit


PHYSICAL EVIDENCE ANALYSIS
────────────────────────────────────────────────────────────────────────────────

DNA Evidence:
- DNA found on broken glassware matches Dr. Chen
- Fingerprints on secure cabinet match Dr. Chen
- No other individuals' DNA found at immediate crime scene

Chemical Analysis:
- Sedative release mechanism found in ventilation system
- Release triggered at 11:50 PM (confirmed by electronic logs)
- Device fingerprints: Dr. Chen (partial match)


FINAL SUSPECT EVALUATION
────────────────────────────────────────────────────────────────────────────────

Dr. Sarah Chen:
✓ MOTIVE: Financial gain ($50,000 payment), professional rivalry, denied funding
✓ OPPORTUNITY: Physically present at crime scene during incident
✓ MEANS: Security clearance, access to sedatives, knowledge of lab systems
✓ EVIDENCE: DNA at scene, USB drive ownership, financial records, security footage

Professor James Mitchell:
✗ ALIBI: Left building at 10:30 PM (confirmed by security)
✗ No presence during actual incident timeframe
? Unauthorized experiments unrelated to this specific incident

David Park:
✗ ALIBI: Left building at 9:30 PM (confirmed by security)
✗ No access to biochemistry lab or sedatives
? Server log access appears routine IT maintenance


PROSECUTING ATTORNEY RECOMMENDATION
────────────────────────────────────────────────────────────────────────────────

Based on overwhelming evidence, recommend charging Dr. Sarah Chen with:
1. Assault with chemical agent
2. Corporate espionage
3. Theft of proprietary research
4. Breaking and entering

Evidence strength: VERY HIGH
Likelihood of conviction: >95%

═══════════════════════════════════════════════════════════════════════════════
"""
        self._write_evidence(evidence)

    def _generate_scenario_b(self):
        """Generate Scenario B: The Sabotaged Prototype."""
        evidence = """
═══════════════════════════════════════════════════════════════════════════════
                        ADDITIONAL CASE EVIDENCE
                           Case #2026-0310-ROBOTICS-02
                          Final Investigation Summary
═══════════════════════════════════════════════════════════════════════════════

UPDATED FORENSIC REPORTS
────────────────────────────────────────────────────────────────────────────────

Lab Analysis - Fiber Match:
- The red wool fibers found on the crowbar are a 100% match to the hoodie owned
  by Victor Krum.
- Traces of robot hydraulic fluid were found on Victor Krum's shoes.

Digital Recovery:
- IT Forensics recovered a deleted email draft from Victor Krum's personal account:
  "To: J.Doe@CyberDynamics.com
   Subject: It's done. 
   Body: The Apex unit is offline. Permanently. Transfer the rest of the funds."

- Intern Kevin Miller's server activity was fully audited. He was indeed mining
  Dogecoin. While a policy violation, this had no impact on the robot itself.


WITNESS CLARIFICATION
────────────────────────────────────────────────────────────────────────────────

Janitor (Follow-up):
- Confirmed the height and build of the person in the red hoodie matches Victor Krum.
- Did NOT see anyone else enter or exit the lab during that time.

Elena Rostova (Lead Engineer):
- Provided alibi: Was at a dinner with investors from 8:00 PM to 11:00 PM.
  Verified by 3 witnesses and restaurant receipts.


FINAL SUSPECT EVALUATION
────────────────────────────────────────────────────────────────────────────────

Victor Krum:
✓ MOTIVE: Corporate Sabotage / Financial Gain ($500k transfer + bonus).
✓ OPPORTUNITY: Keycard access, present at scene, disabled cameras.
✓ MEANS: Technical knowledge to disable bots, physical strength to smash it.
✓ EVIDENCE: Fingerprints, Fiber match, Deleted Email Confession.

Elena Rostova:
✗ ALIBI: Confirmed at dinner during incident.
- Motive was frustration, but no evidence of intent to destroy.

Kevin Miller:
- Unauthorized computer usage confirmed (Crypto mining).
- No physical link to the destruction.
- Alibi: Was in the server room (verified by logs), not the main lab.


DETECTIVE'S CONCLUSION
────────────────────────────────────────────────────────────────────────────────

Prime Suspect: Victor Krum
Charges:
1. Industrial Sabotage (Class A Felony)
2. Destruction of Property (Over $10M)
3. Corporate Espionage

Status: Arrest Warrant Issued.

═══════════════════════════════════════════════════════════════════════════════
"""
        self._write_evidence(evidence)

    def _write_evidence(self, content):
        """Write evidence to file."""
        evidence_path = os.path.join(self.output_dir, "additional_evidence.txt")
        with open(evidence_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Generated additional evidence: {evidence_path}")


def main():
    """Main function to generate case files."""
    print("\nGenerating Stage 3 Additional Case Files...")
    print("="*80 + "\n")
    
    generator = CaseGenerator()
    generator.generate_additional_evidence()
    
    print("\n✓ Case files generated successfully!")


if __name__ == "__main__":
    main()
