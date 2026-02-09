"""
Dummy Dossier Generator for Stage 2 Testing
Creates investigation dossiers with embedded clues about the mystery case.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import Config


class DossierGenerator:
    """Generate dummy investigation dossiers for testing Stage 2."""
    
    def __init__(self, output_dir: str = None):
        """Initialize dossier generator."""
        self.output_dir = output_dir or Config.DUMMY_DOCUMENTS_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
        print(f"  Pages: 8")

    def generate_investigation_dossier(self, scenario: str = "A"):
        """
        Generate investigation dossier for the specified scenario.
        
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
        dossier_content = """
═══════════════════════════════════════════════════════════════════════════════
                        CONFIDENTIAL INVESTIGATION DOSSIER
                           Case #2026-0115-BIOCHEM-01
                        University Research Facility Incident
═══════════════════════════════════════════════════════════════════════════════

PAGE 1: CASE SUMMARY
────────────────────────────────────────────────────────────────────────────────

Date of Incident: January 15, 2026, 07:15 AM
Location: Biochemistry Research Lab, 3rd Floor, Building A
Victim: Dr. Robert Kane (59), Principal Research Scientist
Status: Found unconscious, currently hospitalized in stable condition

Initial Response: Security alerted by Dr. Lisa Park at 07:15 AM. Emergency 
services arrived at 07:28 AM. Lab secured and declared potential crime scene.

Primary Concerns:
- Suspicious circumstances surrounding Dr. Kane's condition
- Missing research documents and proprietary compounds
- Evidence of unauthorized access to secure areas
- Potential corporate espionage or internal sabotage

Lead Investigator: Detective Maria Rodriguez
Case Classification: Suspicious incident under investigation


PAGE 2: PERSONNEL RECORDS AND BACKGROUND
────────────────────────────────────────────────────────────────────────────────

Dr. Robert Kane (Victim)
- Position: Principal Research Scientist, Biochemistry Department
- Tenure: 15 years with the university
- Current Project: Breakthrough therapeutic compound development
- Security Clearance: Level 5 (Highest)
- Recent Activity: Had expressed concerns about research data theft
- Known Conflicts: Professional tensions with Dr. Sarah Chen over budget 
  allocation and research priorities

Dr. Sarah Chen
- Position: Senior Research Scientist, Biochemistry Department
- Tenure: 8 years with the university
- Security Clearance: Level 4
- Recent Activity: Submitted budget increase request (denied by Dr. Kane)
- Access History: Building access on night of incident at 11:47 PM
- Note: Has been accessing financial records system 7 times in the past month,
  including budget allocations, expense reports, and research funding documents

Professor James Mitchell
- Position: Associate Professor, Advanced Chemistry
- Tenure: 12 years with the university
- Security Clearance: Level 3
- Recent Activity: Multiple late-night lab visits
- Note: Has been conducting experiments in the biochemistry lab without proper
  authorization. Lab logs show 12 instances of after-hours access to restricted
  areas. Colleagues report seeing unusual compounds and unapproved experimental
  setups in his workspace.

David Park
- Position: IT Systems Administrator
- Tenure: 5 years with the university
- Security Clearance: Level 4 (IT)
- Recent Activity: Performed system maintenance on January 14th, 9:00 PM
- Access History: David Park accessed the central server logs system on Jan 14th
  at 9:15 PM and again at 10:30 PM. Server logs indicate he viewed access records
  for the biochemistry lab, including keycard entries and security camera timestamps.
  He also accessed the financial database server logs.


PAGE 3: SECURITY AND ACCESS LOGS
────────────────────────────────────────────────────────────────────────────────

Building Access Records - January 14, 2026:

17:45 PM - Dr. Robert Kane (Entry)
18:00 PM - Michael Torres, Lab Assistant (Exit)
20:30 PM - Professor James Mitchell (Entry) - Biochemistry Lab, 3rd Floor
21:00 PM - David Park (Entry) - Server Room, 2nd Floor
22:30 PM - Professor James Mitchell (Exit)
23:47 PM - Dr. Sarah Chen (Entry) - Biochemistry Lab, 3rd Floor
23:52 PM - Security Guard Martinez patrol noted Dr. Chen on 3rd floor
00:07 AM (Jan 15) - Dr. Sarah Chen (Exit) - Hasty departure noted by security

Keycard Anomalies:
- Dr. Chen's late-night access unusual (normal exit time: 6 PM)
- Professor Mitchell accessed restricted biochemistry lab (not authorized)

Security Camera Notes:
- 23:47 PM: Dr. Chen carrying large bag (contents unknown)
- 23:55 PM: Movement in lab visible, appears to be searching through files
- 00:03 AM: Rapid movement, possible altercation or accident
- 00:07 AM: Dr. Chen exits building quickly


PAGE 4: FINANCIAL RECORDS ANALYSIS
────────────────────────────────────────────────────────────────────────────────

Budget Allocation Disputes:

Q4 2025 Research Funding:
- Dr. Kane's Project: $850,000 allocated
- Dr. Chen's Project: $420,000 allocated
- Dr. Chen filed complaint about funding inequality (Dec 2025)

Financial System Access Logs:
- Dr. Sarah Chen: Accessed budget system 7 times in past 30 days
  Viewed: Department budgets, Dr. Kane's funding, expense reports, equipment 
  purchases, grant allocations, salary information, external funding sources
  
- David Park: Accessed financial database server logs on Jan 14th as part of
  system maintenance. Logs show he reviewed who had accessed financial records.

Recent Unusual Transactions:
- Large equipment purchase by Dr. Chen (unauthorized): $15,000
- Research material order flagged by procurement (unusual chemicals)
- Dr. Kane submitted report to administration about unauthorized spending


PAGE 5: LABORATORY EVIDENCE
────────────────────────────────────────────────────────────────────────────────

Crime Scene Analysis (Biochemistry Lab, 3rd Floor):

Physical Evidence:
- Broken glassware found on floor (beakers and test tubes)
- Chemical spill requiring hazmat cleanup
- Dr. Kane's lab notebook found open, pages torn out
- Secure storage cabinet found open (normally locked)
- Missing items: 3 compound samples, 2 notebooks, research USB drive

Chemical Analysis:
- Traces of sedative compound detected in lab air samples
- Concentration suggests deliberate release, not accidental exposure

Document Evidence:
- Computer logs show file access at 23:51 PM (Dr. Kane's workstation)
- Login credentials: Dr. Kane's account (possibly used by another person)
- Files accessed: Research data, patent applications, formula documentation
- External drive connected to workstation at 23:52 PM


PAGE 6: WITNESS STATEMENTS SUMMARY
────────────────────────────────────────────────────────────────────────────────

Security Guard Martinez (Carlos Martinez):
- Observed Dr. Sarah Chen enter building at 11:47 PM (unusual timing)
- Reported Chen appeared nervous and carried large bag
- Heard glass breaking sound around midnight from 3rd floor
- Chen left hurriedly at 12:07 AM, claimed to retrieve "forgotten documents"

Lab Assistant Michael Torres:
- Worked in lab until 8:00 PM on January 14th
- Reports Dr. Kane mentioned having "evidence" of data theft
- Noted tension between Dr. Kane and Dr. Chen over budget and research
- Observed Professor Mitchell spending unusual late hours in the lab
- Kane accused someone of "accessing financial records without authorization"

Professor Emily Watson:
- Saw Professor Mitchell entering biochemistry lab at 10:30 PM
- Mitchell appeared startled when seen, carried gloves and cleaning supplies
- Unusual behavior: Mitchell does not typically work in biochemistry lab
- Also saw David Park accessing server room around 9:00 PM

Dr. Lisa Park (Discovery):
- Found Dr. Kane unconscious at 7:15 AM
- Noted chemical smell and broken glassware
- Secure cabinet open with missing contents
- Called 911 immediately


PAGE 7: EXPERT ANALYSIS
────────────────────────────────────────────────────────────────────────────────

Toxicology Report (Preliminary):
- Dr. Kane tested positive for benzodiazepine sedative
- Concentration suggests involuntary administration
- Substance found in ventilation system of lab

Medical Assessment:
- Dr. Kane suffered minor head trauma (consistent with fall while sedated)
- No signs of physical assault
- Expected full recovery

Digital Forensics:
- Dr. Kane's computer accessed while he was likely incapacitated
- Files copied to external drive between 11:52 PM and 11:58 PM
- Security camera footage shows someone at his desk during this time

Behavioral Analysis:
- Multiple suspects had motive (financial, professional, competitive)
- Evidence suggests premeditation (sedative, timing, file theft)
- Pattern indicates someone with inside knowledge of lab security and schedules


PAGE 8: PERSONS OF INTEREST
────────────────────────────────────────────────────────────────────────────────

Primary Suspects:

1. Dr. Sarah Chen
   Motive: Budget disputes, professional rivalry, denied funding
   Opportunity: Present at crime scene during incident timeframe
   Evidence: Late-night access, witnessed by security, left hastily
   Financial Activity: Excessive access to budget records and financial data
   Means: Has security clearance and lab knowledge

2. Professor James Mitchell
   Motive: Research access, potential competitive advantage
   Opportunity: In building earlier evening, unauthorized lab access
   Evidence: Conducting unauthorized experiments, suspicious behavior
   Means: Chemistry knowledge, access to sedatives

3. David Park
   Motive: Unknown, possible bribery or coercion
   Opportunity: In building for "maintenance," accessed server logs
   Evidence: Viewed security logs and financial access records
   Access: Ability to manipulate digital evidence
   Means: System administrator with high-level access

Areas for Further Investigation:
- Detailed analysis of Dr. Chen's financial records access patterns
- Professor Mitchell's unauthorized experimental activities
- David Park's unusual interest in security and financial logs
- Connection between suspects (possible collaboration)
- External parties who might benefit from stolen research

═══════════════════════════════════════════════════════════════════════════════
                                END OF DOSSIER
═══════════════════════════════════════════════════════════════════════════════
"""
        self._write_dossier(dossier_content)

    def _generate_scenario_b(self):
        """Generate Scenario B: The Sabotaged Prototype."""
        dossier_content = """
═══════════════════════════════════════════════════════════════════════════════
                        CONFIDENTIAL INVESTIGATION DOSSIER
                           Case #2026-0310-ROBOTICS-02
                        Corporate Sabotage - Apex Prototype
═══════════════════════════════════════════════════════════════════════════════

PAGE 1: INCIDENT REPORT
────────────────────────────────────────────────────────────────────────────────

Date: March 10, 2026
Location: Secure Robotics Lab 4, TechWing
Incident: Destruction of 'Apex' Humanoid Robot Prototype
Discovery: 7:00 AM by CEO Marcus Thorne

Summary:
The Apex prototype, valued at $12M, was found destroyed. The central processing
unit was smashed, and servo motors were manually ripped out.
There are no signs of forced entry at the main door.
Access logs show entry by authorized personnel only.

Suspects:
1. Elena Rostova (Lead Engineer)
2. Kevin Miller (Intern)
3. Victor Krum (Senior Developer, recently hired from competitor)


PAGE 2: PERSONNEL PROFILES
────────────────────────────────────────────────────────────────────────────────

Elena Rostova
- Role: Lead Engineer
- History: Project lead for 2 years. Very passionate.
- Notes: Recently expressed extreme frustration with deadlines.
- Access: Full Lab Access.

Kevin Miller
- Role: Engineering Intern
- History: 6 months internship.
- Notes: Caught running unauthorized AI simulations on the main server. 
  He was using the supercomputer to mine crypto-currency and train a personal 
  chatbot. He has been reprimanded twice for unauthorized experiments.
- Access: Basic Lab Access.

Victor Krum
- Role: Senior Developer
- History: Hired 2 weeks ago from 'CyberDynamics' (Main Competitor).
- Notes: Financial background check reveals suspicious large deposits.
- Access: Full Lab Access.


PAGE 3: SYSTEM LOGS & FINANCIALS
────────────────────────────────────────────────────────────────────────────────

System Log Access Analysis:
- Victor Krum: Accessed the main security server logs at 9:15 PM and 10:00 PM.
  He deleted 10 minutes of camera footage.
- Kevin Miller: Accessed the simulation server logs to hide his crypto-mining tracks.

Financial Record Analysis:
- Victor Krum: Accessed the company payroll and financial records to verify his own
  bonus structure.
- Suspicious Activity: Victor Krum received a wire transfer of $500,000 from
  'CD Holdings' (Shell company of CyberDynamics) on March 9th.


PAGE 4: FORENSIC DETAILS
────────────────────────────────────────────────────────────────────────────────

Fingerprints:
- Found on the smashed CPU: Victor Krum (partial thumbprint).
- Found on the door handle: Elena, Kevin, Victor (expected).

Tool Marks:
- The crowbar used to smash the prototype belongs to the janitorial closet.
- Traces of 'Red Wool' fibers found on the crowbar handle.

Security Anomalies:
- 9:30 PM: Victor Krum enters lab.
- 9:45 PM: Loud noise detected (Glass Break Sensor).
- 9:46 PM: Victor Krum exits lab.
- 10:00 PM: Logs accessed and footage deleted by Victor Krum.
- Intern Kevin Miller's unauthorized experiments were running on background servers
  during the incident, causing high CPU usage but no physical damage.

═══════════════════════════════════════════════════════════════════════════════
                                END OF DOSSIER
═══════════════════════════════════════════════════════════════════════════════
"""
        self._write_dossier(dossier_content)

    def _write_dossier(self, content):
        """Write content to dossier file."""
        dossier_path = os.path.join(self.output_dir, "investigation_dossier.txt")
        with open(dossier_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Generated investigation dossier: {dossier_path}")
        print(f"  Length: {len(content)} characters")



def main():
    """Main function to generate dummy dossier."""
    print("\nGenerating Stage 2 Investigation Dossier...")
    print("="*80 + "\n")
    
    generator = DossierGenerator()
    generator.generate_investigation_dossier()
    
    print("\n✓ Dossier generated successfully!")


if __name__ == "__main__":
    main()
