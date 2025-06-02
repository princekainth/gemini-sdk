# eidos/core/memetic_kernel.py

import random
from datetime import datetime
from typing import Any, Dict, List, Tuple
import uuid # <--- ADD THIS LINE HERE

class MemeUnit:
    """
    Represents a fundamental unit of information within the Memetic Kernel™.
    This is a core concept of the Eidos Protocol™.
    """
    def __init__(self, content: Any, context: Dict[str, Any] = None, initial_fitness: float = 0.0):
        self.content = content
        self.context = context if context is not None else {}
        self.fitness = initial_fitness
        self.propagation_bias = 1.0 # Default tendency to spread
        self.lineage = [] # To track its origin and evolution (parent memes, mutations)
        self.associated_behaviors = [] # Pointers to actions or functions it influences
        self.creation_time = datetime.now() # Added for potential 'age' based selection

    def __repr__(self):
        content_str = str(self.content)
        return f"MemeUnit(content='{content_str[:20]}...', fitness={self.fitness:.2f})"

    def mutate(self):
        """Applies a basic, placeholder mutation to the MemeUnit™."""
        # In a real system, this would be more complex (e.g., semantic mutation, data alteration)
        self.content = str(self.content) + "_mutated"
        self.fitness *= 0.9 # Simple fitness decay upon mutation for this example
        self.lineage.append(f"mutated_at_step_{len(self.lineage)}")
        print(f"MemeUnit™ mutated: {self.content}")

    def recombine(self, other_meme: 'MemeUnit') -> 'MemeUnit':
        """Applies a basic, placeholder recombination with another MemeUnit™."""
        # In a real system, this would combine content or rules meaningfully
        new_content = f"({self.content} & {other_meme.content})"
        new_fitness = (self.fitness + other_meme.fitness) / 2
        new_meme = MemeUnit(new_content, initial_fitness=new_fitness)
        new_meme.lineage.extend([
            f"recombined_from_{self.lineage[-1] if self.lineage else self.content}",
            f"recombined_from_{other_meme.lineage[-1] if other_meme.lineage else other_meme.content}"
        ])
        print(f"MemeUnit™ recombined: {new_meme.content}")
        return new_meme


class MemeticKernel:
    """
    The cognitive memory engine (Memetic Kernel™) for intelligent agents.
    It manages the ingestion, evolution, selection, and retrieval of Memetic Units™.
    This is a core component of the Eidos Protocol™.
    """
    def __init__(self):
        self.meme_pool: List[MemeUnit] = [] # Stores all MemeUnit™ instances
        self.history: List[str] = [] # For auditing or long-term analysis of meme evolution
        self.kernel_id = str(uuid.uuid4()) # Added for agent_spawner reference

    def ingest(self, data: Any, context: Dict[str, Any] = None, initial_fitness: float = 0.1) -> MemeUnit:
        """Ingest raw data or information to form new Memetic Units™."""
        new_meme = MemeUnit(content=data, context=context, initial_fitness=initial_fitness)
        self.meme_pool.append(new_meme)
        self.history.append(f"Ingested: {new_meme.content[:50]}")
        print(f"Memetic Kernel™ ingested new MemeUnit™: {new_meme}")
        return new_meme

    def evolve_step(self):
        """
        Performs a single step of memetic evolution within the kernel.
        This is where mutation, recombination, and selection occur.
        """
        print("Memetic Kernel™ is evolving...")
        new_memes_from_evolution: List[MemeUnit] = []

        # Apply mutation to existing memes
        for meme in list(self.meme_pool): # Iterate over a copy to allow modification
            if self.should_mutate(meme): # Placeholder for mutation probability
                meme.mutate()
                # A mutated meme could be considered 'new' or replace original, depending on design
                # For this example, we just modify in place

        # Apply recombination
        if len(self.meme_pool) >= 2:
            m1, m2 = random.sample(self.meme_pool, 2)
            if self.should_recombine(m1, m2): # Placeholder for recombination probability/conditions
                new_memes_from_evolution.append(m1.recombine(m2))

        # Add newly generated memes from evolution to the pool
        self.meme_pool.extend(new_memes_from_evolution)

        # Apply selection/pruning based on fitness
        self.apply_selection()

        self.history.append(f"Evolved step, memes in pool: {len(self.meme_pool)}")
        print(f"Memetic Kernel™ evolution step complete. Current meme pool size: {len(self.meme_pool)}")

    def apply_selection(self):
        """
        Selects memes based on their fitness, potentially pruning low-fitness memes.
        This embodies the 'natural selection' aspect of the Memetic Kernel™.
        """
        # Example: Remove memes below a certain fitness threshold or prune oldest low-fitness memes
        initial_count = len(self.meme_pool)
        self.meme_pool = [meme for meme in self.meme_pool if meme.fitness > 0.05] # Keep memes above threshold
        if len(self.meme_pool) < initial_count:
            print(f"Memetic Kernel™ pruned {initial_count - len(self.meme_pool)} low-fitness memes.")
        
        # Simple fitness decay for all active memes over time
        for meme in self.meme_pool:
            meme.fitness *= 0.95 # Gradual decay

    def retrieve_memes(self, query: Any = None, count: int = 1, sort_by: str = 'fitness') -> List[MemeUnit]:
        """
        Retrieve memes from the pool based on query, fitness, or other criteria.
        """
        if not self.meme_pool:
            return []

        results = list(self.meme_pool)

        if query:
            # Placeholder for semantic search or pattern matching
            results = [meme for meme in results if query.lower() in str(meme.content).lower()]

        if sort_by == 'fitness':
            results = sorted(results, key=lambda m: m.fitness, reverse=True)
        elif sort_by == 'age': # Example for potential future use
            # Would need a timestamp on MemeUnit
            results = sorted(results, key=lambda m: m.creation_time)

        return results[:count]

    def get_status(self) -> Dict[str, Any]:
        """Get current status of the Memetic Kernel™."""
        return {
            "kernel_id": self.kernel_id, # Added kernel_id here for agent_spawner reference
            "total_memes": len(self.meme_pool),
            "avg_fitness": sum(m.fitness for m in self.meme_pool) / len(self.meme_pool) if self.meme_pool else 0,
            "history_length": len(self.history)
        }

    # Placeholder for internal decision heuristics
    def should_mutate(self, meme: MemeUnit) -> bool:
        # Example: Higher probability if meme is old or below certain fitness
        return random.random() < 0.2

    def should_recombine(self, meme1: MemeUnit, meme2: MemeUnit) -> bool:
        # Example: Higher probability if memes are semantically related or from different lineages
        return random.random() < 0.1
