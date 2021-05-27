package Activities;

	public class NotenoughFunds extends RuntimeException {

	    public NotenoughFunds(Integer amount, Integer balance) {
	        super("Attempted to withdraw " + amount + " with a balance of " + balance);
	    }

	}


