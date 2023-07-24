public class jun21_Q6 {

    public class Base {
        public int bPublic;
        protected int bProtect;
        private int bPrivate;
        // public methods follow (omitted here)
    }

    public class Derived extends Base {
        public int dPublic;
        private int dPrivate;
        // public methods follow (omitted here)
    }

    public class Tester {
        private Base B = new Base();

        public static void main(String[] args) {
            Base b = new Base();
            Derived d = new Derived();
            System.out.println(
            B.bPublic + " " +
            b.bProtect + " " +
            // d.bPrivate + " " +
            d.dPublic + " " +
            // d.dPrivate + " " +
            d.bProtect
            );

            }
        }
}