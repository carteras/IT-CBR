using System;
using System.Collections.Generic;

namespace Composition {

    public abstract class Weapon {
        public int Damage { get; set; }
        public abstract int Attack();
    }

    public abstract class Armour {
        public int ArmourClass { get; set; }
        public abstract int ReceiveDamage(int damage);
    }


    public class Combatant {
        public string Name { get; set; }
        public int Health { get; set; }
        public Weapon Weapon { get; set; }
        public Armour Armour { get; set; }

        public Combatant(string name, Weapon weapon, Armour armour) {
            Name = name;
            Health = 5;
            Weapon = weapon;
            Armour = armour;
        }

        public int Attack() {
            return Weapon.Attack();
        }

        public int ReceiveDamage(int damage) {
            int damageReceived = Armour.ReceiveDamage(damage);
            Health -= damageReceived;
            return damageReceived;
        }

        public int GetHealth() {
            return Health;
        }
    }


    public class Sword : Weapon {

        public Sword() {
            Damage = 2;
        }
        public override int Attack() {
            return Damage;
        }
    }

    public class PoleAxe : Weapon {

        public PoleAxe() {
            Damage = 5;
        }

        public override int Attack() {
            return Damage;
        }

    }

    public class Dagger : Weapon {
        public Dagger() {
            Damage = 1;
        }

        public override int Attack() {
            var random = new Random();
            var chance = random.Next(2);
            if (chance >= 1) {
                return Damage * 10;
            }
            return Damage;
        }
    }

    public class ChainMail : Armour {

        public ChainMail() {
            ArmourClass = 2;
        }
        public override int ReceiveDamage(int damage) {
            int finalDamage = damage / ArmourClass;
            return finalDamage;
        }
    }

    public class Gladiator : Armour {
        public Gladiator() {
            ArmourClass = 1;
        }

        public override int ReceiveDamage(int damage) {
            var random = new Random();
            var chance = random.Next(2);
            int finalDamage = damage;
            if (chance >= 1) {
                finalDamage = finalDamage / 3;
            }
            return finalDamage;
        }
    }

    public class Gamberson : Armour {
        
        public override int ReceiveDamage(int damage) {
            return damage;
        }
    }

    public class Clothing : Armour {
        public override int ReceiveDamage(int damage) {
            return damage * 2;
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


            return $"{f1.Name} a {f1.GetType().Name} attacks {f2.Name} a {f2.GetType().Name} for {dmg}. {f2.Name} ends up taking {damageTaken} damage and has {f2.GetHealth()} remaining";
        }

        public string CleanUp() {
            List<string> output = new List<String>();
            List<Combatant> remaining = new List<Combatant>();
            foreach (Combatant f in fighters) {
                if (f.GetHealth() > 0) {
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
            pit.AddFighter(new Combatant("Ada", new Sword(), new ChainMail()));
            pit.AddFighter(new Combatant("Bob", new PoleAxe(), new Gladiator()));
            pit.AddFighter(new Combatant("Charles", new Dagger(), new Gamberson()));
            pit.AddFighter(new Combatant("Eva", new Dagger(), new Clothing()));
            pit.AddFighter(new Combatant("Georgia", new Sword(), new Gamberson()));

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
