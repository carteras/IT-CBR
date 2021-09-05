using System;
using System.Collections.Generic;

namespace Composition {
    public enum CombatantTypes {
        Knight,
        Serf,
        Assassin
    }
    public class Combatant {
        public string Name { get; set; }
        public int Damage {get; set; }
        
        public int Health { get; set; }

        public int Armour { get; set; }

        public CombatantTypes Class {get; set; } 

        public Combatant(string name, CombatantTypes fighterClass) {
            Name = name;
            Damage = 2;
            Health = 5;
            Class = fighterClass;
        }


        public int  Attack() {
            if (Class == CombatantTypes.Knight) {
                return Damage * 2;
            } else if (Class == CombatantTypes.Serf) {
                return Damage / 2;
            } else if (Class == CombatantTypes.Assassin) {
                var random = new Random();
                var chance = random.Next(2);
                if (chance >= 1) return 10;
                return Damage * 1;
            } else {
                return 1;
            }

        }

        public int ReceiveDamage(int damage) {
            int finalDamage = damage;
            if (Class == CombatantTypes.Knight) {
                finalDamage = damage / 2;
            } else if (Class == CombatantTypes.Serf) {
                finalDamage = damage * 2;
            } else if (Class == CombatantTypes.Assassin) {
                finalDamage = damage;
            } 
            Health -= finalDamage;
            return finalDamage;
        }
    }

    public class FightPit {
        List<Combatant> fighters;

        public FightPit() {
            fighters = new List<Combatant>();
        }

        public void AddFighter(Combatant f) {
            fighters.Add(f);
        }

        public Boolean StillFighting() {
            if (fighters.Count > 1) {
                return true;
            }
            return false;
        }

        public string Fight() {
            var random = new Random();
            
            Combatant f1 = fighters[random.Next(fighters.Count)];
            Combatant f2 = fighters[random.Next(fighters.Count)];

            if (f1 == f2) {
                return $"{f1.Name} couldn't find anybody to fight!";
            }

            int dmg = f1.Attack();
            int damageTaken = f2.ReceiveDamage(dmg);
   

            return $"{f1.Name} a {f1.Class} attacks {f2.Name} a {f2.Class} for {dmg}. {f2.Name} ends up taking {damageTaken} damage and has {f2.Health} remaining";
        }

        public string CleanUp() {
            List<string> output = new List<String>();
            List<Combatant> remaining = new List<Combatant>();
            foreach (Combatant f in fighters) {
                if (f.Health > 0) {
                    remaining.Add(f);
                } else {
                    output.Add(f.Name);
                }
            }
            fighters = remaining;
            if (output.Count > 1) return $"{string.Join(",", output.ToArray())} are dead and are removed from the pit.";
            if (output.Count == 1) return $"{string.Join(",", output.ToArray())} is dead and is removed from the pit.";
            return "Nobody died this round!";

        }

        public Combatant GetWinner() {
            return fighters[0];
        }
    }

    public class Program {

        public static void Main(string[] args) {
            FightPit pit = new FightPit();
            pit.AddFighter(new Combatant("Ada", CombatantTypes.Knight));
            pit.AddFighter(new Combatant("Bob", CombatantTypes.Serf));
            pit.AddFighter(new Combatant("Charles", CombatantTypes.Assassin));
            pit.AddFighter(new Combatant("Eva", CombatantTypes.Serf));
            pit.AddFighter(new Combatant("Fred", CombatantTypes.Assassin));
            pit.AddFighter(new Combatant("Georgia", CombatantTypes.Serf));

            while (pit.StillFighting()) {
                Console.WriteLine();
                Console.WriteLine(pit.Fight());
                Console.WriteLine(pit.CleanUp());
                Console.WriteLine();
            }
            Console.WriteLine($"{pit.GetWinner().Name} the {pit.GetWinner().Class} is the winner!");
            
        }
    }
}
