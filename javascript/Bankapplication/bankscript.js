class Bank{
        static accountDetails(){
            let userData={
                1000:{accno:1000,password:"userone",balance:5000},
                1001:{accno:1001,password:"usertwo",balance:5000},
                1002:{accno:1002,password:"userthree",balance:5000},
                1003:{accno:1003,password:"userfour",balance:5000},
            }
            return userData
        }
        static authenticate(accno,password){
            var dataset=Bank.accountDetails()
            if (accno in dataset){
                    if (password==dataset[accno]["password"]){
                        return 1
            }
            else{
                    return 0
            }
        }
        else{
            return -1
        }
    }
        static login(){
            var accno=document.querySelector("#acno").value
            var password=document.querySelector("#pwd").value
            let user=Bank.authenticate(accno,password)
            if(user==0){
                alert("invalid password")
            }
            else if(user==1){
                alert("success")
                window.location.href="home.html"
            }
            else if(user==-1){
                alert("invalid account number")
            }
        }
        static withdraw(accno,amnt){
            let details=Bank.accountDetails()
            var amount=document.querySelector("#amnt")
            var accno=document.querySelector("#accno").value
            var password=document.querySelector("#pwd").value
            let user=Bank.authenticate(accno,password)
            if(user==0){
                alert("invalid success")
            }
            else if(user==1){
                if(amount>details[accno]["balance"])
                {
                    alert("insufficient balance")
                }
                else{
                    alert("Amount Successfully Debited")
                }
            }
            else if(user==-1){
                alert("invalid account number")
            }
        }
        static deposit(){
            var amount=document.querySelector("#amnt")
            var accno=document.querySelector("#accno").value
            var password=document.querySelector("#pwd").value
            let user=Bank.authenticate(accno,password)
            if(user==0){
                alert("invalid password")
            }
            else if(user==1){
                alert("successfully Deposited")
            }
            else if(user==-1){
                alert("invalid account number")
            }
        }
        
        }
