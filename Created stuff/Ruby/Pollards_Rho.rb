# This method does not display the process of GCD calculation

# Calculate Great Common Divisor (GCD) using 
# Euclidean algorithm.

def GCD(a, b)
    
    a, b = a.abs, b.abs

    # Always b => a
    if (a < b)
        a, b = b, a
    end
    while not (a == 0 or b == 0)
        a, b = b, a % b
    end

    if a == 0
        return b
    elsif b == 0
        return a
    end
    
end

# Check if a given number is a prime.
def is_prime(num) # [1]
    div = 5
    increment = 2
    if(num == 1 || num == 0)
        return false
    elsif(num == 2)
        return true
    elsif(num == 3)
        return true
    end
    
    if(num % 2 == 0)
        return false
    elsif(num % 3 == 0)
        return false
    end
    
    sqrt_num = (Math.sqrt(num)).ceil
    while(div <= sqrt_num)
        if(num % div == 0)
            return false
        end
        div += increment
        increment = 6 - increment
    end
    return true
end

def f(x, num)
    return (x*x + 1) % num
end


# Factorize the integer values
# and show the prime numbers as a list.
def pollards_rho_factorization(num) # [2]
    #print "beginning: #{num}\n"
    if num == 1
        return [1]
    end

    # Special case for factorization
    if num == 4
      return [2, 2]
    end
    
    # Return num if it is a prime number.
    if is_prime(num)
        return [num]
    end
    
    while true
        a = rand(10000000).abs
        b = rand(10000000).abs

        while true
            a = f(a, num)
            b = f(f(b, num), num)
            gcd = GCD((a-b).abs, num)
            if gcd == num || gcd== 1
              break
            end
            if (gcd > 1)
                return pollards_rho_factorization(gcd) + pollards_rho_factorization(num/gcd)
            end
        end
    end
end


# Remove comment symbols if you want to conduct the tests
# i = 1
# while i < 10000
#   result = pollards_rho_factorization(i)
#   if i != result.inject(:*)
#     print "error."
#     break
#   end
#   print "Normally finished."
#   i += 1
# end

# Reference:
#
# [1] Alexandru & Dickinson, M. (2009, November/2018, March). What is the best algorithm for checking if a number is prime?. 
#       Retrieved from https://stackoverflow.com/a/1801446/9378952
#
# [2] Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein C. (2009). 
#       Integer factorization In Thomas H. C, Charles E. L., Ronald L. R., & Clifford S. (Eds.), 
#       Number-theoretic algorithms (pp. 926–984) (3rd edition). Cambridge, MA ,USA: MIT Press. 
