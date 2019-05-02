def is_prime(num)
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
  while( div <= sqrt_num)
    if(num % div == 0)
      return false
    end
    div += increment
    increment = 6 - increment
  end
  return true
end

# Reference:
#
# Alexandru, Dickinson, M. (2009, November/2018, March). What is the best algorithm for checking if a number is prime?. 
#   Retrieved from https://stackoverflow.com/a/1801446/9378952