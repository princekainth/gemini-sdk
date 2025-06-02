# examples/core_components_demo.py

# --- UPDATED IMPORT PATHS ---
from eidos.core.memetic_kernel import MemeticKernel, MemeUnit
from eidos.core.agent_spawner import Agent, AgentSpawner
from eidos.protocol.swarm_protocol import SwarmProtocol
from eidos.core.recursive_autonomy import RecursiveAutonomyEngine
from eidos.core.neurostack import Neurostack
from datetime import datetime

print("--- Starting Eidos SDK Test ---") # UPDATED BRANDING

# --- Test MemeUnit™ ---
print("\n--- Testing MemeUnit™ ---")
my_meme = MemeUnit("Initial idea for AGI alignment.")
print(f"Created MemeUnit™: {my_meme}")
my_meme.mutate()
print(f"Mutated MemeUnit™: {my_meme}")

another_meme = MemeUnit("A new thought about swarm intelligence.")
recombined_meme = my_meme.recombine(another_meme)
print(f"Recombined MemeUnit™: {recombined_meme}")


# --- Test MemeticKernel™ ---
print("\n--- Testing MemeticKernel™ ---")
kernel = MemeticKernel()
print(f"MemeticKernel™ initialized. Status: {kernel.get_status()}")

# Ingest some initial memes
meme1 = kernel.ingest("Foundational principles of ethical AI.")
meme2 = kernel.ingest("Optimized algorithm for agent communication.")
meme3 = kernel.ingest("Vision for decentralized AGI governance.")
meme4 = kernel.ingest("Historical data on past AI failures.", context={"source": "history"})

print(f"\nMemetic Kernel™ status after ingestion: {kernel.get_status()}")

# Run a few evolution steps
print("\n--- Running Evolution Steps ---")
for i in range(3):
    print(f"Evolution Step {i+1}:")
    kernel.evolve_step()
    print(f"Status after step {i+1}: {kernel.get_status()}")

# Retrieve high-fitness memes
print("\n--- Retrieving High-Fitness Memes ---")
top_memes = kernel.retrieve_memes(count=3)
if top_memes:
    print("Top 3 memes:")
    for meme in top_memes:
        print(f"- {meme}")
else:
    print("No memes to retrieve after evolution.")

# Test retrieval with a query
print("\n--- Retrieving Memes by Query ---")
query_results = kernel.retrieve_memes(query="ethical", count=5)
if query_results:
    print("Memes related to 'ethical':")
    for meme in query_results:
        print(f"- {meme}")
else:
    print("No memes found for query 'ethical'.")


print("\n--- Eidos SDK Test Complete ---") # UPDATED BRANDING


# --- Test Agent Spawner™ ---
print("\n--- Testing Agent Spawner™ ---")

# A simple mock to provide a kernel_id for Agent Spawner
class MockKernel:
    def get_status(self):
        return {"kernel_id": "mock-kernel-123"}

mock_kernel = MockKernel()

spawner = AgentSpawner(parent_kernel=mock_kernel)
print(f"AgentSpawner™ initialized. Spawned count: {spawner.get_spawned_count()}")

# Spawn some agents
agent1 = spawner.spawn_agent(name="Explorer Alpha", directives=["Explore quadrant 7"])
agent2 = spawner.spawn_agent(name="Builder Beta", directives=["Construct basic habitat"])
agent3 = spawner.spawn_agent(directives=["Monitor energy levels"]) # Default name

print(f"\nAgentSpawner™: Total agents spawned: {spawner.get_spawned_count()}")
print(f"Spawned Agents: {spawner.spawned_agents}")

# Orchestrate agents
print("\n--- Orchestrating Agents ---")
spawner.orchestrate_agents([agent1, agent2, agent3])

# Test individual agent execution
print("\n--- Testing Individual Agent Actions ---")
agent1.execute_directive("Analyze local resource data.")
agent2.update_status("building")
agent2.execute_directive("Request additional materials.")
agent3.execute_directive("Optimizing power grid.")

print("\n--- Agent Spawner™ Test Complete ---")


# --- Test Swarm Protocol™ ---
print("\n--- Testing Swarm Protocol™ ---")

# Create agents for the swarm test
swarm_agent1 = spawner.spawn_agent(name="ConsensusUnit-1", directives=["Participate in consensus"])
swarm_agent2 = spawner.spawn_agent(name="ConsensusUnit-2", directives=["Participate in consensus"])
swarm_agent3 = spawner.spawn_agent(name="ConsensusUnit-3", directives=["Participate in consensus"])
swarm_agent4 = spawner.spawn_agent(name="ConsensusUnit-4", directives=["Participate in consensus"])

# Manually set local beliefs for testing consensus
swarm_agent1.local_belief = "decision_alpha"
swarm_agent2.local_belief = "decision_alpha"
swarm_agent3.local_belief = "decision_beta" # Divergent belief
swarm_agent4.local_belief = "decision_alpha"

