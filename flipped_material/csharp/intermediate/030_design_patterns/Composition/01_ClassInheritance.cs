using System;
using System.Collections.Generic;

namespace Composition {
    public enum CombatantTypes {
        Knight,
        Serf,
        Assassin
    }
    public abstract class Combatant {
        public string Name { get; set; }
        public int Damage {get; set; }
        
        public int Health { get; set; }

        public int Armour { get; set; }

        public CombatantTypes Class {get; set; } 

        public Combatant(string name) {
            Name = name;
            Damage = 1;
            Health = 5;
        }

        public abstract int Attack();
        public abstract int ReceiveDamage(int damage);
    }

    public class Knight : Combatant {

        public Knight(string name) : base(name) {}
        public override int Attack() {
            return Damage * 2;
        }

        public override int ReceiveDamage(int damage) {
            damage = damage / 2;
            Health -= damage;
            return damage;
        }
    }

    public class Assassin : Combatant {
        public Assassin(string name) : base(name) {}

        public override int Attack() {
            var random = new Random();
            var chance = random.Next(2);
            if (chance >= 1) return 10;
            return Damage;
        }

        public override int ReceiveDamage(int damage) {
            Health -= damage;
            return damage;
        }
    }

    public class Serf : Combatant {
        public Serf(string name) : base(name) { }

        public override int Attack() {
            return Damage/2;
        }

        public override int ReceiveDamage(int damage) {
            damage = damage * 2;
            Health -= damage;
            return damage;
        }
    }

    public class Gladiator : Combatant {
        public Gladiator(string name) : base(name) { }

        public override int Attack() {
            return Damage; 
        }

        public override int ReceiveDamage(int damage) {
            var random = new Random();
            var chance = random.Next(2);

            if (chance >=1) {
                return 0;
            }
            Health -= damage;
            return damage;
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
   

            return $"{f1.Name} a {f1.GetType().Name} attacks {f2.Name} a {f2.GetType().Name} for {dmg}. {f2.Name} ends up taking {damageTaken} damage and has {f2.Health} remaining";
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
            pit.AddFighter(new Knight("Ada"));
            pit.AddFighter(new Serf("Bob"));
            pit.AddFighter(new Assassin("Charles"));
            pit.AddFighter(new Gladiator("Eva"));
            pit.AddFighter(new Assassin("Georgia"));

            while (pit.StillFighting()) {
                Console.WriteLine();
                Console.WriteLine(pit.Fight());
                Console.WriteLine(pit.CleanUp());
                Console.WriteLine();
            }
            Console.WriteLine($"{pit.GetWinner().Name} the {pit.GetWinner().GetType().Name} is the winner!");
            
        }
    }
}
