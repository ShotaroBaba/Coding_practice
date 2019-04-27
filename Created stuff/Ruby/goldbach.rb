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

# Check the list of Goldbach.
def find_goldbach(num)
    i = 4
    if num < i
        puts "Please input number more than 4."
        return 
    end
    if num % 2 == 1
        puts "Please input even number."
    end
    dict_class = {}
    plus_list = []
    while i <= num
        if num == 4
            dict_class[num] = [[2, 2]]
        else
            plus_list = []
            tmp = i - 2
            a_num = 3
            b_num = i - 3
            while a_num < tmp
                if(is_prime(a_num) and is_prime(b_num))
                    plus_list += [[a_num, b_num]]
                end
                a_num += 2
                b_num -= 2
            end
            dict_class[i] = plus_list
        end
        i += 2
    end
    return dict_class
end
        
# References:
#
# [1] Alexandru & Dickinson, M. (2009, November/2018, March). What is the best algorithm for checking if a number is prime?. 
#       Retrieved from https://stackoverflow.com/a/1801446/9378952