swarm = SwarmProtocol(swarm_id="main-governance-swarm", agents=[swarm_agent1, swarm_agent2, swarm_agent3, swarm_agent4])
print(f"Swarm Protocol™ initialized. Status: {swarm.get_swarm_status()}")

# Test Majority Vote Consensus
print("\n--- Testing Majority Vote Consensus ---")
agreed_value, consensus_reached = swarm.achieve_consensus(topic="Next Global Action", method="majority_vote")
print(f"Consensus Result: Value='{agreed_value}', Reached={consensus_reached}")
print(f"Swarm Protocol™ status after consensus attempt: {swarm.get_swarm_status()}")

# Test Unanimous Vote Consensus (should fail with current beliefs)
print("\n--- Testing Unanimous Vote Consensus ---")
agreed_value_unanimous, consensus_reached_unanimous = swarm.achieve_consensus(topic="Unanimous Directive", method="unanimous_vote")
print(f"Unanimous Consensus Result: Value='{agreed_value_unanimous}', Reached={consensus_reached_unanimous}")


# Synchronize agents with a new state
print("\n--- Synchronizing Agents ---")
new_global_state = {"timestamp": datetime.now().isoformat(), "status": "all_clear_alpha_protocol"}
swarm.synchronize_agents(new_global_state)
print(f"Agent beliefs after synchronization: {swarm_agent1.local_belief}, {swarm_agent2.local_belief}, {swarm_agent3.local_belief}, {swarm_agent4.local_belief}")

print("\n--- Swarm Protocol™ Test Complete ---")


# --- Test Recursive Autonomy™ ---
print("\n--- Testing Recursive Autonomy™ ---")

# We'll use agent1 spawned earlier for this test
# Ensure agent1 is available in this scope (it should be if you've been copy-pasting the full file)

# Initialize the RecursiveAutonomyEngine for agent1
recursive_engine = RecursiveAutonomyEngine(agent_id=agent1.id, memetic_kernel_ref=kernel) # Pass the main kernel

# Step 1: Agent self-evaluates
current_agent_state = {
    "performance": 0.85, # Simulate current performance
    "alignment": 0.92,   # Simulate current alignment
    "consistency": 0.98  # Simulate internal consistency
}
evaluation = recursive_engine.self_evaluate(current_agent_state)
print(f"Self-Evaluation Result for Agent {agent1.name}: {evaluation}")

# Step 2: Agent proposes self-modification
proposal = recursive_engine.propose_self_modification(evaluation)
print(f"Self-Modification Proposal: {proposal}")

# Step 3: Agent simulates timeline impact of the proposal
simulated_impact = recursive_engine.simulate_timeline_impact(proposal, simulation_horizon_years=5)
print(f"Simulated Timeline Impact: {simulated_impact}")

# Step 4: Agent decides whether to self-modify
if simulated_impact["predicted_alignment_stability"] > 0.9 and simulated_impact["risk_of_unforeseen_consequences"] < 0.05:
    print("\nConditions met: Proceeding with self-modification.")
    recursive_engine.self_modify(proposal)
    print(f"Agent {agent1.name}'s Evolution Log: {recursive_engine.get_evolution_log()}")
else:
    print("\nConditions not met: Deferring self-modification due to risk or low benefit.")

print("\n--- Recursive Autonomy™ Test Complete ---")


# --- Test Neurostack™ ---
print("\n--- Testing Neurostack™ ---")

# We'll use agent1 spawned earlier for this test
# Ensure agent1 is available in this scope (it should be if you've been copy-pasting the full file)

# Initialize the Neurostack™ for agent1
neurostack = Neurostack(agent_id=agent1.id, configuration={"type": "advanced_perceptual_stack", "layers": 5})

# Step 1: Simulate processing neural activity/input
print("\n--- Processing Neural Activity ---")
processed_output = neurostack.process_neural_activity("Raw sensory input: Visual pattern detected.")
print(f"Processed Output: {processed_output}")
print(f"Current Cognitive State (after input): {neurostack.get_current_cognitive_state()}")

# Step 2: Simulate a cognitive task
print("\n--- Simulating Cognition ---")
cognitive_result = neurostack.simulate_cognition("Evaluate threat level of pattern", complexity=0.7)
print(f"Cognitive Result: {cognitive_result}")

# Step 3: Simulate integrating multimodal sensory input
print("\n--- Integrating Sensory Input ---")
sensory_data = {
    "visual": "Red blinking light.",
    "auditory": "High-pitched hum.",
    "tactile": "Slight vibration."
}
integrated_representation = neurostack.integrate_sensory_input(sensory_data)
print(f"Integrated Sensory Representation: {integrated_representation}")

print("\n--- Neurostack™ Test Complete ---")
