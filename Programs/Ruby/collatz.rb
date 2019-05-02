def collatz_path(num)
  list = []
  while true do
    if(num == 1)
      return list
    elsif(num % 2 == 1)
      prev = num
      num = 3 * num + 1
      list << [prev, num]
    elsif(num % 2 == 0)
      prev = num
      num = num / 2
      list << [prev, num]
    end
  end
end
  
# # Plot the frequency of the number that passes through
# def collatz_frequency(num)
#   n = 2
#   while count < num do
#     collatz_num
#   end
# end