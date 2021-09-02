using System;

namespace DecoratorPattern {

    public interface Infantry {
        public int _Damage { get; set; }
        public int _Armour { get; set; }

        public int _Health { get; set; }

        public void ReceiveDamage(int damage);

        public int ShootDamage();
    }

    public class Soldier : Infantry {
        public virtual int _Damage { get; set; }
        public virtual int _Armour { get; set; }

        public virtual int _Health { get; set; }

        public void ReceiveDamage(int damage) {
            _Health -= damage;
        }

        public int ShootDamage() {
            return _Damage;
        }

        public Soldier() {
            _Damage = 6;
            _Armour = 1;
            _Health = 10;
        }
    }

    public abstract class InfantryDecorator : Infantry {
        public int _Damage {
            get => _Infantry._Damage;
            set { }
        }
        public int _Armour {
            get => _Infantry._Armour;
            set { }
        }

        public Infantry _Infantry { get; set; }
        public int _Health { get => _Infantry._Health; set => _Infantry._Health = value; }

        public InfantryDecorator(Infantry infantry) {
            this._Infantry = infantry;
        }

        public virtual void ReceiveDamage(int damage) {
            _Infantry.ReceiveDamage(damage);
        }

        public int ShootDamage() {
            return _Infantry.ShootDamage();
        }
    }

    public class WeaponUpgrade : InfantryDecorator {
        public WeaponUpgrade(Infantry infantry) : base(infantry) {}
    }

    public class ShieldUpgrade : InfantryDecorator {
        public ShieldUpgrade(Infantry infantry) : base(infantry) {}
        public override void ReceiveDamage(int damage) => _Infantry.ReceiveDamage(damage / 2);
    }

    class Program {
        static void Main(string[] args) {
            Infantry soldier = new Soldier();
            Console.WriteLine($"1 {soldier._Damage} {soldier._Armour} {soldier._Health}");
            soldier.ReceiveDamage(2);
            Console.WriteLine(soldier.ShootDamage());
            Console.WriteLine($"2 {soldier._Damage} {soldier._Armour} {soldier._Health}");
            soldier = new ShieldUpgrade(soldier);
            soldier.ReceiveDamage(2);
            Console.WriteLine($"3 {soldier._Damage} {soldier._Armour} {soldier._Health}");
        }
    }
}
