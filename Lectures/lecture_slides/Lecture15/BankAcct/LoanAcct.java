//Subclass
class LoanAcct extends BankAcct
{
	protected double _rate;
	protected double _limit;

	public LoanAcct(int aNum, double bal, double rate, double limit) {
		super(aNum, bal);
		_rate = rate;
		_limit = limit;
	}

	//New method in subclass
	public void payInterest() {
        double interest = this._balance * this._rate;
        this._balance += interest;
	}

	//Method Overriding
	public boolean withdraw( double amount ) {
		if ((this._balance - amount) < this._limit)
		    return false;
		this._balance -= amount;
		return true;
	}

	public void deposit( double amount ) {
		if (amount <= 0 || (amount + this._balance) > 0)
		    return;
		this._balance += amount;
	}


    public static boolean transfer (BankAcct fromAcct, BankAcct toAcct, double amount) {
        if (fromAcct.withdraw(amount)) {
            toAcct.deposit(amount);
            return true;
        }
        return false;
    }
}