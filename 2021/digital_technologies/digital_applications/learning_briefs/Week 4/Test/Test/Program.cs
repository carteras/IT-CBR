using System;
using System.Collections.Generic;
namespace Test {

    public abstract class Door {

        public char ASCII { get; set; }

        public abstract void Open();

        public virtual char Draw() {
            return ASCII;
        }
    }

    public class ClosedState : Door {
        public override void Open() {
            ASCII = '+';
        }

    }
    public class OpenedState : Door {
        public override void Open() {
            ASCII = '=';
        }
    }

    public class LockedState : Door {
        public override void Open() {
            ASCII = '±';
        }
    }

    public class SchoolDoor : Door {
        public Door D {get; set;}

        public SchoolDoor() {
            D = new OpenedState();
        }

        public override void Open() {
             D.Open();
        }

        public override char Draw() {
            return D.Draw();
        }

    }
    public class Program { 
        static void Main(string[] args) {
            SchoolDoor A308 = new SchoolDoor();
            Console.WriteLine(A308.Draw());
            A308.D = new ClosedState();
            Console.WriteLine(A308.Draw());
            A308.D = new LockedState();
            Console.WriteLine(A308.Draw());
        }
    }
}
