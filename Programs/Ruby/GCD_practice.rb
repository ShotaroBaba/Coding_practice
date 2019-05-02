# Calculate Great Common Divisor (GCD) using 
# Euclidean algorithm.

# Display the process of GCD calculation
def GCD_verbose(a, b)
    
    a, b = a.abs, b.abs

    # Always b => a
    if (a < b)
        a,b = b, a
    end
    puts "(A,B) = " + a.to_s() + ", " + b.to_s()
    count = 1
    while not (a == 0 or b == 0)
        puts "*" * 10
        print "Step #{count}:\n"
        tmp = a 
        a, b, division = b, a % b, a / b
        print "#{tmp} = #{a} * #{division} + #{b}\n"
        print "(A,B) = #{a}, #{b}\n"
        puts "*" * 10
        count += 1
    end

    if a == 0
        return b
    elsif b == 0
        return a
    end
    return a, b
end

# This method does not display the process of GCD calculation
def GCD(a, b)
    
    a, b = a.abs, b.abs

    # Always b => a
    if (a < b)
        a,b = b, a
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