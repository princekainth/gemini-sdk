# gemini/protocol/swarm_protocol.py

from typing import List, Dict, Any, Tuple
import random
import time
from datetime import datetime

# --- IMPORTANT: We are now importing the real Agent class ---
from gemini.core.agent_spawner import Agent # Make sure this import is correct

# --- Removed: The mock Agent class was here, it's now removed ---
# You should no longer see 'class Agent:' defined in this file.


class SwarmProtocol:
    """
    The Swarm Protocol™ for the Gemini Protocol™.
    Manages coordination, consensus, and synchronization among a group of agents.
    This is your protocol-level crown jewel for decentralized AGI governance.
    """
    def __init__(self, swarm_id: str, agents: List[Agent]):
        self.swarm_id = swarm_id
        self.agents = agents
        self.consensus_history = []
        print(f"SwarmProtocol™ initialized for Swarm ID: {self.swarm_id} with {len(self.agents)} agents.")

    def broadcast_message(self, sender_id: str, message_type: str, payload: Any):
        """
        Broadcasts a message from a sender to all agents in the swarm.
        """
        message = {
            "sender_id": sender_id,
            "type": message_type,
            "payload": payload,
            "timestamp": datetime.now().isoformat()
        }
        print(f"SwarmProtocol™: Agent {sender_id[:4]} broadcasting '{message_type}'...")
        for agent in self.agents:
            if agent.id != sender_id: # Agent doesn't send message to itself
                agent.receive_message(message)

    def achieve_consensus(self, topic: str, method: str = "majority_vote") -> Tuple[Any, bool]:
        """
        Attempts to achieve consensus among swarm agents on a given topic.
        This embodies the decentralized AI governance aspect of Swarm Protocol™.
        """
        print(f"SwarmProtocol™: Achieving consensus on '{topic}' using '{method}'...")
        if not self.agents:
            return None, False

        # Ensure agents have a local_belief attribute for consensus.
        # In a real system, this would come from their Memetic Kernel™ or current state.
        beliefs = [agent.local_belief for agent in self.agents if agent.local_belief is not None]

        if not beliefs:
            print("SwarmProtocol™: No beliefs expressed for consensus.")
            return None, False

        consensus_reached = False
        agreed_value = None

        if method == "majority_vote":
            from collections import Counter
            # Count occurrences of each belief
            belief_counts = Counter(beliefs)
            # Find the most common belief
            most_common_belief, count = belief_counts.most_common(1)[0]
            
            # Simple majority (more than 50%)
            if count > len(self.agents) / 2:
                consensus_reached = True
                agreed_value = most_common_belief

        elif method == "unanimous_vote":
            if all(b == beliefs[0] for b in beliefs):
                consensus_reached = True
                agreed_value = beliefs[0]
            
        # Record consensus attempt
        self.consensus_history.append({
            "topic": topic,
            "method": method,
            "beliefs": beliefs,
            "agreed_value": agreed_value,
            "consensus_reached": consensus_reached,
            "timestamp": datetime.now().isoformat()
        })

        if consensus_reached:
            print(f"SwarmProtocol™: Consensus reached on '{topic}': {agreed_value}")
            # Update all agents' beliefs to the consensus (synchronization)
            for agent in self.agents:
                agent.update_belief(agreed_value)
        else:
            print(f"SwarmProtocol™: No consensus reached on '{topic}'.")

        return agreed_value, consensus_reached

    def synchronize_agents(self, data: Any):
        """
        Synchronizes agents with common data or state.
        This is a synchronization mechanism within the Swarm Protocol™.
        """
        print(f"SwarmProtocol™: Synchronizing agents with data: {str(data)[:50]}...")
        for agent in self.agents:
            agent.update_belief(data) # Simple update to simulate synchronization
        print("SwarmProtocol™: Agents synchronized.")

    def get_swarm_status(self):
        """Returns the current status of the swarm."""
        return {
            "swarm_id": self.swarm_id,
            "num_agents": len(self.agents),
            "consensus_records": len(self.consensus_history)
        }
