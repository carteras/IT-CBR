using System;
using System.Collections.Generic;
namespace Test {

    abstract class Message {
        public string Payload { get; set; }
        public string Address { get; set; }
        public string Sender { get; set; }

        public Message(string address, string payload) {
            Payload = payload;
            Address = address;
        }

        public abstract string SendMessage();
    }

    class SMS : Message {

        public SMS(string phoneNumber, string payload) : base(phoneNumber, payload){
            Sender = "Foo SMS Service!";
        }

        public override string SendMessage() {
            return $"{{\"phoneTo\" : {Address}, \"packet\" :{Payload} , \"senderPhone\" : {Sender}}}";
        }
    }

    class Email : Message {
        public Email(string address, string payload) : base(address, payload) {
            Sender = "admin@acme.com";
        }

        public override string SendMessage() {
            return $"{{ 'sender':{Sender}, 'receiver':{Address} 'msg':{Payload}   }}";
        }
    }

    class MsgEvent {
        public Message Msg { get; set; }

        public void ChangeMessage(Message m) {
            Msg = m;
        }
        public string SendMessage() {
            return Msg.SendMessage();
        }
    }

    class Program {
        static void Main(string[] args) {

            MsgEvent msgevt = new MsgEvent();
            msgevt.ChangeMessage(new SMS("12345678", "fjoifwejioewf"));
            Console.WriteLine(msgevt.SendMessage());
            msgevt.ChangeMessage(new Email("admin@google.com", "fo fo fo fo fo fo fo fo "));
            Console.WriteLine(msgevt.SendMessage());



        }
    }
}
