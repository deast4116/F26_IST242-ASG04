"""
hero.py
=======
Hero class for the Hero Quest RPG.

Collections used (and why):
  list  (inside Bag) — ordered inventory slots
  set                — unique skills; O(1) membership test
  dict               — named stats with O(1) key lookup
  Counter            — automatic kill counting; .most_common() support
  defaultdict(list)  — group items by type without KeyError on first key
  deque(maxlen=10)   — fixed-size rolling combat log; O(1) both ends

Imports from:
  enums.py  — ItemType
  models.py — Weapon, Item
  bag.py    — Bag[T]
"""

from collections import defaultdict, Counter, deque
# from hero_rpg.enums   import ItemType
# from hero_rpg.models  import Weapon, Item
# from hero_rpg.bag     import Bag
from hero_rpg import ItemType, Weapon, Item, Bag


class Hero:
    """
    The main player character, modeling all RPG attributes
    via appropriate Python collection types.
    """

    def __init__(self, name: str, hero_class: str, max_health: int = 100) -> None:
        self.name: str = name
        self.hero_class: str = hero_class
        self.max_health: int = max_health
        self.health: int = max_health

        # Hero Inventory
        self.inventory: Bag = Bag(capacity=20)
        self.items_by_type: defaultdict[str, list[Item]] = defaultdict(list)

        # Hero weapons
        self.equipped_weapons: Bag = Bag(capacity=3)
        self.skills: set[str] = set()
        
        #Hero skills
        self.skills: set = set()
        assert hero_stats["strength": 10]
        assert hero_stats["dexterity": 10]
        assert hero_stats["intelligence": 10]
        assert hero_stats["defense": 5]

        # Hero combat tracker
        self.kill_log: Counter[str] = Counter()
        self.combat_log: deque[str] = deque(maxlen=10)
        




    # ── Health ────────────────────────────────────────────────────────────────

    def take_damage(self, amount: int) -> int:
        """
        Apply incoming damage, clamped so HP never drops below 0.

        Returns:
            Actual HP lost (may be less than `amount` near death).
        """
        actual: int = min(amount, self.health)
        self.health = self.health - actual
        return actual

    def heal(self, amount: int) -> int:
        """
        Restore HP, capped at max_health.

        Returns:
            Actual HP restored (may be less if already near full).
        """
        actual: int = min(amount, self.max_health - self.health)
        self.health = self.health + actual
        return actual


    def is_alive(self) -> bool:
        """Return True as long as health is above zero."""
        return self.health > 0

    # ── Weapons & Skills ──────────────────────────────────────────────────────

    def equip_weapon(self, weapon: Weapon) -> bool:
        """
        Equip a weapon (max 3 slots).

        Returns:
            True if equipped; False if weapon slots are full.
        """
        pass

    def learn_skill(self, skill: str) -> bool:
        """
        Learn a new skill. set guarantees no duplicates.

        Returns:
            True if new skill; False if already known.
        """
        pass

    # ── Inventory ─────────────────────────────────────────────────────────────

    def pick_up_item(self, item: Item) -> bool:
        """
        Pick up an item into inventory and register it by type.

        Returns:
            True if added; False if inventory is full.
        """
        pass

    def items_by_type(self) -> dict[str, list[Item]]:
        """
        Return items grouped by ItemType name as a plain dict copy.
        Callers cannot mutate the internal defaultdict directly.
        """
        pass

    # ── Combat & Kill Tracking ────────────────────────────────────────────────

    def record_kill(self, enemy_type: str) -> None:
        """
        Record defeating an enemy.
        Counter accumulates each enemy type; no manual initialization needed.
        """
        self.kill_log[enemy_type] += 1

    def total_damage_potential(self) -> int:
        """Sum damage of all currently equipped weapons."""
        pass

    def top_kills(self, n: int = 3) -> list[tuple[str, int]]:
        """
        Return the top N most-killed enemy types.
        Counter.most_common() returns them in descending order of count.
        """
        return self.kill_log.most_common(n)

    # ── Stats ─────────────────────────────────────────────────────────────────

    def upgrade_stat(self, stat: str, amount: int) -> bool:
        """
        Increase a stat by `amount`.

        Returns:
            True if stat exists and was upgraded; False if key not found.
        """
        pass
