
from bankpackage import BankInfo as BNK


acct2 = BNK.Account(3000, "Ali")
acct2.Deposit(500)
acct2.Withdrawal(250)
print(acct2)